import os

with open("./origin","r") as origin:
	ori_txt=origin.readline().strip()
with open("./Pneumotoulthamicrescopicfilicoloaganiconissis-df5bb3d8f83d6d37e16560062cb231bc.txt","r") as compare:
	cmp_txt=compare.readline().strip()
ori_txt=ori_txt.replace(' ','')
cmp_txt=cmp_txt.strip(' ')
i = 0
while i < min(len(ori_txt),len(cmp_txt)):
	if ori_txt[i]!=cmp_txt[i]:
		print(cmp_txt[i],end='')
	i=i+1


