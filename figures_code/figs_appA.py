from figstyle import *
import numpy as np
fig,axs=plt.subplots(1,2,figsize=W2)
for k,ax in enumerate(axs):
    ax.fill([0,1,1],[0,0,1],color=BLUE_L,alpha=0.7)
    ax.plot([0,1],[0,1],color=BLUE,lw=1.4); ax.plot([1,1],[0,1],color=BLUE,lw=1.4)
    ax.set_xlim(0,1.15); ax.set_ylim(0,1.15); ax.set_aspect("equal")
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ax.text(0.98,0.5 if k else 0.2,"$y=x$",color=BLUE,ha="right") if False else None
    ax.text(0.45,0.55,"$y=x$",color=BLUE,rotation=45)
    if k==0:
        x0=0.62; ax.annotate("",xy=(x0,x0),xytext=(x0,0),arrowprops=dict(arrowstyle="->",color=ORANGE,lw=1.6))
        ax.set_title("바깥 $x$: $0<y<x$")
        ax.text(x0+0.02,0.15,"$y:0\\to x$",color=ORANGE)
    else:
        y0=0.35; ax.annotate("",xy=(1,y0),xytext=(y0,y0),arrowprops=dict(arrowstyle="->",color=ORANGE,lw=1.6))
        ax.set_title("바깥 $y$: $y<x<1$")
        ax.text(0.5,y0+0.04,"$x:y\\to 1$",color=ORANGE)
save(fig,"figA_5_1")
