class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = ["+", "-", "/", "*"]
        for i in tokens:
            if i not in operation:
                stack.append(int(i))
            else:
                if i == "+" :
                    r = stack[-1] + stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(r)
                elif i == "-" :
                    r = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(r)
                elif i == "*" :
                    r = stack[-1] * stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(r)
                else :
                    r = int(stack[-2] / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(r)
        return stack[0]
                
