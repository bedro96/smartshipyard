# 조선 Risk 관리 OWL Ontology 필수 요소

## 1. 핵심 클래스 (Classes)

### 1.1 Risk 관련 클래스
```xml
<!-- 최상위 리스크 클래스 -->
<owl:Class rdf:about="#RiskFactor">
    <rdfs:label>위험 요인</rdfs:label>
    <rdfs:comment>조선 건조 과정에서 발생 가능한 위험 요소</rdfs:comment>
</owl:Class>

<!-- 원가에 직접 영향을 주는 리스크 -->
<owl:Class rdf:about="#CostDriver">
    <rdfs:label>원가 동인</rdfs:label>
    <rdfs:subClassOf rdf:resource="#RiskFactor"/>
</owl:Class>

<!-- 리스크 분류 -->
<owl:Class rdf:about="#RootRisk">
    <rdfs:label>근본 원인 리스크</rdfs:label>
    <rdfs:subClassOf rdf:resource="#RiskFactor"/>
    <rdfs:comment>외부 요인, 독립적 발생</rdfs:comment>
</owl:Class>

<owl:Class rdf:about="#IntermediateRisk">
    <rdfs:label>중간 리스크</rdfs:label>
    <rdfs:subClassOf rdf:resource="#RiskFactor"/>
    <rdfs:comment>다른 리스크에 의해 유발됨</rdfs:comment>
</owl:Class>
```

### 1.2 조선 도메인 클래스
```xml
<!-- 조선 공정 -->
<owl:Class rdf:about="#ShipbuildingProcess">
    <rdfs:label>조선 공정</rdfs:label>
</owl:Class>

<!-- 블록, PE, 조립 등 -->
<owl:Class rdf:about="#BlockWork">
    <rdfs:subClassOf rdf:resource="#ShipbuildingProcess"/>
</owl:Class>

<owl:Class rdf:about="#PaintingErection">
    <rdfs:subClassOf rdf:resource="#ShipbuildingProcess"/>
</owl:Class>

<!-- 자원 -->
<owl:Class rdf:about="#Resource">
    <rdfs:label>자원</rdfs:label>
</owl:Class>

<owl:Class rdf:about="#Material">
    <rdfs:subClassOf rdf:resource="#Resource"/>
</owl:Class>

<owl:Class rdf:about="#Manpower">
    <rdfs:subClassOf rdf:resource="#Resource"/>
</owl:Class>

<owl:Class rdf:about="#Equipment">
    <rdfs:subClassOf rdf:resource="#Resource"/>
</owl:Class>
```

---

## 2. 필수 Object Properties (관계)

### 2.1 인과관계 (Causality)
```xml
<!-- 가장 중요: 리스크 간 인과관계 -->
<owl:ObjectProperty rdf:about="#causes">
    <rdfs:label>원인이 됨</rdfs:label>
    <rdfs:domain rdf:resource="#RiskFactor"/>
    <rdfs:range rdf:resource="#RiskFactor"/>
    <rdfs:comment>한 리스크가 다른 리스크를 유발함</rdfs:comment>
</owl:ObjectProperty>

<!-- 역방향 관계 -->
<owl:ObjectProperty rdf:about="#causedBy">
    <rdfs:label>~에 의해 발생</rdfs:label>
    <owl:inverseOf rdf:resource="#causes"/>
</owl:ObjectProperty>

<!-- 영향 관계 -->
<owl:ObjectProperty rdf:about="#impacts">
    <rdfs:label>영향을 미침</rdfs:label>
    <rdfs:domain rdf:resource="#RiskFactor"/>
    <rdfs:range rdf:resource="#ShipbuildingProcess"/>
</owl:ObjectProperty>
```

