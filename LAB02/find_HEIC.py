import os
path='cs114.o21.x.lab01-competition'
list=[]
for file in os.listdir(path):
    if file.endswith('.md'):
        list.append(file)
with open ('md_file.txt', 'w') as f:
    for file in list:
        f.write(file+'\n')
    f.close()