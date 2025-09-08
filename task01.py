from random import randint
num = randint(1, 20)

while True:
    foydalanuvchi = int(input("son kiriting. "))  
    if foydalanuvchi < num:
        print("Katta son")
    elif foydalanuvchi > num:
        print("Kichik son")
    else:
        print("Topildi")
        break