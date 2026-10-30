from figstyle import *
import numpy as np
from matplotlib.patches import Circle, Rectangle

# 그림 3.1.1 조건부확률: 표본공간이 B로 축소
fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.6))
x = np.linspace(-2.2, 2.2, 500); y = np.linspace(-1.6, 1.6, 364)
X, Y = np.meshgrid(x, y)
A = (X + 0.55) ** 2 + Y ** 2 <= 1; B = (X - 0.55) ** 2 + Y ** 2 <= 1
for ax, title in zip(axes, ["원래 표본공간 $S$", "$B$가 일어났다는 정보 이후"]):
    if ax is axes[1]:
        ax.contourf(X, Y, B.astype(float), levels=[.5, 1.5], colors=["#EAF1F8"])
        ax.contourf(X, Y, (A & B).astype(float), levels=[.5, 1.5], colors=[ORANGE_L])
        ax.add_patch(Circle((-0.55, 0), 1, fill=False, ec=GRAY, ls="--", lw=1))
        ax.add_patch(Circle((0.55, 0), 1, fill=False, ec=BLUE, lw=1.8))
        ax.text(0.0, -1.45, r"$P(A\mid B)=P(A\cap B)/P(B)$", ha="center", fontsize=10)
    else:
        ax.contourf(X, Y, (A & B).astype(float), levels=[.5, 1.5], colors=[ORANGE_L])
        ax.add_patch(Circle((-0.55, 0), 1, fill=False, ec=BLUE, lw=1.3))
        ax.add_patch(Circle((0.55, 0), 1, fill=False, ec=BLUE, lw=1.3))
        ax.add_patch(Rectangle((-2.2, -1.6), 4.4, 3.2, fill=False, ec=GRAY))
    ax.text(-1.2, 0.85, "A", style="italic", color=BLUE); ax.text(1.1, 0.85, "B", style="italic", color=BLUE)
    ax.set_xlim(-2.3, 2.3); ax.set_ylim(-1.7, 1.7); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(title, fontsize=10)
save(fig, "fig3_1_1")


def node(ax, x, y, t, fc="white", ec=BLUE):
    ax.text(x, y, t, ha="center", va="center", fontsize=9,
            bbox=dict(boxstyle="round,pad=0.3", fc=fc, ec=ec, lw=1))

# 그림 3.3.1 위험등급 수형도 (Example 3.3.1)
fig, ax = plt.subplots(figsize=(6.6, 3.6))
node(ax, 0, 0, "가입자", fc="#EAF1F8")
cls = [("우량", 0.50, 0.05), ("표준", 0.35, 0.10), ("불량", 0.15, 0.25)]
for i, (c, p, q) in enumerate(cls):
    y = 1.8 - 1.8 * i
    ax.annotate("", xy=(1.5, y), xytext=(0.35, 0), arrowprops=dict(arrowstyle="-", color=GRAY))
    ax.text(0.85, y * 0.55 + 0.12, f"{p:.2f}", fontsize=9, color=ORANGE)
    node(ax, 1.85, y, c)
    for j, (lab, pr) in enumerate([("청구", q), ("무청구", 1 - q)]):
        y2 = y + 0.42 - 0.84 * j
        ax.annotate("", xy=(3.3, y2), xytext=(2.2, y), arrowprops=dict(arrowstyle="-", color=GRAY))
        ax.text(2.6, (y + y2) / 2 + 0.1, f"{pr:.2f}", fontsize=8.5, color=ORANGE)
        node(ax, 3.7, y2, lab, fc=ORANGE_L if lab == "청구" else "white",
             ec=ORANGE if lab == "청구" else BLUE)
        ax.text(4.3, y2, f"{p:.2f}×{pr:.2f} = {p * pr:.4f}", va="center", fontsize=8.5,
                color=ORANGE if lab == "청구" else GRAY, fontweight="bold" if lab == "청구" else None)
ax.text(4.3, -2.75, "P(청구) = 0.0250 + 0.0350 + 0.0375 = 0.0975", fontsize=9.5, color=ORANGE, fontweight="bold")
ax.set_xlim(-0.5, 6.6); ax.set_ylim(-3.0, 2.5); ax.axis("off")
save(fig, "fig3_3_1")

