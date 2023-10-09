# 첫 시도 (deque 활용)
# def solution(scoville, K):
#     from collections import deque
#     scoville = [i for i in scoville if i < K]
#     queue = deque(scoville)
#     s = 0
#     while len(queue)>1:
#         queue = deque(sorted(queue))
#         if queue[0] >= K:
#             return s
#         s1 = queue.popleft()
#         s2 = queue.popleft()
#         new = s1 + (s2*2)
#         queue.appendleft(new)
#         s+=1
#     if sum(queue)/len(queue) < K:
#         return -1
#     return s

# 개선 heapq 활용
import heapq

def solution(scoville, K):
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)

    s = 0
    while heap[0] < K:
        if len(heap) < 2:
            return -1

        s1 = heapq.heappop(heap)
        s2 = heapq.heappop(heap)
        new = s1 + (s2 * 2)
        heapq.heappush(heap, new)

        s += 1

    return s