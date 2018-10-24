a = [3,4,1,5,2] #should return (1 3)(2 4 5)
b = a[:]

cycle1 = []
moving = [1,2,3,4,5]

orig,current = moving[:],moving[:]
status = 1

def power():
    for i in range(0,len(a)):
        shift_to = a[i]-1
        moving[shift_to] = current[i]

    print(moving)


while status == 1:
    power()
    current = moving[:]
    for m in [k for k,j in enumerate(moving) if j == 1]:
        pass
    cycle1.append(m+1)
    
    if m == cycle1[0]:
        break


print(moving)
print(cycle1)
