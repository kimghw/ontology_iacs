# Step 3 — 청킹 및 Work Unit 패킹

## 1. 작업명세

### 1.1 목적

PRE 파이프라인의 최종 스테이지. 문서별 토큰 측정값을 기준으로 LLM 컨텍스트 윈도우에서 안정적으로 처리 가능한 **Work Unit(WU) 집합**을 생성한다.

두 개의 독립 절차로 구성: **청킹**(상한 강제 → split/standalone WU 확정)과 **WU 패킹**(하한 강제 → merge WU 생성).

#### WU 종류

| WU 종류 | 생성 단계 | 트리거 조건 |
|:---|:---|:---|
| **split WU** | 청킹 | 문서 > 상한 → 청크 N개 → 같은 문서끼리 그룹화 |
| **standalone WU** | 청킹 | 하한 ≤ 문서 ≤ 상한 → 단일 청크 = 1 WU |
| **merge WU** | WU 패킹 | 문서 < 하한 → 동질 문서끼리 머지 |

### 1.2 입력

- **[A05]** `doc-{doc_instance_key}__heading__structure.tsv` — 청킹 경계 산정 (헤딩 트리 + 토큰 측정값)
- **[A02]** `file-{source_file_key}__pre__normalised.md` — 오버사이즈 리프 폴백 시 본문 접근 (조건부)
- **[A01]** `file-{source_file_key}__pre__meta.json` — 문서 메타 (`Authority`, `DocType`, `language` 등)
- **[A15]** `doctype-{DocType}__heading__grammar_v{NN}.md` — `grammar_version` 추출
- **[D17]** `shared/thresholds.yaml` — 토큰 임계값 (`chunk_max`, `wu_range`)

### 1.3 산출물

| ID | 파일 | 단위 | 설명 |
|:---|:---|:---|:---|
| **[A07]** | `doc-{doc_instance_key}__heading__chunk_plan.json` | 문서당 1개 | 청크 경계, 토큰 크기, 분할 방법 |
| **[A22]** | `wu-{wu_key}__pre__meta.json` | WU당 1개 | WU 메타데이터 (구성 문서, 청크, 토큰 합) |
| **[A24]** | `corpus__pre__manifest.json` | 코퍼스당 1개 | PRE 마스터 인덱스 (최종 단계로 생성) |

> 모든 산출물은 `results/` 디렉터리에 직접 기록한다. 파일 명명 규칙과 전체 카탈로그는 **[D02]** [pre_specification_ko.md](pre_specification_ko.md) §산출물 카탈로그를 정본으로 한다.

### 1.4 수행 절차

1. **청킹** (문서당 독립 수행) — 헤딩 구조 TSV를 읽어 청크 경계를 결정하고 **[A07]** `doc-{doc_instance_key}__heading__chunk_plan.json`을 생성한다. 토큰 ≤ 상한이면 단일 청크, 초과면 헤딩 경계에서 재귀 분할. 청킹 결과에 따라 즉시 WU를 확정한다:
2. **WU 패킹** (코퍼스 전역 수행) — 청킹에서 인계된 머지 후보들만 처리한다. 동질 문서끼리 묶어 하한 위로 끌어올린 **merge WU**를 생성한다. (상세 규칙은 §3)
3. **이슈 게이트** — 청킹·패킹 단계의 자동 트리거가 발동된 경우에만 이슈 보고서를 표면화하고 에이전트 또는 사용자 결정을 받는다. 트리거가 없으면 자동 완료. (상세 규칙은 §4)
4. **매니페스트 최종화** — 모든 WU 상태가 종료(`processed`/`proceeded`/`revised`/`aborted`)된 후 **[A24]** `corpus__pre__manifest.json`을 생성한다. (상세 규칙은 §5)

### 1.5 에스컬레이션 조건

3단계 게이트:

1. **서브에이전트** — 트리거 발동 시 심각도 **상/중/하** 판정.
2. **오케스트레이터** — **상/중** 이슈를 코퍼스 전역에서 집계하여 공통 지침(임계값 조정, 일괄 처리 규칙 등)을 서브에이전트에 재배포.
3. **사용자** — 공통 지침으로 해결 불가 또는 심각도 **상** → §4 이슈 게이트로 보고, 결정(`proceed`/`revise`/`abort`) 수신.

### 1.6 완료 조건

