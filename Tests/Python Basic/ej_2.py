def fizzBuzz(n):
    for i in range(1, n+1):
        val = True
        if i % 3 == 0: 
            print('Fizz', end='')
            val = False
        if i % 5 == 0: 
            print('Buzz', end='')
            val = False

        if val: print(i, end='')
        print()



if __name__ == '__main__':
    fizzBuzz(15)
