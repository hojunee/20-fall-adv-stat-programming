from datetime import date, datetime

num_to_weekday = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 
                  4:"Friday", 5:"Saturday", 6:"Sunday"}

# Sol (1)
print(datetime.now())
print(datetime.now().weekday())
print(num_to_weekday[datetime.now().weekday()])

# Sol (2)

birthday = [int(i) for i in input("생일을 입력해주세요. ex) 1988-02-10\n").split("-")]

next_birthday = datetime(datetime.now().year, birthday[1], birthday[2])

if (next_birthday - datetime.now()).total_seconds() < 0:
    next_birthday = datetime(datetime.now().year + 1, birthday[1], birthday[2])

print(next_birthday - datetime.now())