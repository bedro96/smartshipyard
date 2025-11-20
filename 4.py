import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
from collections import defaultdict

# Ontology 연동을 위한 추가 import (실제 사용 시)
try:
    from rdflib import Graph, Namespace, URIRef, Literal
    from rdflib.namespace import RDF, RDFS, OWL
    RDFLIB_AVAILABLE = True
except ImportError:
    RDFLIB_AVAILABLE = False
    print("Warning: rdflib not installed. Using sample data mode.")

# =============================================================================
# Layer 1: Risk Ontology Interface (실제로는 Ontology에서 가져온다고 가정)
# =============================================================================

@dataclass
class RiskFactor:
    """리스크 요인"""
    name: str
    probability: float  # 발생 확률
    parents: List[str]  # 선행 요인들
    
@dataclass
class CostImpact:
    """원가 영향"""
    factor: str
    base_cost: float  # 기본 원가 (억원)
    multiplier_if_triggered: float  # 발생시 배수


class OntologyConnector:
    """실제 Ontology 시스템과의 연동 인터페이스"""
    
    def __init__(self, ontology_source: str = "sample", 
                 endpoint_url: str = None,
                 ontology_file: str = None,
                 file_format: str = None):
        """
        Args:
            ontology_source: 'sample', 'owl', 'rdf', 'sparql', 'graphdb'
            endpoint_url: SPARQL endpoint URL (for sparql/graphdb)
            ontology_file: Ontology 파일 경로 (OWL, RDF, Turtle 등)
            file_format: 파일 형식 (자동 감지 가능)
                - 'xml' or 'owl': OWL/RDF XML 형식
                - 'turtle' or 'ttl': Turtle 형식
                - 'n3': N3 형식
                - 'nt': N-Triples 형식
                - None: 파일 확장자로 자동 감지
        """
        self.source = ontology_source
        self.endpoint_url = endpoint_url
        self.ontology_file = ontology_file
        self.file_format = file_format
        
        if ontology_source == 'rdf' and RDFLIB_AVAILABLE:
            self.graph = self._load_rdf_ontology()
            self.ns = Namespace("http://shipbuilding.ontology/risk#")
        elif ontology_source == 'sparql':
            # SPARQL endpoint 연동 준비
            pass
        elif ontology_source == 'graphdb':
            # GraphDB 연동 준비
            pass
    
    def _load_rdf_ontology(self) -> Graph:
        """RDF/OWL 파일에서 Ontology 로드"""
        g = Graph()
        if self.ttl_file:
            g.parse(self.ttl_file, format='turtle')
            print(f"[Ontology] Loaded {len(g)} triples from {self.ttl_file}")
        else:
            # 샘플 Ontology 생성
            g = self._create_sample_rdf_ontology()
        return g
    
    def _create_sample_rdf_ontology(self) -> Graph:
        """샘플 RDF Ontology 생성 (실제로는 별도 파일)"""
        g = Graph()
        ns = Namespace("http://shipbuilding.ontology/risk#")
        g.bind("risk", ns)
        
        # 클래스 정의
        g.add((ns.RiskFactor, RDF.type, OWL.Class))
        g.add((ns.CostDriver, RDF.type, OWL.Class))
        g.add((ns.Process, RDF.type, OWL.Class))
        
        # 프로퍼티 정의
        g.add((ns.causes, RDF.type, OWL.ObjectProperty))
        g.add((ns.impacts, RDF.type, OWL.ObjectProperty))
        g.add((ns.hasProbability, RDF.type, OWL.DatatypeProperty))
        g.add((ns.hasCostImpact, RDF.type, OWL.DatatypeProperty))
        
        # 인스턴스 - Root Risk Factors
        material_delay = ns.MaterialDelay
        g.add((material_delay, RDF.type, ns.RiskFactor))
        g.add((material_delay, RDFS.label, Literal("강재납기지연")))
        g.add((material_delay, ns.hasProbability, Literal(0.30)))
        
        design_change = ns.DesignChange
        g.add((design_change, RDF.type, ns.RiskFactor))
        g.add((design_change, RDFS.label, Literal("설계변경")))
        g.add((design_change, ns.hasProbability, Literal(0.15)))
        
        manpower_shortage = ns.ManpowerShortage
        g.add((manpower_shortage, RDF.type, ns.RiskFactor))
        g.add((manpower_shortage, RDFS.label, Literal("인력부족")))
        g.add((manpower_shortage, ns.hasProbability, Literal(0.25)))
        
        bad_weather = ns.BadWeather
        g.add((bad_weather, RDF.type, ns.RiskFactor))
        g.add((bad_weather, RDFS.label, Literal("악천후")))
        g.add((bad_weather, ns.hasProbability, Literal(0.20)))
        
        # 인스턴스 - Intermediate Factors
        block_delay = ns.BlockDelay
        g.add((block_delay, RDF.type, ns.RiskFactor))
        g.add((block_delay, RDFS.label, Literal("블록작업지연")))
        g.add((material_delay, ns.causes, block_delay))
        g.add((manpower_shortage, ns.causes, block_delay))
        
        rework = ns.Rework
        g.add((rework, RDF.type, ns.RiskFactor))
        g.add((rework, RDFS.label, Literal("재작업")))
        g.add((design_change, ns.causes, rework))
        g.add((bad_weather, ns.causes, rework))
        
        idle_time = ns.IdleTime
        g.add((idle_time, RDF.type, ns.RiskFactor))
        g.add((idle_time, RDFS.label, Literal("대기시간")))
        g.add((material_delay, ns.causes, idle_time))
        g.add((block_delay, ns.causes, idle_time))
        
        # 인스턴스 - Cost Drivers
        overtime = ns.Overtime
        g.add((overtime, RDF.type, ns.CostDriver))
        g.add((overtime, RDFS.label, Literal("특근투입")))
        g.add((block_delay, ns.causes, overtime))
        g.add((idle_time, ns.causes, overtime))
        g.add((overtime, ns.hasCostImpact, Literal(3.0)))  # 기본 비용
        
        material_waste = ns.MaterialWaste
        g.add((material_waste, RDF.type, ns.CostDriver))
        g.add((material_waste, RDFS.label, Literal("자재손실")))
        g.add((rework, ns.causes, material_waste))
        g.add((design_change, ns.causes, material_waste))
        g.add((material_waste, ns.hasCostImpact, Literal(1.0)))
        
        equipment_extend = ns.EquipmentExtend
        g.add((equipment_extend, RDF.type, ns.CostDriver))
        g.add((equipment_extend, RDFS.label, Literal("장비임대연장")))
        g.add((block_delay, ns.causes, equipment_extend))
        g.add((bad_weather, ns.causes, equipment_extend))
        g.add((equipment_extend, ns.hasCostImpact, Literal(2.0)))
        
        print(f"[Ontology] Created sample ontology with {len(g)} triples")
        return g
    
    def query_risk_structure(self) -> Dict[str, RiskFactor]:
        """Ontology에서 리스크 구조 쿼리"""
        
        if self.source == 'sample':
            return self._get_sample_structure()
        
        elif self.source == 'rdf' and RDFLIB_AVAILABLE:
            return self._query_rdf_structure()
        
        elif self.source == 'sparql':
            return self._query_sparql_structure()
        
        elif self.source == 'graphdb':
            return self._query_graphdb_structure()
        
        else:
            print("[Warning] Unknown ontology source, using sample data")
            return self._get_sample_structure()
    
    def _query_rdf_structure(self) -> Dict[str, RiskFactor]:
        """RDF Graph에서 SPARQL로 리스크 구조 추출"""
        risk_structure = {}
        
        # SPARQL 쿼리: 모든 RiskFactor와 CostDriver 가져오기
        query = """
        PREFIX risk: <http://shipbuilding.ontology/risk#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        
        SELECT ?factor ?label ?probability
        WHERE {
            {?factor a risk:RiskFactor} UNION {?factor a risk:CostDriver}
            ?factor rdfs:label ?label .
            OPTIONAL { ?factor risk:hasProbability ?probability }
        }
        """
        
        results = self.graph.query(query)
        
        for row in results:
            factor_uri = str(row.factor).split('#')[-1]
            factor_id = self._uri_to_id(factor_uri)
            label = str(row.label)
            prob = float(row.probability) if row.probability else 0.0
            
            risk_structure[factor_id] = RiskFactor(
                name=label,
                probability=prob,
                parents=[]
            )
        
        # 부모-자식 관계 쿼리
        causes_query = """
        PREFIX risk: <http://shipbuilding.ontology/risk#>
        
        SELECT ?parent ?child
        WHERE {
            ?parent risk:causes ?child .
        }
        """
        
        causes_results = self.graph.query(causes_query)
        
        for row in causes_results:
            parent_id = self._uri_to_id(str(row.parent).split('#')[-1])
            child_id = self._uri_to_id(str(row.child).split('#')[-1])
            
            if child_id in risk_structure:
                risk_structure[child_id].parents.append(parent_id)
        
        print(f"[Ontology] Queried {len(risk_structure)} risk factors from RDF")
        return risk_structure
    
    def _query_sparql_structure(self) -> Dict[str, RiskFactor]:
        """SPARQL Endpoint에서 쿼리 (예: Fuseki, Stardog 등)"""
        # 실제 구현 예시
        """
        from SPARQLWrapper import SPARQLWrapper, JSON
        
        sparql = SPARQLWrapper(self.endpoint_url)
        sparql.setQuery('''
            PREFIX risk: <http://shipbuilding.ontology/risk#>
            SELECT ?factor ?label ?probability WHERE {
                ?factor a risk:RiskFactor .
                ?factor rdfs:label ?label .
                ?factor risk:hasProbability ?probability .
            }
        ''')
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        
        # 결과 파싱하여 RiskFactor 객체 생성
        ...
        """
        print("[Info] SPARQL query not implemented, using sample data")
        return self._get_sample_structure()
    
    def _query_graphdb_structure(self) -> Dict[str, RiskFactor]:
        """GraphDB에서 쿼리 (Neo4j, Amazon Neptune 등)"""
        # Neo4j 예시
        """
        from neo4j import GraphDatabase
        
        driver = GraphDatabase.driver(self.endpoint_url, 
                                      auth=("neo4j", "password"))
        
        with driver.session() as session:
            result = session.run('''
                MATCH (r:RiskFactor)
                OPTIONAL MATCH (parent)-[:CAUSES]->(r)
                RETURN r.id, r.label, r.probability, collect(parent.id) as parents
            ''')
            
            for record in result:
                # RiskFactor 객체 생성
                ...
        """
        print("[Info] GraphDB query not implemented, using sample data")
        return self._get_sample_structure()
    
    def query_cost_impacts(self) -> Dict[str, CostImpact]:
        """Ontology에서 원가 영향 쿼리"""
        
        if self.source == 'rdf' and RDFLIB_AVAILABLE:
            cost_impacts = {}
            
            query = """
            PREFIX risk: <http://shipbuilding.ontology/risk#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            
            SELECT ?driver ?label ?cost
            WHERE {
                ?driver a risk:CostDriver .
                ?driver rdfs:label ?label .
                ?driver risk:hasCostImpact ?cost .
            }
            """
            
            results = self.graph.query(query)
            
            for row in results:
                driver_id = self._uri_to_id(str(row.driver).split('#')[-1])
                label = str(row.label)
                base_cost = float(row.cost)
                
                cost_impacts[driver_id] = CostImpact(
                    factor=label,
                    base_cost=base_cost,
                    multiplier_if_triggered=1.5  # 기본값
                )
            
            print(f"[Ontology] Queried {len(cost_impacts)} cost impacts from RDF")
            return cost_impacts
        
        else:
            return self._get_sample_cost_impacts()
    
    def _uri_to_id(self, uri_fragment: str) -> str:
        """URI fragment를 Python identifier로 변환"""
        # MaterialDelay -> material_delay
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', uri_fragment)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    def _get_sample_structure(self) -> Dict[str, RiskFactor]:
        """샘플 데이터 (Ontology 없이 테스트용)"""
        return {
            'material_delay': RiskFactor('강재납기지연', 0.30, []),
            'design_change': RiskFactor('설계변경', 0.15, []),
            'manpower_shortage': RiskFactor('인력부족', 0.25, []),
            'bad_weather': RiskFactor('악천후', 0.20, []),
            'block_delay': RiskFactor('블록작업지연', 0.0, 
                                     ['material_delay', 'manpower_shortage']),
            'rework': RiskFactor('재작업', 0.0, 
                                ['design_change', 'bad_weather']),
            'idle_time': RiskFactor('대기시간', 0.0, 
                                   ['material_delay', 'block_delay']),
            'overtime': RiskFactor('특근투입', 0.0, 
                                  ['block_delay', 'idle_time']),
            'material_waste': RiskFactor('자재손실', 0.0, 
                                        ['rework', 'design_change']),
            'equipment_extend': RiskFactor('장비임대연장', 0.0, 
                                          ['block_delay', 'bad_weather'])
        }
    
    def _get_sample_cost_impacts(self) -> Dict[str, CostImpact]:
        """샘플 원가 영향 데이터"""
        return {
            'overtime': CostImpact('특근투입', 3.0, 1.5),
            'material_waste': CostImpact('자재손실', 1.0, 2.0),
            'equipment_extend': CostImpact('장비임대연장', 2.0, 1.3),
            'rework': CostImpact('재작업', 1.5, 1.8)
        }


