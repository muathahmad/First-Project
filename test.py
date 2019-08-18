print ("Muath")

def comparmarks(x):
    if x>=50:
        print ("You Pass")
        if x>=90:
            print("enta a5o sharmota")
        elif x>=70:
            print("You are good")
        else:
            print("You Bad")

    else:
        print ("You failed")

def fuck(x):
    Res=0
    for y in range (1,x+1):
        Res= Res+ y
        print(y, "      ", Res )

    return Res

print(fuck(5))
comparmarks(80)
