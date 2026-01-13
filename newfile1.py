f = open("newfile.txt", "r+")
l = 0
w = 0
c = 0
file = f.read()
row = file.split()
for i in row:
    for j in i:
        c += 1
for i in file:
    if i == "\n":
        l += 1
print("words:", len(row)) 
print("characters:", c)
print("lines:", l)
f.close()               