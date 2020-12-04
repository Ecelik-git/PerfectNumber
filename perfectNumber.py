def PerfectNumber(n):#create a function to check given number
    #creating sum to hold sum of divisors
    sum = 0
    # if the number users enter is bigger than 1, continue
    if n > 1:
        #we need to check all divisors
        for i in range(1, n):
            if n % i == 0: #if the number is divisor of n 
                sum += i #then we need to add it to sum
    else: # if the number is less than 1 or 1, ask users to enter another
        print("Please enter a number bigger than 1")
        
    if sum is n: # if sum of divisors are equal to the number
        print(str(n) + " is a perfect number")#then it is a PERFECT number
    else:#if sum of divisors are not the number
        print(str(n) + " is not a perfect number")# the number is not perfect :/

number = int(input("Please enter a number: "))#ask users to enter a number
PerfectNumber(number)#call the function to check the number

