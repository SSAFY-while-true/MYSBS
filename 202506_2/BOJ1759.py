from itertools import combinations
L, C = map(int, input().split())
word_list = list(input().split())
consonant_list = []
gather_list = []
results = []
# 자음과 모음 분리
for word in word_list:
    if word in ('a', 'e', 'i', 'o', 'u'):
        gather_list.append(word)
    else:
        consonant_list.append(word)   

# 이제부터 자음과 모음 뽑을 갯수 분리
for g_num in range(1, len(gather_list)+ 1): # 최소 1개부터 최대 모음 전부
    c_num = L - g_num   # 남은 갯수파악
    if c_num >= 2:  # 자음도 2개이상 조건에 맞으면 진행시켜
        for g_word in combinations(gather_list, g_num):     # 모음 뽑고
            for c_word in combinations(consonant_list, c_num):  #자음뽑고
                results.append(list(g_word) + list(c_word))

# 비밀번호 후보지생성                
passwords = []    
for result in results:  # 작은 단위 먼저 정렬시키고
    result.sort()
    passwords.append(''.join(result))   # 단어로 만든다
# 큰 뭉치 정렬시킨다
passwords.sort() 
for password in passwords:
    print(password)
