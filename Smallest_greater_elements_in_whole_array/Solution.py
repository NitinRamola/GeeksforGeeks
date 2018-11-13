def getoutput(a):
    
    b= a.split()
    b = [int(i) for i in b]
    sb= sorted(b)
    #print(b)
    #print(sb)

    for i in range(len(b)):
        if b[i] == max(b):
            print("_",end = " ")
        else:
            for j in sb: 
                if j <= b[i]:
                    continue
                print(j,end = " ")
                
                #o = " " + .join(j)
                break
    print("\n",end="")

n = int(input())

for i in range(n):
    
    l = input()
    a = input()
    getoutput(a)