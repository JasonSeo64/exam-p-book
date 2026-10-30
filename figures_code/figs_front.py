# -*- coding: utf-8 -*-
"""앞부분(front.md) 그림
front_fig1.png  주제별 출제 비중 (실라버스 Probability Exam – January 2027)
front_fig2.png  이 책의 구성도 (3부 13장, 부록 A–H)
실행: python3 code/figs_front.py  (출력: <책 폴더>/figures)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.environ.setdefault("FIG_DIR", os.path.join(os.path.dirname(HERE), "figures"))
sys.path.insert(0, HERE)
from fig_style import *  # noqa: E402,F401
import fig_style  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

NAVY, ORANGE, GRAY, TEAL = COLORS[0], COLORS[1], COLORS[2], COLORS[3]

# ---------------------------------------------------------------- 그림 0-1 출제 비중
topics = ["주제 1 일반확률", "주제 2 단변량 확률변수", "주제 3 다변량 확률변수"]
lo = [23, 44, 23]
hi = [30, 50, 30]
N_Q = 30  # 문항 수
fig, ax = new(6.3, 2.3)
for i, (t, a, b) in enumerate(zip(topics, lo, hi)):
    y = 2 - i
    ax.barh(y, a, color="#DCE4EC", ec=NAVY, height=0.55, label="최소 비중" if i == 0 else None)
    ax.barh(y, b - a, left=a, color="white", ec=ORANGE, height=0.55, hatch="///",
            label="비중의 범위" if i == 0 else None)
    ax.text(b + 1, y, f"{a}–{b}%  (약 {round(N_Q * a / 100)}–{round(N_Q * b / 100)}문항)",
            va="center", fontsize=8.5)
ax.set_yticks([2, 1, 0])
ax.set_yticklabels(topics)
ax.set_xlim(0, 75)
ax.set_xlabel("출제 비중(%)")
ax.grid(axis="y", visible=False)
ax.legend(loc="lower right", frameon=False)
fig_style.save(fig, "front_fig1.png")

# ---------------------------------------------------------------- 그림 0-2 구성도
fig, ax = new(6.3, 4.6)


def box(x, y, w, h, text, fc, ec, fs=8.0, bold=False, ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.06",
                                fc=fc, ec=ec, lw=1.1, ls=ls))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else None)


parts = [
    ("제1부 일반확률\n주제 1 (23–30%)", ["제1장 확률의 공리적 정의", "제2장 경우의 수", "제3장 조건부확률과 독립"], NAVY, "-"),
    ("제2부 단변량 확률변수\n주제 2 (44–50%)", ["제4장 확률변수와 분포함수", "제5장 기댓값과 분포의 특성치", "제6장 주요 이산분포",
                                      "제7장 주요 연속분포", "제8장 보험 응용: 손실과 지급"], ORANGE, "--"),
    ("제3부 다변량 확률변수\n주제 3 (23–30%)", ["제9장 결합분포(이산형)", "제10장 결합분포의 적률", "제11장 독립확률변수의 선형결합",
                                      "제12장 순서통계량", "제13장 중심극한정리"], TEAL, "-."),
]
for i, (head, items, c, ls) in enumerate(parts):
    x = 0.1 + i * 2.35
    box(x, 4.55, 2.1, 0.75, head, "white", c, fs=8.3, bold=True, ls=ls)
    for j, it in enumerate(items):
        box(x + 0.02, 3.85 - j * 0.62, 2.06, 0.48, it, "#F7F7F7", c, fs=6.9, ls=ls)
    if i < 2:
        ax.annotate("", xy=(x + 2.33, 4.92), xytext=(x + 2.12, 4.92),
                    arrowprops=dict(arrowstyle="-|>", color=GRAY))

ax.text(3.6, 1.0, "각 장: 학습목표 → 실라버스 대응표 → 개요 → 본문 → 기출 연결 → 요약 → 연습문제(기본·실전) → 참고문헌과 근거",
        ha="center", va="center", fontsize=6.9, color=GRAY)
box(0.1, -0.95, 3.45, 1.35,
    "참고·도구\nA 수학적 준비\nB 정규분포표\nC 적률생성함수(심화)\nD 연속형 결합분포(심화)",
    "white", GRAY, fs=7.2, ls=":")
box(3.65, -0.95, 3.45, 1.35,
    "실전·정리\nE 모의고사 2회와 SOA 공개 문항 대응표\nF 영어 문제 표현집\nG 기호·용어 대조표\nH 연습문제 해설",
    "#EEEEEE", GRAY, fs=7.2)
ax.text(3.6, 0.62, "부록", ha="center", va="center", fontsize=8, fontweight="bold")
ax.set_xlim(0, 7.2)
ax.set_ylim(-1.05, 5.4)
ax.axis("off")
ax.grid(False)
fig_style.save(fig, "front_fig2.png")
print("saved:", os.environ["FIG_DIR"])
