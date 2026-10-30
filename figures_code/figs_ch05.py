from figstyle import *
import numpy as np
from scipy import stats
# fig5_2_1 survival area = E[X], limited expectation
fig,ax=plt.subplots(figsize=W1)
t=np.linspace(0,3000,500); S=(1000/(1000+t))**3
ax.plot(t,S,color=BLUE,label="$S(x)=(1000/(1000+x))^3$")
ax.fill_between(t,S,where=t<=1000,color=BLUE_L,alpha=.9,label="$E[X\\wedge 1000]=375$")
ax.fill_between(t,S,where=t>=1000,color=ORANGE_L,alpha=.7,label="나머지 면적 $=125$")
ax.axvline(1000,color=GRAY,ls='--',lw=.8); ax.set_xlabel("$x$"); ax.set_title("생존함수 아래 면적 = 기댓값 ($E[X]=500$)")
ax.legend(fontsize=9)
save(fig,"fig5_2_1")
# fig5_4_1 same mean different variance
fig,ax=plt.subplots(figsize=W1)
x=np.linspace(-1,11,400)
for s,c in ((0.8,BLUE),(2.0,ORANGE)):
    ax.plot(x,stats.norm.pdf(x,5,s),color=c,label=f"평균 5, 표준편차 {s}")
ax.axvline(5,color=GRAY,ls='--',lw=.8); ax.legend(); ax.set_title("평균이 같아도 분산에 따라 흩어진 정도가 다르다"); ax.set_xlabel("$x$")
save(fig,"fig5_4_1")
# fig5_5_1 median & percentile on cdf
fig,ax=plt.subplots(figsize=W1)
t=np.linspace(0,4000,500); F=1-(1000/(1000+t))**2
ax.plot(t,F,color=BLUE)
for q,xv,c in ((0.5,414.21,ORANGE),(0.9,2162.28,GREEN)):
    ax.plot([0,xv],[q,q],ls='--',color=c,lw=1); ax.plot([xv,xv],[0,q],ls='--',color=c,lw=1)
    ax.text(xv+40,0.03,f"$\\pi_{{{q}}}\\approx{xv:,.0f}$",color=c,fontsize=9)
ax.set_ylim(0,1.02); ax.set_xlabel("$x$"); ax.set_ylabel("$F(x)$"); ax.set_title("백분위수: $F(\\pi_p)=p$를 만족하는 값")
save(fig,"fig5_5_1")
# fig5_6_1 chebyshev bound vs exact
fig,ax=plt.subplots(figsize=W1)
k=np.linspace(1,4,200)
ax.plot(k,1/k**2,color=GRAY,lw=2,label="체비셰프 상한 $1/k^2$")
ax.plot(k,2*(1-stats.norm.cdf(k)),color=BLUE,label="정규분포")
ax.plot(k,np.exp(-(1+k)),color=ORANGE,label="지수분포(평균 1)")
ax.plot(k,np.clip(1-k/np.sqrt(3),0,None),color=GREEN,label="균등분포")
ax.set_xlabel("$k$"); ax.set_ylabel("$P(|X-\\mu|\\geq k\\sigma)$"); ax.legend(); ax.set_title("체비셰프 부등식은 모든 분포에 성립하지만 보수적이다")
save(fig,"fig5_6_1")
