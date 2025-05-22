ebt = int(input("Enter ebt order price: "))
bbt = int(input("Enter bbt order price: "))
kbt = int(input("Enter kbt order price: "))

if ebt > 500:
    ebtDisPrice = ebt - (ebt * 10 / 100)
    print("Final discounted price is:", ebtDisPrice)
else:
    print("No discount for you!, pay", ebt)

if bbt > 1000:
    bbtDisPrice = bbt - (bbt * 10 / 100)
    print("Final discounted price is:", bbtDisPrice)
else:
    print("No discount for you!, pay", bbt)

if kbt > 100:
    kbtDisPrice = kbt - (kbt * 5 / 100)
    print("Final discounted price is:", kbtDisPrice)
else:
    print("No discount for you!, pay", kbt)
