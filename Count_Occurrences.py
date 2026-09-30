numbers=[]
count=0

for i in range(1,11):
    num=int(input(f"Enter number {i} :"))
    numbers.append(num)
target=int(input("Enter a terget number you want to the occurrence:"))

for j in range(len(numbers)):
    if target == numbers[j] :
        count+=1

numbers=[]
count=0

for i in range(1,11):
    num=int(input(f"Enter number {i} :"))
    numbers.append(num)
target=int(input("Enter a terget number you want to the occurrence:"))

for j in range(len(numbers)):
    if target == numbers[j] :
        count+=1
 # print("Number of times the target appers:",numbers.count(target))

print("numbers of time the number appers:",count)
