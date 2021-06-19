txt=input("Enter the message:")
cipher=''
for char in txt:
    if not char.isalpha():
        continue
    char=char.upper()
    code=ord(char)+1
    if code>ord('Z'):
        code=ord('A')
    cipher+=chr(code)
print(cipher)