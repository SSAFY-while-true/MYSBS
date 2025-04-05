import sys
from collections import deque
input = sys.stdin.readline

def command_D(num):
    return (2 * num) % 10000

def command_S(num):
    if num == 0:
        return 9999
    else:
        return num - 1

def command_L(num):
    now_num = format(num, '04')
    fix_num = now_num[1:] + now_num[0]
    return int(fix_num)

def command_R(num):
    now_num = format(num, '04')
    fix_num = now_num[3] + now_num[:3]
    return int(fix_num)

def DSLR_bfs(start_num):
    command_root = ''
    queue = deque([(command_root, start_num)])
    visited = set()
    visited.add(start_num)

    while queue:
        cur_root, cur_num = queue.popleft()

        for command_str in ['D', 'S', 'L', 'R']:
            next_num = function_map[command_str](cur_num)
            command_root = cur_root + command_str

            if next_num == goal_num:
                return command_root
            
            if next_num not in visited:
                visited.add(next_num)
                queue.append((command_root, next_num))

function_map = {
    'D': command_D,
    'S': command_S,
    'L': command_L,
    'R': command_R
}

T = int(input())
for tc in range(1, T+1):
    start_num, goal_num = map(int, input().split())
    
    print(DSLR_bfs(start_num))


