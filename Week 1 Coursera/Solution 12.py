a = int(input())
b = int(input())
n = int(input())

price_cents_total = (a * 100 + b) * n
price_roubles = price_cents_total // 100
price_cents = price_cents_total % 100

print(price_roubles)
print(price_cents)
