for i in range(1,16):
 # print(i)
    numFizz  = i % 3
    numBuzz = i % 5
    fizzBuzz = 'WTF!!!'


    if numFizz > 0:
      iFizz = numFizz
    else: i = 'Fizz' 
    if numBuzz > 0:
      iBuzz = numBuzz
    else: i = 'Buzz'
    if numFizz == 0 and numBuzz == 0:
      i = 'FizzBuzz' 
    print(i)