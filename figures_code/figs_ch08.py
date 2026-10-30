from figstyle import *
import numpy as np
x=np.linspace(0,4000,801)
# fig8_1_1: payment functions
d,u,a=500,2500,0.8
fig,axs=plt.subplots(1,3,figsize=(7.2,2.6),sharey=True)
cases=[("정액공제 $d=500$",np.maximum(x-d,0)),
       ("보상한도 $m=u=2500$ ($d=0$)",np.minimum(x,u)),
       ("공제+한도+공동보험 80%",a*(np.minimum(x,u)-np.minimum(x,d)))]
for ax,(t,y) in zip(axs,cases):
    ax.plot(x,x,color=GRAY,lw=0.8,ls="--",label="$y=x$")
    ax.plot(x,y,color=BLUE,lw=2)
    ax.set_title(t,fontsize=9.5); ax.set_xlabel("손실 $x$")
    ax.set_xlim(0,4000); ax.set_ylim(0,4000)
axs[0].set_ylabel("지급액 $y$"); axs[0].legend(loc="upper left",fontsize=8)
axs[0].annotate("$d$",(d,0),(d+250,600),arrowprops=dict(arrowstyle="->",color=ORANGE),color=ORANGE)
axs[2].annotate("최대 지급액\n$m=\\alpha(u-d)=1600$",(3200,1600),(1700,2900),fontsize=8,arrowprops=dict(arrowstyle="->",color=ORANGE),color=ORANGE)
fig.tight_layout(); save(fig,"fig8_1_1")

# fig8_2_1: survival area split
th=1000; d=500
xx=np.linspace(0,4000,600); S=np.exp(-xx/th)
fig,ax=plt.subplots(figsize=W1)
ax.plot(xx,S,color=BLUE,lw=2,label="$S_X(x)=e^{-x/1000}$")
ax.fill_between(xx,0,S,where=xx<=d,color=BLUE_L,alpha=0.8,label="$E[X\\wedge d]=\\int_0^d S_X(x)\\,dx$")
ax.fill_between(xx,0,S,where=xx>=d,color=ORANGE_L,alpha=0.8,label="$E[(X-d)_+]=\\int_d^\\infty S_X(x)\\,dx$")
ax.axvline(d,color=ORANGE,lw=1,ls="--"); ax.text(d+40,0.92,"$d=500$",color=ORANGE)
ax.set_xlabel("$x$"); ax.set_ylabel("$S_X(x)$"); ax.set_xlim(0,4000); ax.set_ylim(0,1.02)
ax.legend(loc="upper right",fontsize=9)
ax.text(120,0.25,"393.47",color=BLUE,fontsize=10); ax.text(1200,0.12,"606.53",color=ORANGE,fontsize=10)
save(fig,"fig8_2_1")

# fig8_3_1: limited expected value curves
uu=np.linspace(0,3000,400)
lev_exp=1000*(1-np.exp(-uu/1000))
lev_uni=np.where(uu<=2000,uu-uu**2/4000,1000)
lev_par=500*(1-(1000/(1000+uu))**2)
fig,ax=plt.subplots(figsize=W1)
ax.plot(uu,lev_exp,color=BLUE,lw=2,label="지수분포 (평균 1000)")
ax.plot(uu,lev_uni,color=GREEN,lw=2,label="균등분포 $U(0,2000)$ (평균 1000)")
ax.plot(uu,lev_par,color=ORANGE,lw=2,label="$S(x)=(1000/(1000+x))^3$ (평균 500)")
ax.plot(uu,uu,color=GRAY,ls="--",lw=0.8,label="$y=u$")
for m,c in ((1000,BLUE),(500,ORANGE)): ax.axhline(m,color=c,lw=0.6,ls=":")
ax.set_xlabel("한도 $u$ (공제 없음, $u=m$)"); ax.set_ylabel("$E[X\\wedge u]$"); ax.set_ylim(0,1150); ax.set_xlim(0,3000)
ax.legend(loc="lower right",fontsize=8.5)
save(fig,"fig8_3_1")

