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

establish_identity()#Dynamically establish identity permutations
orig,current = moving[:],moving[:]

for findloops in range(1,len(a)+1): #starts at each number and follows the path it takes as it moves.
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

    cycle.append(temp)#list of lists containing how each number moves
                      #There will be duplicates. Now must remove duplicates
clean_cycles()

count=0
if len(long) != 1 and len(long) != 0:
    for soclose in range(len(long)-1,-1,-1):
        count = 0
        for iii in range(len(long)-1,-1,-1):
            if set(long[soclose]).issubset(set(long[iii])):
                count = count+1

            if count > 1:
                long[soclose] = [0] #If dup found replace it with a one element list
                                    #Simple to filter out at the end
for clean1 in range(len(long)-1,-1,-1):
        if len(long[clean1]) == 1:
            del long[clean1]
            
for i in range(0,len(long)):
    out1 = str(long[i])
    sys.stdout.write(out1)
