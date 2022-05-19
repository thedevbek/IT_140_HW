
## The problem:
    ## Write a program that prints the number from 1 to 20.
    ## For multiples of three print 'Fizz' instead of the number.
    ## For the multiples of five print 'Buzz' instead of the number.
    ## For the numbers which are multiples of both three and five  print'FizzBuzz' instead
    ## For numbers not divisible by 3, or 5, or both, print the number as is.

#@ FOR LOOP
#@ Set counter to 1
#@ Break when counter reaches 20
#@ Increment counter by 1
    #! IF number MOD 15 === 0 then
        #$ print 'FizzBuzz' 
    #! ELSE IF number MOD 3 === 0 
        #$ print 'Fizz'
    #! ELSE IF number MOD 5 === 0 
        #$ 'Buzz' 
    #! ELSE
        #$ print number

## In JavaScript
    ## for(let i =1; i <= 20; i++)
    ## if (i % 15 === 0) {
    ##   console.log('FizzBuzz');}
    ## else if (i % 3 === 0) {
    ##   console.log('Fizz')};
    ## else if (i % 5 === 0) {
    ##   console.log('Buzz'); }
    ## else {
    ## console.log(i)}

num = 1
while (num <=100):
    if (num % 3 == 0 and num % 5 == 0):
        print (str(num) + '. FizzBuzz!')
    elif (num % 3 == 0):
        print (str(num) + '. Fizz!')
    elif (num % 5 == 0):
        print (str(num) + '. Buzz!')
    else:
        print(str(num) + '.')
    num += 1
 


    