A, B, C = map(int, input().split())

result = 1
A = A % C
while B > 0:
    if B % 2 == 1:
        result = (result * A) % C 
    A = (A * A) % C
    B //= 2
print(result)