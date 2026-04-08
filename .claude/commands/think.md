# Claude Code Thinking 강제 설정 가이드

> 출처: news.hada.io #28272 (2026-02 Adaptive Thinking 도입 / 3-3 effort 기본값 medium 하향 논쟁) + 댓글 정리
> 목적: thinking 예산을 모델 자동조절(adaptive)에 맡기지 말고 사용자가 강제로 최대치 유지

## 1. 배경 요약

- **2026-02-09 Adaptive Thinking 도입**: 모델이 스스로 thinking 시간 조절 → 작업에 따라 사고량 급감
- **2026-03-03 effort 기본값 `medium`으로 하향**: 체감 품질 저하 보고 급증
- Anthropic(Boris) 입장: `redact-thinking` 헤더는 UI 숨김용 베타이고 토큰 예산엔 영향 없음. 실제 원인은 위 두 변경
- 커뮤니티 결론: **명시적 강제만이 해법**. "simplest fix" 같은 조기 중단 멘트가 보이면 effort=max 재시도

## 2. 영구 설정 — `.claude/settings.local.json`

```json
{
  "env": {
    "CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING": "1",
    "MAX_THINKING_TOKENS": "31999"
  },
  "effort": "max",
  "showThinkingSummaries": true,
  "cleanupPeriodDays": 365
}
```

| 키 | 의미 |
|---|---|
| `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` | 모델 자동 thinking 절감 차단 |
| `MAX_THINKING_TOKENS=31999` | thinking 토큰 상한 강제 (API 레벨) |
| `effort: "max"` | 3-3 이후 기본값 medium을 max로 복구 |
| `showThinkingSummaries: true` | thinking 과정 표시 — 실제 사고 여부 검증 |
| `cleanupPeriodDays: 365` | 로그 보존 (기본 7일이라 사후 분석 불가) |

## 3. 세션 단위 강제

- 프롬프트에 `ULTRATHINK` / `ultrathink` 키워드 → 해당 응답 한정 최대 thinking
- 슬래시 `/effort max` → 1회 최대 강도
- 키워드 단계: `think` < `think hard` < `think harder` < `ultrathink`

## 4. 조기 중단 감시 (선택)

조기 종료 멘트("simplest fix", "좀 할까요?", "이대로 진행할까요?") 감지 시 effort=max로 재실행하는 hook을 `stop-phrase-guard.sh`로 등록 가능.

## 5. 주의사항

- `MAX_THINKING_TOKENS`, `effort`, `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING`은 일부 비공식 키 포함 — 버전 따라 무시될 수 있음
- 적용 후 `showThinkingSummaries`로 실제 thinking 토큰이 늘었는지 검증 필수
- thinking 토큰 증가 → 비용 증가. 사용량 모니터링 병행 권장

## 6. 체크리스트

- [ ] settings.local.json에 위 5개 키 반영
- [ ] 재시작 후 응답에 thinking summary 노출 확인
- [ ] 복잡한 작업에서 ULTRATHINK 키워드 병행
- [ ] 조기 중단 멘트 발견 시 즉시 재시도
