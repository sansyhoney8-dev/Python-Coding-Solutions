#cheking leapyear
num_year = int(input("Enter the year :"))
if (num_year%4 ==0):
    if(num_year % 100 ==0):
        if(num_year % 400 == 0):
            print("this is a leap year")
else :
    print("it's not a leap year")
