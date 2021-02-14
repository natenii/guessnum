import random
start = int(input('請輸入起始範圍： '))
end = int(input('請輸入結束範圍： '))

r = random.randint(start, end)
count = 0
while True:
    count += 1
    num = int(input('猜數字：'))
    if num == r:
        print('猜對了！')
        print('這是猜了第', count, '次')
        break
    elif num > r:
        print('比答案大')
    else:
        print('比答案小')
    print('這是猜了第', count, '次')