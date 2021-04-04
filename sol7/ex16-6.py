class Time(object):
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

def mul_time(time, num):
    mul = Time(time.hour, time.minute, time.second)
    mul.hour *= num
    mul.minute *= num 
    mul.second *= num

    if mul.second >= 60:
        mul.minute += (mul.second // 60)
        mul.second -= (mul.second // 60) * 60 
    
    if mul.minute >= 60:
        mul.hour += (mul.minute // 60)
        mul.minute -= (mul.minute // 60) * 60

    if mul.hour > 24:
        mul.hour %= 24

    return mul

now_time = Time(4, 40, 0)
next_time = mul_time(now_time, 2)
print(next_time.hour, next_time.minute, next_time.second)