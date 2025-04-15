import sys
import heapq
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    k = int(input())

    min_queue = []
    max_queue = []
    used_num = set()

    i_count = 0

    for identifier in range(k):
        command, num = input().split()
        if command == 'I':
            i_count += 1
            heapq.heappush(min_queue, (int(num), identifier))   # 식별자 포함
            heapq.heappush(max_queue, (int(num) * -1, identifier))
            
        else:
            if num == '1':
                while max_queue:
                    max_num, now_ident = heapq.heappop(max_queue)
                    if now_ident not in used_num:
                        used_num.add(now_ident)
                        break


            else:
                while min_queue:
                    min_num, now_ident = heapq.heappop(min_queue)
                    if now_ident not in used_num:
                        used_num.add(now_ident)
                        break
    if len(used_num) == i_count:
        print('EMPTY')
    else:
        result = []
        while True:
            max_num, now_ident = heapq.heappop(max_queue)
            if now_ident not in used_num:
                result.append(max_num * -1) 
                break
        while True:
            min_num, now_ident = heapq.heappop(min_queue)
            if now_ident not in used_num:
                result.append(min_num)
                break
        print(*result)