# 그림 3.4.1 베이즈 정리의 면적도 (Example 3.4.2)
prev, sens, fpr = 0.02, 0.95, 0.04
fig, ax = plt.subplots(figsize=(6.4, 3.0))
wD = 0.12  # 시각화를 위해 질병군 폭을 과장(실제 2%)
ax.add_patch(Rectangle((0, 0), wD, sens, fc=ORANGE, ec="white"))
ax.add_patch(Rectangle((0, sens), wD, 1 - sens, fc=ORANGE_L, ec="white"))
hF = 0.14  # 시각화를 위해 위양성 높이를 과장(실제 4%)
ax.add_patch(Rectangle((wD, 0), 1 - wD, hF, fc=BLUE, ec="white"))
ax.add_patch(Rectangle((wD, hF), 1 - wD, 1 - hF, fc="#EAF1F8", ec="white"))
ax.text(wD / 2, 0.45, "질병\n& 양성\n0.0190", ha="center", va="center", fontsize=8, color="white")
ax.text(0.55, hF / 2, "비질병 & 양성  0.98×0.04 = 0.0392 (높이 과장)", ha="center", va="center", fontsize=8.5, color="white")
ax.text(0.55, 0.55, "비질병 & 음성  0.9408", ha="center", fontsize=9, color=BLUE)
ax.text(wD / 2, 1.04, "질병 2%\n(폭 과장)", ha="center", fontsize=8, color=ORANGE)
ax.text(0.55, 1.04, "비질병 98%", ha="center", fontsize=9, color=BLUE)
ax.text(1.03, 0.5, r"$P(D\mid +)=\dfrac{0.0190}{0.0190+0.0392}=0.3265$", fontsize=11, va="center")
ax.set_xlim(0, 1.75); ax.set_ylim(0, 1.15); ax.axis("off")
save(fig, "fig3_4_1")

# 그림 3.5.1 직렬·병렬 시스템
fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.2))
ax = axes[0]
for i, r in enumerate([0.9, 0.8, 0.7]):
    ax.add_patch(Rectangle((1 + 1.6 * i, -0.35), 1.0, 0.7, fc="#EAF1F8", ec=BLUE))
    ax.text(1.5 + 1.6 * i, 0, f"{r}", ha="center", va="center")
ax.plot([0, 1], [0, 0], color=GRAY); ax.plot([2, 2.6], [0, 0], color=GRAY)
ax.plot([3.6, 4.2], [0, 0], color=GRAY); ax.plot([5.2, 6.2], [0, 0], color=GRAY)
ax.set_title("직렬: 0.9×0.8×0.7 = 0.504", fontsize=10)
ax.set_xlim(-0.2, 6.4); ax.set_ylim(-1.3, 1.3); ax.axis("off")
ax = axes[1]
for i, r in enumerate([0.9, 0.8, 0.7]):
    y = 0.9 - 0.9 * i
    ax.add_patch(Rectangle((2, y - 0.3), 1.2, 0.6, fc="#EAF1F8", ec=BLUE))
    ax.text(2.6, y, f"{r}", ha="center", va="center")
    ax.plot([1, 2], [y, y], color=GRAY); ax.plot([3.2, 4.2], [y, y], color=GRAY)
ax.plot([1, 1], [-0.9, 0.9], color=GRAY); ax.plot([4.2, 4.2], [-0.9, 0.9], color=GRAY)
ax.plot([0, 1], [0, 0], color=GRAY); ax.plot([4.2, 5.2], [0, 0], color=GRAY)
ax.set_title("병렬: 1−0.1×0.2×0.3 = 0.994", fontsize=10)
ax.set_xlim(-0.2, 5.4); ax.set_ylim(-1.3, 1.3); ax.axis("off")
save(fig, "fig3_5_1")

# 그림 3.6.1 세 위험요인의 8개 영역 (Example 3.6.1)
fig, ax = plt.subplots(figsize=(5.6, 4.2))
cen = {"H": (-0.55, 0.35), "D": (0.55, 0.35), "O": (0.0, -0.55)}
cols = {"H": BLUE, "D": ORANGE, "O": GREEN}
for k, (cx, cy) in cen.items():
    ax.add_patch(Circle((cx, cy), 1.0, fill=False, ec=cols[k], lw=1.6))
ax.text(-1.55, 1.25, "$H$ (0.29)", color=BLUE, fontsize=10)
ax.text(1.05, 1.25, "$D$ (0.23)", color=ORANGE, fontsize=10)
ax.text(0.95, -1.15, "$O$ (0.26)", color=GREEN, fontsize=10)
reg = [(-0.95, 0.65, "0.12"), (0.95, 0.65, "0.08"), (0.0, -1.05, "0.10"),
       (0.0, 0.85, "0.06"), (-0.62, -0.42, "0.07"), (0.62, -0.42, "0.05"), (0.0, 0.03, "0.04")]
for x, y, t in reg:
    ax.text(x, y, t, ha="center", va="center", fontsize=10)
ax.add_patch(Rectangle((-2.0, -1.8), 4.0, 3.4, fill=False, ec=GRAY))
ax.text(-1.9, -1.65, "어느 요인도 없음: 0.48", ha="left", fontsize=9, color=GRAY)
ax.text(0.0, 1.47, "$P(H\\cap D)=0.10$ 가운데 0.04가 세 요인 모두", ha="center", fontsize=9, color=GRAY)
ax.set_xlim(-2.05, 2.05); ax.set_ylim(-1.85, 1.65); ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig3_6_1")
