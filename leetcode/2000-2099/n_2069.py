"""
2069. 模拟行走机器人 II
"""
from typing import List, Tuple


class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.s = 0
        
    def step(self, num: int) -> None:
        self.s = (self.s + num - 1) % ((self.w + self.h - 2) * 2) + 1

    def _getstate(self) -> Tuple[int, int, str]:
        w, h, s = self.w, self.h, self.s
        if s < w:
            return s, 0, 'East'
        if s < w + h - 1:
            return w - 1, s - w + 1, 'North'
        if s < w * 2 + h -2:
            return w * 2 + h - s - 3, h - 1, 'West'
        return 0, (w + h) * 2 - s - 4, 'South'

    def getPos(self) -> List[int]:
        x, y, _ = self._getstate()
        return [x, y]

    def getDir(self) -> str:
        return self._getstate()[-1]