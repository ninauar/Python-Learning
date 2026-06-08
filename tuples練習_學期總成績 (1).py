# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:13:29 2023

@author: USER
"""

"""
weight為成績比重, peter,may,andy每個人的成績如下,student為所有學生的集合,
請計算出每個學生的學期總成績?
"""
weight=(0.3,0.3,0.2,0.2)
peter=[95,84,60,70]
may=[75,88,90,85]
andy=[86,78,63,92]
student=[peter,may,andy]
print(student)

for stu  in student:
    tal=0
    for i in range(len(stu)):
        tal+=stu[i]*weight[i]
        print(stu[i],"*",weight[i]*100,"%=",stu[i]*weight[i])
    print("學期成績:",tal)
    
        