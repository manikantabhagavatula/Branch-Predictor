# -*- coding: utf-8 -*-

result1 = []
result2 = []

print("**********One level Branch Predictor**********"+"\n")
size = input("Please enter the counter size(bits): ")
phtsize = input("Please enter the value of n in n-bit pattern history table size(2^n-bits): ")
x=2**int(phtsize)
print("Reading the input file")
with open("branch-trace-gcc.trace") as infile:
    for line in infile:
        result1.append(line.split(' ')[0].strip())
        result2.append(line.split(' ')[1].strip())
        
    infile.closed

n = 2**int(size)
pht = [0]*x
status = [0]*x
i=0
j=0
while i<len(result1):
    address=result1[i]
    confidence = result2[i]
    modaddr=int(address)%x
    if pht[modaddr] != address:
        pht[modaddr] = address
        
        if ((confidence=="N") and (status[modaddr]>=0 and status[modaddr]<=(n/2)-1)):
            if(status[modaddr]!=0):
                status[modaddr]=status[modaddr]-1
            else:
                status[modaddr]=0
        elif ((confidence=="T" and (status[modaddr]>=(n/2) and status[modaddr]<=n-1))):
            if (status[modaddr]!=n-1):
                status[modaddr]=status[modaddr]+1
            else:
                status[modaddr]=n-1
        elif (confidence=="N" and (status[modaddr]>=(n/2) and status[modaddr]<=n-1)):
            status[modaddr]=status[modaddr]-1
            j=j+1
        elif (confidence=="T" and (status[modaddr]>=0 and status[modaddr]<=(n/2)-1)):
            status[modaddr]=status[modaddr]+1
            j=j+1
    elif pht[modaddr] == address:
        if ((confidence=="N") and (status[modaddr]>=0 and status[modaddr]<=(n/2)-1)):
            if(status[modaddr]!=0):
                status[modaddr]=status[modaddr]-1
            else:
                status[modaddr]=0
        elif ((confidence=="T" and (status[modaddr]>=(n/2) and status[modaddr]<=n-1))):
            if (status[modaddr]!=n-1):
                status[modaddr]=status[modaddr]+1
            else:
                status[modaddr]=n-1
        elif (confidence=="N" and (status[modaddr]>=(n/2) and status[modaddr]<=n-1)):
            status[modaddr]=status[modaddr]-1
            j=j+1
        elif (confidence=="T" and (status[modaddr]>=0 and status[modaddr]<=(n/2)-1)):
            status[modaddr]=status[modaddr]+1
            j=j+1
    i = i+1

totalentries=float(len(result1))
j=float(j)
missrate=float(float((j/(totalentries)))*100)            
print("total number of entries: "+str(len(result1))+"\n")
print("total number of misses: "+str(j)+"\n")
print("Prediction Miss rate -- "+str(round(missrate, 5))+" %"+"\n")
hitrate=float(100-missrate)
print("Prediction Hit rate -- "+str(round(hitrate, 5))+" %"+"\n")
            
    
        
        

