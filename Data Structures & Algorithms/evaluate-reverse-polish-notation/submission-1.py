class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == '+':
                n1 = stack.pop(-1)
                n2 = stack.pop(-1)
                stack.append(int(n2)+int(n1))
                print(stack)
            elif i == '-':
                n1 = stack.pop(-1)
                n2 = stack.pop(-1)
                stack.append(int(n2)-int(n1))
                print(stack)
            elif i == '*':
                n1 = stack.pop(-1)
                n2 = stack.pop(-1)
                stack.append(int(n2)*int(n1))
                print(stack)
            elif i == '/':
                n1 = stack.pop(-1)
                n2 = stack.pop(-1)
                stack.append(int(int(n2)/int(n1)))
                print(stack)
            else:
                stack.append(i)
                print(stack)

        return int(stack[0])