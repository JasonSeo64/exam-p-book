from figstyle import *
import numpy as np
from matplotlib.patches import Circle, Rectangle


def frame(ax, label="S"):
    ax.add_patch(Rectangle((-2.2, -1.6), 4.4, 3.2, fill=False, lw=1.0, ec=GRAY))
    ax.text(-2.05, 1.35, label, fontsize=10, color=GRAY, style="italic")
    ax.set_xlim(-2.3, 2.3); ax.set_ylim(-1.7, 1.7)
    ax.set_aspect("equal"); ax.axis("off")


def region_mask(n=600):
    x = np.linspace(-2.2, 2.2, n); y = np.linspace(-1.6, 1.6, int(n * 3.2 / 4.4))
    X, Y = np.meshgrid(x, y)
    A = (X + 0.55) ** 2 + Y ** 2 <= 1.0
    B = (X - 0.55) ** 2 + Y ** 2 <= 1.0
    return X, Y, A, B


def shade(ax, mask, color=BLUE_L):
    X, Y, _, _ = region_mask()
    ax.contourf(X, Y, mask.astype(float), levels=[0.5, 1.5], colors=[color], alpha=0.85)


def circles(ax):
    ax.add_patch(Circle((-0.55, 0), 1.0, fill=False, lw=1.3, ec=BLUE))
    ax.add_patch(Circle((0.55, 0), 1.0, fill=False, lw=1.3, ec=BLUE))
    ax.text(-1.15, 0.85, "A", fontsize=11, color=BLUE, style="italic")
    ax.text(1.05, 0.85, "B", fontsize=11, color=BLUE, style="italic")

# 그림 1.1.1 집합 연산 네 가지
_, _, A, B = region_mask()
fig, axes = plt.subplots(1, 4, figsize=(8.4, 2.3))
panels = [(A | B, r"$A\cup B$ (합집합)"), (A & B, r"$A\cap B$ (교집합)"),
          (A & ~B, r"$A\cap B^{c}$ (차집합 $A-B$)"), (~A, r"$A^{c}$ (여집합)")]
for ax, (m, t) in zip(axes, panels):
    shade(ax, m); circles(ax); frame(ax); ax.set_title(t, fontsize=10)
save(fig, "fig1_1_1")

# 그림 1.1.2 드모르간 법칙
fig, axes = plt.subplots(1, 2, figsize=(6.0, 2.5))
shade(axes[0], ~(A | B)); circles(axes[0]); frame(axes[0])
axes[0].set_title(r"$(A\cup B)^{c}=A^{c}\cap B^{c}$", fontsize=10)
shade(axes[1], ~(A & B)); circles(axes[1]); frame(axes[1])
axes[1].set_title(r"$(A\cap B)^{c}=A^{c}\cup B^{c}$", fontsize=10)
save(fig, "fig1_1_2")

# 그림 1.4.1 세 사건의 벤 다이어그램과 영역별 확률 (Example 1.4.2)
fig, ax = plt.subplots(figsize=(4.6, 3.8))
cA, cH, cL = (-0.6, 0.35), (0.6, 0.35), (0.0, -0.6)
for c, lab, pos in [(cA, "자동차 A", (-1.85, 1.35)), (cH, "주택 H", (1.15, 1.35)), (cL, "생명 L", (-0.35, -1.95))]:
    ax.add_patch(Circle(c, 1.05, fill=True, alpha=0.12, fc=BLUE, ec=BLUE, lw=1.3))
    ax.text(*pos, lab, fontsize=10, color=BLUE)
vals = {(-1.05, 0.65): "0.20", (1.05, 0.65): "0.15", (0.0, -1.15): "0.10",
        (0.0, 0.75): "0.15", (-0.62, -0.35): "0.10", (0.62, -0.35): "0.05", (0.0, 0.03): "0.05"}
for (x, y), v in vals.items():
    ax.text(x, y, v, ha="center", va="center", fontsize=10, fontweight="bold", color="#222222")
ax.add_patch(Rectangle((-2.2, -2.15), 4.4, 3.85, fill=False, ec=GRAY))
ax.text(1.55, -2.0, "0.20", fontsize=10, fontweight="bold")
ax.text(-2.1, 1.5, "S", style="italic", color=GRAY)
ax.set_xlim(-2.3, 2.3); ax.set_ylim(-2.25, 1.8); ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig1_4_1")

# 그림 1.5.1 표본공간의 분할
fig, ax = plt.subplots(figsize=(5.2, 2.6))
xs = [0, 1.1, 2.6, 3.5, 5.0]
labs = [r"$B_1$", r"$B_2$", r"$B_3$", r"$B_4$"]
cols = [BLUE_L, "#C9DDF0", ORANGE_L, "#FBE3D0"]
for i in range(4):
    ax.add_patch(Rectangle((xs[i], 0), xs[i + 1] - xs[i], 2.0, fc=cols[i], ec="white", lw=2))
    ax.text((xs[i] + xs[i + 1]) / 2, 1.75, labs[i], ha="center", fontsize=11)
ax.add_patch(Rectangle((0, 0), 5, 2, fill=False, ec=GRAY))
from matplotlib.patches import Ellipse
ax.add_patch(Ellipse((2.5, 0.85), 3.6, 1.0, fill=False, ec=ORANGE, lw=1.8))
ax.text(2.5, 0.85, r"$A$", ha="center", va="center", fontsize=12, color=ORANGE)
ax.text(0.05, -0.25, r"$S=B_1\cup B_2\cup B_3\cup B_4,\ \ B_i\cap B_j=\varnothing$", fontsize=10)
ax.set_xlim(-0.1, 5.1); ax.set_ylim(-0.45, 2.1); ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig1_5_1")
