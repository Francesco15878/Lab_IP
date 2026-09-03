"""for primos in range(1, 101):
    i = 2
    primo = 1
    while i < primos:
        if primos % i == 0:
            primo = 0
            break
        i = i+1
    if primo != 0:
        print(f"{primos}")
        """
for i in range(1,101):
    if i==1 or i%2==0 and i!=2 or i%3==0 and i!=3 or i%5==0 and i!=5 or i%7==0 and i!=7:print("")
    else:print(f"{i} es primo")
