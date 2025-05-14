import sys
input = sys.stdin.readline

origin_word = list(input())
boom_word = list(input())
len_boom = len(boom_word)

stack = []
for word in origin_word:
    stack.append(word)
    if len(stack) >= len_boom and stack[-len_boom:] == boom_word:
        for _ in range(len_boom):
            stack.pop()
if stack:
    result = ''.join(stack)
else:
    result = 'FRULA'
print(result)