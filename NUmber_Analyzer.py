Total=0
Even_No=0
Odd_No=0
numbers=[]

for i in range(1,6):
    num=int(input(f"Enter number{i}: "))
    
    numbers.append(num)
    Total+=num
    
    if num%2==0:
        Even_No += 1
    else:
        Odd_No+=1

print("Total:",Total)
print("Number of even numbers:",Even_No)
print("Number of odd numbers:",Odd_No)
print("Largest number:",max(numbers))
print("Smallest number:",min(numbers))