class ShipbuildingOntology:
    """조선 Ontology 인터페이스"""
    
    def __init__(self, connector: OntologyConnector = None):
        """
        Args:
            connector: OntologyConnector 인스턴스
                      None이면 샘플 데이터 사용
        """
        if connector is None:
            # 기본: 샘플 데이터 모드
            connector = OntologyConnector(ontology_source='sample')
        
        self.connector = connector
        self.risk_structure = connector.query_risk_structure()
        self.cost_impacts = connector.query_cost_impacts()
        
        print(f"\n[ShipbuildingOntology] Initialized with {len(self.risk_structure)} risk factors")
        print(f"[ShipbuildingOntology] Loaded {len(self.cost_impacts)} cost impact definitions")

# =============================================================================
# Layer 2: Probabilistic Model - Bayesian Network
# =============================================================================

class BayesianNetworkModel:
    """조건부 확률 기반 베이지안 네트워크"""
    
    def __init__(self, ontology: ShipbuildingOntology):
        self.ontology = ontology
        self.risk_structure = ontology.risk_structure
        
        # 조건부 확률 테이블 (CPT) - 실제로는 과거 데이터로 학습
        self.cpt = self._initialize_cpt()
        
        # 현재 상태 (증거)
        self.evidence: Dict[str, bool] = {}
    
    def _initialize_cpt(self) -> Dict[str, Dict]:
        """조건부 확률 테이블 초기화 (과거 데이터 기반이라고 가정)"""
        return {
            # P(block_delay | material_delay, manpower_shortage)
            'block_delay': {
                (True, True): 0.85,
                (True, False): 0.60,
                (False, True): 0.55,
                (False, False): 0.10
            },
            # P(rework | design_change, bad_weather)
            'rework': {
                (True, True): 0.75,
                (True, False): 0.50,
                (False, True): 0.30,
                (False, False): 0.05
            },
            # P(idle_time | material_delay, block_delay)
            'idle_time': {
                (True, True): 0.90,
                (True, False): 0.70,
                (False, True): 0.50,
                (False, False): 0.05
            },
            # P(overtime | block_delay, idle_time)
            'overtime': {
                (True, True): 0.95,
                (True, False): 0.70,
                (False, True): 0.60,
                (False, False): 0.10
            },
            # P(material_waste | rework, design_change)
            'material_waste': {
                (True, True): 0.80,
                (True, False): 0.60,
                (False, True): 0.40,
                (False, False): 0.05
            },
            # P(equipment_extend | block_delay, bad_weather)
            'equipment_extend': {
                (True, True): 0.85,
                (True, False): 0.65,
                (False, True): 0.45,
                (False, False): 0.10
            }
        }
    
    def set_evidence(self, factor: str, occurred: bool):
        """증거 설정 (실제 발생한 이벤트)"""
        self.evidence[factor] = occurred
        print(f"[증거 입력] {factor}: {'발생' if occurred else '미발생'}")
    
    def calculate_probability(self, factor: str) -> float:
        """특정 요인의 발생 확률 계산"""
        risk = self.risk_structure[factor]
        
        # Root node인 경우
        if not risk.parents:
            if factor in self.evidence:
                return 1.0 if self.evidence[factor] else 0.0
            return risk.probability
        
        # 부모가 있는 경우 - 조건부 확률 사용
        if factor in self.evidence:
            return 1.0 if self.evidence[factor] else 0.0
        
        # 부모 노드들의 상태 조합별로 확률 계산
        parent_probs = [self.calculate_probability(p) for p in risk.parents]
        
        if factor not in self.cpt:
            # CPT가 없으면 부모들의 OR 로직으로 근사
            return 1.0 - np.prod([1.0 - p for p in parent_probs])
        
        # CPT를 사용한 정확한 계산
        total_prob = 0.0
        for i in range(2 ** len(risk.parents)):
            # 부모들의 모든 조합 생성
            parent_states = tuple(bool(i & (1 << j)) for j in range(len(risk.parents)))
            
            # 이 조합의 확률
            combination_prob = 1.0
            for parent, state in zip(risk.parents, parent_states):
                parent_prob = self.calculate_probability(parent)
                combination_prob *= parent_prob if state else (1.0 - parent_prob)
            
            # 조건부 확률 곱하기
            if parent_states in self.cpt[factor]:
                conditional_prob = self.cpt[factor][parent_states]
                total_prob += combination_prob * conditional_prob
        
        return total_prob
    
    def get_all_probabilities(self) -> Dict[str, float]:
        """모든 요인의 현재 확률 계산"""
        return {name: self.calculate_probability(name) 
                for name in self.risk_structure.keys()}

