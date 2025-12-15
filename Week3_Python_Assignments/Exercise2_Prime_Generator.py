# Prime Number Generator
# This program is designed to generate prime numbers within a certain range
# and displays them with 10 numbers per line.

# Task 1: Takes two positive integers as input (range start and end)

def prime_gen():
    try:
        # inputs for both start and end
        start = int(input("Enter your starting number: "))
        end = int(input("Enter your ending number: "))

# Task 2: Validates the input (must be positive integers)

        # Validate that numbers are positive
        if start < 0 or end < 0:
            print("Please enter positive integers only.")
            return
        # Ensuring start is less than or equal to end
        if start > end:
            print("Starting number must be less than or equal to ending number.")
            return

# Task 3: Finds all prime numbers within the given range (inclusive)
        # creating a list
        prime = []
        # starting a loop from start to end 
        for i in range(start,end+1):
            factor = 0  # initially assigning factor to 0
            if i==1:
                continue # because 1 is composite and so we can skip it.
            
            if i%1 == 0 and i%i==0: # every number has atleast 2 factors.
                factor += 2         #  with itself and with one 
            
            for j in range(2,i):
                if i%j==0:  # checking if there exists more than 2 factors or not
                    factor += 1

            if factor == 2:
                prime.append(i) # if not exists then its a prime

# Task 4: Displays the primes in a formatted output (10 numbers per line)

        if not prime:
            print("No prime numbers found in the given range.")
        else:
            print("\nPrime Numbers:")
        for i in range(0, len(prime), 10): # displaying the output 10 numbers per line
            print(" ".join(str(p) for p in prime[i:i + 10]))

# Task 5: Handles invalid inputs gracefully

    except ValueError: # handling value error
        print("Please enter valid input.")
    except Exception as e: # handling other exception
        print('An unexpected error {e} occur')         

prime_gen()
