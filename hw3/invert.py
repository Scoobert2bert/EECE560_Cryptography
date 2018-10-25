#William Cass
import sys #sys allows for the use of STDIN and STDOUT
import ast #ast allows for easy parsing of input string into list

a = ast.literal_eval(sys.argv[1])
b,d = a[:],[]

def sorter():
    for i in range (0,len(b)):
        n = b[0]    
        m = 0                           #m holds the position of n
        for j in range (0,len(b)):
            if n >= b[j]:
                n = b[j]
                for m in [k for k,l in enumerate(a) if l == n]:
                    pass
                
        b.remove(n)
        d.append(m+1)

sorter()
out = str(d)                            #output must be string
sys.stdout.write(out)
