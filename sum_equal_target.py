def equalsum(X,size,target):
    for i in range(0,size-1):
        for j in range(i+1,size):
            if(X[i]+X[j]==target):
                return 1
    return 0
while __name__=="__main__":
    X=[0,5,8,9,3]
    target=int(input("Enter a target value"))
    size=len(X)
    if (equalsum(X,size,target)):
        print("No.of integers:" ,size )
        print("Numbers:",X)
        print("Target sum:",target)
        print("Possible")
    else:
        print("Not possible")

