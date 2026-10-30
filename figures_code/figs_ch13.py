from figstyle import *
import numpy as np
from scipy.stats import gamma, norm, binom, poisson

# 그림 13.1.1 지수(1) 표본평균의 표준화 분포 → N(0,1)
z = np.linspace(-3.5, 4, 500)
fig, ax = plt.subplots(figsize=W1)
for n, c in zip([1, 2, 5, 30], [ORANGE_L, ORANGE, GREEN, BLUE]):
    # Xbar ~ Gamma(n, 1/n); Z = (Xbar-1)*sqrt(n)
    xb = 1 + z/np.sqrt(n)
    dens = gamma.pdf(xb, a=n, scale=1/n)/np.sqrt(n)
    ax.plot(z, dens, color=c, lw=1.6, label=f"$n={n}$")
ax.plot(z, norm.pdf(z), color="black", ls="--", lw=1.2, label="$N(0,1)$")
ax.set_xlabel("$z$"); ax.set_ylabel("밀도"); ax.set_ylim(0, 0.75)
ax.set_title(r"지수분포 모집단: $(\bar X_n-\mu)/(\sigma/\sqrt{n})$의 밀도")
ax.legend()
save(fig, "fig13_1_1")

# 그림 13.2.1 이항(180,1/6)의 정규근사와 연속성 보정
k = np.arange(15, 46)
p = binom.pmf(k, 180, 1/6)
fig, ax = plt.subplots(figsize=W1)
ax.bar(k, p, width=1.0, color=[ORANGE_L if kk >= 36 else "#DDE8F3" for kk in k], ec="white", lw=0.5)
xx = np.linspace(14.5, 45.5, 400)
ax.plot(xx, norm.pdf(xx, 30, 5), color=BLUE, lw=1.8, label="$N(30,\\,5^2)$")
sel = xx >= 35.5
ax.fill_between(xx[sel], 0, norm.pdf(xx[sel], 30, 5), color=ORANGE, alpha=0.35, label="$P(Y>35.5)$")
ax.axvline(35.5, color=ORANGE, ls="--", lw=1)
ax.text(35.8, 0.075, "35.5", color=ORANGE, fontsize=9)
ax.set_xlabel("$N$ (6의 눈이 나온 횟수)"); ax.set_ylabel("확률")
ax.set_title("$N\\sim \\mathrm{Bin}(180,1/6)$:  $P(N\\geq 36)\\approx P(Y>35.5)$")
ax.legend(loc="upper left")
save(fig, "fig13_2_1")

# 그림 13.2.2 포아송(100) 누적분포와 정규근사(보정 전후)
x = np.arange(85, 116)
fig, ax = plt.subplots(figsize=W1)
ax.step(x, poisson.cdf(x, 100), where="post", color="black", lw=1.4, label="정확한 $P(S\\leq x)$ (포아송)")
xs = np.linspace(85, 116, 400)
ax.plot(xs, norm.cdf((np.floor(xs)+0.5-100)/10), color=BLUE, lw=1.4, label="정규근사 (연속성 보정)")
ax.plot(xs, norm.cdf((np.floor(xs)-100)/10), color=ORANGE, lw=1.2, ls="--", label="정규근사 (보정 없음)")
ax.set_xlabel("$x$"); ax.set_ylabel("$P(S\\leq x)$"); ax.set_title("$S\\sim \\mathrm{Poi}(100)$의 분포함수 근사")
ax.legend(loc="upper left", fontsize=8.5)
save(fig, "fig13_2_2")

# 그림 13.3.1 가입자 수 n과 손실이 보험료를 초과할 확률
n = np.arange(100, 4001)
prob = 1 - norm.cdf(20*np.sqrt(n)/400)
fig, ax = plt.subplots(figsize=W1)
ax.plot(n, prob, color=BLUE, lw=2)
ax.axhline(0.025, color=ORANGE, ls="--", lw=1); ax.axvline(1537, color=ORANGE, ls=":", lw=1)
ax.text(1600, 0.2, "$n=1537$", color=ORANGE)
ax.text(2800, 0.035, "목표 0.025", color=ORANGE, fontsize=9)
ax.set_xlabel("가입자 수 $n$"); ax.set_ylabel("$P(S_n>120n)$")
ax.set_title("보험료 120(손실 평균 100, 표준편차 400)일 때 초과손실 확률")
save(fig, "fig13_3_1")
