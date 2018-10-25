#William Cass
import sys #sys allows for the use of STDIN and STDOUT
import ast #ast allows for easy parsing of input string into list/int

a = ast.literal_eval(sys.argv[1])
b = ast.literal_eval(sys.argv[2])
w,x,z,out = [],[],[],[]

def establish_identity():
    for i in range(1,len(a)+1): 
        w.append(i),x.append(i),z.append(i)
#This might be a bad way to establish identity permutations.
#I can't think of a better way to establish them with dynamic size.

def power():
    for i in range(0,len(a)):
        shiftto = a[i]-1
        x[shiftto]=w[i]
#Does the shifting. x contains final positions.

def findshift():
    for i in range(0,len(a)):
        n = z[i]
        for m in [k for k,j in enumerate(x) if j == n]:
            out.append(m+1)
#Finds the permutation that results in positions of x.
#Does so by comparing x to the identity permutation.

establish_identity()
for ii in range(0,b):
    power()
    w = x[:]

findshift()
out1 = str(out)
sys.stdout.write(out1)
