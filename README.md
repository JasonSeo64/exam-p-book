# SOA Exam P 확률론 — 보충자료

『SOA Exam P 확률론: 보험계리사를 위한 확률의 기초와 응용』(서재영 지음, 2026년 초판)의 보충자료 저장소입니다.
출제범위는 SOA *Probability Exam – January 2027* 실라버스를 기준으로 합니다.

## 받는 법

- **한 번에 받기:** 오른쪽 **Releases**에서 책의 판에 맞는 버전(초판은 `v1.0`)을 고르고 ZIP 파일을 내려받습니다.
- **최신 파일 받기:** 초록색 **Code** 버튼 → **Download ZIP**.

책에 인쇄된 링크(`…/tree/v1.0`)는 초판 출간 시점의 파일을 가리킵니다. 정오표 반영 등으로 파일이 바뀌면 최신 버전에서 확인할 수 있습니다.

## 들어 있는 것

| 폴더·파일 | 내용 |
|---|---|
| `figures_code/` | 본문 그림을 만드는 파이썬 코드. 장별 `figs_chNN.py`, 공통 스타일 `fig_style.py` |
| `errata.md` | 정오표 |

### 그림 코드 실행

```bash
pip install -r requirements.txt
cd figures_code
python figs_ch07.py        # → ../figures/ch07_fig1.png … 가 만들어집니다
```

그림의 한글 글꼴은 Noto Sans CJK KR(또는 맑은 고딕)을 씁니다. 모수를 바꿔 실행해 보면 분포의 모양이 어떻게 달라지는지 직접 확인할 수 있습니다.

## 정오표·문의

오류를 발견하시면 이 저장소의 **Issues**에 장·쪽·내용을 적어 주세요. 확인된 오류는 `errata.md`에 반영합니다.

## 라이선스

- 코드(`*.py`): MIT License — `LICENSE` 참고
- 그 밖의 자료: © 2026 서재영. 책 본문·문제·해설은 이 저장소에 포함되지 않으며, 무단 전재와 복제를 금합니다.

## 인용

`CITATION.cff`를 참고하세요. GitHub 저장소 화면 오른쪽의 **Cite this repository**에서 인용 형식을 바로 복사할 수 있습니다.
