
ball = 0

while True:
    foydalanuvchi = input("matn: ")
    if foydalanuvchi == '+':
        ball += 10
        print(f"ball {ball}")
    elif foydalanuvchi == 'stop':
        print(f"umumiy ball {ball}")
        break
    else:
        print("Faqat + yoki (stop) yozing. ")