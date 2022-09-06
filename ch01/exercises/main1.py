print(10 * 5)
print(10 ** 2)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10 / 15) ##the solution creates an infinite response that is only limited by the computer, so you will never see the full answer

## part 2
rate = int(input("What is the current exchange rate from Euro to Dollar? "))
amount = int(input("How much would you like to exchange? "))
total=rate*amount
total=total-3
print(total)