- **정상 종료**: 다운스트림에 제공할 WU 집합이 산출되면 본 단계를 종료한다.
- **예외 종료**: 자동 처리 경로로 해결되지 않은 문서는 서브에이전트가 직접 본문을 읽어 상황을 판단하고 보고서를 작성한 뒤 종료한다. 미처리 문서와 사유는 보고에 명시한다.

---

## 2. 청킹 — 상한 분할 및 split/standalone WU 확정

### 2.1 절차 (문서당 독립 수행)

1. **재귀 헤딩 분할** — 문서 토큰이 `chunk_max` 초과면 최상위 헤딩 경계부터 청크를 만들고, 청크가 여전히 상한을 넘으면 하위 헤딩에서 재귀 분할. 헤딩 없는 구간은 문단/문장 단위 폴백.
2. **오버사이즈 리프 처리** — 단일 헤딩 리프가 상한을 넘는 경우 본문 파일(§1.2 **[A02]**)을 직접 읽어 폴백 분할하고, 트리거 이벤트를 기록.
3. **WU 라벨링** — 결과를 §1.1 「WU 종류」 표 기준으로 split / standalone / merge_candidate 로 분기.

### 2.2 산출 파일

- **[A07]** `doc-{doc_instance_key}__heading__chunk_plan.json` — 문서당 1개, `results/`에 직접 기록.

```json
{
  "doc_instance_key": "...",
  "source_file_key": "...",
  "doctype": "...",
  "grammar_version": "v01",
  "total_tokens": 48210,
  "chunk_max": 32000,
  "wu_min": 16000,
  "split_method": "heading_recursive",   // heading_recursive | fallback_paragraph | none
  "chunks": [
    {
      "chunk_id": "c01",
      "heading_path": ["1", "1.2"],
      "token_count": 24800,
      "span": {"start_line": 12, "end_line": 410}
    }
  ],
  "wu_decision": "split",                // split | standalone | merge_candidate
  "wu_key": "wu-...",                    // 확정된 경우만
  "triggers": []                         // 오버사이즈 리프, 폴백 사용 등
}
```

---

## 3. WU 패킹 — 하한 머지 (merge WU 생성)

### 3.1 절차 (코퍼스 전역 1회 수행)

1. **동질 그룹화** — `Authority`, `DocType`, `language`, `grammar_version`이 모두 일치하는 문서끼리 그룹화 (이종 머지 금지). 그룹 내 정렬은 `doc_instance_key` 사전순(재현성 확보).
2. **머지 빌드** — 그룹 내에서 토큰 합이 `wu_min` 이상 `chunk_max` 이하가 되도록 First-Fit Decreasing으로 묶는다.
   - 합이 `wu_min` 미만으로 남은 잔여는 단독 merge WU로 확정하고 **하한 미달 트리거**를 기록 (§4에서 처리).
   - 문서 추가 시 `chunk_max`를 넘으면 새 묶음을 시작.
3. **WU_Key 부여** — `wu-merge-{Authority}-{DocType}-{language}-{seq:03d}` 형식.

### 3.2 산출 파일

- **[A22]** `wu-{wu_key}__pre__meta.json` — WU당 1개 (split / standalone / merge 공통 스키마).

```json
{
  "wu_key": "wu-merge-IACS-UR-en-001",
  "wu_type": "merge",                    // split | standalone | merge
  "authority": "IACS",
  "doctype": "UR",
  "language": "en",
  "grammar_version": "v01",
  "members": [
    {
      "doc_instance_key": "...",
      "source_file_key": "...",
      "chunk_ids": ["c01"],              // split WU는 다수, merge/standalone은 보통 1개
      "token_count": 8200
    }
  ],
  "total_tokens": 24600,
  "status": "processed",                 // processed | proceeded | revised | aborted
  "triggers": []                         // 하한 미달, 머지 실패 등
}
```

## 4. 이슈 게이트

청킹·패킹 단계의 자동 트리거가 발동된 경우에만 이슈 보고서를 표면화하고 에이전트 또는 사용자 결정(`proceed`/`revise`/`abort`)을 받는다. 트리거가 없으면 자동 완료.

> *(상세 지침은 후속 작성 — 이슈 보고서 필드, 사용자 응답 매핑, WU 라이프사이클 상태)*

## 5. 산출물 저장 및 매니페스트 최종화

> *(상세 지침은 후속 작성 — `results/` 저장 정책, 임시 산출물 자동 삭제, 매니페스트 인터페이스 contract)*