# =============================================================================
# Layer 2: Monte Carlo Simulation Engine
# =============================================================================

class MonteCarloSimulator:
    """몬테카를로 시뮬레이션으로 원가 분포 예측"""
    
    def __init__(self, ontology: ShipbuildingOntology, 
                 bayesian_model: BayesianNetworkModel):
        self.ontology = ontology
        self.bayesian_model = bayesian_model
        self.base_cost = 100.0  # 기본 원가 100억원
    
    def run_simulation(self, n_iterations: int = 10000) -> pd.DataFrame:
        """시뮬레이션 실행"""
        results = []
        
        for i in range(n_iterations):
            # 각 리스크 요인의 발생 여부 샘플링
            iteration_state = {}
            for factor in self.bayesian_model.risk_structure.keys():
                prob = self.bayesian_model.calculate_probability(factor)
                iteration_state[factor] = np.random.random() < prob
            
            # 원가 계산
            total_cost = self.base_cost
            cost_breakdown = {'base': self.base_cost}
            
            for factor, impact in self.ontology.cost_impacts.items():
                if factor in iteration_state and iteration_state[factor]:
                    additional_cost = impact.base_cost * impact.multiplier_if_triggered
                    total_cost += additional_cost
                    cost_breakdown[factor] = additional_cost
                else:
                    cost_breakdown[factor] = 0.0
            
            cost_breakdown['total'] = total_cost
            cost_breakdown.update(iteration_state)
            results.append(cost_breakdown)
        
        return pd.DataFrame(results)
    
    def analyze_results(self, results: pd.DataFrame) -> Dict:
        """시뮬레이션 결과 분석"""
        total_costs = results['total']
        
        analysis = {
            'mean_cost': total_costs.mean(),
            'median_cost': total_costs.median(),
            'std_cost': total_costs.std(),
            'percentile_10': total_costs.quantile(0.10),
            'percentile_50': total_costs.quantile(0.50),
            'percentile_90': total_costs.quantile(0.90),
            'percentile_95': total_costs.quantile(0.95),
            'prob_over_budget': (total_costs > self.base_cost * 1.1).mean(),
            'prob_over_budget_20': (total_costs > self.base_cost * 1.2).mean()
        }
        
        return analysis

