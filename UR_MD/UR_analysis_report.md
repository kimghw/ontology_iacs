# IACS Unified Requirements 전체 분석 보고서

> 분석 일자: 2026-03-31
> 대상: IACS UR 전체 문서 (284개, 54,837줄)
> 방법: 10개 청크 병렬 분석 후 종합

---

## 1. 문서 규모 총괄

| 시리즈 | 주제 | 유효 문서 수 | 삭제 문서 수 | 포함 청크 |
|--------|------|-------------|-------------|-----------|
| **A** | Anchoring, Towing, Mooring | 2 | 0 | 01 |
| **C** | Container Ships | 2 | 0 | 01 |
| **D** | Mobile Offshore Drilling Units | 8 | 2 | 01 |
| **E** | Electrical/Electronic | 17 | 6 | 01 |
| **F** | Fire Protection / Tanker Safety | 15 | ~20 | 01 |
| **G** | Gas Carrier Cargo Containment | 3 | 1 | 02 |
| **H** | Ammonia Fuel (신규) | 1(철회, Rev.1 대체 예정) | 0 | 02 |
| **I** | Polar Class | 3 | 0 | 02 |
| **K** | Propellers | 1 | 2 | 02 |
| **L** | Stability / Load Line | 3 | 2 | 02 |
| **M** | Machinery | ~35 | ~35 | 02, 03 |
| **N** | Navigation | 0 | 2 | 03 |
| **P** | Piping | 4 | 1 | 03, 04 |
| **S** | Strength (Hull Structure) | ~30 | 2 | 04, 05 |
| **W** | Materials & Welding | ~18 | 7 | 05, 06, 07 |
| **Z** | Surveys & Classification | ~25 | 5 | 07, 08, 09, 10 |

**총 284개 문서** (유효 ~166개 + 삭제 ~118개)

---

## 2. 요구사항(Requirements) 표현 패턴 - 전 시리즈 공통

### 2.1 의무 표현 계층

| 표현 | 강도 | 비고 |
|------|------|------|
| **"is to be" / "are to be"** | **가장 높은 빈도의 의무 표현** | IACS 고유의 표준 의무 표현. "shall"과 동등 |
| **"shall"** | 강한 의무 | 최신 문서(E26, E27, M87 등)에서 증가 추세 |
| **"must"** | 절대적 의무 | 안전 관련 항목에 한정적 사용 |
| **"is not to" / "shall not"** | 금지 | 상한/하한 제한, 금지 행위 |
| **"may"** | 허용/재량 | 검사관 재량, 조건부 완화 |
| **"should"** | 권고 | Annex/가이드라인에서 주로 사용 |

### 2.2 조건부 요구 패턴
- "Where..." / "When..." + 의무 표현 (조건부 요구)
- "unless..." + 의무 표현 (예외 조건)
- "provided that..." (조건 충족 시 대안 허용)
- "subject to..." (검토/승인 조건)
- "to the satisfaction of the Surveyor" (검사관 재량 판단)
- "as deemed necessary by the Surveyor" (검사관 판단에 따른 확장)

### 2.3 수치 기반 요구사항 패턴
- **"is not to be less than" + 공식**: 최소값 요구 (예: 두께, 단면계수)
- **"is not to exceed" + 수치**: 최대값 제한 (예: 응력, 비율)
- **"is to satisfy the following criterion" + 수식**: 수학적 판정 기준

### 2.4 시대별 변화
- **1970년대**: "must" 중심 (M2, M11, M12 등)
- **2000년대 이후**: "shall" + "is to be" 표준화
- **2020년대 최신**: "shall" 비중 증가 (E26, E27, M87, M88)

---

## 3. 산출물(Deliverables) 패턴 - 전체 유형 분류

### 3.1 인증서/증서 (Certificates)

