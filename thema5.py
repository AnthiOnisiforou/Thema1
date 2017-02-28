i= 1
for i in range(1000):
    number = raw_input("dwse arithmo : ")
    l = int (number)
    
    if l > 0 and l <10:
        print ("is harshad number")
        print l
    elif l > 9 and l<100:
        mon=  l % 10
        dek=  l // 10
        sum= mon + dek
        gin= mon * dek
        if ( l % sum)==0:
            print ("is a harshad number")
            gin = (l % 10) * (l // 10)
        if gin!=0:
            if (l % gin)==0:
                print ("to ginomeno twn psifiwn tou diairei akrivws ton arithmo")
                print l
        elif gin==0:
            print ("adinati praksi")
    elif l>99 and l<1000:
        mon= l % 10
        dek=( l // 10) % 10
        ek=( l // 10) // 10
        sum= mon + dek + ek
        gin= mon * dek * ek
        if (l % sum)==0:
            print ("is a harshad number")
        if gin!=0:
            if (l % gin)==0:
                print (l)
                print ("to ginomeno twn psifiwn tou diairei akrivws ton arithmo")
        elif gin==0:
             print ("adinati praksi")
    elif l==1000:
        print ("is a harshad number")
        print ("adinati praksiS")
