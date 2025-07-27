from collections import deque
import sys
input = sys.stdin.readline

def step1():
    durability.rotate() #  밸트도 돌리고 
    robot_location.rotate() # 로봇도 돌리고
    robot_location[-1] = 0    # 로봇 하차 시키고
    
def step2():
    global zero_count
    # 절반 전칸 부터 거꾸로 보면서 로봇을 이동 시킬 수 있는지? 옆으로 간다면 내릴껀지 
    for idx in range(N-2, -1 , -1):
        # 로봇이 있고, 옆칸에 로봇도 없고 내구도가 있으면 옮긴다
        if robot_location[idx] == 1 and robot_location[idx+1] == 0 and durability[idx+1] > 0:
            durability[idx+1] -= 1  # 내구도 1깍고
            robot_location[idx] = 0 # 내로봇 치우고
            robot_location[idx+1] = 1   # 옆으로 옮ㄱ기고
            if durability[idx + 1] == 0:
                zero_count += 1
            
    robot_location[-1] = 0    # 로봇 하차 시키고       
    
def step3():
    global zero_count
    if durability[0] > 0:
        durability[0] -= 1
        robot_location[0] = 1
        if durability[0] == 0:
            zero_count += 1
        
# def step4():
#     coin = K
#     for idx in range(2*N):
#         if durability[idx] == 0:
#             coin -= 1
    
#     if coin > 0:
#         return True
    
#     return False

N, K = map(int, input().split())
durability = list(map(int, input().split()))
durability = deque(durability)

robot_location = deque([0] * N)


step = 0
zero_count = 0
while zero_count < K:
    step1()
    step2()
    step3()
    step += 1
print(step)

# is_go = True

# while is_go:
#     step1()
#     step2()
#     step3()
#     is_go = step4()
#     step += 1
# print(step)
