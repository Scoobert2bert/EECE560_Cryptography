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

def out(count):
    wow = 0
    while wow < len(long):
        if all(elem in long[done]  for elem in long[wow]):
              count = count + 1

        if count > 1:
            del long[wow]
            return 0
        wow = wow+1

establish_identity()
orig,current = moving[:],moving[:]

for findloops in range(1,len(a)+1):
    temp = []
    temp.append(findloops)
    for i in range(0,len(a)):
        power()
        current = moving[:]
        for m in [k for k,j in enumerate(moving) if j == findloops]:
            pass
        
        if m+1 == findloops:
            break

        if i > len(a):
            pass
        else:
            temp.append(m+1)


    cycle.append(temp)

clean_cycles()

for finish in range(0,len(long)):
    long[finish].sort(key=int)

done = 0
while done < len(long):
    count = 0
    out(count)
    done = done+1

done = 0
while done < len(long):
    count = 0
    out(count)
    done = done+1

out1 = str(long)
sys.stdout.write(out1)
