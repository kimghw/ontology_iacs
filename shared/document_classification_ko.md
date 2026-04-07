# 문서 분류

원천 문서(IACS, IMO, KR, EU 해사 규정)에서 추출한 분류 체계 및 구조 패턴 정의.

> **작성 방침** — 본 문서는 원천 문서 분석이 완료된 후 그 결과를 반영하여 작성한다. 새로운 Authority, DocType 또는 Source Family가 식별되면 해당 항목을 추가한다.

## Authority

규정을 발행하는 기관 또는 규제 프레임워크.

| Authority | 설명 |
|:---|:---|
| **IACS** | International Association of Classification Societies |
| **IMO** | International Maritime Organization |
| **KR** | Korean Register of Shipping |
| **EU** | European Union maritime legislation |

## DocType

각 Authority 내 문서 유형 분류.

| Authority | DocType | 설명 |
|:---|:---|:---|
| IACS | `UR` | Unified Requirements |
| IACS | `UI` | Unified Interpretations |
| IACS | `Rec` | Recommendations |
| IACS | `PR` | Procedural Requirements |
| IMO | `SOLAS` | Safety of Life at Sea |
| IMO | `MARPOL` | Marine Pollution Prevention |
| KR | `Rules` | Classification Rules |
| EU | `Directive` | EU Directives |
| EU | `Regulation` | EU Regulations |

## Source Family(예시)

DocType의 상위 그룹. 분할 기준, 문법 선택 및 정규화 규칙을 결정한다.

| Source Family | 포함 DocType | 문서 경계 기준 |
|:---|:---|:---|
| **IACS UR/UI/Rec/PR** | UR, UI, Rec, PR | 1 파일 = 1 문서. 복수 문서 또는 중복 내용 → 사용자 에스컬레이션. |
| **IMO Conventions** | SOLAS, MARPOL | 1 Chapter 또는 Annex = 1 문서 |
| **KR Rules** | Rules | 1 Part + Chapter = 1 문서 |
| **EU Legislation** | Directive, Regulation | 1 Directive / Regulation = 1 문서 |

## Heading Level

문서 내부의 구조적 계층. 사용되는 레벨 명칭은 Source Family에 따라 다르다.

### IACS

```
Document → Part → Section → Paragraph → Sub-paragraph
```

### IMO (SOLAS/MARPOL)

```
Document → Part → Chapter → Regulation → Paragraph
```

### KR Rules

```
Document → Part → Chapter → Section → Paragraph
```

### EU Legislation

```
Document → Title → Chapter → Article → Paragraph
```

> Heading level 명칭은 각 Source Family의 문법에서 정의된다. 위의 계층 구조는 대표적인 패턴이며, 실제 문서에 따라 다를 수 있다.
