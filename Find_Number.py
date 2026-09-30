Numbers=[]

for i in range(1,11):
    num=int(input(f"Enter number {i} : "))
    Numbers.append(num)

Target= int(input("Enter the number you want to search:"))

if Target in Numbers:
    print("Number found!")
    
else:
    print("Number not found!") 
