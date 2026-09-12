Python= int(input("Enter marks for Python:"))
DSA= int(input("Enter marks for DSA:"))
Mathematics= int(input("Enter marks for Mathematics:"))
Physics= int(input("Enter marks for Physics:"))
English= int(input("Enter marks for English:"))

Total= Python+DSA+Mathematics+Physics+English
Percentage= (Python+DSA+Mathematics+Physics+English)/5

print("Total marks:",Total)
print(f"Percentage:{Percentage}%")

if 450 <= Total <= 500:
    print("Grade: A+")
elif 400 <= Total <= 449:
    print("Grade: A")
elif 350 <= Total <= 399:
    print("Grade: B")
elif 300 <= Total <= 349:
    print("Grade: C")
elif 250 <= Total <= 299:
    print("Grade: D")
else:
    print("Grade: F")