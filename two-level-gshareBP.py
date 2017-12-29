# -*- coding: utf-8 -*-

result1 = []
result2 = []

print("***********Two level gshare Branch Predictor**********"+"\n")
size = input("Please enter the counter size(bits): ")
phtsize = input("Please enter the value of n in n-bit global history register size(2^n-bits): ")
x=2**int(phtsize)
print("Reading file")
with open("branch-trace-gcc.trace") as infile:
    for line in infile:
        result1.append(line.split(' ')[0].strip())
        result2.append(line.split(' ')[1].strip())
        
    infile.closed

n = 2**int(size)
ghr = [0]*phtsize
ght = [0]*x
i=0  
j=0
while i<len(result1):
    s=0
    t=0
    k=int(("".join(str(x) for x in ghr)),2)
    address=int(result1[i])
    confidence = result2[i]
    strAddr = str(bin(address))
    temp = int(strAddr[-10:],2)
    s= k^temp
    
    modaddr=int(address)%1024
    
    
    if ((confidence=="N") and (ght[s]>=0 and ght[s]<=(n/2)-1)):
            if(ght[s]!=0):
                ght[s]=ght[s]-1
            else:
                ght[s]=0
            m=0
            for m in range(0,phtsize-1):
                ghr[m]=ghr[m+1]
            ghr[phtsize-1]=0
    elif ((confidence=="T" and (ght[s]>=(n/2) and ght[s]<=n-1))):
            if (ght[s]!=n-1):
                ght[s]=ght[s]+1
            else:
                ght[s]=n-1
            m=0
            for m in range(0,phtsize-1):
                ghr[m]=ghr[m+1]
            ghr[phtsize-1]=1
    elif (confidence=="N" and (ght[s]>=(n/2) and ght[s]<=n-1)):
            ght[s]=ght[s]-1
            j=j+1
            m=0
            for m in range(0,phtsize-1):
                ghr[m]=ghr[m+1]
            ghr[phtsize-1]=0
    elif (confidence=="T" and (ght[s]>=0 and ght[s]<=(n/2)-1)):
            ght[s]=ght[s]+1
            j=j+1
            m=0
            for m in range(0,phtsize-1):
                ghr[m]=ghr[m+1]
            ghr[phtsize-1]=1
            
    
           
    i=i+1
            
            
            
totalentries=float(len(result1))
j=float(j)
missrate=float(float((j/(totalentries)))*100)            
print("total number of entries: "+str(len(result1))+"\n")
print("total number of misses: "+str(j)+"\n")
print("Prediction Miss rate -- "+str(round(missrate, 5))+" %"+"\n")
hitrate=float(100-missrate)
print("Prediction Hit rate -- "+str(round(hitrate, 5))+" %"+"\n")
