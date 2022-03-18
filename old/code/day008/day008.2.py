#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    counter = 2
    #check if divisible by 2
    if number == 1:
        is_prime = True
    elif number == 2:
        is_prime = True
    else:
        while counter < number:
            if number % counter == 0:
                is_prime = False
                break
            else:
                counter += 1
    #for i in range(2, number):
        #if number % i ==0:
            #is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)