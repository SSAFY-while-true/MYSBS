def solution(n, bans):
    answer = []
    alpha_dict = {chr(97+ i): i+1 for i in range(26)}
    num_dict = {f'{i+1}': chr(97+ i) for i in range(26)}
    
    for idx, word in enumerate(bans):
        temp_num = 0
        for jdx, alpha in enumerate(word):
            temp_num += alpha_dict[alpha] * (26 ** (len(word) - 1 - jdx))
        bans[idx] = temp_num
    bans.sort()
    
    for i in range(len(bans)):
        if n >= bans[i]:
            n += 1
        else:
            break
            
    while n > 0 :
        c_num = n % 26
        if c_num == 0:
            c_num = 26
            n -= 1
        answer.append(num_dict[str(c_num)])
        n = n // 26
    
    answer = answer[::-1]
    answer = ''.join(answer)
    
    return answer