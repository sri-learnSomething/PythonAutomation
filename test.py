num = 100000001
while num < 999999999:
    if (num % 9) == 0 and (num % 8) == 0 and (num % 7) == 0 and (num % 9) == 0 and (num % 5) == 0:
        n = num
    else:
        num += 1

print(num)