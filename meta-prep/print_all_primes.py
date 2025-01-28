def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_all_primes(array):
    for k in array:
        if is_prime(k):
            print(k)

# O(n)? Include all the things, make a reasonable assumptions,
# and then make a reasonable guess about the time complexity.
#1 :  Include all the things
#2 : Use logical variable names. Don't just toss around "n". You might forget what it means
#3 : Define the variables you need
#4 : Add runtimes together; Adding vs Multiplying
#5 : Drop constants in determining the Big O for the functions
#6 : Use big O for space, remember the call stack!
#7 : Drop the non-dominant terms