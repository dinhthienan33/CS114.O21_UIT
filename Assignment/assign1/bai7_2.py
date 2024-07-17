def main():
    prices= list(map(int, input().split()))
    notes=[]
    for _ in range(len(prices)):
        notes.append(input().split())
    x=int(input())
    print(solve(prices,notes,x))
def not_float(s):
    try:
        float(s)
        return False
    except ValueError:
        return True
def check_string(s):
  if not_float(s[0][:-1]): 
      return False
  elif s[0][-1]!='%': 
      return False
  elif s[0][0]=='-': 
      return False
  elif s[1]!='lower' and s[1]!='higher':
      return False
  elif s[1]=='higher' and float(s[0][:-1])>=100.: 
      return False
  elif s[2]!='than': 
      return False
  elif s[3]!='in-store':
      return False
  return True
def identify_number(string):
    number = string.strip('%')  
    try:
        number = float(number)  
        return number
    except ValueError:
        return None 
def solve(prices,notes,x):
    if(sum(prices)<=x):
        return 'true'
    k=[]
    for i in range(len(prices)):
        note=notes[i]
        for j in range(len(note)-3):
            if(check_string(note[j:j+4])):
                f=identify_number(note[j])
                if(f!=None):
                    if(note[j+1]=='higher'):
                        k.append(-1*prices[i]*f/100)
                        break
                    if(note[j+1]=='lower'):
                        k+=1*prices[i]*f/100
                        break
    if (k<=x):
        return 'true'
    return 'false'
if __name__ == "__main__":
    main()