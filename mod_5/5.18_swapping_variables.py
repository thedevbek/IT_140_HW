'''Write a program whose input is two integers and whose output is the two integers swapped.'''

def swap_values(user_val1, user_val2):
    return user_val2, user_val1

if __name__ == '__main__':  
   user_input1 = int(input())
   user_input2 = int(input())

   output1, output2 = swap_values(user_input1, user_input2)  
   print(str(output1) + ' ' + str(output2))       