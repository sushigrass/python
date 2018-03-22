if __name__ == '__main__':
    import time
    while True:
        while True:
            print('How many iterations of each function would you like to run?')
            try:
                iterations = int(input())
                break
            except:
                print('Please input an integer value.')
        normal_time = 0
        list_comp_time = 0
        def runFuncs():
            global normal_time
            global list_comp_time
            def fizzNormal():
                global iterations
                global normal_time
                start = time.time()
                for num in range(1,iterations):
                    if num%3==0 and num%5==0:
                        print('FizzBuzz')
                    elif num%3==0:
                        print('Fizz')
                    elif num%5==0:
                        print('Buzz')
                    else:
                        print(num)
                end = time.time()
                normal_time = (end - start)
            def fizzListComp():
                global iterations
                global list_comp_time
                start = time.time()
                print(*['fizzbuzz' if num%3==0 and num%5==0 else 'fizz' if num%3==0 else 'buzz' if num%5==0 else num for num in range(1,iterations)], sep='\n')
                end = time.time()
                list_comp_time = (end - start)
            fizzNormal()
            fizzListComp()
            print('Normal for loop: %.10f'%(normal_time))
            print('Fancy list comprehension: %.10f'%(list_comp_time))
        runFuncs()
        print('Run again? (Enter Y for yes or anything else for no).')
        ans = input()
        if ans=='y' or ans=='Y':
            continue
        else:
            break
