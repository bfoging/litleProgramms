#!/usr/bin/python3
amount = int(input("Сколько хотите взять денег: "))
pct = int(input("Под какой процент вам их дают: ")) / 100
years = 12 * int(input("Насколько лет берете: "))
c = 12 * (amount * pct)

print ("Вы взяли : ",amount,  "на ", years, "месяцов")

j = 0
num = amount
ret = 0

while j < years :
	num =  int(num + num * pct)
	j+=1

ostatok = num - amount 

print("Вы переплотили на", c,"процентов")
print("Вы заплатили всего:",num,",а переплатили:", ostatok)
