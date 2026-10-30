from figstyle import *
import numpy as np
from scipy import stats

# 그림 7.1.1 연속균등분포 pdf, cdf
fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.6))
a, b = 2, 6
x = np.linspace(0, 8, 400)
axes[0].plot(x, stats.uniform.pdf(x, a, b - a), color=BLUE, lw=1.8)
axes[0].fill_between(x, stats.uniform.pdf(x, a, b - a), where=(x >= 3) & (x <= 5), color=BLUE_L, alpha=0.7)
axes[0].text(4, 0.12, "$P(3\\leq X\\leq 5)$\n$=2/4$", ha="center", fontsize=8.5)
axes[0].set_title("확률밀도함수 $f_X(x)=1/(b-a)$")
axes[0].set_xlabel("$x$"); axes[0].set_ylim(0, 0.4)
axes[0].set_xticks([0, 2, 3, 5, 6, 8]); axes[0].set_xticklabels(["0", "$a=2$", "3", "5", "$b=6$", "8"])
axes[1].plot(x, stats.uniform.cdf(x, a, b - a), color=ORANGE, lw=1.8)
axes[1].set_title("누적분포함수 $F_X(x)=(x-a)/(b-a)$")
axes[1].set_xlabel("$x$"); axes[1].set_xticks([0, 2, 6, 8])
save(fig, "fig7_1_1")

# 그림 7.2.1 지수분포 pdf
fig, ax = plt.subplots(figsize=W1)
x = np.linspace(0, 8, 400)
for th, c in zip([0.5, 1, 2, 4], SERIES):
    ax.plot(x, stats.expon.pdf(x, scale=th), color=c, lw=1.6, label=f"$\\theta={th}$")
ax.set_ylim(0, 1.2); ax.set_xlabel("$x$"); ax.set_ylabel("$f_X(x)$")
ax.set_title("지수분포의 확률밀도함수 $f_X(x)=\\frac{1}{\\theta}e^{-x/\\theta}$")
ax.legend()
save(fig, "fig7_2_1")

# 그림 7.2.2 무기억성
fig, ax = plt.subplots(figsize=W1)
th = 10
t = np.linspace(0, 40, 400)
S = np.exp(-t / th)
ax.plot(t, S, color=BLUE, lw=1.8, label="$S(t)=P(T>t)$")
s0 = 5
tt = t[t >= s0]
ax.plot(tt, np.exp(-(tt - s0) / th) , color=ORANGE, lw=1.8, ls="--",
        label="$P(T>t\\mid T>5)=S(t-5)$")
ax.axvline(s0, color=GRAY, lw=0.8, ls=":")
ax.annotate("5년 생존 후에도\n같은 모양으로 다시 시작", xy=(12, np.exp(-0.7)), xytext=(20, 0.75),
            arrowprops=dict(arrowstyle="->", color=GRAY), fontsize=8.5)
ax.set_xlabel("$t$ (년)"); ax.set_ylabel("생존확률")
ax.set_title("지수분포의 무기억성 ($\\theta=10$)")
ax.legend(loc="upper right")
save(fig, "fig7_2_2")

# 그림 7.3.1 감마분포
fig, ax = plt.subplots(figsize=W1)
x = np.linspace(0, 15, 500)
for al, c in zip([1, 2, 3, 5], SERIES):
    ax.plot(x, stats.gamma.pdf(x, al, scale=1), color=c, lw=1.6, label=f"$\\alpha={al}$")
ax.set_ylim(0, 1.0); ax.set_xlabel("$x$"); ax.set_ylabel("$f_X(x)$")
ax.set_title("감마분포의 확률밀도함수 ($\\theta=1$): $\\alpha=1$이면 지수분포")
ax.legend()
save(fig, "fig7_3_1")

# 그림 7.4.1 베타분포
fig, ax = plt.subplots(figsize=W1)
x = np.linspace(0.001, 0.999, 500)
for (a_, b_), c in zip([(1, 1), (2, 3), (3, 2), (0.5, 0.5), (5, 5)], SERIES):
    ax.plot(x, stats.beta.pdf(x, a_, b_), color=c, lw=1.6, label=f"$a={a_},\\ b={b_}$")
ax.set_ylim(0, 3.2); ax.set_xlabel("$x$"); ax.set_ylabel("$f_X(x)$")
ax.set_title("베타분포의 다양한 형태 (구간 $[0,1]$)")
ax.legend(fontsize=8, ncol=2)
save(fig, "fig7_4_1")

