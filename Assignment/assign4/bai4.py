from sys import stdin,stdout
arr = []

while True:
    ip = [int(i) for i in stdin.readline().split()]
    if(ip[0]==6):
        break
    if ip[0] == 0:
        arr.insert(0,ip[1])
    
    elif ip[0] == 1:
        arr.append(ip[1])
    
    elif ip[0] == 2:
        try:
            index = arr.index(ip[1])
            arr.insert(index + 1, ip[2])
        except ValueError:
            arr.insert(0, ip[2])
    
    elif ip[0] == 3:
        if ip[1] in arr:
            arr.remove(ip[1])
    
    else :
        arr.pop(0)
if not arr:
    stdout.write('blank')
else:
    output = ' '.join(map(str, arr))
    stdout.write(output)