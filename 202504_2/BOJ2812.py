"""
스텍에 담으면서 스택의 마지막보다 현재가 크면 스택의 마지막을 날린다
"""
N, K = map(int, input().split())
num_list = list(map(int, input()))

stack = []
count = 0
for idx in range(N):
    while True: # 계속해서 비교 해준다
        if stack and num_list[idx] > stack[-1]: # 스택이 있는 상태에서 top과 비교 후 더 크면  삭제작업 진행
            stack.pop()
            count += 1      # 삭제를 몇번 했는지 보고
        else:
            break   # 조건을 만족하지 않으면 멈추고

        if count == K:      # 혹은 삭제 횟수를 다쓰면 멈춘다
            break

    stack.append(num_list[idx])

    if count == K:
        result = ''.join(map(str,stack)) + ''.join(map(str,num_list[idx+1:]))   # 결과는 스택은 든수 + 리스트의 남은 수
        break
else:
    result = ''.join(map(str,stack))   
    result = result[:-(K-count)]  # 이미 정렬 완료상태 뒤에서 부터 삭제 작업 들어감

print(result)

