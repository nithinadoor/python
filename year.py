currentyear=int(input("Enter current year"))
fut_y=int(input("Enter a future year"))
for year in range(currentyear,fut_y+1):
    if (year%4==0) or (year%100!=0) & (year%400==0):
     print(year)
