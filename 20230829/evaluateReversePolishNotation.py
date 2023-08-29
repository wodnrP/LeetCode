class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        중위 -> 후위
        피연산자가 나오면 스택에 푸시하고, 
        연산자가 나오면 스택에서 피연산자를 팝하여 연산을 수행한 후 결과를 다시 스택에 푸시합니다.
        표현식의 끝까지 이 과정을 반복한 후, 스택의 맨 위에 있는 값이 최종 결과값

        + - * /
        후위 -> 중위
        만약 피연산자가 나오면 스택에 푸시
        stack = [2,1]
        만약 연산자가 나오면
            + 일 경우
            팝 연산자 팝 을 스택에 푸시

        """
        import math
        stack=[]
        oper = ['+','-','*','/']
        for i in tokens:
            if i == oper[0]:
                if len(stack) >= 2:
                    stack.append(stack.pop() + stack.pop())
            elif i == oper[1]:
                if len(stack) >= 2:
                    a,b = stack.pop(), stack.pop()
                    stack.append(b-a)
            elif i == oper[2]:
                if len(stack) >= 2:
                    stack.append(stack.pop() * stack.pop())
            elif i == oper[3]:
                if len(stack) >= 2:
                    a,b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
            else:
                stack.append(int(i))
        
        return stack[0]

# 확인
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5", "+"]
# # 예상 출력 
# # ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# # = ((10 * (6 / (12 * -11))) + 17) + 5
# # = ((10 * (6 / -132)) + 17) + 5
# # = ((10 * 0) + 17) + 5
# # = (0 + 17) + 5
# # = 17 + 5
# # = 22
# print(Solution().evalRPN(tokens))