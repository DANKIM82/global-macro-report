# UPDATE_SPEC.md — Global Macro Intelligence Report 갱신 명세

`index.html`(Global Macro Intelligence Report)은 **스크립트로 생성되지 않는다.**
라이브 웹 리서치 → HTML 재작성 방식이며, 매일 Claude 예약작업이 이 명세대로 갱신·push한다.
(원래 `DANKIM82/industry-analyzer`의 `geopolitics.html`이었으며 2026-11-23 이 레포로 분리.)

라이브 URL: https://dankim82.github.io/global-macro-report/

---

## 0. 갱신 모드

매 실행 시 아래 순서로 모드를 판정한다.

**전면 개정 (Full)** — 다음 중 하나라도 해당하면:
- 직전판 `AS OF`가 7일 이상 지났다
- 블로터 트레이드 중 하나가 invalidation에 도달했다
- 지배적 리스크(우선순위 1)가 바뀔 만한 사건이 발생했다 (전쟁·정권교체·중앙은행 서프라이즈·시장 급변 등)
- 월요일(KST) 실행

전면 개정은 §3의 전 섹션을 다시 쓴다. 우선순위·확률·블로터 재평가 포함.

**일일 갱신 (Daily)** — 그 외. 논지와 블로터 구조는 유지하고 다음만 갱신한다:
- 헤더 `AS OF` 날짜·시각
- Prior Book Scorecard: 각 트레이드의 현재 레벨, invalidation까지 거리
- Cross-Asset Level Dashboard 레벨 (직전판 ref 열은 직전 **전면 개정판** 값 유지)
- Timeline and Impact Matrix: 직전 실행 이후 신규 사건 추가
- Hard Catalyst Calendar: 지난 일정 제거·신규 일정 추가
- Monitoring Triggers 중 발동된 항목에 `TRIGGERED YYYY-MM-DD` 표시
- Executive Summary 맨 위에 "오늘의 변화" 1~3줄 (변화 없으면 "의미 있는 변화 없음"이라고 쓴다)
- Live Verification Checklist 갱신
- 개정 이력에 한 줄 추가

변화가 없는 날에도 레벨과 날짜는 갱신한다. 내용을 지어내서 채우지 않는다.

## 1. 산출물 규격

- 단일 파일 `geopolitics.html`, **완전 self-contained**.
  CDN·외부 폰트·외부 스크립트·이미지 **금지**. 오프라인/인쇄 렌더링 대응.
- 언어: 한국어 본문 + 영문 섹션 헤더.
- CSS는 기존 파일의 `:root` 토큰·클래스 체계를 **그대로 승계**한다.
  (`.tag`, `.blotter`, `.card`, `.scn`, `.trig`, `.cross`, `.res`, `.pill` 등)
- 표는 반드시 `.tblwrap`(overflow-x:auto)로 감싼다 — 모바일에서 본문이 가로 스크롤되면 안 된다.
- 리터럴 `&`는 `&amp;`로 이스케이프.

## 2. 신뢰도 태깅 규칙 (절대 준수)

| 태그 | 의미 | 사용 조건 |
|---|---|---|
| `F` | 검증가능 사실 | **1차 출처 또는 복수 통신사로 확인된 것만.** 날짜를 함께 적는다 |
| `M` | 시장 해석/컨센서스 | 프라이싱·애널리스트 견해. "누가 그렇게 본다"를 명시 |
| `V` | 전략가 추론/가정 | 확률·variant view·사이징은 전부 여기 |
| `⚠ verify` | 단말 확인 필요 | 라이브 레벨 전부. **출처 간 값이 다르면 단일값 금지 → 밴드로 표기** |
| `post-cutoff` | 컷오프 이후 | 모델 지식 컷오프 이후 사건. 라이브 조회 기반임을 명시 |

**금지 사항**
- 모르는 수치를 그럴듯하게 채우지 않는다. "데이터 미확보, 라이브 확인 필요"로 남긴다.
- YTD와 y/y를 섞지 않는다. (06-26판이 KOSPI에서 이 실수를 했다.)
- 2차 출처(집계 사이트)만으로 `F`를 붙이지 않는다.

