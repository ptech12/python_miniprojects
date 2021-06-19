text=input("Enter the message: ")
shift=0
while shift == 0:
    try:
        shift = int(input("Enter cipher's shift(1..25): "))
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        shift=0
        if shift == 0:
            print("bad shift")
cipher=''
for char in text:
    if char.isalpha():
        code=ord(char)+shift
        if char.isupper():
            first=ord('A')
        else:
            first=ord('a')
        code-=first
        code%= 26
        cipher+=chr(first+code)
    else:
        cipher+=char
print(cipher)