| 산출물 | 관련 시리즈 | 설명 |
|--------|------------|------|
| Type Approval Certificate (TAC) | E, M, P, W | 형식승인 인증서 (장비, 엔진, 재료) |
| Product Certificate | M | 개별 제품 인증서 |
| Design Evaluation Certificate (DEC) | M | 제조자 평가 불가 시 TAC 대신 발급 |
| Classification Certificate | Z | 5년 주기 선급증서 갱신 |
| Certificate of Approval (서비스공급업체) | Z | NDT업체, 두께측정업체 등 승인 (3~5년 주기) |
| Material/Test Certificate | W | 재료 화학성분, 기계적 성질 인증 |
| Welder Qualification Certificate | W | 용접사 자격 인증서 (3년 주기) |
| Engine Certificate | M | 각 선박용 디젤엔진에 대해 발급 |

### 3.2 도면/계산서 (Drawings/Calculations)

| 산출물 | 관련 시리즈 | 설명 |
|--------|------------|------|
| 구조 강도 계산서 | S | 종강도, 전단력, 좌굴, 극한강도 |
| FE 해석 보고서 | S, I | 화물창, 해치커버, 프로펠러 등 |
| 설계 도면/배치도 | A, D, E, M, P | 장비 배치, 배관, 전기 계통도 |
| 적하 매뉴얼 (Loading Manual) | S | 설계 화물/밸러스트 조건 |
| Loading Instrument | S | 컴퓨터 기반 적하 계산기, 승인 대상 |
| 기어 하중능력 계산서 | M | ISO 6336 기반 |
| 빙하중 계산서 | I | Polar Class 전용 |
| 비틀림 진동 계산서 | M | 110kW 이상 발전기 세트 |
| 종강력 평가 계산서 | Z | 130m 이상 유조선(10년 이상) |
| 크랭크축 계산서 | M | UR M53에 따름 |

### 3.3 시험보고서 (Test Reports)

| 산출물 | 관련 시리즈 | 설명 |
|--------|------------|------|
| 형식시험 보고서 | E, M | 환경/EMC/성능 시험 (E10: 21개 항목) |
| NDT 보고서 | W, Z | RT, UT, PT, MT, PAUT, TOFD 결과 |
| 수압/기밀 시험 보고서 | G, P, Z | 배관, 탱크, 밸브 |
| 해상시운전 보고서 | M | 후진시험, 조타시험, 가스엔진 시험 |
| FAT 프로토콜 (공장인수시험) | M | 환경조건, 부하별 측정값 |
| 두께 측정 보고서 | Z | TM1~TM7 표준 양식 (선종별) |
| 취성균열정지 시험 보고서 | W | Kca/CAT 시험 결과 |
| 마모시험 보고서 | M | 선미관 베어링 합성재료 (M85) |
| 폭발시험 보고서 | M | 가스연료 ICE 방폭밸브 (M82) |
| WPQR (용접절차인정시험기록) | W | 용접절차 시험 결과 |
| 사이버 복원력 시험 보고서 | E | E26 전용 |
| 기계적 이음쇠 시험보고서 | P | 8종 시험 (기밀, 진동, 파열, 내화 등) |

### 3.4 매뉴얼/운영문서 (Manuals/Operational)

| 산출물 | 관련 시리즈 | 설명 |
|--------|------------|------|
| Operation & Maintenance Manual (OMM) | S, M | 선수문/선측문, 장비 등 |
| 사이버 보안 설계 설명서 | E | E26 전용, CBS 자산 목록 포함 |
| 사이버 보안 및 복원력 프로그램 | E | E26 전용 |
| 사고 대응 계획 (Incident Response Plan) | E | E26 전용 |
| 복구 계획 (Recovery Plan) | E | E26 전용 |
| Cargo Securing Manual | C | 컨테이너 고박 |
| 안전 개념서 (Safety Concept) | M | 가스연료 엔진 (M78) |
| 운전/정비 매뉴얼 | M | 엔진, 오일미스트 감지장비 등 |
| 래싱 소프트웨어 운영 매뉴얼 | C | C6 전용 |
| 보안 구성 가이드라인 | E | E27 전용 |

### 3.5 검사계획/보고서 (Survey Documents)

