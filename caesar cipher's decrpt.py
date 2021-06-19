cipher=input("enter the crptogram: ")
txt=''
for char in cipher:
    if not char.isalpha():
        continue
    char=char.upper()
    code=ord(char)-1
    if code<ord('A'):
        code=ord('Z')
    txt+=chr(code)
print(txt)
