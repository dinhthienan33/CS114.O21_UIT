def main():
    city1=list(input())
    city2=list(input())

    if(check(city1,city2)):
       print("Yes")
       return True
    else: 
       print("No")
       return
   
def check(city1, city2):
    if(len(set(city1))==1 or len(set(city2))==1):
        return True
    for i in range(2):
       if(city1[i] == city2[i]):
           return True
    
            
if __name__ == '__main__':
    main()