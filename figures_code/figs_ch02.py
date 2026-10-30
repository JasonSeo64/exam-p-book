from figstyle import *
from math import comb
from matplotlib.patches import FancyBboxPatch


def node(ax, x, y, text, fc="white", ec=BLUE, fs=9):
    ax.text(x, y, text, ha="center", va="center", fontsize=fs,
            bbox=dict(boxstyle="round,pad=0.3", fc=fc, ec=ec, lw=1.0))

# 그림 2.1.1 곱셈의 원리: 수형도 (보장기간 3 × 납입방식 2)
fig, ax = plt.subplots(figsize=(6.2, 3.4))
node(ax, 0, 0, "시작", fc="#EAF1F8")
terms = ["10년", "20년", "종신"]
pays = ["월납", "연납"]
k = 0
for i, t in enumerate(terms):
    y1 = 1.6 - i * 1.6
    ax.plot([0.25, 1.4], [0, y1], color=GRAY, lw=0.9)
    node(ax, 1.75, y1, t)
    for j, p in enumerate(pays):
        y2 = y1 + 0.4 - j * 0.8
        ax.plot([2.1, 3.2], [y1, y2], color=GRAY, lw=0.9)
        node(ax, 3.55, y2, p)
        k += 1
        ax.text(4.25, y2, f"({t}, {p})", va="center", fontsize=8.5, color=BLUE)
ax.text(1.75, 2.45, "1단계: 3가지", ha="center", fontsize=9, color=ORANGE)
ax.text(3.55, 2.45, "2단계: 각 2가지", ha="center", fontsize=9, color=ORANGE)
ax.text(4.9, 2.45, r"합계 $3\times2=6$", ha="center", fontsize=9, color=ORANGE)
ax.set_xlim(-0.5, 5.6); ax.set_ylim(-2.3, 2.7); ax.axis("off")
save(fig, "fig2_1_1")

# 그림 2.3.1 파스칼의 삼각형
fig, ax = plt.subplots(figsize=(5.6, 3.3))
N = 7
for n in range(N):
    for k in range(n + 1):
        x = k - n / 2; y = -n
        hl = (n == 6 and k in (2, 3)) or (n == 7 and k == 3)
        ax.text(x, y, str(comb(n, k)), ha="center", va="center", fontsize=10,
                bbox=dict(boxstyle="circle,pad=0.25", fc=ORANGE_L if (n == 6 and k in (2, 3)) else "#EAF1F8",
                          ec=ORANGE if (n == 6 and k in (2, 3)) else BLUE_L, lw=0.8))
    ax.text(-N / 2 - 0.6, -n, f"$n={n}$", ha="right", va="center", fontsize=9, color=GRAY)
n = 7
for k in range(n + 1):
    fc = ORANGE if k == 3 else "white"
    ax.text(k - n / 2, -n, str(comb(n, k)), ha="center", va="center", fontsize=10,
            color="white" if k == 3 else "black",
            bbox=dict(boxstyle="circle,pad=0.25", fc=fc, ec=ORANGE if k == 3 else BLUE_L, lw=0.8))
ax.text(-N / 2 - 0.6, -n, "$n=7$", ha="right", va="center", fontsize=9, color=GRAY)
ax.text(3.2, -5.7, r"$\binom{6}{2}+\binom{6}{3}=\binom{7}{3}$" "\n" r"$15+20=35$", fontsize=10, color=ORANGE)
ax.set_xlim(-5.2, 5.2); ax.set_ylim(-7.6, 0.6); ax.axis("off")
save(fig, "fig2_3_1")

# 그림 2.4.1 별과 막대 (x1+x2+x3=7 의 한 해)
fig, ax = plt.subplots(figsize=(6.0, 1.6))
seq = "**|***|**"
x = 0
for ch in seq:
    if ch == "*":
        ax.text(x, 0, "★", ha="center", va="center", fontsize=20, color=BLUE)
    else:
        ax.plot([x, x], [-0.45, 0.45], color=ORANGE, lw=3)
    x += 1
ax.text(0.5, -0.85, r"$x_1=2$", ha="center", fontsize=10)
ax.text(4, -0.85, r"$x_2=3$", ha="center", fontsize=10)
ax.text(7.5, -0.85, r"$x_3=2$", ha="center", fontsize=10)
ax.text(10, 0, r"별 7개, 막대 2개 $\Rightarrow\ \binom{9}{2}=36$가지", va="center", fontsize=10)
ax.set_xlim(-0.6, 16.5); ax.set_ylim(-1.2, 0.8); ax.axis("off")
save(fig, "fig2_4_1")

# 그림 2.5.1 생일문제형: 서로 다른 달일 확률 vs 청구 건수
import numpy as np
fig, ax = plt.subplots(figsize=W1)
ns = np.arange(1, 13)
p = [np.prod([(12 - i) / 12 for i in range(n)]) for n in ns]
ax.bar(ns, p, color=BLUE_L, ec=BLUE)
ax.bar([5], [p[4]], color=ORANGE_L, ec=ORANGE)
ax.text(5, p[4] + 0.03, f"{p[4]:.4f}", ha="center", fontsize=9, color=ORANGE)
ax.set_xlabel("청구 건수 $n$"); ax.set_ylabel("모두 서로 다른 달일 확률")
ax.set_xticks(ns); ax.set_ylim(0, 1.08)
save(fig, "fig2_5_1")
