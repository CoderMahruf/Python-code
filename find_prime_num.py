def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True

def print_primes(limit):
    print(f"prime numbers up to{limit}are:")
    for num in range(2, limit + 1):
      if is_prime (num):
         print(num,end=" ")            
        
        
limit = 50
print_primes(limit)