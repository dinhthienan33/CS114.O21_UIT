def is_not_float(s):
    try:
        float(s)
        return False
    except ValueError:
        return True

def check(s):
  if is_not_float(s[0][:-1]): return False
  elif s[0][-1]!='%': return False
  elif s[0][0]=='-': return False
  elif s[1]!='lower' and s[1]!='higher': return False
  elif s[1]=='higher' and float(s[0][:-1])>=100.: return False
  elif s[2]!='than': return False
  elif s[3]!='in-store': return False
  return True

def ProcStr(s):
  s = s.split()
  l = len(s)-3
  i = -1
  for j in range(l):
    if check(s[j:j+4]):
      i=j
      break
  if(i==-1): return 1, 0
  return 1 if s[i+1]=='lower' else -1, float(s[i][:-1])

def solve():
  inp = [int(i) for i in input().split()]
  n = len(inp)
  delta = []
  for i in range(n):
    s = input()
    symb, sale = ProcStr(s)
    delta.append(inp[i]*symb*sale/100)
  budget = float(input())
  delta = min(sum(delta), 0)
  total = sum(inp) + delta
  #print(total)
  if(budget>=total): print("true")
  else: print("false")

if _name__=="__main_":
  solve()