# fig8_5_1: leverage effect of inflation on deductible
dd=np.linspace(0,3000,300); r=0.10
ratio=(1+r)*1000*np.exp(-dd/(1000*(1+r)))/(1000*np.exp(-dd/1000))
lim=(1+r)*1000*(1-np.exp(-dd/(1100)))/(1000*(1-np.exp(-dd/1000)+1e-12))
fig,ax=plt.subplots(figsize=W1)
ax.plot(dd,ratio,color=ORANGE,lw=2,label="공제 $d$ 적용: $E[(X^*-d)_+]/E[(X-d)_+]$")
ax.plot(dd[1:],lim[1:],color=BLUE,lw=2,label="한도 $u$ 적용: $E[X^*\\wedge u]/E[X\\wedge u]$")
ax.axhline(1+r,color=GRAY,ls="--",lw=1); ax.text(2300,1.112,"$1+r=1.10$",color=GRAY)
ax.set_xlabel("공제금액 $d$ 또는 한도 $u$"); ax.set_ylabel("인플레이션 후/전 기대지급액")
ax.set_ylim(0.98,1.45); ax.legend(loc="upper left",fontsize=9)
ax.set_title("손실 $X\\sim\\mathrm{Exp}(1000)$, 인플레이션 10% ($X^*=1.1X$)",fontsize=10)
save(fig,"fig8_5_1")

# fig8_6_1: distribution of Y^L (mixed) and Y^P
y=np.linspace(0,4000,400)
fig,axs=plt.subplots(1,2,figsize=W2)
p0=1-np.exp(-0.5)
ax=axs[0]; ax.plot(y[1:],np.exp(-0.5)*np.exp(-y[1:]/1000)/1000*1000,color=BLUE,lw=2)
ax.vlines(0,0,p0,color=ORANGE,lw=3); ax.plot(0,p0,"o",color=ORANGE)
ax.text(400,0.85,f"$P(Y^L=0)={p0:.4f}$",color=ORANGE,fontsize=9)
ax.set_title("손실당 지급액 $Y^L$ (혼합형)",fontsize=10); ax.set_xlabel("$y$"); ax.set_ylabel("밀도×1000 / 점확률")
ax=axs[1]; ax.plot(y,np.exp(-y/1000),color=BLUE,lw=2)
ax.set_title("지급당 지급액 $Y^P$ (지수, 평균 1000)",fontsize=10); ax.set_xlabel("$y$"); ax.set_ylabel("밀도×1000")
for a in axs: a.set_xlim(-100,4000); a.set_ylim(0,1.05)
fig.tight_layout(); save(fig,"fig8_6_1")

# fig8_7_1: CDF of Y^L and Y^P (Ex 8.7.1: X~U(0,5000), d=500, alpha=0.8, m=2000)
d,a,m=500,0.8,2000
yy=np.linspace(0,m,400,endpoint=False)
FL=(d+yy/a)/5000; FP=(FL-0.1)/0.9
fig,axs=plt.subplots(1,2,figsize=W2,sharey=True)
for ax,F,t,p0,pm in ((axs[0],FL,"손실당 지급액 $Y^L$",0.1,"0.4"),(axs[1],FP,"지급당 지급액 $Y^P$",0.0,"4/9")):
    ax.plot([-200,0],[0,0],color=BLUE,lw=2); ax.plot(yy,F,color=BLUE,lw=2); ax.plot([m,2400],[1,1],color=BLUE,lw=2)
    ax.plot(m,F[-1],"o",mfc="white",color=BLUE); ax.plot(m,1,"o",color=BLUE)
    if p0>0: ax.plot(0,0,"o",mfc="white",color=BLUE); ax.plot(0,p0,"o",color=BLUE); ax.annotate(f"$P(Y^L=0)={p0}$",(0,p0),(250,0.02),fontsize=8.5,color=ORANGE,arrowprops=dict(arrowstyle="->",color=ORANGE))
    ax.vlines(m,F[-1],1,color=ORANGE,lw=1,ls="--")
    ax.annotate(f"$y=m$의 점확률 {pm}",(m,0.78),(700,0.72),fontsize=8.5,color=ORANGE,arrowprops=dict(arrowstyle="->",color=ORANGE))
    ax.axhline(0.5,color=GRAY,ls=":",lw=0.8); ax.axhline(0.9,color=GRAY,ls=":",lw=0.8)
    ax.set_title(t,fontsize=10); ax.set_xlabel("$y$"); ax.set_xlim(-200,2400); ax.set_ylim(-0.03,1.05)
axs[0].set_ylabel("분포함수")
axs[0].plot(1600,0.5,"s",color=GREEN,ms=4); axs[0].text(1000,0.55,"중앙값 1600",color=GREEN,fontsize=8.5)
axs[1].plot(1800,0.5,"s",color=GREEN,ms=4); axs[1].text(1150,0.55,"중앙값 1800",color=GREEN,fontsize=8.5)
axs[0].text(30,0.93,"90번째 백분위수 $=m=2000$",color=GREEN,fontsize=8.5)
fig.tight_layout(); save(fig,"fig8_7_1")