# =============================================================================
# Layer 3: Decision Support System
# =============================================================================

class DecisionSupportSystem:
    """의사결정 지원 시스템"""
    
    def __init__(self, ontology: ShipbuildingOntology):
        self.ontology = ontology
        self.bayesian_model = BayesianNetworkModel(ontology)
        self.simulator = MonteCarloSimulator(ontology, self.bayesian_model)
    
    def update_status(self, events: Dict[str, bool]):
        """현재 상황 업데이트"""
        print("\n" + "="*60)
        print("현재 프로젝트 상황 업데이트")
        print("="*60)
        for factor, occurred in events.items():
            self.bayesian_model.set_evidence(factor, occurred)
    
    def analyze_current_risk(self):
        """현재 리스크 분석"""
        print("\n[현재 리스크 확률 분석]")
        probs = self.bayesian_model.get_all_probabilities()
        
        # 원가 영향 요인만 출력
        cost_factors = ['overtime', 'material_waste', 'equipment_extend', 'rework']
        for factor in cost_factors:
            if factor in probs:
                print(f"  - {self.bayesian_model.risk_structure[factor].name}: "
                      f"{probs[factor]*100:.1f}%")
    
    def run_cost_simulation(self, n_iterations: int = 10000):
        """원가 시뮬레이션 실행 및 리포트"""
        print(f"\n[몬테카를로 시뮬레이션 실행: {n_iterations:,}회]")
        results = self.simulator.run_simulation(n_iterations)
        analysis = self.simulator.analyze_results(results)
        
        print("\n[원가 예측 결과]")
        print(f"  • 평균 예상 원가: {analysis['mean_cost']:.1f}억원")
        print(f"  • 중앙값: {analysis['median_cost']:.1f}억원")
        print(f"  • 표준편차: {analysis['std_cost']:.1f}억원")
        print(f"  • 10% 분위수: {analysis['percentile_10']:.1f}억원 (낙관)")
        print(f"  • 50% 분위수: {analysis['percentile_50']:.1f}억원")
        print(f"  • 90% 분위수: {analysis['percentile_90']:.1f}억원 (비관)")
        print(f"  • 95% 분위수: {analysis['percentile_95']:.1f}억원 (최악)")
        
        print(f"\n[리스크 평가]")
        print(f"  • 예산 10% 초과 확률: {analysis['prob_over_budget']*100:.1f}%")
        print(f"  • 예산 20% 초과 확률: {analysis['prob_over_budget_20']*100:.1f}%")
        
        return results, analysis
    
    def what_if_analysis(self, scenario_name: str, events: Dict[str, bool]):
        """What-if 시나리오 분석"""
        print(f"\n{'='*60}")
        print(f"What-If 시나리오: {scenario_name}")
        print("="*60)
        
        # 기존 상태 백업
        original_evidence = self.bayesian_model.evidence.copy()
        
        # 시나리오 적용
        for factor, occurred in events.items():
            self.bayesian_model.set_evidence(factor, occurred)
        
        # 분석
        self.analyze_current_risk()
        results, analysis = self.run_cost_simulation(5000)
        
        # 원상 복구
        self.bayesian_model.evidence = original_evidence
        
        return results, analysis
    
    def recommend_actions(self, analysis: Dict):
        """리스크 완화 조치 권고"""
        print("\n[권장 조치사항]")
        
        if analysis['prob_over_budget'] > 0.5:
            print("  ⚠️  고위험 상태입니다!")
            print("  → 즉시 대응 필요:")
            
            probs = self.bayesian_model.get_all_probabilities()
            if probs.get('block_delay', 0) > 0.5:
                print("     • 블록 작업에 추가 인력 투입 검토")
            if probs.get('material_delay', 0) > 0.3:
                print("     • 자재 조달 일정 단축 방안 협의")
            if probs.get('overtime', 0) > 0.6:
                print("     • 주말 작업 스케줄 최적화")
                
        elif analysis['prob_over_budget'] > 0.3:
            print("  ⚡ 중위험 상태")
            print("  → 예방적 조치 권장:")
            print("     • 주간 진척률 모니터링 강화")
            print("     • 협력업체 납기 독려")
            
        else:
            print("  ✓ 양호한 상태")
            print("  → 현재 계획대로 진행")
    
    def visualize_results(self, results: pd.DataFrame):
        """결과 시각화"""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # 1. 총 원가 히스토그램
        axes[0, 0].hist(results['total'], bins=50, edgecolor='black', alpha=0.7)
        axes[0, 0].axvline(self.simulator.base_cost, color='green', 
                          linestyle='--', label='기본 원가')
        axes[0, 0].axvline(self.simulator.base_cost * 1.1, color='orange', 
                          linestyle='--', label='예산 +10%')
        axes[0, 0].axvline(self.simulator.base_cost * 1.2, color='red', 
                          linestyle='--', label='예산 +20%')
        axes[0, 0].set_xlabel('총 원가 (억원)')
        axes[0, 0].set_ylabel('빈도')
        axes[0, 0].set_title('총 원가 분포')
        axes[0, 0].legend()
        
        # 2. 누적 확률 분포
        sorted_costs = np.sort(results['total'])
        cumulative = np.arange(1, len(sorted_costs) + 1) / len(sorted_costs)
        axes[0, 1].plot(sorted_costs, cumulative, linewidth=2)
        axes[0, 1].axhline(0.5, color='gray', linestyle=':', alpha=0.5)
        axes[0, 1].axhline(0.9, color='gray', linestyle=':', alpha=0.5)
        axes[0, 1].set_xlabel('총 원가 (억원)')
        axes[0, 1].set_ylabel('누적 확률')
        axes[0, 1].set_title('누적 확률 분포 (CDF)')
        axes[0, 1].grid(True, alpha=0.3)
        
        # 3. 원가 요인별 기여도
        cost_factors = ['overtime', 'material_waste', 'equipment_extend', 'rework']
        factor_costs = [results[f].mean() for f in cost_factors if f in results]
        factor_names = [f.replace('_', '\n') for f in cost_factors if f in results]
        
        axes[1, 0].bar(range(len(factor_costs)), factor_costs, 
                      color=['#ff6b6b', '#4ecdc4', '#45b7d1', '#f9ca24'])
        axes[1, 0].set_xticks(range(len(factor_costs)))
        axes[1, 0].set_xticklabels(factor_names, fontsize=9)
        axes[1, 0].set_ylabel('평균 추가 원가 (억원)')
        axes[1, 0].set_title('원가 요인별 평균 영향')
        
        # 4. 리스크 발생 빈도
        risk_factors = ['material_delay', 'design_change', 'manpower_shortage', 'bad_weather']
        risk_probs = [results[f].mean() for f in risk_factors if f in results]
        risk_names = [f.replace('_', '\n') for f in risk_factors if f in results]
        
        axes[1, 1].barh(range(len(risk_probs)), risk_probs, 
                       color=['#ee5a6f', '#f7b731', '#20bf6b', '#0fb9b1'])
        axes[1, 1].set_yticks(range(len(risk_probs)))
        axes[1, 1].set_yticklabels(risk_names, fontsize=9)
        axes[1, 1].set_xlabel('발생 확률')
        axes[1, 1].set_title('리스크 요인 발생 빈도')
        axes[1, 1].set_xlim(0, 1)
        
        plt.tight_layout()
        plt.savefig('shipbuilding_risk_analysis.png', dpi=150, bbox_inches='tight')
        print("\n[시각화 완료] 'shipbuilding_risk_analysis.png' 저장됨")
        plt.show()

