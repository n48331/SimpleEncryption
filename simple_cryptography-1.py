# Simple Encrytion without key
text = input("Enter a text : ")
s1 = ("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM 0123456789.")
s2 = s1[::-1]
a = {}

for i in range(len(s2)):
    a.update({s1[i]: s2[i]})
c = []
for x in text:
    c.append(a[x])
print("".join(c))
# input ALL CAPS works better
