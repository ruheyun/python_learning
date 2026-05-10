# 逆波兰表达式求值
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signal = ['+', '-', '*', '/']
        stk = []
        for token in tokens:
            if token not in signal:
                stk.append(int(token))
            else:
                num1 = stk.pop()
                num2 = stk.pop()
                if token == '+':
                    stk.append(num1 + num2)
                elif token == '-':
                    stk.append(num2 - num1)
                elif token == '*':
                    stk.append(num1 * num2) 
                else:
                    flag = 1
                    if num1 * num2 < 0:
                        flag = -1
                    stk.append(flag * (abs(num2) // abs(num1)))  # 这里可以直接用 int(num2 / num1) 向零取整
        return stk[0]
    

sol = Solution()

print(sol.evalRPN(["10","6","9","3","+","11","*","/","*","17","+","5","+"]))