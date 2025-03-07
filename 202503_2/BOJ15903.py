import sys
import heapq
input = sys.stdin.readline

n, m  = map(int, input().split())
cards = []
for num in map(int, input().split()):
    heapq.heappush(cards, num)

for _ in range(m):
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)
    heapq.heappush(cards, num1 + num2)
    heapq.heappush(cards, num1 + num2)


print(sum(cards))