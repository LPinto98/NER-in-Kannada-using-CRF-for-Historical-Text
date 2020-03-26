import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
word = []
pos=[]
num=[]
no = 1
with open(os.path.join(BASE_DIR,'main/intermediate.txt'), mode='r',encoding='utf-8') as filey:
    for line in filey:
        l = line.split('\t')
        word.append(l[0])
        pos.append(l[1])
        num.append(no)
        if(l[0]=='.'):
            no+=1
f = open(os.path.join(BASE_DIR,'main/inter2.txt'), mode='w',encoding='utf-8')
f.write('Sentence#\tWord\tPOS\n')
for i in range(len(word)):
    f.write(str(num[i])+"\t"+str(word[i])+"\t"+str(pos[i]))
f.close()        
