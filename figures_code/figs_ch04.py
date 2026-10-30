from figstyle import *
import numpy as np
# fig4_2_1: pmf & step cdf
x=np.array([0,1,2,3]); p=np.array([0.2,0.3,0.4,0.1])
fig,(a1,a2)=plt.subplots(1,2,figsize=W2)
a1.vlines(x,0,p,color=BLUE,lw=3); a1.plot(x,p,'o',color=BLUE)
for xi,pi in zip(x,p): a1.text(xi,pi+0.02,f"{pi:.1f}",ha='center',fontsize=9)
a1.set_xticks(x); a1.set_ylim(0,0.5); a1.set_title("확률질량함수 $p_X(x)$"); a1.set_xlabel("$x$ (청구건수)")
F=np.cumsum(p); xs=[-1,0,1,2,3,4]
for i in range(len(xs)-1):
    y=0 if i==0 else F[i-1]
    a2.hlines(y,xs[i],xs[i+1],color=BLUE,lw=2)
    if i>0: a2.plot(xs[i],y,'o',color=BLUE,ms=5)
    if i<len(xs)-2: a2.plot(xs[i+1],y,'o',mfc='white',mec=BLUE,ms=5)
a2.set_ylim(-0.05,1.1); a2.set_xticks(x); a2.set_title("누적분포함수 $F_X(x)$ (계단함수)"); a2.set_xlabel("$x$")
save(fig,"fig4_2_1")
# fig4_3_1 pdf area & cdf
fig,(a1,a2)=plt.subplots(1,2,figsize=W2)
t=np.linspace(0,3,300); f=t**2/9
a1.plot(t,f,color=BLUE); m=(t>=1)&(t<=2); a1.fill_between(t[m],f[m],color=BLUE_L,alpha=.8)
a1.text(1.5,0.08,"면적 $=7/27$",ha='center',fontsize=9); a1.set_title("밀도 $f(x)=x^2/9$"); a1.set_xlabel("$x$")
Fx=t**3/27; a2.plot(t,Fx,color=ORANGE)
for v in (1,2): a2.plot([v,v],[0,v**3/27],ls='--',color=GRAY,lw=.8); a2.plot([0,v],[v**3/27]*2,ls='--',color=GRAY,lw=.8)
a2.annotate("",xy=(0.15,8/27),xytext=(0.15,1/27),arrowprops=dict(arrowstyle='<->',color=BLUE))
a2.text(0.22,0.15,"$F(2)-F(1)$",fontsize=9,color=BLUE); a2.set_title("분포함수 $F(x)=x^3/27$"); a2.set_xlabel("$x$")
save(fig,"fig4_3_1")
# fig4_5_1 mixed cdf with jumps
fig,ax=plt.subplots(figsize=W1)
ax.plot([-0.5,0],[0,0],color=BLUE,lw=2); ax.plot([0,1],[0,0.25],color=BLUE,lw=2)
ax.plot([1,2],[0.5,0.75],color=BLUE,lw=2); ax.plot([2,3],[1,1],color=BLUE,lw=2)
for xv,lo,hi in ((1,0.25,0.5),(2,0.75,1)):
    ax.plot(xv,lo,'o',mfc='white',mec=BLUE); ax.plot(xv,hi,'o',color=BLUE)
    ax.annotate(f"점프 = {hi-lo:.2f}",xy=(xv,(lo+hi)/2),xytext=(xv+0.25,(lo+hi)/2-0.08),arrowprops=dict(arrowstyle='->',color=ORANGE),color=ORANGE,fontsize=9)
ax.set_title("혼합형 분포의 누적분포함수: 연속 부분 + 점프(확률질량)"); ax.set_xlabel("$x$"); ax.set_ylabel("$F_X(x)$"); ax.set_ylim(-0.05,1.1)
save(fig,"fig4_5_1")
# fig4_6_1 hazard shapes
fig,(a1,a2)=plt.subplots(1,2,figsize=W2)
t=np.linspace(0.01,5,300)
hs={"증가 (와이블 $\\tau=2$)":(lambda t:t, lambda t:np.exp(-t**2/2)),
    "일정 (지수)":(lambda t:0*t+0.8, lambda t:np.exp(-0.8*t)),
    "감소 (파레토형)":(lambda t:3/(1+t), lambda t:(1/(1+t))**3)}
for (lab,(h,S)),c in zip(hs.items(),SERIES):
    a1.plot(t,h(t),color=c,label=lab); a2.plot(t,S(t),color=c,label=lab)
a1.set_ylim(0,3.2); a1.set_title("위험률 $h(x)$"); a2.set_title("생존함수 $S(x)=e^{-\\int_0^x h(t)dt}$")
a1.legend(fontsize=8); a1.set_xlabel("$x$"); a2.set_xlabel("$x$")
save(fig,"fig4_6_1")
