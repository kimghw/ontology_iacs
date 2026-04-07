# 파일 명명 규칙

출력 파일 명명 패턴, 범위/단계/산출물 분류, 저장 경로, DocumentKey 슬러그 규칙을 정의한다.

> **유지보수 정책** — 프로젝트 개발 중 새로운 범위, 단계 또는 산출물이 추가될 때마다 이 문서를 갱신한다. 향후 이 규칙을 기반으로 파일명 검증 스크립트를 생성하여 자동 검증에 활용할 예정이다.

모든 출력 파일명은 이중 밑줄(`__`)로 구분된 3부분 패턴을 따른다.

```
{scope}__{phase}__{artifact}.{ext}
```

## Scope (범위)

| 접두어 | 용도 | 예시 |
|:---|:---|:---|
| `file-{source_file_key}` | 원본 입력 파일별 출력 (정규화) | `file-iacs_ur_2024__pre__normalised.md` |
| `doc-{doc_instance_key}` | 문서별 PRE 출력 (분할, 메타, 제목 추출) | `doc-ur_a2_rev5_en__heading__structure.tsv` |
| `documentSplit-{doc_instance_key}_s{NNN}` | 임시 documentSplit (병합 후 폐기) | `documentSplit-ur_a2_rev5_en_s001__heading__extraction_llm.tsv` |
| `doctype-{DocType}` | DocType별 공유 자산 | `doctype-UR__heading__grammar_v01.md` |
| `wu-{wu_key}` | WU별 실행 출력 | `wu-ur_e26_rev1_en__true_def__extracted_segments.tsv` |
| `corpus` | 전체 코퍼스 | `corpus__pre__manifest.json` |

## Phase (단계)

| 단계 | 설명 |
|:---|:---|
| `pre` | 사전 준비 — 문서 분할, 정규화, WU 패킹 |
| `heading` | 제목 구조 추출 |
| `true_def` | 정의 추출 |
| `applicability` | 적용 범위 추출 |
| `controlled_term` | 통제 용어 추출 |

## Artifact (주요 산출물)

| 산출물 | 설명 |
|:---|:---|
| `meta` | 메타데이터 JSON |
| `normalised` | 정규화된 텍스트 |
| `split` | 분할된 문서 |
| `structure` | 제목 구조 TSV |
| `regex_spec` | 정규식 명세 JSON |
| `grammar_candidate` | 문법 갱신 제안 |
| `chunk_plan` | 청크 경계 정의 JSON |
| `extraction_llm` | LLM 추출 결과 TSV |
| `extraction_script` | 스크립트 추출 결과 TSV |
| `discrepancy` | 불일치 로그 TSV (중간 산출물) |
| `discrepancy_final` | 최종 불일치 로그 TSV (승격됨) |
| `validated` | 검증된 TSV |
| `coverage` | 라인 수준 분류 감사 JSON |
| `manifest` | PRE 마스터 인덱스 |
| `document_manifest` | 문서 레지스트리 |
| `task_brief` | 작업 개요서 |
| `extracted_segments` | 추출된 세그먼트 |
| `patterns` | 패턴 카탈로그 |

## 저장 경로

| 경로 | 용도 |
|:---|:---|
| `results/temp/pre/` | 임시 출력 (승인 전) |
| `results/temp/pre/documentSplits/` | documentSplit 임시 출력 (병합 후 폐기) |
| `results/` | 영구 출력 (승인 후 승격) |
| `results/grammars/` | 확정된 제목 문법 |
| `results/grammars/staging/` | 문법 후보 (미확정, 재사용 불가) |

## DocumentKey 슬러그 규칙

문서 이름에서 DocumentKey를 결정론적으로 생성한다:

1. 소문자로 변환
2. 공백, 하이픈, 슬래시, 마침표를 `_`로 대체
3. `[a-z0-9_]` 범위 밖의 문자를 제거
4. 연속된 `_`를 하나의 `_`로 축약
5. 앞뒤의 `_`를 제거

| 입력 | 결과 |
|:---|:---|
| `UR A2` | `ur_a2` |
| `SOLAS II-1` | `solas_ii_1` |
| `KR Rules Pt.3 Ch.1` | `kr_rules_pt_3_ch_1` |
| `MARPOL Annex I` | `marpol_annex_i` |