| 산출물 | 관련 시리즈 | 설명 |
|--------|------------|------|
| Survey Programme | Z | 선주+선급 공동 작성 검사계획 |
| Survey Report File | Z | 구조검사+두께측정+Executive Summary |
| Executive Hull Summary | Z | 특별검사 완료 시 발행, 선급 본사 확인 |
| Ship Construction File (SCF) | Z | SOLAS 대상 선박, 수명 동안 유지 |
| Survey Planning Questionnaire | Z | 선주가 작성하여 선급 제출 |
| Owner's Inspection Report | Z | 선주 자체 검사 기록 |
| Coating Technical File | Z | 도장기술파일 (Z23) |
| Cable Transit Seal Systems Register | Z | 수밀 케이블 관통부 대장 (Z28) |
| NDT 계획서 | W, Z | 검사 영역, 시험 범위, 품질 수준 |
| Shipyard Review Record | Z | 조선소 품질관리 평가 기록 (Z23) |

### 3.6 위험분석/평가 (Risk Assessment)

| 산출물 | 관련 시리즈 | 설명 |
|--------|------------|------|
| 사이버 리스크 평가서 | E | E26, CBS 제외 시 필수 |
| 위험 분석 보고서 | M | IEC 31010 기반 (M78 가스연료) |
| FMEA 보고서 | M | 배기가스 세정(M86), 엔진(M44) |

---

## 4. 문서 구조 패턴 - 전 시리즈 공통

### 4.1 표준 문서 골격

```
1. 문서 ID + 제목 + 개정 이력
2. Application (적용 범위)
3. Definitions (정의)
4. Technical Requirements (기술 요구사항)
5. Testing/Inspection (시험/검사)
6. Certification/Documentation (인증/문서)
7. Tables / Figures
8. Annexes / Appendices
9. Implementation Note (시행일 + PR No.29 참조)
10. "End of Document"
```

### 4.2 시행일 표준 문구 (거의 모든 문서 공통)

> *"This UR is to be uniformly implemented by IACS Societies on ships contracted for construction on or after [날짜]"*
> *"The 'contracted for construction' date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of 'contract for construction', refer to IACS Procedural Requirement (PR) No. 29."*

### 4.3 시리즈별 구조 특화

| 시리즈 | 구조 특화 패턴 |
|--------|---------------|
| **S** (강도) | 수학 공식 중심, Net scantling 접근법, 허용응력/좌굴 판정, Annex에 상세 계산법 |
| **W** (재료) | 화학성분표 → 기계적성질표 → 열처리 → 시험 → 인증 순서 |
| **Z** (검사) | Special(5년)/Annual(매년)/Intermediate(2.5년) 3단계, 선령별 단계적 강화 |
| **M** (기관) | 설계 → 형식시험 → FAT → 선상시험 4단계 프로세스 |
| **E** (전기) | 최신 문서는 Goal-based 5기능 (Identify-Protect-Detect-Respond-Recover) |
| **P** (배관) | Class I/II/III 등급별 차등 요구, 재료-용접-NDT-수압시험 순서 |
| **I** (극지) | PC1~PC7 7단계 등급, Class Factor 차등, 구조+기관 통합 |
| **G** (가스선) | 탱크 유형별(적분형/멤브레인/독립형A,B,C) 세분화 설계기준 |

---

## 5. 핵심 패턴 및 메커니즘

### 5.1 생애주기별 요구사항 분포

```
설계(Design)     → S(강도계산), I(빙하중), M(엔진설계), E(사이버보안설계)
                   G(탱크설계), P(배관설계), D(MODU 설계)

제조(Build)      → W(재료/용접), P(배관 시공), Z23(신조선 검사)
                   W28(용접절차인정), W32(용접사 자격)

시험(Test)       → E10(형식시험), M71(엔진 형식시험), M88(선상시운전)
                   W28(용접절차인정시험), M51(FAT)

인증(Certify)    → M87(엔진인증체계), W(재료인증), Z26(대안인증)
                   Z17(서비스공급업체 승인)

운항(Operate)    → Z(주기검사), Z20(PMS), Z27(CBM), Z29(원격검사)
                   E26(사이버복원력 운영), Z13(항해 중 수리)
```

### 5.2 참조 체계 (3계층)

**1단계 - IACS 내부:**
- UR 간 상호참조 (예: M87→M44→M71→M72→M51→M88)
- IACS Recommendations (Rec. 10, 39, 42, 68, 69, 76, 87, 120, 148, 166 등)
- IACS Procedural Requirements (PR 1C, 6, 7, 29, 35, 37)

