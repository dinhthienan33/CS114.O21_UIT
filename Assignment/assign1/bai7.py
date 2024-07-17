def main():
    prices= list(map(int, input().split()))
    notes=[]
    for _ in range(len(prices)):
        notes.append(input())
    x=int(input())
    print(solve(prices,notes,x))
def check_number(number):
    if isinstance(number, int) or isinstance(number, float):
        return True
    else:
        return False
def identify_number(string):
    number = string.strip('%')  
    try:
        number = float(number)  
        return number
    except ValueError:
        return None  
def solve(prices, notes,x):
    if(x<=0) or sum(prices)<=0:
        return 'true'
    if(sum(prices)<=x):
        return 'true'
    k=0
    for i in range(len(prices)):
        words=notes[i].split()
        for char in words:
            char=identify_number(char)
            if check_number(char):
                if('higher' in words):
                    k+=float(prices[i]/(1-float(char/100)))
                    if(k<0):
                        continue
                    break
                if('lower' in words):
                    k+=float(prices[i]/(1+float(char/100)))
                    break
                if('as' in words):
                    k+=0
                    break
    if(round(k,2)<=x):
        return 'true'
    return 'false'
if __name__ == "__main__":
    main()