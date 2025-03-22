#Remove vowels
phrase=input("Input: ")
vowels=["A","E","I","O","U","a","e","i","o","u"]
x=len(vowels)
for i in range(x):
    if vowels[i] in phrase:
        phrase=phrase.replace(vowels[i],"")
        i+=1
print("Output:",phrase)
