from figstyle import *
import numpy as np
from scipy.stats import beta
from matplotlib.patches import FancyBboxPatch, Polygon

# 그림 12.1.1 최댓값/최솟값 밀도 (U(0,1), n=1,2,5,10)
x = np.linspace(0, 1, 400)
fig, axs = plt.subplots(1, 2, figsize=W2, sharey=True)
for n, c in zip([1, 2, 5, 10], SERIES):
    axs[0].plot(x, n*x**(n-1), color=c, label=f"$n={n}$")
    axs[1].plot(x, n*(1-x)**(n-1), color=c, label=f"$n={n}$")
axs[0].set_title("최댓값 $X_{(n)}$의 밀도  $n x^{n-1}$")
axs[1].set_title("최솟값 $X_{(1)}$의 밀도  $n(1-x)^{n-1}$")
for a in axs: a.set_xlabel("$x$"); a.set_ylim(0, 10.5)
axs[0].legend(loc="upper left")
save(fig, "fig12_1_1")

# 그림 12.1.2 지수분포 생존함수: X(평균10), Y(평균15), min, max
t = np.linspace(0, 40, 400)
SX, SY = np.exp(-t/10), np.exp(-t/15)
fig, ax = plt.subplots(figsize=W1)
ax.plot(t, SX, color=BLUE_L, label="$S_X(t)=e^{-t/10}$")
ax.plot(t, SY, color=ORANGE_L, label="$S_Y(t)=e^{-t/15}$")
ax.plot(t, SX*SY, color=BLUE, lw=2, label=r"$S_{\min}(t)=e^{-t/6}$")
ax.plot(t, 1-(1-SX)*(1-SY), color=ORANGE, lw=2, label=r"$S_{\max}(t)=1-(1-S_X)(1-S_Y)$")
ax.set_xlabel("$t$ (년)"); ax.set_ylabel("생존확률"); ax.legend()
ax.set_title("독립 지수분포의 최솟값·최댓값 생존함수")
save(fig, "fig12_1_2")

# 그림 12.2.1 n=5 균등분포 순서통계량의 밀도 = Beta(k, 6-k)
fig, ax = plt.subplots(figsize=W1)
for k, c in zip(range(1, 6), [BLUE, BLUE_L, GREEN, ORANGE_L, ORANGE]):
    ax.plot(x, beta.pdf(x, k, 6-k), color=c, lw=1.8, label=f"$X_{{({k})}}$  (평균 {k}/6)")
    ax.axvline(k/6, color=c, ls=":", lw=1)
ax.set_xlabel("$x$"); ax.set_ylabel("밀도"); ax.set_ylim(0, 5.3)
ax.set_title(r"$U(0,1)$ 표본 5개의 순서통계량: $X_{(k)}\sim \mathrm{Beta}(k,\,6-k)$")
ax.legend(ncol=5, fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.18), handlelength=1.2, columnspacing=0.8)
save(fig, "fig12_2_1")

# 그림 12.3.1 (X(1),X(2)) 지지영역과 범위 R<=0.5
fig, axs = plt.subplots(1, 2, figsize=W2)
a = axs[0]
a.add_patch(Polygon([[0, 0], [1, 1], [0, 1]], closed=True, fc="#EAF1F8", ec=BLUE))
a.add_patch(Polygon([[0, 0], [0.5, 0.5], [1, 1], [0.5, 1], [0, 0.5]], closed=True, fc=BLUE_L, ec=BLUE, alpha=.9))
a.text(0.12, 0.78, "$f=2$", fontsize=10)
a.text(0.60, 0.80, "$y-x\\leq 0.5$", fontsize=9, color=BLUE, ha="center")
a.set_xlim(0, 1); a.set_ylim(0, 1); a.set_aspect("equal")
a.set_xlabel("$x$ (최솟값)"); a.set_ylabel("$y$ (최댓값)"); a.set_title("결합밀도의 지지영역 $0<x<y<1$")
a.grid(False)
r = np.linspace(0, 1, 200)
b = axs[1]
b.plot(r, 2*(1-r), color=BLUE, lw=2)
b.fill_between(r[r <= .5], 0, 2*(1-r[r <= .5]), color=BLUE_L)
b.text(0.12, 0.5, "면적 0.75", color=BLUE)
b.set_xlabel("$r$"); b.set_title("범위 $R=X_{(2)}-X_{(1)}$의 밀도 $2(1-r)$")
save(fig, "fig12_3_1")

# 그림 12.4.1 직렬·병렬·2-out-of-3 시스템 도해
fig, axs = plt.subplots(1, 3, figsize=(6.6, 2.2))
def comp(ax, x, y, lab):
    ax.add_patch(FancyBboxPatch((x-0.32, y-0.17), 0.64, 0.34, boxstyle="round,pad=0.02", fc="#EAF1F8", ec=BLUE))
    ax.text(x, y, lab, ha="center", va="center", fontsize=9)
for ax in axs:
    ax.set_xlim(0, 4); ax.set_ylim(-1.3, 1.3); ax.axis("off")
ax = axs[0]
ax.plot([0.1, 3.9], [0, 0], color=GRAY, lw=1, zorder=0)
for i, xx in enumerate([1, 2, 3]): comp(ax, xx, 0, f"$X_{i+1}$")
ax.set_title("직렬: $T=\\min(X_1,X_2,X_3)$", fontsize=9.5)
ax = axs[1]
ax.plot([0.1, 0.8], [0, 0], color=GRAY); ax.plot([3.2, 3.9], [0, 0], color=GRAY)
ax.plot([0.8, 0.8], [-0.8, 0.8], color=GRAY); ax.plot([3.2, 3.2], [-0.8, 0.8], color=GRAY)
for i, yy in enumerate([0.8, 0, -0.8]):
    ax.plot([0.8, 3.2], [yy, yy], color=GRAY, lw=1, zorder=0); comp(ax, 2, yy, f"$X_{i+1}$")
ax.set_title("병렬: $T=\\max(X_1,X_2,X_3)$", fontsize=9.5)
ax = axs[2]
for i, yy in enumerate([0.8, 0, -0.8]):
    ax.plot([0.4, 1.8], [yy, yy], color=GRAY, lw=1, zorder=0); comp(ax, 1.1, yy, f"$X_{i+1}$")
    ax.annotate("", xy=(2.55, 0), xytext=(1.45, yy), arrowprops=dict(arrowstyle="->", color=GRAY, lw=0.8))
ax.add_patch(FancyBboxPatch((2.55, -0.3), 1.1, 0.6, boxstyle="round,pad=0.02", fc="#FDF0E6", ec=ORANGE))
ax.text(3.1, 0, "2개 이상\n작동?", ha="center", va="center", fontsize=8)
ax.set_title("2-out-of-3: $T=X_{(2)}$", fontsize=9.5)
save(fig, "fig12_4_1")
