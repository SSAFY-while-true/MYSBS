from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    
    for discounts in product([10, 20, 30, 40], repeat=len(emoticons)):
        plus_member = 0
        total_money = 0


        for user_discount, user_money in users:
            temp_money = 0
            for i in range(len(emoticons)):
                if discounts[i] >= user_discount:
                    temp_money += emoticons[i] * (100 - discounts[i]) // 100
                    
            if temp_money >= user_money:
                plus_member += 1

            else:
                total_money += temp_money

        # 최적의 결과 갱신: 플러스 가입자 수 우선, 같으면 판매액 비교
        if plus_member > answer[0] :
            answer = [plus_member, total_money]
            
        elif plus_member == answer[0] and total_money > answer[1]:
            answer[1] = total_money

    return answer