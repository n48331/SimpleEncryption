# Simple Encrytion with key
b = input("Enter a text : ")
key = input('Enter key : ')

s1 = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm 0123456789."+key

s2 = s1[::-1]

a = {}
for i in range(len(s2)):
    a.update({s1[i]: s2[i]})

for j in range(len(key)):
    a.update({s1[j]: key[j]})
c = []
for x in b:
    c.append(a[x])
print("".join(c))

# it will not work perfectly all the time...Try to fix it with python UPPER inbuild fuction :)
# there are also encryption modules which you can install and import
