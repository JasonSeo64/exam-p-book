from figstyle import *
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
cm=LinearSegmentedColormap.from_list("p",["#FFFFFF",BLUE_L,BLUE])
T=np.array([[.30,.10,.05],[.15,.15,.05],[.05,.05,.10]])
pX,pY=T.sum(1),T.sum(0)

def heat(ax,M,title):
    ax.imshow(M,cmap=cm,vmin=0,vmax=0.32,origin="upper")
    for i in range(3):
        for j in range(3):
            ax.text(j,i,f"{M[i,j]:.3f}".rstrip("0").rstrip("."),ha="center",va="center",fontsize=10,color="white" if M[i,j]>0.2 else "black")
    ax.set_xticks(range(3),[f"$y={j}$" for j in range(3)]); ax.set_yticks(range(3),[f"$x={i}$" for i in range(3)])
    ax.grid(False); ax.set_title(title,fontsize=10)
    for s in ax.spines.values(): s.set_visible(False)

# fig9_1_1 joint pmf heatmap with marginals
fig=plt.figure(figsize=(5.4,4.4))
gs=fig.add_gridspec(2,2,width_ratios=[3,1],height_ratios=[1,3],wspace=0.08,hspace=0.08)
ax=fig.add_subplot(gs[1,0]); heat(ax,T,"")
ax.set_xlabel("주택보험 청구건수 $Y$"); ax.set_ylabel("자동차보험 청구건수 $X$")
axt=fig.add_subplot(gs[0,0],sharex=ax); axt.bar(range(3),pY,color=ORANGE,width=0.6)
for j,v in enumerate(pY): axt.text(j,v+0.01,f"{v:.2f}",ha="center",fontsize=9)
axt.set_ylim(0,0.62); axt.set_ylabel("$p_Y(y)$"); axt.tick_params(labelbottom=False); axt.grid(False)
axr=fig.add_subplot(gs[1,1],sharey=ax); axr.barh(range(3),pX,color=GREEN,height=0.6)
for i,v in enumerate(pX): axr.text(v+0.01,i,f"{v:.2f}",va="center",fontsize=9)
axr.set_xlim(0,0.6); axr.set_xlabel("$p_X(x)$"); axr.tick_params(labelleft=False); axr.grid(False)
save(fig,"fig9_1_1")

# fig9_1_2 joint cdf region F(1,1)
fig,ax=plt.subplots(figsize=SQ)
for i in range(3):
    for j in range(3):
        c=BLUE if (i<=1 and j<=1) else GRAY
        ax.scatter(i,j,s=T[i,j]*3000,color=c,alpha=0.75)
        ax.text(i+0.18,j+0.12,f"{T[i,j]:.2f}",fontsize=9)
ax.fill_between([-0.6,1.0],-0.6,1.0,color=BLUE_L,alpha=0.35)
ax.text(1.05,-0.5,"음영: $\\{X\\leq 1,\\,Y\\leq 1\\}$",color=BLUE,fontsize=9)
ax.set_xlim(-0.6,2.6); ax.set_ylim(-0.6,2.6); ax.set_xticks(range(3)); ax.set_yticks(range(3))
ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_title("$F_{X,Y}(1,1)=0.70$",fontsize=10)
save(fig,"fig9_1_2")

# fig9_3_1 conditional distributions of X given Y=y
fig,ax=plt.subplots(figsize=W1)
w=0.25
for k,j in enumerate(range(3)):
    cond=T[:,j]/pY[j]
    ax.bar(np.arange(3)+(k-1)*w,cond,width=w,color=SERIES[k],label=f"$p_{{X|Y}}(x\\mid {j})$")
ax.plot(np.arange(3),pX,"k--o",lw=1,ms=4,label="주변분포 $p_X(x)$")
ax.set_xticks(range(3),[f"$x={i}$" for i in range(3)]); ax.set_ylabel("확률"); ax.set_ylim(0,0.8); ax.legend(fontsize=9,ncol=2,loc="upper center")
ax.set_title("$Y$의 값에 따른 $X$의 조건부분포",fontsize=10)
save(fig,"fig9_3_1")

# fig9_4_1 independence check
fig,axs=plt.subplots(1,2,figsize=(6.4,3.0))
heat(axs[0],T,"실제 결합확률 $p_{X,Y}(x,y)$"); heat(axs[1],np.outer(pX,pY),"주변확률의 곱 $p_X(x)\\,p_Y(y)$")
fig.tight_layout(); save(fig,"fig9_4_1")
