count = 0
x = list()
while True:
    i = int(input())
    if i == -1:
        print("Invalid Entry \n The results are below: ")
        break
    if i > 30:
        count += 1
    x.append(i)
    

print("count = ",count)
print("x = ",x)

