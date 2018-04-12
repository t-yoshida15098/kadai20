

import sys
#import Counter as count

file=open(sys.argv[1],'r')
a=file.read()
file.close()

dict={}
words=a.split()
for w in words:
    if w not in dict:
        dict[w]=1
    else:
        dict[w]+=1
i=0

#print(sorted(dict.items()))

for k,value in sorted(dict.items(),key=lambda x: -x[1]):
    print(str(k)+'\t:'+str(value))
    i+=1
    if i==9:
        break