# 그림 7.5.1 정규 표준화
fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.7))
mu, sd = 5000, 1000
x = np.linspace(mu - 4 * sd, mu + 4 * sd, 500)
axes[0].plot(x, stats.norm.pdf(x, mu, sd), color=BLUE, lw=1.6)
axes[0].fill_between(x, stats.norm.pdf(x, mu, sd), where=x >= 6500, color=ORANGE_L)
axes[0].set_title("$X\\sim N(5000,\\ 1000^2)$")
axes[0].set_xticks([3000, 5000, 6500]); axes[0].set_yticks([])
z = np.linspace(-4, 4, 500)
axes[1].plot(z, stats.norm.pdf(z), color=BLUE, lw=1.6)
axes[1].fill_between(z, stats.norm.pdf(z), where=z >= 1.5, color=ORANGE_L)
axes[1].set_title("$Z=(X-\\mu)/\\sigma\\sim N(0,1)$")
axes[1].set_xticks([-2, 0, 1.5]); axes[1].set_yticks([])
axes[1].text(2.2, 0.12, "$1-\\Phi(1.5)$\n$=0.0668$", fontsize=8.5)
fig.suptitle("표준화: 같은 면적(확률)을 표준정규분포표로 읽는다", y=1.03, fontsize=11)
save(fig, "fig7_5_1")

# 그림 7.5.2 68-95-99.7
fig, ax = plt.subplots(figsize=W1)
z = np.linspace(-4, 4, 600)
ax.plot(z, stats.norm.pdf(z), color=BLUE, lw=1.6)
for k, c in zip([3, 2, 1], ["#DDEBF7", BLUE_L, "#5B9BD5"]):
    ax.fill_between(z, stats.norm.pdf(z), where=np.abs(z) <= k, color=c)
for k, txt, yy in zip([1, 2, 3], ["68.27%", "95.45%", "99.73%"], [0.2, 0.06, 0.015]):
    ax.annotate("", xy=(k, yy), xytext=(-k, yy), arrowprops=dict(arrowstyle="<->", color="black", lw=0.8))
    ax.text(0, yy + 0.008, txt, ha="center", fontsize=8.5)
ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
ax.set_xticklabels(["$\\mu-3\\sigma$", "$\\mu-2\\sigma$", "$\\mu-\\sigma$", "$\\mu$", "$\\mu+\\sigma$", "$\\mu+2\\sigma$", "$\\mu+3\\sigma$"], fontsize=8)
ax.set_yticks([]); ax.set_title("정규분포에서 평균으로부터 $k\\sigma$ 이내의 확률")
save(fig, "fig7_5_2")

# 그림 7.6.1 연속성 보정
fig, ax = plt.subplots(figsize=W1)
n, p = 100, 0.2
k = np.arange(8, 33)
pm = stats.binom.pmf(k, n, p)
cols = [ORANGE_L if kk >= 25 else "#DDEBF7" for kk in k]
ax.bar(k, pm, width=1.0, color=cols, edgecolor="white", lw=0.6)
xx = np.linspace(8, 33, 400)
ax.plot(xx, stats.norm.pdf(xx, 20, 4), color=BLUE, lw=1.6, label="$N(20,\\ 4^2)$")
ax.axvline(24.5, color=ORANGE, lw=1.2, ls="--")
ax.text(24.7, 0.085, "$x=24.5$\n(연속성 보정)", color=ORANGE, fontsize=8.5)
ax.set_xlabel("$x$"); ax.set_ylabel("확률")
ax.set_title("$\\mathrm{Bin}(100,0.2)$의 $P(X\\geq 25)$: 막대 $[24.5,25.5]$부터 면적을 잰다")
ax.legend(loc="upper left")
save(fig, "fig7_6_1")

# 그림 7.S.1 로그정규 (보충)
fig, ax = plt.subplots(figsize=W1)
x = np.linspace(0.01, 6, 500)
for s_, c in zip([0.25, 0.5, 1.0], SERIES):
    ax.plot(x, stats.lognorm.pdf(x, s_, scale=1), color=c, lw=1.6, label=f"$\\mu=0,\\ \\sigma={s_}$")
ax.set_xlabel("$x$"); ax.set_ylabel("$f_X(x)$"); ax.legend()
ax.set_title("로그정규분포: 오른쪽 꼬리가 긴 손해액 분포")
save(fig, "fig7_7_1")
