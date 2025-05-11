from itertools import combinations

N, K = map(int, input().split())
input_word = [input() for _ in range(N)]
if K < 5:
    print(0)
else:
    # req_char = {'a', 'n', 't', 'i', 'c'}  # 그냥 모아서 처리
    req_char = set("antic")
    left_K = K- 5
    left_char = set()
    left_char_count = 0
    for i in range(N):
        for j in range(len(input_word[i])):
            if input_word[i][j] not in req_char and input_word[i][j] not in left_char:
                left_char.add(input_word[i][j])
                left_char_count += 1

    if left_K >= left_char_count:
        print(N)
    
    else:
        result = 0
        for char_case in combinations(left_char, left_K):
            temp_result = 0
            for i in range(N):
                for j in range(len(input_word[i])):
                    if input_word[i][j] not in req_char and input_word[i][j] not in char_case:
                        break
                else:
                    temp_result += 1
            result = max(result, temp_result)

        print(result)