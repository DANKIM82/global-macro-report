# Global Macro Intelligence Report

Buy-side L/S desk용 지정학·매크로 리포트. 매일 Claude 예약작업이 웹 리서치 후 갱신한다.

최신판: https://dankim82.github.io/global-macro-report/
아카이브: https://dankim82.github.io/global-macro-report/archive/

## 구조

- `index.html` 최신판 (self-contained, 외부 의존성 없음)
- `archive/YYYY-MM-DD.html` 과거판
- `UPDATE_SPEC.md` 갱신 명세 (일일/전면 개정 판정, 태깅 규칙, 필수 섹션, 배포 절차)
- `scripts/archive.py` 현재판 보관 + 아카이브 목록 재생성
- `scripts/check.py` push 전 검증

## 수동 갱신

Claude에 "global-macro-report 레포의 UPDATE_SPEC.md 명세대로 index.html 갱신해줘"라고 요청.

원래 `DANKIM82/industry-analyzer/geopolitics.html`에서 2026-11-23 분리.
