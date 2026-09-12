Numbers=[]
Even=[]
Odd=[]

for i in range(1,11):
    num=int(input(f"Enter number {i}: "))

    Numbers.append(num)

    if num%2==0:
        Even.append(num)
    else:
        Odd.append(num)

print("List of all numbers:", Numbers)
print("List of Even Numbeers:", Even)
print("List of Odd Numbeers:", Odd)
