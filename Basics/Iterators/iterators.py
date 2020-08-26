def main():
    days = ["Sun","Mon","Tues","Wed","Thurs","Fri","Sat"]
    daysFr = ["Dim","Lun","Mar","Mer","Jeu","Ven","Sam"]
    
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))

    with open("textfile.txt","r") as fp:
        #'' in iter function indicates to stop when the empty string comes
        for line in iter(fp.readline,''):
            print(line)
    
    for m in days:
        print(m)

    for m in range(len(days)):
        print(m,days[m])
        print(m+1, days[m])

    for i, m in enumerate(days,start=1):
        print(i,m)
    
    #Use zip to combine sequences   
    for m in zip(days, daysFr):
        print(m)
    
    for i,m in enumerate(zip(days,daysFr),start=1):
        print(i,m[0],"=",m[1],"in French") 
    


if __name__=="__main__":main()
