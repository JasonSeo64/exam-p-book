from figstyle import *
import numpy as np

P = np.array([[0.30, 0.10], [0.20, 0.15], [0.10, 0.15]])
xs = [0, 1, 2]; ys = [0, 1]

# 그림 (10.1.1) 결합확률표 히트맵 + 주변분포
fig = plt.figure(figsize=(5.6, 3.6))
gs = fig.add_gridspec(2, 2, width_ratios=[3, 1], height_ratios=[1, 3], wspace=0.05, hspace=0.05)
ax = fig.add_subplot(gs[1, 0]); axt = fig.add_subplot(gs[0, 0], sharex=ax); axr = fig.add_subplot(gs[1, 1], sharey=ax)
ax.imshow(P.T, origin="lower", cmap="Blues", vmin=0, vmax=0.4, aspect="auto",
          extent=[-0.5, 2.5, -0.5, 1.5])
for i in range(3):
    for j in range(2):
        ax.text(i, j, f"{P[i, j]:.2f}", ha="center", va="center", fontsize=11,
                color="white" if P[i, j] > 0.25 else BLUE)
ax.set_xticks(xs); ax.set_yticks(ys); ax.grid(False)
ax.set_xlabel("$X$ (자동차보험 청구건수)"); ax.set_ylabel("$Y$ (주택보험 청구건수)")
axt.bar(xs, P.sum(1), color=BLUE_L, edgecolor=BLUE, width=0.6)
for i, v in enumerate(P.sum(1)): axt.text(i, v + 0.01, f"{v:.2f}", ha="center", fontsize=9)
axt.set_ylim(0, 0.55); axt.axis("off"); axt.set_title("주변분포 $p_X(x)$", fontsize=9, loc="left")
axr.barh(ys, P.sum(0), color=ORANGE_L, edgecolor=ORANGE, height=0.5)
for j, v in enumerate(P.sum(0)): axr.text(v + 0.02, j, f"{v:.2f}", va="center", fontsize=9)
axr.set_xlim(0, 0.85); axr.axis("off"); axr.set_title("$p_Y(y)$", fontsize=9)
save(fig, "fig10_1_1")

# 그림 (10.2.1) 조건부분포와 조건부 기댓값
fig, axs = plt.subplots(1, 2, figsize=W2, sharey=True)
for j, ax in enumerate(axs):
    c = P[:, j] / P[:, j].sum(); m = (np.array(xs) * c).sum()
    ax.bar(xs, c, color=[BLUE_L, ORANGE_L][j], edgecolor=[BLUE, ORANGE][j], width=0.55)
    for i, v in enumerate(c): ax.text(i, v + 0.015, f"{v:.3f}", ha="center", fontsize=8.5)
    ax.axvline(m, color=[BLUE, ORANGE][j], ls="--", lw=1.4)
    ax.text(m + 0.05, 0.56, f"$E[X\\mid Y={j}]={m:.3f}$", color=[BLUE, ORANGE][j], fontsize=9)
    ax.set_title(f"$Y={j}$일 때 $X$의 조건부분포"); ax.set_xticks(xs); ax.set_ylim(0, 0.62)
axs[0].set_ylabel("$p_{X\\mid Y}(x\\mid y)$")
save(fig, "fig10_2_1")

# 그림 (10.3.1) 분산분해 (혼합 포아송)
lam = np.array([0.2, 0.8]); w = np.array([0.7, 0.3])
EN = (w * lam).sum(); EV = EN; VE = (w * lam**2).sum() - EN**2
fig, ax = plt.subplots(figsize=(5.6, 1.9))
ax.barh([0], [EV], color=BLUE_L, edgecolor=BLUE, height=0.45, label="$E[\\mathrm{Var}(N\\mid\\Lambda)]$ (등급 내 변동)")
ax.barh([0], [VE], left=[EV], color=ORANGE_L, edgecolor=ORANGE, height=0.45, label="$\\mathrm{Var}(E[N\\mid\\Lambda])$ (등급 간 변동)")
ax.text(EV / 2, 0, f"0.3800\n({EV/(EV+VE):.1%})", ha="center", va="center", fontsize=9)
ax.text(EV + VE / 2, 0, f"0.0756\n({VE/(EV+VE):.1%})", ha="center", va="center", fontsize=8.5)
ax.text(EV + VE + 0.005, 0, f"  $\\mathrm{{Var}}(N)=0.4556$", va="center", fontsize=10)
ax.set_xlim(0, 0.62); ax.set_yticks([]); ax.set_xlabel("분산"); ax.grid(axis="y")
ax.legend(loc="lower center", bbox_to_anchor=(0.45, 1.0), ncol=2, fontsize=8.5)
save(fig, "fig10_3_1")

# 그림 (10.4.1) 상관계수에 따른 산점도
rng = np.random.default_rng(7)
rhos = [-0.8, 0.0, 0.5, 0.95]
fig, axs = plt.subplots(1, 4, figsize=(6.6, 1.9), sharey=True)
for ax, r in zip(axs, rhos):
    z = rng.multivariate_normal([0, 0], [[1, r], [r, 1]], 250)
    ax.scatter(z[:, 0], z[:, 1], s=5, color=BLUE, alpha=0.55)
    ax.set_title(f"$\\rho={r}$"); ax.set_xlim(-3.2, 3.2); ax.set_ylim(-3.2, 3.2)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_aspect("equal")
save(fig, "fig10_4_1")

# 그림 (10.4.2) 상관계수 0이지만 종속
fig, ax = plt.subplots(figsize=(3.8, 2.8))
xx = np.array([-1, 0, 1]); ax.scatter(xx, xx**2, s=120, color=ORANGE, zorder=3)
for a in xx: ax.text(a, a**2 + 0.12, "1/3", ha="center", fontsize=9)
ax.axhline(2/3, color=GRAY, ls=":", lw=1); ax.text(1.12, 2/3 + 0.07, "$E[Y]=2/3$", fontsize=9, color=GRAY)
ax.set_xlim(-1.6, 1.9); ax.set_ylim(-0.3, 1.45); ax.set_xticks(xx); ax.set_yticks([0, 1])
ax.set_xlabel("$X$"); ax.set_ylabel("$Y=X^2$"); ax.set_title("$\\mathrm{Cov}(X,Y)=0$ 이지만 $Y$는 $X$의 함수")
save(fig, "fig10_4_2")
