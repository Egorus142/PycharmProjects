a = int(input())
x = int(input())
y = int(input())
kopeyki = x * 100 + y
kopeyki += int(kopeyki * a / 100)

rub = kopeyki // 100
cop = (kopeyki / 100 - kopeyki // 100) * 100
print(int(rub), round(cop))
