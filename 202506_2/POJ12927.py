def solution(n, works):
    if sum(works) <= n:
        return 0
    answer = 0
    len_works = len(works)
    works.sort(reverse=True)
    now_idx = 0
    while n != 0:
        works[now_idx] -= 1
        if works[now_idx] < works[(now_idx+1)%len_works]:
            now_idx = (now_idx+1)%len_works
        else:
            now_idx = 0

        n -= 1
    print(works)

    for work in works:
        answer += work**2
    
    return answer