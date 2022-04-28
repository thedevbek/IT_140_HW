#write a while loop 
#prints user_num / 2
#until user_num is < 1
user_num = int(input())

while user_num >= 1:
   print(user_num)
   user_num = float(user_num / 2)
   
'''
prints out 
20
10.0
5.0
2.5
1.25
'''
####################################
'''
What it needs to print out is 
10.0
5.0
2.5
1.25
0.625
'''
####################################

'''prints out 0.625''' 
user_num = int(input())

while user_num >= 1:
   user_num = float(user_num / 2)
  
print(user_num)