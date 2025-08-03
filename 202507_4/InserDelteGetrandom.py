import random

class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.index = {}
        self.index_count = 0
    def insert(self, val):
        if val in self.index:
            return False
        
        self.nums.append(val)
        self.index[val] = self.index_count
        self.index_count += 1
        return True
                                    
    def remove(self, val):
        if val not in self.index:
            return False
        idx = self.index[val]
        self.index[self.nums[-1]] = idx

        self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]

        self.nums.pop()
        self.index_count -= 1
        del self.index[val]
        return True

    def getRandom(self):
        return self.nums[random.randint(0, self.index_count - 1)]
    
    def size(self):
        # 내부 요소의 개수를 반환하는 함수를 구현해주세요.
        return len(self.nums)


## 가입해서 제출하는게 귀찮은 분들을 위한
def performance_test():
    """대용량 데이터로 성능 테스트"""
    import time
    
    rs = RandomizedSet()
    n = 1000000
    
    # 삽입 성능 테스트
    start = time.time()
    for i in range(n):
        rs.insert(i)
    insert_time = time.time() - start
    
    # 삭제 성능 테스트
    start = time.time()
    for i in range(0, n, 2):  # 절반만 삭제
        rs.remove(i)
    remove_time = time.time() - start

    # 랜덤 샘플링 성능 테스트
    start = time.time()
    for i in range(n):
        rs.getRandom()
    random_time = time.time() - start
    
    length = rs.size()
    print(f"\n=== 성능 테스트 결과 (n={n}) ===")
    print(f"삽입 시간(n회): {insert_time:.4f}초")
    print(f"랜덤 샘플링 시간 (n회): {random_time:.4f}초")
    print(f"삭제 시간 (2/n회): {remove_time:.4f}초")
    print(f"최종 크기: {length}")

    print()
    print("채점 기준:") 
    print(f"삽입시간: 1초 이내: {insert_time:.4f}초")
    if insert_time < 1:
        print("성공")
    else:
        print("실패")
    print()

    print(f"삭제시간: 1초 이내: {remove_time:.4f}초")
    if remove_time < 1:
        print("성공")
    else:
        print("실패")
    print()

    print(f"랜덤 샘플링 시간: 1초 이내: {random_time:.4f}초")
    if random_time < 1:
        print("성공")
    else:
        print("실패")
    print()

    print(f"남은 원소 개수 500000개:  {length}")
    if length == 500000:
        print("성공")
    else:
        print("실패")

performance_test()