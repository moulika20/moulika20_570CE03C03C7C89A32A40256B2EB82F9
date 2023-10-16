year=int(input("Enter the year:"))

if (year%400==0) and (year%100==0):
  print(year,"is loop year")

elif (year%4==0) and (year%100 !=0):
  print(year,"is leap year") 