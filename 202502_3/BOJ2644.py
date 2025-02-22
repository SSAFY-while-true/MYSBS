from collections import deque


def BFS_family(person1, person2):
    deq = deque([person1])
    check_point = [-1] * (n + 1)

    check_point[person1] = 0

    while deq:
        current_person = deq.popleft()

        for next_person in adj_list[current_person]:
            if next_person == person2:
                return check_point[current_person] + 1
            
            elif check_point[next_person] == -1:
                check_point[next_person] = check_point[current_person] + 1
                deq.append(next_person)

    return -1


n = int(input())
person1, person2 = map(int, input().split())
m = int(input())

adj_list = [[] for _ in range(n + 1)]

for i in range(m):
    parent_num, child_num = map(int, input().split())
    adj_list[parent_num].append(child_num)
    adj_list[child_num].append(parent_num)

print(BFS_family(person1, person2))
