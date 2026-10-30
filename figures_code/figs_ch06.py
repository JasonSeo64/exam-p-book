from figstyle import *
import numpy as np
from scipy import stats
from matplotlib.patches import FancyBboxPatch

# 그림 6.1.1 이산균등분포
fig, ax = plt.subplots(figsize=(5.2, 2.8))
k = np.arange(1, 11)
ax.bar(k, np.full(10, 0.1), color=BLUE, width=0.6)
ax.set_xticks(k); ax.set_ylim(0, 0.15)
ax.set_xlabel("$x$"); ax.set_ylabel("$p_X(x)$")
ax.set_title("이산균등분포: $\\{1,2,\\ldots,10\\}$ 위의 확률질량함수")
save(fig, "fig6_1_1")

# 그림 6.2.1 이항분포 모수별 비교
fig, axes = plt.subplots(1, 3, figsize=(6.6, 2.6), sharey=True)
k = np.arange(0, 21)
for ax, p, c in zip(axes, [0.1, 0.3, 0.5], [BLUE, ORANGE, GREEN]):
    ax.bar(k, stats.binom.pmf(k, 20, p), color=c, width=0.7)
    ax.set_title(f"$n=20,\\ p={p}$")
    ax.set_xlabel("$x$")
    ax.set_xticks([0, 5, 10, 15, 20])
axes[0].set_ylabel("$p_X(x)$")
fig.suptitle("이항분포 $\\mathrm{Bin}(20,p)$의 확률질량함수", y=1.03, fontsize=11)
save(fig, "fig6_2_1")

# 그림 6.3.1 기하분포 두 가지 정의
fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.6), sharey=True)
p = 0.2
k0 = np.arange(0, 16)
axes[0].bar(k0, p * (1 - p) ** k0, color=BLUE, width=0.7)
axes[0].set_title("실패 횟수 $N\\in\\{0,1,2,\\ldots\\}$")
axes[0].set_xlabel("$n$"); axes[0].set_ylabel("확률")
k1 = np.arange(1, 17)
axes[1].bar(k1, p * (1 - p) ** (k1 - 1), color=ORANGE, width=0.7)
axes[1].set_title("시행 횟수 $X=N+1\\in\\{1,2,\\ldots\\}$")
axes[1].set_xlabel("$x$")
fig.suptitle("기하분포 ($p=0.2$): 두 가지 정의", y=1.03, fontsize=11)
save(fig, "fig6_3_1")

# 그림 6.4.1 음이항분포 (r 별)
fig, ax = plt.subplots(figsize=W1)
x = np.arange(0, 31)
for r, c in zip([1, 3, 6], [BLUE, ORANGE, GREEN]):
    ax.plot(x, stats.nbinom.pmf(x, r, 0.3), "o-", ms=3.5, lw=1.2, color=c, label=f"$r={r}$")
ax.set_xlabel("$r$번째 성공 전의 실패 횟수 $n$")
ax.set_ylabel("$P(N=n)$")
ax.set_title("음이항분포 ($p=0.3$): $r$이 커질수록 오른쪽으로 이동·퍼짐")
ax.legend()
save(fig, "fig6_4_1")

# 그림 6.5.1 초기하 vs 이항
fig, ax = plt.subplots(figsize=W1)
k = np.arange(0, 9)
h = stats.hypergeom.pmf(k, 100, 10, 8)
b = stats.binom.pmf(k, 8, 0.1)
ax.bar(k - 0.18, h, width=0.36, color=BLUE, label="초기하 (비복원, $N=100,K=10,n=8$)")
ax.bar(k + 0.18, b, width=0.36, color=ORANGE_L, label="이항 (복원, $n=8,p=0.1$)")
ax.set_xlabel("표본 중 사기 청구 건수 $x$"); ax.set_ylabel("확률")
ax.set_title("초기하분포와 이항근사")
ax.legend()
save(fig, "fig6_5_1")

# 그림 6.6.1 포아송 모수별
fig, ax = plt.subplots(figsize=W1)
k = np.arange(0, 16)
for lam, c, off in zip([1, 3, 6], [BLUE, ORANGE, GREEN], [-0.25, 0, 0.25]):
    ax.bar(k + off, stats.poisson.pmf(k, lam), width=0.25, color=c, label=f"$\\lambda={lam}$")
ax.set_xlabel("청구 건수 $n$"); ax.set_ylabel("$P(N=n)$")
ax.set_title("포아송분포의 확률질량함수")
ax.legend()
save(fig, "fig6_6_1")

# 그림 6.6.2 포아송 근사
fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.7), sharey=True)
k = np.arange(0, 11)
for ax, (n, p) in zip(axes, [(10, 0.2), (1000, 0.002)]):
    ax.bar(k - 0.2, stats.binom.pmf(k, n, p), width=0.4, color=BLUE, label="이항")
    ax.bar(k + 0.2, stats.poisson.pmf(k, n * p), width=0.4, color=ORANGE_L, label="포아송 ($\\lambda=np=2$)")
    ax.set_title(f"$n={n},\\ p={p}$")
    ax.set_xlabel("$x$"); ax.set_xticks(k)
axes[0].set_ylabel("확률"); axes[1].legend(fontsize=8)
fig.suptitle("이항분포의 포아송 근사: $n$이 크고 $p$가 작을수록 정확", y=1.03, fontsize=11)
save(fig, "fig6_6_2")

# 그림 6.7.1 분포 간 관계 도해
fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
HW, HH = 0.95, 0.5
nodes = {
    "bern": (1.3, 4.8, "베르누이\n$\\mathrm{Bin}(1,p)$"),
    "bin": (5.0, 4.8, "이항\n$\\mathrm{Bin}(n,p)$"),
    "poi": (8.7, 4.8, "포아송\n$\\mathrm{Poi}(\\lambda)$"),
    "geo": (1.3, 1.2, "기하\n$\\mathrm{Geo}(p)$"),
    "nb": (5.0, 1.2, "음이항\n$\\mathrm{NB}(r,p)$"),
    "hyp": (8.7, 1.2, "초기하\n$\\mathrm{HG}(N,K,n)$"),
}
for key, (x, y, t) in nodes.items():
    ax.add_patch(FancyBboxPatch((x - HW, y - HH), 2 * HW, 2 * HH, boxstyle="round,pad=0.05",
                                fc="#EAF1F8", ec=BLUE, lw=1.0))
    ax.text(x, y, t, ha="center", va="center", fontsize=9)

def arr(p1, p2, label, lp, ha="center"):
    ax.annotate("", xy=p2, xytext=p1, arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.3))
    ax.text(lp[0], lp[1], label, ha=ha, va="center", fontsize=8.5, color=ORANGE)

arr((2.35, 4.8), (3.95, 4.8), "독립 $n$개의 합", (3.15, 5.25))
arr((6.05, 4.8), (7.65, 4.8), "$n\\to\\infty,\\ np=\\lambda$", (6.85, 5.25))
arr((1.3, 4.2), (1.3, 1.8), "첫 성공까지의\n실패(시행) 횟수", (1.45, 3.0), ha="left")
arr((2.35, 1.2), (3.95, 1.2), "독립 $r$개의 합", (3.15, 1.65))
arr((8.2, 1.8), (5.6, 4.2), "$N\\to\\infty,\\ K/N=p$", (7.55, 3.0), ha="left")
ax.set_title("주요 이산분포 사이의 관계", fontsize=11)
save(fig, "fig6_7_1")
