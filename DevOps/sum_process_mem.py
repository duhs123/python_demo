import sys
import os

list=[]
sum=0

str1=os.popen("ps aux","r").readlines()

for i in str1:
        str2=i.split()
        new_rss=str2[5]
        list.append(new_rss)
for i in list[1:-1]:
        num=int(i)
        sum=sum+num

print("%s ---> %s M"%(list[0],float(sum)/1024))