# =============================================================================
# 실행 예제
# =============================================================================

def main():
    """메인 실행 함수"""
    
    print("="*60)
    print("조선 건조 Risk 관리 시스템 v1.0")
    print("="*60)
    
    # =========================================================================
    # Ontology 연동 방법 선택
    # =========================================================================
    print("\n[Ontology 연동 모드 선택]")
    print("1. Sample Mode (샘플 데이터)")
    print("2. RDF Mode (Turtle/OWL 파일)")
    print("3. SPARQL Mode (SPARQL Endpoint)")
    print("4. GraphDB Mode (Neo4j, Neptune 등)")
    
    # 여기서는 자동으로 RDF 모드 사용 (샘플 ontology 생성)
    mode = 'rdf'  # 'sample', 'rdf', 'sparql', 'graphdb'
    
    if mode == 'sample':
        print("\n→ Sample Mode 선택: 내장 샘플 데이터 사용")
        connector = OntologyConnector(ontology_source='sample')
    
    elif mode == 'rdf':
        print("\n→ RDF Mode 선택: RDF/OWL Ontology 사용")
        # 실제 파일이 있다면: ttl_file='shipbuilding_risk.ttl'
        connector = OntologyConnector(ontology_source='rdf', ttl_file=None)
        
    elif mode == 'sparql':
        print("\n→ SPARQL Mode 선택: SPARQL Endpoint 연동")
        # 예: Apache Jena Fuseki
        # connector = OntologyConnector(
        #     ontology_source='sparql',
        #     endpoint_url='http://localhost:3030/shipbuilding/sparql'
        # )
        connector = OntologyConnector(ontology_source='sample')
        
    elif mode == 'graphdb':
        print("\n→ GraphDB Mode 선택: Graph Database 연동")
        # 예: Neo4j
        # connector = OntologyConnector(
        #     ontology_source='graphdb',
        #     endpoint_url='bolt://localhost:7687'
        # )
        connector = OntologyConnector(ontology_source='sample')
    
    # Ontology 로드
    ontology = ShipbuildingOntology(connector)
    
    # =========================================================================
    # Risk 관리 시스템 초기화
    # =========================================================================
    dss = DecisionSupportSystem(ontology)
    
    # 시나리오 1: 정상 상황
    print("\n\n### 시나리오 1: 기준선 (정상 상황) ###")
    results_baseline, analysis_baseline = dss.run_cost_simulation(10000)
    dss.recommend_actions(analysis_baseline)
    
    # 시나리오 2: 강재 납기 지연 발생
    print("\n\n### 시나리오 2: 강재 납기 2일 지연 발생 ###")
    dss.update_status({'material_delay': True})
    dss.analyze_current_risk()
    results_delay, analysis_delay = dss.run_cost_simulation(10000)
    dss.recommend_actions(analysis_delay)
    
    # 시나리오 3: What-if - 추가 인력 투입 시
    print("\n\n### 시나리오 3: What-If - 추가 인력 투입으로 인력부족 해결 ###")
    results_whatif, analysis_whatif = dss.what_if_analysis(
        "추가 인력 투입",
        {'material_delay': True, 'manpower_shortage': False}
    )
    
    # 비교 분석
    print("\n\n" + "="*60)
    print("시나리오 비교 분석")
    print("="*60)
    print(f"\n{'시나리오':<20} {'평균원가':>12} {'예산초과확률':>14} {'비용증가':>12}")
    print("-"*60)
    print(f"{'1. 정상 상황':<20} {analysis_baseline['mean_cost']:>10.1f}억 "
          f"{analysis_baseline['prob_over_budget']*100:>12.1f}% {0:>10.1f}억")
    print(f"{'2. 강재 지연':<20} {analysis_delay['mean_cost']:>10.1f}억 "
          f"{analysis_delay['prob_over_budget']*100:>12.1f}% "
          f"{analysis_delay['mean_cost']-analysis_baseline['mean_cost']:>10.1f}억")
    print(f"{'3. 인력 추가투입':<20} {analysis_whatif['mean_cost']:>10.1f}억 "
          f"{analysis_whatif['prob_over_budget']*100:>12.1f}% "
          f"{analysis_whatif['mean_cost']-analysis_baseline['mean_cost']:>10.1f}억")
    
    # 시각화
    dss.visualize_results(results_delay)
    
    # =========================================================================
    # Ontology 데이터 확인 (디버깅용)
    # =========================================================================
    print("\n\n" + "="*60)
    print("Ontology 데이터 확인")
    print("="*60)
    print(f"\n[Risk Structure from Ontology]")
    for risk_id, risk_factor in list(ontology.risk_structure.items())[:5]:
        print(f"  • {risk_id}: {risk_factor.name}")
        if risk_factor.parents:
            print(f"    ↳ 선행요인: {', '.join(risk_factor.parents)}")
        if risk_factor.probability > 0:
            print(f"    ↳ 기본확률: {risk_factor.probability*100:.1f}%")
    
    print(f"\n[Cost Impact from Ontology]")
    for cost_id, cost_impact in ontology.cost_impacts.items():
        print(f"  • {cost_id}: {cost_impact.factor}")
        print(f"    ↳ 기본비용: {cost_impact.base_cost}억원, "
              f"발생시 배수: {cost_impact.multiplier_if_triggered}x")
    
    print("\n\n프로그램 종료")


