k=raw_input("dwse lista arithmon")
x=list(k)
pl=len(x)
i=1
megaliteros=max(x)
mikroteros=min(x)
plmin=x.count(mikroteros)
plmax=x.count(megaliteros)
plmax1=0
plmin1=0
mikroteros1=0
megaliteros1=0
sum=0
pl=0
b=False
b1=False
c=1

while c<pl and b==True and b1==True:
    if x[c]<megaliteros:
        megaliteros1=x[1]
        b=True
    if x[c]>mikroteros:
        mikroteros1=x[1]
        b1=True
    c=c+1
while i <pl:
    if x[i]<mikroteros1:
    	mikroteros1=x[i]
    	plmin1=0
    if x[i]==mikroteros1:
    	mikroteros1=x[i]
    	plmin1=plmin1+1
    if x[i]>megaliteros1:
    	megaliteros1=x[i]
    	plmax1=0
    if x[i]==megaliteros1:
    	megaliteros1=x[i]
    	plmax1=plmax1+1
    sum=sum+x[i]
    pl=pl+1
    i=i+1

telpl=pl-(plmax+plmin+plmax1+plmin1)
if telpl!=0:
    mesos=sum/telpl
    print mesos
elif telpl==0:
    print ("adinati praksi")
    
