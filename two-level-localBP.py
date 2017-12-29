# -*- coding: utf-8 -*-

result1 = []
result2 = []
print("**********Two level local Branch Predictor**********"+"\n")
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
lhr = [[0]*phtsize]*128
addr = [0]*128
i=0  
j=0
while i<len(result1):
    k=0
    address=int(result1[i])
    confidence = result2[i]
    modaddr=int(address)%128
    k=int(("".join(str(x) for x in lhr[modaddr])),2)
    if(addr[modaddr]==address):
        if ((confidence=="N") and (pht[k]>=0 and pht[k]<=(n/2)-1)):
            if(pht[k]!=0):
                pht[k]=pht[k]-1
            else:
                pht[k]=0
            m=0
            for m in range(0,phtsize-1):
                lhr[modaddr][m]=lhr[modaddr][m+1]
            lhr[modaddr][phtsize-1]=0
        elif ((confidence=="T" and (pht[k]>=(n/2) and pht[k]<=n-1))):
            if (pht[k]!=n-1):
                pht[k]=pht[k]+1
            else:
                pht[k]=n-1
            m=0
            for m in range(0,phtsize-1):
                lhr[modaddr][m]=lhr[modaddr][m+1]
            lhr[modaddr][phtsize-1]=1
        elif (confidence=="N" and (pht[k]>=(n/2) and pht[k]<=n-1)):
            pht[k]=pht[k]-1
            j=j+1
            m=0
            for m in range(0,phtsize-1):
                lhr[modaddr][m]=lhr[modaddr][m+1]
            lhr[modaddr][phtsize-1]=0
        elif (confidence=="T" and (pht[k]>=0 and pht[k]<=(n/2)-1)):
            pht[k]=pht[k]+1
            j=j+1
            m=0
            for m in range(0,phtsize-1):
                lhr[modaddr][m]=lhr[modaddr][m+1]
            lhr[modaddr][phtsize-1]=1
            
    elif(addr[modaddr]!=address):
        addr[modaddr]=address
        lhr[modaddr]=[0]*10
        if ((confidence=="N") and (pht[k]>=0 and pht[k]<=(n/2)-1)):
            if(pht[k]!=0):
                pht[k]=pht[k]-1
            else:
                pht[k]=0
            m=0
            for m in range(0,phtsize-1):
                lhr[modaddr][m]=lhr[modaddr][m+1]
            lhr[modaddr][phtsize-1]=0
        elif ((confidence=="T" and (pht[k]>=(n/2) and pht[k]<=n-1))):
            if (pht[k]!=n-1):
                pht[k]=pht[k]+1
            else:
                pht[k]=n-1
            m=0
            for m in range(0,phtsize-1):
                lhr[modaddr][m]=lhr[modaddr][m+1]
            lhr[modaddr][phtsize-1]=1
        elif (confidence=="N" and (pht[k]>=(n/2) and pht[k]<=n-1)):
            pht[k]=pht[k]-1
            j=j+1
            m=0
            for m in range(0,phtsize-1):
                lhr[modaddr][m]=lhr[modaddr][m+1]
            lhr[modaddr][phtsize-1]=0
        elif (confidence=="T" and (pht[k]>=0 and pht[k]<=(n/2)-1)):
            pht[k]=pht[k]+1
            j=j+1
            m=0
            for m in range(0,phtsize-1):
                lhr[modaddr][m]=lhr[modaddr][m+1]
            lhr[modaddr][phtsize-1]=1
            
    
           
    i=i+1
            
            
            
totalentries=float(len(result1))
j=float(j)
missrate=float(float((j/(totalentries)))*100)            
print("total number of entries: "+str(len(result1))+"\n")
print("total number of misses: "+str(j)+"\n")
print("Prediction Miss rate -- "+str(round(missrate, 5))+" %"+"\n\n")
hitrate=float(100-missrate)
print("Prediction Hit rate -- "+str(round(hitrate, 5))+" %"+"\n")
                