### 2.2 공정 관계
```xml
<!-- 공정 선후 관계 -->
<owl:ObjectProperty rdf:about="#precedes">
    <rdfs:label>선행함</rdfs:label>
    <rdfs:domain rdf:resource="#ShipbuildingProcess"/>
    <rdfs:range rdf:resource="#ShipbuildingProcess"/>
</owl:ObjectProperty>

<!-- 리스크-공정 연결 -->
<owl:ObjectProperty rdf:about="#affectsProcess">
    <rdfs:label>공정에 영향</rdfs:label>
    <rdfs:domain rdf:resource="#RiskFactor"/>
    <rdfs:range rdf:resource="#ShipbuildingProcess"/>
</owl:ObjectProperty>

<!-- 자원 의존성 -->
<owl:ObjectProperty rdf:about="#requiresResource">
    <rdfs:label>자원 필요</rdfs:label>
    <rdfs:domain rdf:resource="#ShipbuildingProcess"/>
    <rdfs:range rdf:resource="#Resource"/>
</owl:ObjectProperty>
```

---

## 3. 필수 Data Properties (확률 및 원가 속성)

### 3.1 확률 관련 속성 ⭐ 가장 중요
```xml
<!-- 기본 발생 확률 (Root Risk용) -->
<owl:DatatypeProperty rdf:about="#hasBaseProbability">
    <rdfs:label>기본 발생 확률</rdfs:label>
    <rdfs:domain rdf:resource="#RootRisk"/>
    <rdfs:range rdf:resource="xsd:float"/>
    <rdfs:comment>0.0 ~ 1.0 사이 값, 예: 0.30 = 30%</rdfs:comment>
</owl:DatatypeProperty>

<!-- 조건부 확률 테이블 (CPT) - JSON 형식으로 저장 -->
<owl:DatatypeProperty rdf:about="#hasConditionalProbability">
    <rdfs:label>조건부 확률</rdfs:label>
    <rdfs:domain rdf:resource="#IntermediateRisk"/>
    <rdfs:range rdf:resource="xsd:string"/>
    <rdfs:comment>
        부모 리스크 조합에 따른 확률
        예: "{(True,True):0.85, (True,False):0.60}"
    </rdfs:comment>
</owl:DatatypeProperty>
```

### 3.2 원가 영향 속성 ⭐ 두 번째로 중요
```xml
<!-- 기본 원가 (억원) -->
<owl:DatatypeProperty rdf:about="#hasBaseCost">
    <rdfs:label>기본 원가</rdfs:label>
    <rdfs:domain rdf:resource="#CostDriver"/>
    <rdfs:range rdf:resource="xsd:float"/>
    <rdfs:comment>단위: 억원</rdfs:comment>
</owl:DatatypeProperty>

<!-- 발생 시 비용 증가 배수 -->
<owl:DatatypeProperty rdf:about="#hasCostMultiplier">
    <rdfs:label>원가 배수</rdfs:label>
    <rdfs:domain rdf:resource="#CostDriver"/>
    <rdfs:range rdf:resource="xsd:float"/>
    <rdfs:comment>리스크 발생 시 기본 원가에 곱해지는 배수</rdfs:comment>
</owl:DatatypeProperty>

<!-- 최소/최대 원가 (Monte Carlo용) -->
<owl:DatatypeProperty rdf:about="#hasMinCost">
    <rdfs:label>최소 원가</rdfs:label>
    <rdfs:domain rdf:resource="#CostDriver"/>
    <rdfs:range rdf:resource="xsd:float"/>
</owl:DatatypeProperty>

<owl:DatatypeProperty rdf:about="#hasMaxCost">
    <rdfs:label>최대 원가</rdfs:label>
    <rdfs:domain rdf:resource="#CostDriver"/>
    <rdfs:range rdf:resource="xsd:float"/>
</owl:DatatypeProperty>
```

