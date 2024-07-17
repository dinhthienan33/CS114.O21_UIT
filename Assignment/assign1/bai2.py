def main():
    loto = []
    for i in range(3):
        row = list(map(int,input().split()))
        loto.append(row)
    
    n=int(input())
    if(n<1 or n>10):
        return
    for _ in range(n):
        a=int(input())
        check(loto, a)

    if(kinh(loto)):
        print("Yes")
    else:
        print("No")
def kinh(loto):
    if(loto[0][0]==loto[0][1]==loto[0][2] or loto[1][0]==loto[1][1]==loto[1][2] or loto[2][0]==loto[2][1]==loto[2][2]):
        return True
    if(loto[0][0]==loto[1][0]==loto[2][0] or loto[0][1]==loto[1][1]==loto[2][1] or loto[0][2]==loto[1][2]==loto[2][2]):
        return True
    if (loto[0][0]==loto[1][1]==loto[2][2]==0):
            return True
    if(loto[0][2]==loto[1][1]==loto[2][0]):
        return True
    return False

     
def check(loto, element):
    for i in range(3):
        for j in range(3):
            if loto[i][j]==element:
                loto[i][j]=0
          
    return loto   
if __name__ == "__main__":
    main()