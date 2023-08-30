# 1차시도 - min함수 사용, topnum 변수로 top 위치 확인
# class MinStack(object):

#     def __init__(self):
#         self.stack=[]
#         self.topnum = -1

#     def push(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         self.stack.append(val)
#         self.topnum += 1

#     def pop(self):
#         """
#         :rtype: None
#         """
#         self.stack.pop()
#         self.topnum -= 1

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.stack[self.topnum]
        

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return min(self.stack)

# 개선 후    
class MinStack:

    def __init__(self):
        self.stack=[]
        self.topnum = -1
        self.minnum=[]

    def push(self, val):
        if len(self.stack)==0:
            self.stack.append(val)
            self.topnum += 1
            self.minnum.append(val)
        else:
            self.stack.append(val)
            self.topnum += 1
            
            if self.minnum[-1] > val:
                self.minnum.append(val)
            else:
                self.minnum.append(self.minnum[-1])


    def pop(self):
        self.stack.pop()
        self.minnum.pop() 
        self.topnum -= 1

    def top(self):
        return self.stack[self.topnum]

    def getMin(self):
        return self.minnum[-1]
# 확인
"""
obj = MinStack()
print(obj.stack)
obj.push(-2)
print(obj.stack)
obj.push(0)
print(obj.stack)
obj.push(-3)
print(obj.stack)
obj.getMin()
print(obj.getMin())
obj.pop()
print(obj.stack)
obj.top()
print(obj.top())
obj.getMin()
print(obj.getMin())
"""