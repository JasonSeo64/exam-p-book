# -*- coding: utf-8 -*-
"""이 책의 그림 스크립트(figs_chNN.py)가 쓰는 연결 모듈.
공통 스타일 fig_style.py(교재제작표준 11.1절)를 그대로 불러 쓰고, 예전 그림 이름(fig4_3_1)을
표준 이름(ch04_fig2.png)으로 바꾸어 저장한다. 이름 대응은 _numbering_map.json의 fig_file 항목을 따른다."""
import os, json
HERE = os.path.dirname(os.path.abspath(__file__))
os.environ.setdefault("FIG_DIR", os.path.join(HERE, "..", "figures"))
from fig_style import *          # noqa: F401,F403  공통 스타일
import fig_style as _fs
import matplotlib.pyplot as plt  # noqa: F401
import numpy as np               # noqa: F401

# 예전 스크립트가 쓰던 색 이름을 공통 팔레트에 대응
BLUE, ORANGE, GRAY, GREEN, PURPLE = _fs.COLORS[0], _fs.COLORS[1], _fs.COLORS[2], _fs.COLORS[3], _fs.COLORS[4]
BLUE_L, ORANGE_L = "#9FB3C8", "#F0C08F"
SERIES = list(_fs.COLORS)
W1 = (_fs.W, _fs.H)
W2 = (_fs.W, 2.8)
SQ = (4.2, 3.4)
FIGDIR = _fs.FIG_DIR

_MAP = json.load(open(os.path.join(HERE, "_numbering_map.json"), encoding="utf-8"))["fig_file"]


def save(fig, name):
    old = name if name.endswith(".png") else name + ".png"
    new = _MAP.get(old)
    if new is None:          # 본문에서 쓰지 않는 그림
        plt.close(fig)
        return None
    p = _fs.save(fig, new)
    print("saved", p)
    return p
