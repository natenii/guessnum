import random

r = random.randint(1,100)
count = 0
while True:
    count += 1
    num = input('猜數字：')
    num = int(num)
    if num == r:
        print('猜對了！')
        print('這是猜了第', count, '次')
        break
    elif num > r:
        print('比答案大')
    else:
        print('比答案小')
    print('這是猜了第', count, '次')
