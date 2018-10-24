import sys #sys allows for the use of STDIN and STDOUT
import ast #ast allows for easy parsing of input string into list/int

a = ast.literal_eval(sys.argv[1])
b = ast.literal_eval(sys.argv[2])
w,x,z = [],[],[]
out = []

def start():
    for i in range(1,len(a)+1):
        w.append(i),x.append(i),z.append(i)

def power():
    for i in range(0,len(a)):
        shiftto = a[i]-1
        x[shiftto]=w[i]

def findshift():
    for i in range(0,len(a)):
        n = z[i]
        for m in [k for k,j in enumerate(x) if j == n]:
            out.append(m+1)

start()
for ii in range(0,b):
    power()
    w = x[:]

findshift()
out1 = str(out)
sys.stdout.write(out1)
