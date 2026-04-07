# 프로젝트 정의

전체 파이프라인에서 공유하는 식별자 체인, 토큰 측정 기준, 처리 단위, 승인 상태를 정의한다.

> **유지보수 정책** — 프로젝트 개발 중 식별자, 측정 기준 또는 용어가 변경될 때마다 이 문서를 업데이트한다. 파이프라인 단계가 추가되거나 수정되면 용어 섹션도 함께 업데이트한다.

> 도메인 분류 체계(Authority, DocType, Source Family, Heading Level)는 `document_classification.md`를 참조한다.

## 식별자 체인

> Authority → DocType → Document 분류는 `document_classification.md`에 정의되어 있다. 아래 체인은 **키 생성 규칙**만을 다룬다.

| 수준 | 식별자 | 형식 | 고유성 | 예시 |
|:---|:---|:---|:---|:---|
| Document | `DocumentKey` | Slug 규칙 적용 (리비전 독립). `naming_convention.md` §DocumentKey Slug Rule 참조 | DocType 내 | `ur_a2` |
| Document Instance | `DocumentInstanceKey` | `{DocumentKey}_{revision}_{language}` | 전역 (결정적) | `ur_a2_rev5_en` |
| documentSplit (임시) | `documentSplitKey` | `{doc_instance_key}_s{NNN}` | Document 내 | `ur_a2_rev5_en_s001` |
| Chunk | `ChunkKey` | `{doc_instance_key}_ch{NNN}` (zero-padded) | Document 내 | `ur_a2_rev5_en_ch001` |
| Work Unit | `WU_Key` | standalone: `{doc_instance_key}`, split: `{doc_instance_key}_wu{NNN}`, merged: `merge_{short_hash}` | 전역 | `ur_e26_rev1_en` |
| Heading | `Heading_ID` | `{DocumentKey}_HD_{NNN}` (최소 폭 3) | Document 내 | `ur_a2_HD_042` |

> `DocumentInstanceKey`는 실행별 고유 값이 **아니다**. 동일한 인스턴스는 재실행 시에도 동일한 키를 생성한다. 실행별 고유 식별이 필요한 경우 별도의 `RunID`를 사용한다.

## 토큰 측정 기준

| 항목 | 정의 |
|:---|:---|
| **Tokenizer** | `cl100k_base` (OpenAI tiktoken). 근사치: 영문 1 토큰 ≈ 4자, 한글 1 토큰 ≈ 1.5자 |
| **Est_Tokens_Inclusive** | `[Start_Line, End_Line]` 전체 범위의 토큰 수 (하위 항목 포함). **비가산적** |
| **Est_Tokens_Exclusive** | 해당 제목 자체 콘텐츠만의 토큰 수 (하위 항목 제외). **가산적** |
| **가산성 공식** | `parent.Exclusive + Σ(children.Inclusive) = parent.Inclusive` |
| **Hard limit** | 컨텍스트 윈도우의 절대 상한 (64K, 128K 등) |
| **Content budget** | Hard limit − 예약 공간 (system ~2K + output ~2K + safety). 64K 기준 ≈ 60K |
| **char_approx** | tiktoken 사용 불가 시 대체 방식: `ceil(char_count / 4 × 1.1)` — **10% 상향** 버퍼 |
| **Line reference** | 모든 `Start_Line`/`End_Line` 값은 **정규 입력 파일** 기준 상대값 |

## 토큰 임계값

| 단위 | 역할 |
|:---|:---|
| **documentSplit** | 제목 추출 전 임시 분할. 임계값은 `prerequisite/step2_heading_extraction.md` 참조 |
| **Chunk** | 제목 정렬 기반 최종 분할. Upper Bound는 `prerequisite/step3_workunit_packing.md` 참조 |
| **Work Unit** | 실행 단위 패킹. Lower/Upper Bound는 `prerequisite/step3_workunit_packing.md` 참조 |

> 구체적인 수치(64K, 32K, 16K 등)는 조정 가능한 파라미터이므로 여기에 기재하지 않는다. 항상 해당 명세서의 최신 값을 참조한다.

## 용어 정의

### 전역 (전체 파이프라인)

| 약어 | 전체 명칭 | 설명 | PRE 범위 |
|:---|:---|:---|:---:|
| **HD** | `HEADING` | 문서 제목 추출 | Yes |
| **TD** | `TRUE_DEF` | 정의 추출 | No |
| **APP** | `APPLICABILITY` | 적용 범위 추출 | No |
| **CT** | `CONTROLLED_TERM` | 통제 용어 추출 | No |

### 처리 단위

| 단위 | 성격 | 수명 |
|:---|:---|:---|
| **Document** | 독립 문서 단위; 최소 관리 단위 | 전체 파이프라인 |
| **documentSplit** | 대용량 문서의 임시 줄 기반 분할 | 제목 추출 단계에서 생성, 병합 후 폐기 |
| **Chunk** | 제목 기준 최종 분할 | 모든 문서에 존재 (소규모 문서 → 단일 Chunk) |
| **Work Unit (WU)** | 실행 단위 (standalone / split / merged) | WU 패킹 이후 전체 파이프라인 |

### 승인 상태

| 상태 | 설명 |
|:---|:---|
| `approve_all` | 모든 WU 승인 → 승격 |
| `approve_partial` | 일부 WU 승인, 나머지 `held` |
| `revise_and_rerun` | 임계값 조정 후 재실행 |
| `reject` | PRE 중단 |