### 3.3 리스크 심각도 속성
```xml
<!-- 심각도 점수 -->
<owl:DatatypeProperty rdf:about="#hasSeverity">
    <rdfs:label>심각도</rdfs:label>
    <rdfs:domain rdf:resource="#RiskFactor"/>
    <rdfs:range rdf:resource="xsd:integer"/>
    <rdfs:comment>1(낮음) ~ 5(매우높음)</rdfs:comment>
</owl:DatatypeProperty>

<!-- 감지 용이성 -->
<owl:DatatypeProperty rdf:about="#hasDetectability">
    <rdfs:label>감지 용이성</rdfs:label>
    <rdfs:domain rdf:resource="#RiskFactor"/>
    <rdfs:range rdf:resource="xsd:integer"/>
    <rdfs:comment>1(쉬움) ~ 5(어려움)</rdfs:comment>
</owl:DatatypeProperty>
```

### 3.4 시간 관련 속성
```xml
<!-- 평균 지연 일수 -->
<owl:DatatypeProperty rdf:about="#hasAverageDelayDays">
    <rdfs:label>평균 지연 일수</rdfs:label>
    <rdfs:domain rdf:resource="#RiskFactor"/>
    <rdfs:range rdf:resource="xsd:integer"/>
</owl:DatatypeProperty>

<!-- 공정 소요 시간 -->
<owl:DatatypeProperty rdf:about="#hasDurationDays">
    <rdfs:label>소요 기간</rdfs:label>
    <rdfs:domain rdf:resource="#ShipbuildingProcess"/>
    <rdfs:range rdf:resource="xsd:integer"/>
</owl:DatatypeProperty>
```

### 3.5 메타데이터
```xml
<!-- 설명 -->
<owl:DatatypeProperty rdf:about="#hasDescription">
    <rdfs:label>설명</rdfs:label>
    <rdfs:range rdf:resource="xsd:string"/>
</owl:DatatypeProperty>

<!-- 카테고리 -->
<owl:DatatypeProperty rdf:about="#hasCategory">
    <rdfs:label>카테고리</rdfs:label>
    <rdfs:domain rdf:resource="#RiskFactor"/>
    <rdfs:range rdf:resource="xsd:string"/>
    <rdfs:comment>예: "자재", "인력", "날씨", "설계"</rdfs:comment>
</owl:DatatypeProperty>

<!-- 데이터 출처 -->
<owl:DatatypeProperty rdf:about="#hasDataSource">
    <rdfs:label>데이터 출처</rdfs:label>
    <rdfs:range rdf:resource="xsd:string"/>
    <rdfs:comment>확률값의 근거, 예: "2020-2024 프로젝트 데이터"</rdfs:comment>
</owl:DatatypeProperty>
```

---

## 4. 인스턴스 예시 (실제 데이터)

### 4.1 Root Risk 인스턴스
```xml
<!-- 강재 납기 지연 -->
<RootRisk rdf:about="#MaterialDelay">
    <rdfs:label>강재납기지연</rdfs:label>
    <hasBaseProbability rdf:datatype="xsd:float">0.30</hasBaseProbability>
    <hasSeverity rdf:datatype="xsd:integer">4</hasSeverity>
    <hasAverageDelayDays rdf:datatype="xsd:integer">3</hasAverageDelayDays>
    <hasCategory>자재</hasCategory>
    <hasDescription>협력업체 납기 지연 또는 자재 공급 차질</hasDescription>
    <hasDataSource>2020-2024 건조 프로젝트 25건 분석</hasDataSource>
</RootRisk>

<!-- 인력 부족 -->
<RootRisk rdf:about="#ManpowerShortage">
    <rdfs:label>인력부족</rdfs:label>
    <hasBaseProbability rdf:datatype="xsd:float">0.25</hasBaseProbability>
    <hasSeverity rdf:datatype="xsd:integer">3</hasSeverity>
    <hasCategory>인력</hasCategory>
</RootRisk>

<!-- 설계 변경 -->
<RootRisk rdf:about="#DesignChange">
    <rdfs:label>설계변경</rdfs:label>
    <hasBaseProbability rdf:datatype="xsd:float">0.15</hasBaseProbability>
    <hasSeverity rdf:datatype="xsd:integer">5</hasSeverity>
    <hasCategory>설계</hasCategory>
</RootRisk>

<!-- 악천후 -->
<RootRisk rdf:about="#BadWeather">
    <rdfs:label>악천후</rdfs:label>
    <hasBaseProbability rdf:datatype="xsd:float">0.20</hasBaseProbability>
    <hasSeverity rdf:datatype="xsd:integer">2</hasSeverity>
    <hasCategory>날씨</hasCategory>
</RootRisk>
```

