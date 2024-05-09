#!/usr/bin/env python3


"""
Example of dynamic programming:
   Calculate the sum of the first N number

Derived formular:
   f(n) = f(n-1) + n
"""

#Using recursion
def sum_n(n: int) -> int:
    """
    Calculate the sum of first N number
    """
    if n == 0:
        return 0
    else:
        return sum_n(n - 1) + n
    
def fact(n: int) -> int:
    if n == 0:
        return 1
    else:
        return fact(n - 1) * n
    
#Using normal function
def sum_n2(n: int) -> int:
    """
    Calculate the sum of first N number
    """
    if n == 0:
        return 0
    
    dp = []
    sum = 0
    
    for i in range(1, n + 1):
        sum += i
        dp.append(sum)
    return dp[-1]



"""
Example 2 of dynamic programming
Problem:
  Climbing stairs
  
  You are climbing a stair case. It takes n steps to reach to the top.
  Each time you can either climb 1 or 2 steps. In how many distinct
  ways can you climb to the top.
  
Framework for solving dynamic programming
1. Define the objective function
   f(i) is the number of distinct ways to reach the i-th stair
2. Identify the base cases
   f(0) = 1
   f(1) = 1
3. Write down a recurrence relation for the optimized objective function
   f(n) = f(n - 1) + f(n - 2)
4. What's the order of execution?
   buttom-up
5. Location of the answer
   f(n)
"""

def climb_stairs(n: int)-> int:
    """
    Calculate the number of distinct ways to reach the n-th stair
    """
    
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return climb_stairs(n - 1) + climb_stairs(n - 2)

def climb_stair(n: int) -> int:
    
    sum = [0] * (n + 1)
    sum[0] = 1
    sum[1] = 1
    
    i = 2
    while i <= n:
        sum[i] = sum[i - 1] + sum[i - 2]
        i += 1
    return sum[-1]

def main():
    n = 4
    ways = sum_n2(n)
    print("Sum of first N number: ", ways)

if __name__ == "__main__":
    main()