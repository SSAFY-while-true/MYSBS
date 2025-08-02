import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
# 거꾸로 생각하면 1이 나오면 무조건 1은 빼줘야한다
# 1이 없으면 반으로 나눈다
count_list = []
count = 0


for num in arr:
    if num == 1:        # 이번 바로 때려 넣어줘야함
        count += 1
    elif num > 1:
        count_list.append(num)


# 찾았으면 세트를 돌린다
while True:
    # 우선 홀수부터 찾는다. 있으면 -1 씩 뺀다
    for idx in range(len(count_list)):
        if count_list[idx] % 2 == 1:
            count_list[idx] -= 1
            count += 1
    # 여기서 끝나는 경우가 발생한다
    if sum(count_list) == 0:
        break
    # 그다음은 전부 반으로 나눠준다.
    for idx in range(len(count_list)):
        count_list[idx] //= 2

    # 2로 나눴으니까 1 더해주고
    count += 1


print(count)