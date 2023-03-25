name=input("Enter the name of batsman ")
r=input("Enter the runs scored by batsman ")
r=int(r)
b=input("Enter the number of balls faced by batsman ")
b=int(b)
avg=r/b
str=avg*100
print("The strike rate of ", name , "is", str)