s1=input("Enter the 1st string: ")
s2=input("Enter the 2nd string: ")
s1=''.join(sorted(list(s1.upper().replace(' ',''))))
s2=''.join(sorted(list(s2.upper().replace(' ',''))))
if (len(s1)>0 and s1==s2):
    print("Anagram")
else:
    print("Not a Anagram")