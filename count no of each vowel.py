vowels='aeiou'
str=input()
str=str.casefold()
count={}.fromkeys(vowels,0)
for chr in str:
    if chr in count:
        count[chr]+=1
print(count)