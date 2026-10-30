from figstyle import *
import numpy as np
from scipy.stats import norm
fig,axs=plt.subplots(1,2,figsize=W2)
x=np.linspace(-3.5,3.5,400)
for ax,(title,mask,lab) in zip(axs,[("$\\Phi(z)=P(Z\\leq z)$, $z=1.25$",x<=1.25,"0.8944"),
                                    ("$P(|Z|\\leq 1.96)=0.95$",np.abs(x)<=1.96,"0.95")]):
    ax.plot(x,norm.pdf(x),color=BLUE,lw=1.6)
    ax.fill_between(x,0,norm.pdf(x),where=mask,color=BLUE_L,alpha=0.8)
    ax.set_title(title); ax.set_ylim(0,0.45); ax.set_xlabel("$z$")
    ax.text(0,0.12,lab,ha="center",color=BLUE,fontsize=11,fontweight="bold")
axs[0].axvline(1.25,color=ORANGE,ls="--",lw=1)
save(fig,"figB_1_1")