**2단계 - 국제표준:**
- ISO 시리즈 (5817, 6336, 9712, 15614, 17636, 19921 등)
- IEC 시리즈 (60068, 60079, 60092, 60533, 61000, 62443)
- ASTM, ASME, BS, CISPR 등

**3단계 - IMO 협약:**
- SOLAS (Chapter II-1, II-2, XII)
- MARPOL (Annex I, VI)
- IGC/IGF/IBC Code
- Polar Code
- International Convention on Load Lines (ICLL) 1966/1988
- ISM Code, ISPS Code
- IMO MODU Code 2009
- BWM Convention

### 5.3 핵심 메커니즘

| 메커니즘 | 설명 | 관련 시리즈 |
|----------|------|------------|
| **선령별 단계적 강화** | 5/10/15년 기준 검사 범위 확대 | Z |
| **코팅 상태 연동** | GOOD/FAIR/POOR에 따라 검사 범위 조정 | Z |
| **Severity Zone (A/B/C)** | 구역별 차등 검사/수리 기준 | W |
| **배관 등급 분류** | Class I/II/III (압력/온도/매체별) | P |
| **CSR 이중체계** | CSR 선박과 비CSR 선박 구분 적용 | S, Z |
| **제조소 승인** | 5년 주기 갱신, 재시험 프로그램 | W |
| **Polar Class 등급** | PC1~PC7, Class Factor 차등 | I |
| **Net Scantling 접근법** | 부식여유를 감한 순 두께로 강도 평가 | S |
| **5년 주기 선급증서 갱신** | Special Survey 완료 시 갱신 | Z |
| **검사관 재량권** | "to the satisfaction of the Surveyor" | Z 전반 |

---

## 6. 시리즈별 상세 특성

### 6.1 A 시리즈 - Anchoring, Towing, Mooring
- **범위**: 500GT 이상 재래형 선박의 예인/계류 장치
- **핵심**: SWL/TOW 마킹 의무, FEM 해석 요건, 윈들러스 설계/시험
- **산출물**: 배치도, 강도 계산서, 시험보고서

### 6.2 C 시리즈 - Container Ships
- **범위**: 컨테이너 전용선 화물 고박 시스템
- **핵심**: 래싱 소프트웨어 기능/정확도, 고박장치 형식시험
- **적용**: 2025년 7월 이후 건조계약 선박

### 6.3 D 시리즈 - Mobile Offshore Drilling Units
- **범위**: 이동식 해양 시추장치 전반 (D1~D11 완결 체계)
- **핵심**: 유형별(자기부양식/칼럼안정형/수면형) 특수 요건
- **운전모드**: Operating / Severe storm / Transit 개념

### 6.4 E 시리즈 - Electrical/Electronic
- **범위**: 전기/전자 장비, 케이블, 사이버 복원력
- **핵심**: E10(형식시험 21개 항목), E26/E27(사이버 복원력)
- **E26 구조**: Goal-based 5기능 (Identify-Protect-Detect-Respond-Recover)
- **E27**: 30개 필수 보안 기능 + 11개 추가 기능, SDLC 준수

### 6.5 F 시리즈 - Fire Protection / Tanker Safety
- **범위**: 탱커 안전, 소방, 방폭, 배관
- **특징**: 가장 오래된 문서 다수 (1971년~), 삭제 비율 매우 높음
- **유효 문서**: F15(밸러스트 배관), F20(IG 시스템), F44(선수피크), F45(BWMS) 등

### 6.6 G 시리즈 - Gas Carrier Cargo Containment
- **범위**: 액화가스 화물격납장치 및 배관
- **핵심**: 탱크 유형별 세분화 설계기준, IGC Code 연계
- **G5**: ESD 밸브 Fail-Close 기능 (2022년 신규)

