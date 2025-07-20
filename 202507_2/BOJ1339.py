from collections import defaultdict
N = int(input())
words = [list(input()) for _ in range(N)]
words.sort()


# 딕서너리에 배정시키는 작업을 하자

weight = defaultdict(int)

# 각 알파벳의 자릿수 가중치를 계산
for word in words:
    word_length = len(word)
    for idx, char in enumerate(word):
        digit = word_length - idx - 1
        weight[char] +=  (10 ** digit)

# 이제 가중치 기반으로 알파벳 넣는다
alphabet_dict = defaultdict(str)
now_num  = 9
#### 지선생님.. 여기서 아이탬스로 뽑아야 키를 가져 올 수있고 
# 이걸 리스트로 만들어지면 [(키,밸류)] 형태의 리스트가 된다. 그래서 람다 x[1](밸류)를 사용
sorted_weights = sorted(weight.items(), key=lambda x: x[1], reverse=True)

for alpha, now_wight in sorted_weights:
    alphabet_dict[alpha] = str(now_num)
    now_num -= 1


result = 0
for word in words:
    chage_num = ''
    for alphabet in word:
        chage_num += alphabet_dict[alphabet]
        

    # 다 돌렸으면 숫자를 더해줌
    result += int(chage_num)

print(result)