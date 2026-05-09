# LG Innotek 카메라 모듈 제조 공정과 설비 보고서

## 1 서론

LG 이노텍의 카메라 모듈 공정은 스마트폰·자동차 분야에서 세계적 경쟁력을 갖는다. 본 보고서는 LG 이노텍에 공개된 정보(청정 생산 환경, 액티브 얼라인 공정, 다층 검사, 신뢰성 시험 등)를 바탕으로, 자동차와 스마트폰에 사용되는 **범용 카메라모듈 제조 공정**을 조사하고 여러 제조업체의 사례(삼성, Camemake, Trioptics, Nordson 등)와 비교하였다. 이를 통해 **전반적인 공정 흐름**과 **공정별 핵심 설비**를 정리하고, 이후 온톨로지(owl rdf/xml) 구축의 기초 자료로 삼는다.

## 2 LG 이노텍 공정 특징 및 AI 혁신

### 2.1 청정 제조 환경

- LG 이노텍의 카메라모듈 공정은 반도체 수준의 청정도를 요구한다. 작업자는 먼지 한 점이 제품 수율을 좌우하기 때문에 **호흡도 조심**하며 조립과 검사를 수행한다는 보도가 있다[11](https://www.trioptics.com/applications/alignment-and-testing-of-optoelectronic-systems/active-alignment-and-assembly-of-camera-modules).  부품을 작은 컨테이너로 전달할 때도 **이물질 유입을 철저히 차단**한다[11](https://www.trioptics.com/applications/alignment-and-testing-of-optoelectronic-systems/active-alignment-and-assembly-of-camera-modules).

### 2.2 액티브 얼라인 및 다층 검사

- 이미지 센서와 렌즈를 정밀하게 맞추기 위해 **액티브 얼라인** 공정이 적용된다. 자동 장비가 렌즈와 센서를 움직여 최적 초점을 맞추고 UV 접착제를 경화한다[9](https://dothecamera.com/whats-the-journey-of-a-camera-module-from-wafer-to-finished-product/#What_Final_Tests_Guarantee_a_Flawless_Camera_Module).  
- 조립 후에는 **용접 상태, 색조, OIS 정확도, 화질** 등을 확인하는 내부 검사와 최종품질 검사가 진행되며, 각 검사 후 불량품을 즉시 선별해 수율을 높인다[9](https://dothecamera.com/whats-the-journey-of-a-camera-module-from-wafer-to-finished-product/#What_Final_Tests_Guarantee_a_Flawless_Camera_Module).  
- 출하 전에는 먼지 시험기·고온·저온 챔버·진동·낙하 시험기 등으로 **신뢰성 시험**을 수행하여 다양한 환경에서 성능을 검증한다[9](https://dothecamera.com/whats-the-journey-of-a-camera-module-from-wafer-to-finished-product/#What_Final_Tests_Guarantee_a_Flawless_Camera_Module).

### 2.3 AI 기반 공정 혁신

- LG 이노텍은 2024년에 **AI 기반 공정 레시피**를 도입하여 수천만건의 실험·생산 데이터를 학습한 모델로 최적 공정을 찾는다. 이에 따라 신제품 공정 조건을 찾는 시간이 72시간에서 6시간으로 단축되고 특정 공정의 불량률이 90 % 감소했다고 발표하였다(회사 뉴스). 
- 2025년 인텔과의 협력으로 판형(Intel) CPU와 GPU를 탑재한 **AI 비전 검사 시스템**이 도입되어 생산라인에서 즉시 불량 데이터를 분석하고 딥러닝 모델을 훈련할 수 있다. 이러한 구조는 AI 검사를 다른 생산라인으로 쉽게 확장할 수 있게 한다.

## 3 일반 카메라 모듈 제조 공정

이 장에서는 카메라 모듈의 전반적인 제조 흐름을 정리한다. 공정 순서는 제조사마다 차이가 있으나, 일반적으로 다음 단계로 구성된다.

### 3.1 웨이퍼 도징과 이미지 센서 제조

1. **웨이퍼 도싱 및 칩 분할** – 카메라의 핵심인 이미지 센서는 큰 실리콘 웨이퍼에서 대량으로 만든다. 웨이퍼는 초정밀 절단 장비로 **수천 개의 센서 칩으로 분리**되며, 각 칩은 청정 환경에서 세척·검사되어 결함을 선별한다[8](https://dothecamera.com/whats-the-journey-of-a-camera-module-from-wafer-to-finished-product/).
2. **칩온보드(COB) 조립** – 분리된 센서 칩을 PCB 기판에 접착하고 **금선(wire bonding)**으로 전기 패드를 연결한다. 연결된 금선은 에폭시로 encapsulation하여 외부 충격과 습기로부터 보호한다[8](https://dothecamera.com/whats-the-journey-of-a-camera-module-from-wafer-to-finished-product/).  
   - CSP(CSP/Chip Scale Package) 센서는 SMT 리플로우 공정에 바로 실장되기도 한다[3](https://www.camemake.eu/inside-the-camemake-factory).

### 3.2 회로 보드(SMT) 조립

- 이미지 센서 외에도 ISP(이미지 신호 프로세서), 드라이버 IC, 저항·커패시터 등이 PCB에 실장된다. 이를 위해 **솔더 페이스트 인쇄**, **고속 픽앤플레이스**, **리플로우 솔더링**, **AOI 검사**, **X‑ray 검사**를 거친다[3](https://www.camemake.eu/inside-the-camemake-factory).  
- 리플로우 후 보드는 **초음파 또는 플라즈마 세정**으로 잔류 플럭스를 제거하고, 보드 불량을 최소화한다[3](https://www.camemake.eu/inside-the-camemake-factory).

### 3.3 렌즈 제조와 모터 부품

1. **렌즈 제조** – 광학 유리 또는 플라스틱을 성형(mold)하고, 다단계 연마 및 **코팅**을 통해 렌즈를 만든다. 표면 결함을 검사하여 불량 렌즈를 제거한다[7](https://www.sinoseen.com/camera-manufacturing-process-from-design-to-productiona-step-by-step-guide).  렌즈 제조는 카메라 제조사의 핵심 경쟁력으로 공개 정보가 적지만, 일반적으로 몰드 성형→연마→코팅→검사 순으로 진행된다.
2. **VCM 조립 및 OIS 모듈** – 자동 초점과 손떨림 보정을 위해 **보이스 코일 모터(VCM)**와 **OIS 모듈**이 렌즈 홀더에 통합된다. 정밀한 자석·코일·스프링을 조립하고, **MEMS 기반 OIS 장치**를 장착한다[6](https://www.hcdpcba.com/blog/camera-module-assembly-factory).  VCM 조립은 매우 작은 틀과 정밀 인라인 검사를 필요로 한다.

### 3.4 렌즈 및 필터 조립

- 이 단계는 이미지 품질을 좌우한다. 렌즈 홀더와 렌즈 스택을 **청정실(Class 100–1000)**에서 조립하며, 렌즈와 센서를 임시 접착제로 고정한 뒤 **액티브 얼라인 방식**으로 초점을 맞춘다[3](https://www.camemake.eu/inside-the-camemake-factory). 
- **IR‑컷 필터**나 IR‑패스 필터를 결합하고, **광학 접착제**를 정밀하게 도포한 뒤 UV 또는 열을 이용해 **프리 큐어(pre‑cure)**와 **열 경화**를 진행한다[3](https://www.camemake.eu/inside-the-camemake-factory). 설계에 따라 블랙 코팅된 접착제는 외부 광 유입을 차단한다[10](https://www.dexerials.jp/en/products/adhesive/sa2300.html).

#### 3.4.1 액티브 얼라인 공정

- **라이브 이미지를 보면서 6 자유도(6‑DOF)**로 렌즈를 조절하여 가장 높은 MTF·SFR 값을 찾는다[3](https://www.camemake.eu/inside-the-camemake-factory)[9](https://dothecamera.com/whats-the-journey-of-a-camera-module-from-wafer-to-finished-product/#What_Final_Tests_Guarantee_a_Flawless_Camera_Module).  이는 렌즈의 **이동(x, y, z)**과 **기울기(roll/pitch) 및 회전(yaw)**을 조절하는 로봇 플랫폼을 이용해 수행한다[5](https://www.vvdntech.com/en-us/blog/precision-in-every-pixel-the-role-of-active-alignment-in-high-performance-camera-manufacturing/).  
- 최적 위치가 결정되면 **초고속 UV 광**으로 접착제를 부분 경화하고, 전체 부위가 그림자인 영역까지 완전 경화하도록 열 처리를 한다. Addison Clear Wave와 Dexerials 등은 **UV + 열 이중 경화(dual‑cure) 에폭시**를 제공한다. 이 접착제는 렌즈·센서를 임시 고정한 후 주위의 그늘진 부분까지 열로 완전 경화하여 위치를 안정시키며, 단일 성분 에폭시라 내부 불균일 경화를 방지한다[4](https://www.addisoncw.com/applications/camera-module-adhesives/).  Dexerials의 SA2300 시리즈는 UV 경화 후 80 °C에서 60 분 이상 열경화하여 음영 영역까지 완전 경화시키며, 검은색 수지로 하우징 내부의 빛 유입을 감소시킨다[10](https://www.dexerials.jp/en/products/adhesive/sa2300.html).

### 3.5 초점 조정 및 접착

- 렌즈를 6 자유도로 조절한 뒤, **초점 조정(Focus adjustment)** 을 위해 자동화된 포커스 기기가 렌즈를 구동하며 라이브 이미지의 MTF를 최대화한다[3](https://www.camemake.eu/inside-the-camemake-factory).  렌즈 위치가 결정되면 UV 접착제와 열경화로 영구 고정하며, 일부 프로토타입에서는 수동으로 초점을 맞추기도 한다[3](https://www.camemake.eu/inside-the-camemake-factory).

### 3.6 광학 및 전자 보정

- **이미지 품질 보정** – 모듈 조립 후 렌즈의 수차·시야각·대비 등을 측정하고 화이트밸런스, 렌즈 셰이딩(LSC), 왜곡 계수(LGD/TV distortion) 등을 보정한다[3](https://www.camemake.eu/inside-the-camemake-factory)[2](https://www.trioptics.com/products/camtest-camera-modules-testing/#products).  
- **센서 특성 측정** – 화소 결점, FPN(고정 패턴 노이즈), OECF, 상대 조도(Relative Illumination), 동적 범위 등을 측정하기 위해 **적분구(integrating sphere)**와 테스트 차트를 사용하는 기기(CamTest Spectral)가 사용된다[2](https://www.trioptics.com/products/camtest-camera-modules-testing/#products).   
- **MTF/초점 측정** – Trioptics의 CamTest Focus 장비는 1 m~무한대의 거리를 가상으로 투사하는 **전동 콜리메이터**로 렌즈의 MTF, SFR, 초점면 기울기, 보어사이트 이동 등을 측정한다[2](https://www.trioptics.com/products/camtest-camera-modules-testing/#products). CamTest MTF 시스템은 한 번의 측정으로 MTF, SFR, ESF를 확인하여 대량 생산 시 최종 품질 검사를 수행한다[2](https://www.trioptics.com/products/camtest-camera-modules-testing/#products).

### 3.7 기능 시험 및 전기적 테스트

- **기능 및 화질 테스트** – 모듈이 완전히 조립되면 해상도, 노출, HDR/WDR 지원, 자동초점 및 OIS 성능, 통신 안정성 등 기능을 검사한다[3](https://www.camemake.eu/inside-the-camemake-factory). 아울러 IR‑패스·IR‑컷 필터의 특성도 확인한다[3](https://www.camemake.eu/inside-the-camemake-factory).
- **온도·환경 조건에서 테스트** – CamTest TempControl은 –40 °C부터 +120 °C까지 다양한 온도에서 카메라 모듈의 이미지 품질 변화를 측정한다[2](https://www.trioptics.com/products/camtest-camera-modules-testing/#products). 카메라 모듈은 온도 변화에 따른 초점 이동 및 이미지 평면 기울기 변화를 데이터베이스에 저장하여 설계 개선에 활용한다[2](https://www.trioptics.com/products/camtest-camera-modules-testing/#products).

### 3.8 신뢰성/환경 시험

- **먼지 시험** – 미세분진이 광로에 영향을 미치는지 확인하기 위해 먼지 시험기를 사용한다[9](https://dothecamera.com/whats-the-journey-of-a-camera-module-from-wafer-to-finished-product/#What_Final_Tests_Guarantee_a_Flawless_Camera_Module).  
- **고온·저온 및 습도 챔버** – 제품이 –40 °C~+120 °C의 온도와 다양한 습도 조건에서 정상 동작하는지 확인한다[2](https://www.trioptics.com/products/camtest-camera-modules-testing/#products).  
- **진동·충격/낙하 시험** – 진동 플랫폼과 낙하(tumble) 시험기를 사용하여 외부 충격/진동에 대한 내성을 검증한다[9](https://dothecamera.com/whats-the-journey-of-a-camera-module-from-wafer-to-finished-product/#What_Final_Tests_Guarantee_a_Flawless_Camera_Module). ASLI의 THV‑1000 장비는 온도, 습도, 진동을 동시에 부여하는 환경 시험 시스템으로 3–15 °C / 분의 빠른 온도변화와 다양한 진동 조건을 지원한다[1](https://aslitestequipment.com/product/temperature-humidity-vibration-combined-test-system/comprehensive-vibration-temperature-and-humidity-testing-equipment/).  
- **기타 시험** – 염수분무, ESD, 방사선 등 제품 적용 분야에 따라 추가 시험을 실시한다.

### 3.9 포장 및 출하

- 모든 시험을 통과한 모듈은 추적성이 보장된 포장 시스템으로 개별 포장·라벨링 후 출하된다. 생산 추적을 위해 바코드 또는 QR 코드로 불량 여부와 공정 데이터를 기록한다[3](https://www.camemake.eu/inside-the-camemake-factory).

## 4 공정별 주요 설비 목록

| 공정 단계 | 주요 설비 및 기술 | 출처 |
| --- | --- | --- |
| **웨이퍼 도징·세정** | 웨이퍼를 절단하는 **도싱(dicing) 장비**, 세정기 및 자동 칩 검사 시스템 | 웨이퍼를 개별 센서 칩으로 분리하고 청정 환경에서 세척·검사함[8](https://dothecamera.com/whats-the-journey-of-a-camera-module-from-wafer-to-finished-product/) |
| **칩온보드(COB)/CSP** | **다이 본더(die bonder)**·**와이어 본더**, **에폭시 디스펜서**, **엔캡슐레이션 장비**; CSP의 경우 재흘로 리플로우 장비 | 센서를 PCB에 붙이고 금선으로 접속한 뒤 에폭시로 보호[8](https://dothecamera.com/whats-the-journey-of-a-camera-module-from-wafer-to-finished-product/) |
| **SMT 보드 조립** | 솔더 페이스트 프린터, 고속 **픽앤플레이스**, **리플로우 오븐**, **AOI**, **X‑ray 검사**, **초음파/플라즈마 세정기** | SMT 공정을 통한 다른 부품 실장 및 세정[3](https://www.camemake.eu/inside-the-camemake-factory) |
| **렌즈 제조** | 몰드 프레스, 렌즈 연마기, 소형 코팅 장비, 검사기 | 렌즈를 성형·연마·코팅하여 품질 검사[7](https://www.sinoseen.com/camera-manufacturing-process-from-design-to-productiona-step-by-step-guide) |
| **VCM/OIS 모듈 조립** | 미세 전자석 조립 장비, 자석·코일 조립기, 고해상도 검사 장비, MEMS OIS 삽입기 | AF 및 OIS를 위한 보이스 코일 모터 조립 및 검사[6](https://www.hcdpcba.com/blog/camera-module-assembly-factory) |
| **렌즈·센서 조립 및 액티브 얼라인** | **액티브 얼라인 시스템**(6 자유도 조정), **접착제 디스펜서**, **UV LED/열경화 장비** | 라이브 이미지를 기반으로 센서와 렌즈를 정밀하게 맞춘 후 UV 및 열로 접착제를 경화[5](https://www.vvdntech.com/en-us/blog/precision-in-every-pixel-the-role-of-active-alignment-in-high-performance-camera-manufacturing/)[4](https://www.addisoncw.com/applications/camera-module-adhesives/) |
| **초점 조정 및 고정** | 자동 포커싱 기기, 전동 콜리메이터, 고속 화질 분석 소프트웨어 | 렌즈를 구동하여 최적 초점을 찾은 뒤 접착제로 고정[3](https://www.camemake.eu/inside-the-camemake-factory) |
| **보정/시험 장비** | **MTF/SFR 측정장비(CamTest Focus/MTF)**, **왜곡 측정 장비(CamTest Chart)**, **센서 특성 장비(CamTest Spectral)**, **적분구** | MTF, SFR, 이미지 면 기울기, 왜곡, 색재현성, 상대 조도 등을 측정[2](https://www.trioptics.com/products/camtest-camera-modules-testing/#products) |
| **환경·신뢰성 시험** | 온도·습도·진동 복합 챔버(THV‑1000), 먼지 시험기, 진동·낙하 시험기(tumbler) | 가혹 환경에서 카메라 모듈을 테스트하며, THV‑1000은 온도·습도·진동을 동시에 시뮬레이션[1](https://aslitestequipment.com/product/temperature-humidity-vibration-combined-test-system/comprehensive-vibration-temperature-and-humidity-testing-equipment/) |

## 5 정비 및 시험 설비 관리

카메라 모듈 제조는 정밀한 설비를 요구하며 정기적 관리·보정이 필수적이다.

- **세정 장비** – 렌즈·센서·커버 글래스는 초음파, 플라즈마, 이온수 세정장비를 이용해 세척한다. 이물질이 남으면 접착·얼라인 과정에서 수율이 크게 떨어지므로 설비 유지관리가 중요하다.
- **광학 조정 장비** – 액티브 얼라인 시스템과 디스펜서, UV 경화 장비는 주기적으로 **정렬(calibration)**을 수행해야 한다. 센서 위치 오류와 접착제 도포량 오차를 최소화하기 위해 모션 제어 축과 광학 센서를 점검한다.
- **환경 시험 장비** – 온도·습도 챔버, 진동·낙하 시험기는 정기적으로 센서와 PID 제어 시스템을 점검하여 정확한 환경 조건을 재현해야 한다. 시험 규격(예: IEC 60068)과 국제 자동차 표준(AEC‑Q100)을 준수하는지 확인한다.

## 6 온톨로지 설계 개요

본 보고서를 기반으로 **카메라 모듈 제조 온톨로지**를 설계할 때 다음 요소를 고려하였다.

- **클래스(Classes)**: `ManufacturingProcess`, `ProcessStep`, `Equipment`, `Component`, `Test`, `Material` 등. 
- **개체(Individuals)**: `WaferDicing`, `SensorAssembly`, `SMTAssembly`, `LensManufacturing`, `VCMAssembly`, `ActiveAlignment`, `FocusAdjustment`, `OpticalCalibration`, `ReliabilityTesting` 등이 `ProcessStep`에 속한다. 각 공정은 `usesEquipment` 속성으로 설비에 연결된다. 
- **관계(Object Properties)**: `hasSubProcess` (공정 → 하위 공정), `usesEquipment` (공정 → 장비), `involvesComponent` (공정 → 부품), `performedInEnvironment` (시험 → 환경), `precedes` (공정 순서) 등을 정의한다.
- **데이터 속성(Data Properties)**: 장비의 정밀도, 온도 범위, 경화시간 등 수치 데이터를 표현하는 속성을 포함한다.

이 온톨로지는 카메라 모듈 공정의 계층적 구조와 공정–설비–부품 간 관계를 표현함으로써, 공정 지식 관리나 AI 기반 최적화 시스템 구축에 활용될 수 있다.

## 7 결론

LG 이노텍의 카메라 모듈 공정은 청정 환경과 액티브 얼라인, 다층 검사, 신뢰성 시험 등을 통해 높은 품질을 달성하고 있으며, 최근에는 AI 알고리즘으로 공정을 최적화하고 있다. 본 보고서는 공개 자료와 경쟁사의 공정을 분석하여 **일반적인 카메라 모듈 제조 흐름과 장비 목록**을 정리하였다. 또한, UV + 열 이중경화 접착제와 6 자유도 액티브 얼라인 장비, 환경 시험 장비 등 주요 설비를 제시하고, 이 지식을 온톨로지 구조로 전환하는 방법을 간략히 소개하였다. 이 자료가 카메라 모듈 공정 최적화와 설비 투자 계획 수립에 참고가 되기를 기대한다.
