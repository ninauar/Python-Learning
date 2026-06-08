# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:09:30 2023

@author: USER
"""
"""
定義以下student的Dictionary集合,如下:
student={'bill':{'chinese':95,'english':86,'math':75,'tal':0,'avg':0},
        'jack':{'chinese':71,'english':68,'math':59,'tal':0,'avg':0},
        'mary':{'chinese':65,'english':72,'math':82,'tal':0,'avg':0}  }
請計算每位學生的總分,平均,並找出那一個位第一名?
"""

student={'bill':{'chinese':95,'english':86,'math':75,'tal':0,'avg':0},
        'jack':{'chinese':71,'english':68,'math':59,'tal':0,'avg':0},
        'mary':{'chinese':65,'english':72,'math':82,'tal':0,'avg':0}  }
max=0
stu=""
for name,score in student.items():
    print(name,end=" ")
    for course,s in score.items():
           print(score[course],end=" ")           
           if course!="tal":
              score["tal"]+=score[course]
           else:
              score["avg"]=score["tal"]/3
              print(score["tal"],score["avg"])
              if score["avg"]>max:
                  max=score["avg"]
                  stu=name
              break

print("最高分是:",stu,"分數:",max)
    
              
              
         