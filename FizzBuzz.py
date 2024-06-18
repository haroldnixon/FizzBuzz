#   Sudo Code
#
#  iterate varable i to 15
#    numBuzz = anthing divisible by 3
#    numFizz = anthing divisible by 5
#    
#    if numFizz { i = 'Fizz' }
#    if numBuzz { i = 'Buzz' }
#    if numFizz == numBuzz { i = 'FizzBuzz' }
#
#    print(i)
#

#Version 1:
for i in range(1,16):
 # print(i)
    numFizz  = i % 3
    numBuzz = i % 5


    if numFizz > 0:
      iFizz = numFizz
    else: i = 'Fizz' 
    if numBuzz > 0:
      iBuzz = numBuzz
    else: i = 'Buzz'
    if numFizz == 0 and numBuzz == 0:
      i = 'FizzBuzz' 
    print(i)
    
print('Version 2:')
# Version 2 - Cleaner Version:
for i in range(1,16):
 # print(i)
    numFizz  = i % 3
    numBuzz = i % 5

    if numFizz == 0:
      i = 'Fizz'
    if numBuzz == 0:
      i = 'Buzz'
    if numFizz == 0 and numBuzz == 0:
      i = 'FizzBuzz' 
    print(i)

  #print(i , numFizz, numBuzz)