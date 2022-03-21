a=input(" enter strings use space to seperate:")
b=[]
for i in a.split():
    if i==i[::-1]:
        b.append(i)
print()
for i in range (len(b)):
    print(b[i])
print()
print("total {} pelindrome words in sring []".format(len(b),b))