### 4.2 Intermediate Risk 인스턴스
```xml
<!-- 블록 작업 지연 -->
<IntermediateRisk rdf:about="#BlockDelay">
    <rdfs:label>블록작업지연</rdfs:label>
    <causedBy rdf:resource="#MaterialDelay"/>
    <causedBy rdf:resource="#ManpowerShortage"/>
    <hasConditionalProbability>
        {
            "(True,True)": 0.85,
            "(True,False)": 0.60,
            "(False,True)": 0.55,
            "(False,False)": 0.10
        }
    </hasConditionalProbability>
    <hasSeverity rdf:datatype="xsd:integer">4</hasSeverity>
    <affectsProcess rdf:resource="#BlockFabrication"/>
</IntermediateRisk>

<!-- 재작업 -->
<IntermediateRisk rdf:about="#Rework">
    <rdfs:label>재작업</rdfs:label>
    <causedBy rdf:resource="#DesignChange"/>
    <causedBy rdf:resource="#BadWeather"/>
    <hasConditionalProbability>
        {
            "(True,True)": 0.75,
            "(True,False)": 0.50,
            "(False,True)": 0.30,
            "(False,False)": 0.05
        }
    </hasConditionalProbability>
</IntermediateRisk>
```

### 4.3 Cost Driver 인스턴스
```xml
<!-- 특근 투입 -->
<CostDriver rdf:about="#Overtime">
    <rdfs:label>특근투입</rdfs:label>
    <causedBy rdf:resource="#BlockDelay"/>
    <causedBy rdf:resource="#IdleTime"/>
    <hasBaseCost rdf:datatype="xsd:float">3.0</hasBaseCost>
    <hasCostMultiplier rdf:datatype="xsd:float">1.5</hasCostMultiplier>
    <hasMinCost rdf:datatype="xsd:float">2.5</hasMinCost>
    <hasMaxCost rdf:datatype="xsd:float">4.5</hasMaxCost>
    <hasDescription>
        야간/주말 특근 투입으로 인한 추가 인건비 및 관리비용
    </hasDescription>
</CostDriver>

<!-- 자재 손실 -->
<CostDriver rdf:about="#MaterialWaste">
    <rdfs:label>자재손실</rdfs:label>
    <causedBy rdf:resource="#Rework"/>
    <causedBy rdf:resource="#DesignChange"/>
    <hasBaseCost rdf:datatype="xsd:float">1.0</hasBaseCost>
    <hasCostMultiplier rdf:datatype="xsd:float">2.0</hasCostMultiplier>
    <hasMinCost rdf:datatype="xsd:float">0.5</hasMinCost>
    <hasMaxCost rdf:datatype="xsd:float">2.5</hasMaxCost>
</CostDriver>

<!-- 장비 임대 연장 -->
<CostDriver rdf:about="#EquipmentExtension">
    <rdfs:label>장비임대연장</rdfs:label>
    <causedBy rdf:resource="#BlockDelay"/>
    <causedBy rdf:resource="#BadWeather"/>
    <hasBaseCost rdf:datatype="xsd:float">2.0</hasBaseCost>
    <hasCostMultiplier rdf:datatype="xsd:float">1.3</hasCostMultiplier>
</CostDriver>
```

---

## 5. 필수 데이터 체크리스트

### ✅ Layer 1 (Ontology) 필수 요소
- [ ] **RiskFactor 클래스** 정의
- [ ] **CostDriver 클래스** 정의 (RiskFactor의 하위)
- [ ] **causes** 관계 (ObjectProperty)
- [ ] **hasBaseProbability** 속성 (Root Risk용)
- [ ] **hasConditionalProbability** 속성 (Intermediate Risk용)
- [ ] **hasBaseCost** 속성 (CostDriver용)
- [ ] **hasCostMultiplier** 속성 (CostDriver용)

