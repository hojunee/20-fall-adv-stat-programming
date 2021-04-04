from collections import Counter
import numpy as np
import math

class Data:
    def __init__(self, data):
        self.lst = data # data
        self.size = len(data) # data size
        self.sorted_lst = sorted(data) # sorted data

    # 평균 Mean 구하기    
    def mean(self):
        return sum(self.lst) / self.size
    
    # 중위수 Median 구하기
    def median(self):
        if self.size % 2 == 1: # 중위수 있슴
            return self.sorted_lst[self.size // 2]
        else: # 중위수 음슴 - 3.5면 둘의 평균
            return (self.sorted_lst[self.size // 2] 
                    + self.sorted_lst[self.size // 2 - 1]) / 2
    
    # 최빈값 Mode 구하기
    def mode(self):
        cnt = Counter(self.lst)
        max_cnt = max(cnt.values())
        return [i for (i , freq) in cnt.items() if freq == max_cnt ]

    # 최댓값 Max 구하기
    def max(self):
        return self.sorted_lst[-1]

    # 최솟값 Min 구하기
    def min(self):
        return self.sorted_lst[0]

    # 범위 Range 구하기
    def range(self):
        return self.max() - self.min()

    # 분산 Variance 구하기
    def variance(self):
        square_of_error = [(i - self.mean()) ** 2 for i in self.lst]
        try:
            return sum(square_of_error) / (self.size - 1)
        except ZeroDivisionError:
            print("Variance를 구하는 과정에서 self.size가 0이 되는 문제가 발생했습니다.")
            return -1

    # 표준편차 Std 구하기
    def std(self):
        try:
            return math.sqrt(self.variance())
        except ValueError:
            return -1


weight = [1]

x = Data(weight)

print("mean :", x.mean())
print("median :", x.median())
print("mode :", x.mode())

print("max :", x.max())
print("min :", x.min())
print("range :", x.range())

print("variance :", x.variance())
print("standard_deviation :", x.std())
 