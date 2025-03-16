import sys
import ast
from collections import deque
input = sys.stdin.readline



T= int(input())
for tc in range(T):
    command = input()
    n = int(input())
    num_list = deque(ast.literal_eval(input()))

    count_R = command.count('R')
    count_D = command.count('D')
    isreverse = False

    if count_D > n:
        num_list = 'error'
    
    else :
        for i in range(len(command)):
            if command[i] == "R":
                isreverse = not(isreverse)
            elif command[i] == 'D':
                if isreverse:
                    num_list.pop()
                else:
                    num_list.popleft()
                temp_count = 0

        if isreverse:
            num_list.reverse()

        num_list = '[' + ','.join(map(str, num_list)) + ']'

    print(num_list)