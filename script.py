def prime_finder(n):
  # Write your code here
  primes= []
  if n < 2:
    return primes
  elif n == 2:
    primes.append(2)
    return primes
  else:
    primes.append(2)
    for i in range(3, n+1):
      flag= False
      for prime in primes:
        if i % prime == 0:
          flag= True
      if flag == False:
        primes.append(i)
    return primes
    

 
print(prime_finder(11))
