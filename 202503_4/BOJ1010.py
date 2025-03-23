T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    molecule = 1
    denominator = 1

    for i in range(N):
        molecule *= (M - i)

    for j in range(1, N+1):
        denominator *= j
    
    result = int(molecule / denominator)
    print(result)

