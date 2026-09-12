Total=0
List=[]
for i in range(1,6):
    Marks=int(input(f"Enter marks of subjects {i}: "))
    List.append(Marks)
    Total+=Marks

Avg=Total/5
print("Total marks:",Total)
print("List of marks of 5 subjects:",List)
print("Highest marks:",max(List))
print("Lowest marks:",min(List))
print("Average mark:",Avg)