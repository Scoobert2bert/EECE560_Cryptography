#William Cass
import sys #sys allows for the use of STDIN and STDOUT
import ast #ast allows for easy parsing of input string into list/int

a = ast.literal_eval(sys.argv[1])
b = a[:]
moving = []
cycle = []
long = []
temp = []
count = 0

def establish_identity():
    for i in range(1,len(a)+1): 
        moving.append(i)

def power():
    for position in range(0,len(a)):
        shift_to = a[position]-1
        moving[shift_to] = current[position]

def clean_cycles():
    for clean1 in range(0,len(a)):
        if len(cycle[clean1]) > 1:
            long.append(cycle[clean1])

establish_identity()
orig,current = moving[:],moving[:]

for findloops in range(1,len(a)+1):
    temp = []
    moving,current = orig[:],orig[:]
    temp.append(findloops)
    power()
    i = 0
    while moving[:] != orig[:]:
        current = moving[:]
        for m in [k for k,j in enumerate(moving) if j == findloops]:
            pass
        
        if m+1 == findloops:
            break

        if i > len(a):
            pass
        else:
            temp.append(m+1)

        power()
        i = i + 1

    cycle.append(temp)

print(cycle)
clean_cycles()

k = []
for finish in range(0,len(long)):
    k.append(sum(i*i for i in long[finish]))

print(k)
count=0
kill1 = []
for soclose in range(0,len(k)):
    count = 0
    for iii in range(0,len(k)):
        if k[soclose] == k[iii]:
            count = count+1

        print(count)
        if count > 1:
            kill1.append(iii)

kill1 = set(kill1)
kill1 = list(kill1)
print(kill1)

for end2 in range(len(kill1)-1,-1,-1):
    del long[kill1[end2]]

print(k)
print(long)

print(k)
count=0
kill1 = []

if len(long) != 1 and len(long) != 0:
    for soclose in range(0,len(long)):
        count = 0
        for iii in range(0,len(long)):
            if all(elem in long[soclose] for elem in long[iii]):
                count = count+1

            print(count)
            if count > 1:
                kill1.append(iii)

    kill1 = set(kill1)
    kill1 = list(kill1)
    print(kill1)

for end2 in range(len(kill1)-1,-1,-1):
    del long[kill1[end2]]

for i in range(0,len(long)):
    out1 = str(long[i])
    sys.stdout.write(out1)
