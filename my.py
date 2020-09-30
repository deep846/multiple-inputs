count = 0
x = list()
while input() != "-1":
    x.append(int(input()))
    if int(input()) <= 30:
        count += 1
    

print(count)
print(x)