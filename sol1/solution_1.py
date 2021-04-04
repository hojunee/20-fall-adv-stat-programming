## Index is based on KOR version

## Ex 2.3
width = 17
height = 12.0
delimiter = '.'

# Solution 1 - width/2
print(width/2)
print(type(width/2))

# Solution 2 - width/2.0
print(width/2.0)
print(type(width/2.0))

# Solution 3 - height/3
print(height/3)
print(type(height/3))

# Solution 4 - 1+2*5
print(1 + 2 * 5)
print(type(1 + 2 * 5))

# Solution 5 - delimiter*5
print(delimiter * 5)
print(type(delimiter * 5))

## Ex 2.4
# Solution 1
PI = 3.141592
r = 5
sphere_vol = (4/3) * PI * (r**3)

print(sphere_vol)

# Solution 2
copy_size = 60

book_cost = (24.95 * (4/10)) * copy_size
ship_cost = 3 + (3/4)*(copy_size-1)

total_cost = book_cost + ship_cost
print(total_cost)

# Solution 3
current_sec = (6 * 3600) + 52*60

easy_pace = (8 * 60) + 15 
hard_pace = (7 * 12) + 15

end_sec = current_sec + (easy_pace * 2) + (hard_pace * 3)

end_time = (end_sec // 3600, (end_sec % 3600) // 60, (end_sec % 3600) % 60)

print("운동 후 시간은 {}시 {}분 {}초입니다.".format(end_time[0], end_time[1], end_time[2]))