## 3. 필수 섹션 순서

0. **Errata** — 직전판에서 사실관계가 틀린 것이 있으면 **맨 위에** 명시. 없으면 생략.
1. **Prior Book Scorecard** — 직전판 트레이드별 entry ref / 현재 레벨 / PAID·LOSS / 사후 판단·다음 행동.
   *사후 평가 없는 리서치는 리서치가 아니다. 이 섹션은 생략 불가.*
2. **Trade Blotter** — conviction 내림차순. 각 행: Idea / Direction·Instrument / Conv(0-5) / Horizon /
   **Invalidation(반증조건)** / Sizing. 신규는 `NEW` 배지, 승계는 "← T# 승격/교정" 표기.
3. **Executive Summary (Manager's Note)** — 번호 목록 5~6개. 각 항목은 굵은 리드 문장으로 시작.
   마지막 항목은 항상 **북 구성**(상관·세타예산·합산 사이징 상한).
4. **Section Cards** — 우선순위별. 각 카드는 **7단계 고정**:
   `1 Temporal Evolution` / `2 Transmission` / `3 Current Pricing + Variant View` /
   `4 Scenarios` / `5 Trade Expression` / `6 Portfolio Fit` / `7 Monitoring Triggers` + 하단 `Cross-Asset Confirmation`.
   **우선순위는 매판 재평가한다.** 그 시점의 지배적 리스크가 1번이다 (08-27판은 미국 통화·재정을 신설해 1번에 놓았다).
5. **Scenario Probability Matrix** — 섹션 × Base/Bull/Bear(합 100%) + Tail(별도, 합산 제외).
   직전판 대비 확률이 바뀐 행은 표 하단에 이유를 적는다.
6. **Cross-Asset Level Dashboard** — 자산 / 현재 레벨 / 직전판 ref / 비고·신뢰도.
7. **Timeline and Impact Matrix** — 직전판 이후 신규 사건만. 사건 / 시기 / 시장 반응 / 현재 영향도 / 신뢰도.
8. **Hard Catalyst Calendar** — 날짜 / 이벤트 / 연결 트레이드 / 왜 중요한가.
   **모든 옵션 만기는 이 표의 관련 날짜 이후로 설정한다.**
9. **Live Verification Checklist** — `RATES / FX / CMDTY / EQUITY / VOL / EVENT / POSITIONING / FUND` 카테고리.
   본문의 모든 `⚠ verify`가 여기 집계되어야 한다.
10. **Disclaimer + 개정 이력.**

## 4. 하우스 스타일 (트레이드 표현)

- 절대방향(outright)보다 **상대가치(RV)·비대칭 옵션(convexity)** 우선.
- 북 전체는 **long-vol, low-gross, delta≈flat**.
- 모든 아이디어에 **명시적 invalidation**이 있어야 한다. 없으면 아이디어가 아니다.
- 크라우디드 트레이드는 **0.5x 상한**. (이 규율이 06-26판 T6의 손실을 절반으로 막았다.)
- 상관된 컨벡시티(risk-off·USD 축 등)는 **합산 프리미엄 상한**을 명시.
- 세타 예산을 bps로 명시하고, 캐리·RV로 어떻게 상쇄하는지 적는다.

## 5. 리서치 절차

1. 직전판의 `AS OF` 날짜를 확인하고, **그날 이후 오늘까지**를 조사 구간으로 잡는다.
2. 섹션별로 병렬 조사한다. 최소 축: **미국 통화·재정 / 중동·에너지 / 미중 / 동북아 / 유럽**
   + **크로스에셋 레벨**(금리·FX·원자재·주식·변동성) 별도 1건.
3. 각 조사는 **(a) 날짜·출처 있는 사실 (b) 타임스탬프 있는 레벨 (c) 컨센서스 해석 (d) 확인 실패 항목**으로
   분리해서 받는다. (d)를 빠뜨리면 안 된다 — 그게 체크리스트가 된다.
4. **직전판의 전제를 능동적으로 반증 시도한다.** 06-26판의 "8월 관세 절벽"은 애초에 존재하지 않았고,
   이는 리서치가 아니라 캘린더 검증을 안 해서 생긴 오류였다.
5. 중앙은행·정부·통계청 **1차 자료**를 우선한다 (federalreserve.gov, boj.or.jp, ecb.europa.eu,
   bls.gov, bea.gov, treasury.gov, eurostat, federalregister.gov, IR 공시).
6. 출처 간 값이 충돌하면 **양쪽을 다 적고 밴드로 표기 + 체크리스트 등재.** 임의 선택 금지.

## 6. 배포 (이 레포)

```bash
python3 scripts/archive.py          # 현재 index.html을 archive/<AS OF 날짜>.html로 보관 + archive/index.html 재생성
# 새 index.html 작성
python3 scripts/check.py            # 외부 의존성·필수 섹션·AS OF 날짜 검증. 실패 시 push 금지
git add -A
git commit -m "report: daily|full update AS OF YYYY-MM-DD"
git push origin main
```

GitHub Pages(main 브랜치 루트)로 ~1분 내 반영.
같은 날 두 번 돌면 아카이브는 덮어쓴다.

## 7. 개정 이력

| 판 | 헤드라인 변화 |
|---|---|
| 2026-06-26 | 초판. 4섹션(미중·동북아·중동·유럽), T1~T8 |
| 2026-08-27 | 전면 개정. Prior Book Scorecard·Errata·Cross-Asset Dashboard·Hard Catalyst Calendar 신설. 우선순위 1에 **미국 통화·재정(초장기 텀프리미엄)** 추가 → 5섹션. 블로터 N1~N8로 재구성 |
| 2026-11-23 | industry-analyzer에서 분리, 일일 갱신 체계 도입. (08-27판은 원 레포에 push되지 않아 06-26판에서 출발) |
| 2026-11-23 (full) | 전면 개정(150일 경과·월요일). Errata 6건(미중 2025/2026 혼동, Strait Thunder, HSI/HSCEI 등). Scorecard: T1·T3 PAID, T2·T4·T5·T6·T7 LOSS. 우선순위 1 미국 통화·재정(Fed 인상 × AI 주식 급락) 신설, 미중 1→5. 블로터 N1~N8 |
| 2026-11-24 (daily) | 일일 갱신. NVIDIA Huang 복귀 → S&P +4.73%·VIX 27.1, 앞단 매파 유지(2y 4.66-4.70%·DXY 104.3). Brent $89.37. Errata 2건(NVIDIA 경위·KOSPI 종가). Scorecard에 N1~N8 일일 추적표 추가. 반증 도달 0건, 확인 실패 26건 |
| 2026-11-25 (daily) | 일일 갱신. 美 AI 칩 되돌림(NVDA 약 -7.4%, Nasdaq -1.48%)·11월 소비자신뢰 103.3 → 2y ~4.685%, Jan 추가 인상 69%. 아시아 지연 급반등(KOSPI +6.32% 5,006·SK하이닉스 +6.73%·TAIEX +8.99%) → N5 시차 손실 해소. Brent $91.40(+2.3%). Errata 2건(NVDA 11/23 종가·트럼프 발언 해석). 반증 도달 0건, 확인 실패 26건 |
| 2026-11-26 (daily) | 일일 갱신. USTR Section 301 과잉생산 관세 제안(中 20% 등 14개국, 빨라야 2027-01) → N7 테제 강화, 11/30 전면 개정에서 미중 우선순위 재평가 예정. 10월 core PCE 3.3%(예상 3.2%)에도 2y 4.637%(-4.6bp)·10y 4.846%(-8.4bp) → N1 유리·N6 불리. 아시아 칩 재급락(KOSPI -6.16% 4,697.51·SK하이닉스 -11.05%·TAIEX -4.80%), BNP Micron 하향. Brent $94.61(+3.5%). Errata 3건(NVDA 11/24 종가·SOX·NVIDIA 의회 일정). 반증 도달 0건, 확인 실패 27건. TradingView 한도 소진으로 FX 종가 다수 미확보 |
