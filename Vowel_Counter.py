Sentence=input("Enter a sentence:")
Sentence=Sentence.lower()
count=0
vowels="aeiou"
for i in Sentence:
    if i in vowels:
        count+=1
print(count)