### ✅ 각 Risk 인스턴스마다 필요한 정보
- [ ] **rdfs:label** - 한글 이름
- [ ] **확률 정보** - baseProbability 또는 conditionalProbability
- [ ] **부모 관계** - causedBy 관계 (Intermediate Risk인 경우)
- [ ] **심각도** - hasSeverity (선택적이지만 권장)
- [ ] **카테고리** - hasCategory (필터링/분석용)

### ✅ 각 CostDriver 인스턴스마다 필요한 정보
- [ ] **기본 원가** - hasBaseCost (억원)
- [ ] **비용 배수** - hasCostMultiplier
- [ ] **최소/최대 원가** - hasMinCost, hasMaxCost (Monte Carlo용)
- [ ] **원인 리스크** - causedBy 관계

---

## 6. Protégé에서 작성 순서

1. **클래스 계층 구조 먼저**
   - RiskFactor (최상위)
   - ├─ RootRisk
   - ├─ IntermediateRisk
   - └─ CostDriver

2. **Object Properties 정의**
   - causes (가장 중요!)
   - causedBy (역방향)
   - affectsProcess

3. **Data Properties 정의**
   - hasBaseProbability (필수)
   - hasConditionalProbability (필수)
   - hasBaseCost (필수)
   - hasCostMultiplier (필수)

4. **인스턴스 생성**
   - Root Risks 먼저 (자재지연, 인력부족 등)
   - Intermediate Risks (블록지연, 재작업 등)
   - Cost Drivers 마지막 (특근, 자재손실 등)

5. **관계 연결**
   - causes 관계로 리스크 체인 구성
   - 확률/원가 값 입력

---

## 7. 검증 SPARQL 쿼리

Ontology가 제대로 작성되었는지 확인하는 쿼리들:

```sparql
# 1. 모든 Root Risk와 확률 확인
SELECT ?risk ?label ?prob
WHERE {
    ?risk a :RootRisk .
    ?risk rdfs:label ?label .
    ?risk :hasBaseProbability ?prob .
}

# 2. 인과관계 체인 확인
SELECT ?parent ?child
WHERE {
    ?parent :causes ?child .
}

# 3. Cost Driver와 원가 정보 확인
SELECT ?driver ?label ?cost ?multiplier
WHERE {
    ?driver a :CostDriver .
    ?driver rdfs:label ?label .
    ?driver :hasBaseCost ?cost .
    ?driver :hasCostMultiplier ?multiplier .
}

# 4. 조건부 확률이 있는 리스크 확인
SELECT ?risk ?label ?cpt
WHERE {
    ?risk :hasConditionalProbability ?cpt .
    ?risk rdfs:label ?label .
}
```

---

## 8. 최종 파일 구조 예시

완성된 OWL 파일은 대략 이런 구조:

```
shipbuilding_risk.owl
├── Ontology Header (메타데이터)
├── Classes (10개)
│   ├── RiskFactor
│   ├── RootRisk
│   ├── IntermediateRisk
│   ├── CostDriver
│   └── ...
├── Object Properties (5개)
│   ├── causes ⭐
│   ├── causedBy
│   └── ...
├── Data Properties (10개)
│   ├── hasBaseProbability ⭐
│   ├── hasConditionalProbability ⭐
│   ├── hasBaseCost ⭐
│   ├── hasCostMultiplier ⭐
│   └── ...
└── Instances (20~50개)
    ├── Root Risks (4~10개)
    ├── Intermediate Risks (5~15개)
    └── Cost Drivers (3~10개)
```

---

## 요약: 반드시 있어야 할 것

**최소 필수 3가지:**
1. **causes 관계** - 리스크 체인 구성
2. **확률 정보** - hasBaseProbability + hasConditionalProbability
3. **원가 정보** - hasBaseCost + hasCostMultiplier

이 3가지만 제대로 있으면 시스템이 작동합니다!