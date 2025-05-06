def hanoi(num, start, end, sub):
    if num == 0:
        return
    
    hanoi(num-1, start, sub, end)
    print(start, end)
    hanoi(num-1, sub, end, start)

K = int(input())
print(2**K - 1)
hanoi(K, 1, 3, 2)