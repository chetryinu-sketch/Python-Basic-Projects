numbers=[]

for i in range(1,11):
    num=int(input(f"Enter number{i} :"))
    numbers.append(num)

for j in numbers:
    largest=numbers[0]
    if largest > numbers[j]:
        print("largest number:",largest)
    else:
        largest=numbers[j]
        

    