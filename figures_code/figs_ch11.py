from figstyle import *
import numpy as np
from scipy.stats import poisson, nbinom, norm

# 그림 (11.2.1) 합성곱 도해
px = np.array([0.5, 0.3, 0.2]); py = np.array([0.6, 0.4]); ps = np.convolve(px, py)
fig, axs = plt.subplots(1, 3, figsize=(6.6, 2.3), sharey=True,
                        gridspec_kw={"width_ratios": [3, 2, 4]})
for ax, p, c, t in [(axs[0], px, BLUE, "$p_X$  (독립)"), (axs[1], py, GREEN, "$p_Y$"), (axs[2], ps, ORANGE, "$p_S$  ($S=X+Y$, 합성곱)")]:
    k = np.arange(len(p))
    ax.bar(k, p, color=c, alpha=0.75, width=0.6)
    for i, v in enumerate(p): ax.text(i, v + 0.02, f"{v:.2f}", ha="center", fontsize=8.5)
    ax.set_xticks(k); ax.set_title(t); ax.set_ylim(0, 0.72)
save(fig, "fig11_2_1")

# 그림 (11.2.2) 포아송 합
k = np.arange(0, 14)
fig, ax = plt.subplots(figsize=W1)
w = 0.27
ax.bar(k - w, poisson.pmf(k, 2), w, color=BLUE_L, edgecolor=BLUE, label="$N_A\\sim$ Poi(2)")
ax.bar(k, poisson.pmf(k, 3), w, color=ORANGE_L, edgecolor=ORANGE, label="$N_B\\sim$ Poi(3)")
ax.bar(k + w, poisson.pmf(k, 5), w, color=GREEN, alpha=0.8, label="$N_A+N_B\\sim$ Poi(5)")
ax.set_xticks(k); ax.set_xlabel("청구건수"); ax.set_ylabel("확률"); ax.legend()
save(fig, "fig11_2_2")

# 그림 (11.2.3) 기하분포 합 -> 음이항
p = 0.3; k = np.arange(0, 25)
fig, ax = plt.subplots(figsize=W1)
for r, c in zip([1, 2, 3, 5], SERIES):
    ax.plot(k, nbinom.pmf(k, r, p), "o-", ms=3.5, lw=1.2, color=c,
            label=f"$r={r}$" + (" (기하분포)" if r == 1 else ""))
ax.set_xlabel("실패 횟수의 합 $S=X_1+\\cdots+X_r$"); ax.set_ylabel("$P(S=k)$")
ax.set_title("독립인 기하분포 $r$개의 합 = 음이항분포 ($p=0.3$)"); ax.legend()
save(fig, "fig11_2_3")

# 그림 (11.3.1) 정규확률변수의 합
x = np.linspace(0, 2200, 600)
fig, ax = plt.subplots(figsize=W1)
for m, s, c, lab in [(500, 100, BLUE, "$X_1\\sim N(500,100^2)$"), (800, 150, GREEN, "$X_2\\sim N(800,150^2)$"),
                     (1300, np.sqrt(100**2 + 150**2), ORANGE, "$X_1+X_2\\sim N(1300,180.3^2)$")]:
    ax.plot(x, norm.pdf(x, m, s), color=c, lw=1.8, label=lab)
sd = np.sqrt(32500); xr = x[x >= 1500]
ax.fill_between(xr, norm.pdf(xr, 1300, sd), color=ORANGE, alpha=0.3)
ax.annotate("$P(X_1+X_2>1500)\\approx0.1335$", xy=(1600, norm.pdf(1600, 1300, sd) * 0.6), xytext=(1700, 0.0026),
            arrowprops=dict(arrowstyle="->", color=ORANGE), fontsize=9, color=ORANGE)
ax.set_xlabel("손실액"); ax.set_ylabel("밀도"); ax.legend(loc="upper right", fontsize=8.5)
save(fig, "fig11_3_1")

# 그림 (11.3.2) P(X>Y) = P(X-Y>0)
d = np.linspace(-30, 50, 500)
fig, ax = plt.subplots(figsize=W1)
ax.plot(d, norm.pdf(d, 10, 10), color=BLUE, lw=1.8, label="$D=X-Y\\sim N(10,\\,10^2)$")
dd = d[d > 0]; ax.fill_between(dd, norm.pdf(dd, 10, 10), color=BLUE_L, alpha=0.7)
ax.axvline(0, color=GRAY, lw=1, ls="--")
ax.text(14, 0.012, "$P(D>0)=\\Phi(1)=0.8413$", fontsize=10, color=BLUE)
ax.set_xlabel("$d$"); ax.set_ylabel("밀도"); ax.legend(loc="upper left")
save(fig, "fig11_3_2")
