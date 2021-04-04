# Solution for Ex 8-11.

# Correct
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

# Wrong...

# 1. 문자열 'c'가 lowercase인지 확인 - Always True in if statement
# 2. return value is 'True'(string, not bool)
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

# Wrong...

# 1. 시퀀스 s의 원소를 순회하는 건 OK, but flag를 항상 갱신함. 
# 2. 인덱스 len(s)-1 (s>0) 의 원소의 소문자 여부를 반환
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# Wrong...

# 1. flag와 c.islower()를 OR연산 -> c.islower()가 한번이라도 True가 나오면 결과적으로 flag는 true
# 2. 문자열 s 안에 소문자가 exist하는지 check하는 코드
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# Correct Code
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase5("abcaaA"))