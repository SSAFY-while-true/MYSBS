def solution(players, m, k):
    answer = 0
    
    n = len(players)
    sever_timetable = [m-1] * n
    time = 0
    while time < n:
        if players[time] > sever_timetable[time]:
            answer += 1
            for i in range(k):
                if time + i < n:
                    sever_timetable[time + i] += m
                else:
                    break
            continue
        time += 1
    
    return answer