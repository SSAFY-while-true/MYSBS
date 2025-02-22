from itertools import permutations

def calculator(num1, num2, symbol):
    if symbol == 0:
        return num1 + num2
    elif symbol == 1:
        return num1 - num2
    elif symbol == 2:
        return num1 * num2 
    else:
        if num1 < 0:
            return -((-num1) // num2)
        elif num1 == 0:
            return 0
        else:
            return num1 // num2

N = int(input())
numbers = list(map(int, input().split()))
symbol_count = list(map(int, input().split()))

symbol_list = []
for symbol in range(4):
    for _ in range(symbol_count[symbol]):
        symbol_list.append(symbol)

max_val = -1000000000
min_val = 1000000000

for case in set(permutations(symbol_list)):     # 중복제거를 위한 세트처리
    new_numbers = numbers[:]
    for num in range(1, N):
        new_numbers[num] = calculator(new_numbers[num-1], new_numbers[num], case[num -1])
    result_number = new_numbers.pop()
    max_val = max(max_val, result_number)
    min_val = min(min_val, result_number)


print(max_val)
print(min_val)



# def number_make(start, total_len, symbol_list):
#     if start == total_len:
#         return [symbol_list[:]]
        
#     else:
#         result = []
#         for j in range(start, total_len):
#             symbol_list[start], symbol_list[j] = symbol_list[j], symbol_list[start]
#             result.extend(number_make(start + 1, total_len, symbol_list))
#             symbol_list[start], symbol_list[j] = symbol_list[j], symbol_list[start]
#         return result



# for case in number_make(0, N-1, symbol_list):
#     new_numbers = numbers[:]
#     for num in range(1, N):
#         new_numbers[num] = calculator(new_numbers[num-1], new_numbers[num], case[num -1])
#     result_number = new_numbers.pop()
#     max_val = max(max_val, result_number)
#     min_val = min(min_val, result_number)
