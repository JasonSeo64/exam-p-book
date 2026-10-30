from figstyle import *
import numpy as np
from matplotlib.patches import Polygon
# D.1.1 joint density surface-like heatmap f(x,y)=6(1-y) on 0<x<y<1 -> use f=6x? choose f(x,y)=x+y on unit square
fig,axs=plt.subplots(1,2,figsize=W2)
g=np.linspace(0,1,200); X,Y=np.meshgrid(g,g); F=X+Y
im=axs[0].contourf(X,Y,F,levels=12,cmap="Blues")
axs[0].set_aspect("equal"); axs[0].set_title("결합밀도 $f(x,y)=x+y$")
axs[0].set_xlabel("$x$"); axs[0].set_ylabel("$y$"); fig.colorbar(im,ax=axs[0],shrink=0.8)
axs[1].plot(g,g+0.5,color=BLUE,lw=1.6,label="주변밀도 $f_X(x)=x+1/2$")
axs[1].set_ylim(0,1.6); axs[1].set_xlabel("$x$"); axs[1].legend(loc="lower right"); axs[1].set_title("주변밀도")
save(fig,"figD_1_1")
# D.2.1 regions: P(X+Y<1) and P(X>2Y)
fig,axs=plt.subplots(1,2,figsize=W2)
for ax in axs:
    ax.plot([0,1,1,0,0],[0,0,1,1,0],color=GRAY,lw=1)
    ax.set_xlim(-0.05,1.1); ax.set_ylim(-0.05,1.1); ax.set_aspect("equal"); ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
axs[0].fill([0,1,0],[0,0,1],color=ORANGE_L,alpha=0.8); axs[0].plot([0,1],[1,0],color=ORANGE,lw=1.5)
axs[0].set_title("$\\{x+y<1\\}$"); axs[0].text(0.55,0.5,"$x+y=1$",color=ORANGE)
axs[1].fill([0,1,1],[0,0,0.5],color=BLUE_L,alpha=0.8); axs[1].plot([0,1],[0,0.5],color=BLUE,lw=1.5)
axs[1].set_title("$\\{x>2y\\}$"); axs[1].text(0.45,0.32,"$y=x/2$",color=BLUE)
save(fig,"figD_2_1")
# D.4.1 transformation cdf method: Y=X^2, X~U(0,1)
fig,axs=plt.subplots(1,2,figsize=W2)
x=np.linspace(0,1,200); axs[0].plot(x,x**2,color=BLUE,lw=1.6); y0=0.36
axs[0].axhline(y0,color=ORANGE,ls="--",lw=1); axs[0].axvline(np.sqrt(y0),color=ORANGE,ls="--",lw=1)
axs[0].fill_between(x,0,1,where=x<=np.sqrt(y0),color=ORANGE_L,alpha=0.4)
axs[0].set_title("$Y=X^2\\leq y \\Leftrightarrow X\\leq\\sqrt{y}$"); axs[0].set_xlabel("$x$"); axs[0].set_ylabel("$y$")
yy=np.linspace(0.01,1,200); axs[1].plot(yy,1/(2*np.sqrt(yy)),color=BLUE,lw=1.6)
axs[1].set_ylim(0,4); axs[1].set_title("$f_Y(y)=\\frac{1}{2\\sqrt{y}}$"); axs[1].set_xlabel("$y$")
save(fig,"figD_4_1")
# D.5.1 convolution of two U(0,1)
fig,ax=plt.subplots(figsize=W1)
s=np.linspace(0,2,300); ax.plot(s,np.where(s<1,s,2-s),color=BLUE,lw=1.8,label="$X+Y$ 밀도 (삼각분포)")
ax.fill_between(s,0,np.where(s<1,s,2-s),where=s<=1.5,color=BLUE_L,alpha=0.5)
ax.text(0.9,0.3,"$P(S\\leq 1.5)=0.875$",color=BLUE)
ax.set_xlabel("$s$"); ax.set_title("독립 균등$(0,1)$ 두 개의 합"); ax.legend(loc="upper right")
save(fig,"figD_5_1")