### 6.7 I 시리즈 - Polar Class
- **범위**: 극지 운항 선박 (구조 + 기관)
- **핵심**: PC1~PC7 7단계, 빙하중 계산 공식, 피라미드 강도 원칙
- **특징**: 매우 상세한 수학적 공식 (빙하중 계산, Miner's Rule 피로평가)

### 6.8 M 시리즈 - Machinery
- **범위**: 기관 전반 (엔진, 축계, 기어, 조타장치, 보조기관)
- **핵심**: M87(엔진 인증 프레임워크), M78(가스연료 엔진), M44(도면승인)
- **특징**: 가장 많은 문서 수, 2015년 대규모 통합
- **최신**: M87/M88(2025) - 엔진 인증 체계 재정비

### 6.9 P 시리즈 - Piping
- **범위**: 배관 설계, 시공, 시험
- **핵심**: P2(13개 하위 섹션으로 포괄적 규정), Class I/II/III 분류
- **특징**: ISO/ASME 광범위 참조, 정량적 시험 기준

### 6.10 S 시리즈 - Strength (Hull Structure)
- **범위**: 선체 구조 강도 전반
- **핵심**: S11/S11A(종강도), S10(타), S35(좌굴), S21(해치커버)
- **특징**: 수학 공식 풍부, CSR 적용 제외 명시, 벌크선 관련 UR 다수

### 6.11 W 시리즈 - Materials & Welding
- **범위**: 재료 사양, 용접 절차, NDT
- **핵심**: W11(선체구조강), W16(고장력강), W22(계류체인), W28(용접절차인정)
- **특징**: 제조-검사-수리 프로세스 규정, 추적성(Traceability) 강조

### 6.12 Z 시리즈 - Surveys & Classification
- **범위**: 검사 및 인증 전반
- **핵심**: Z10.1~Z10.5(선종별 선체검사), Z23(신조선 검사), Z7(기본 선체검사)
- **특징**: 5년 주기 체계, 선령별 단계적 강화, 코팅 상태 연동
- **최신**: Z29(원격검사), Z27(CBM/상태감시)

---

## 7. 종합 관찰

### 7.1 문서 성숙도 차이
- 1971년 단문 규정(F1, F3 등 1-2문단)부터 2024년 수십 페이지 체계적 규정(E26, Z10.2)까지 폭넓게 공존
- 최신 문서일수록 구조가 정교 (E26/E27: Requirement - Rationale - Details - Demonstration 반복 구조)

### 7.2 삭제 문서 비율
- 전체 ~42% 삭제: IMO 규정 발전에 따른 통합/삭제
- F 시리즈: 삭제 비율 최고 (~60%)
- M 시리즈: 2015년 대규모 통합으로 다수 삭제

### 7.3 상호참조 밀도
- W↔Z: 건조 단계 품질보증(W) ↔ 운항 단계 상태유지(Z) 연계
- M 내부: M87→M44→M71→M72→M51→M88 체인 구조
- S↔Z: 강도 기준(S) ↔ 검사 시 적용(Z) 연계
- E26↔E27: 선박 수준(E26) ↔ 시스템/장비 수준(E27) 연계

### 7.4 최신 기술 반영 추세
- **사이버보안**: E26/E27 (2023), IEC 62443 기반
- **원격검사**: Z29 - 라이브 스트리밍, AI/IoT 검증 소프트웨어
- **상태감시**: Z27 - AI/ML/IoT 기반 CBM
- **가스연료**: M78(천연가스), M82(가스연료 방폭), H1(암모니아, 철회 후 재발행 예정)
- **디지털**: L5(복원성 소프트웨어), C6(래싱 소프트웨어)

---

## 부록: 청크별 시리즈 배분

| 청크 | 줄 수 | 시리즈 | 문서 수 |
|------|-------|--------|---------|
| 01 | 5,463 | A, C, D, E, F | 83 |
| 02 | 5,526 | G, H, I, K, L, M | 29 |
| 03 | 5,369 | M, N, P | 68 |
| 04 | 5,504 | P, S | 16 |
| 05 | 5,787 | S, W | 28 |
| 06 | 5,272 | W | 17 |
| 07 | 5,599 | W, Z | 13 |
| 08 | 6,315 | Z (Z10.1, Z10.2) | 2 |
| 09 | 4,354 | Z | 23 |
| 10 | 5,649 | Z | 5 |
