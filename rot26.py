#rot26 ! - ~ 即ASCII 33-126
s= 'g!0{]n`7*+0y~+1|(!y.+0yKM9'
b=''
for a in s:
    if(ord(a)<(26+33)):
        b=b+chr(ord(a)-33-26+127)
    else:
        b=b+chr(ord(a)-26)
print(str(b))