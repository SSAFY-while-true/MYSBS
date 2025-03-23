"""
gg 아직 못함
"""


def solution(users, emoticons):
    users.sort(key=lambda x : (x[0], x[1]))
    emoticons.sort(reverse = True)
    
    plus_user = 0
    total_money = 0
    
    break_idx = []

    
    for idx, user in enumerate(users):
        per_sale = user[0] // 10
        if user[0] % 10 == 0:
            per_sale = per_sale * 10
        else:
            per_sale = (per_sale + 1) * 10
            
        if sum(emoticons) * (100 - per_sale) / 100 >= user[1]:
            plus_user += 1
            
        else:
            break_idx.append(idx)
            
            
    if break_idx:
        print(break_idx)
            
    
    answer = [plus_user, total_money]
    return answer