def demo_ontology_creation():
    """
    Ontology 파일 생성 데모
    실제로는 Protégé, TopBraid Composer 등의 툴로 작성
    """
    print("="*60)
    print("조선 Risk Ontology 생성 데모 (RDF/Turtle 형식)")
    print("="*60)
    
    if not RDFLIB_AVAILABLE:
        print("\n[Error] rdflib 설치 필요: pip install rdflib")
        return
    
    # Sample ontology 생성
    connector = OntologyConnector(ontology_source='rdf')
    
    # Turtle 형식으로 저장
    output_file = 'shipbuilding_risk_ontology.ttl'
    connector.graph.serialize(destination=output_file, format='turtle')
    
    print(f"\n[Success] Ontology 저장 완료: {output_file}")
    print(f"총 {len(connector.graph)} triples")
    
    print("\n[생성된 Ontology 미리보기]")
    print("-"*60)
    sample_ttl = """
@prefix risk: <http://shipbuilding.ontology/risk#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .

# 클래스 정의
risk:RiskFactor a owl:Class .
risk:CostDriver a owl:Class .

# 프로퍼티 정의
risk:causes a owl:ObjectProperty .
risk:hasProbability a owl:DatatypeProperty .

# 인스턴스
risk:MaterialDelay a risk:RiskFactor ;
    rdfs:label "강재납기지연" ;
    risk:hasProbability 0.30 ;
    risk:causes risk:BlockDelay .

risk:BlockDelay a risk:RiskFactor ;
    rdfs:label "블록작업지연" ;
    risk:causes risk:Overtime .

risk:Overtime a risk:CostDriver ;
    rdfs:label "특근투입" ;
    risk:hasCostImpact 3.0 .
    """
    print(sample_ttl)
    print("-"*60)
    
    print("\n[사용 방법]")
    print("1. Protégé로 ontology 편집: https://protege.stanford.edu/")
    print("2. 프로그램에서 로드:")
    print("   connector = OntologyConnector(")
    print("       ontology_source='rdf',")
    print("       ttl_file='shipbuilding_risk_ontology.ttl'")
    print("   )")
    print("   ontology = ShipbuildingOntology(connector)")


if __name__ == "__main__":
    # 메인 프로그램 실행
    main()
    
    # Ontology 파일 생성 데모 (선택사항)
    # demo_ontology_creation()