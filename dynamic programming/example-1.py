'''
First example is climbing stair question.
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top
Leetcode question link - Easy Question
https://leetcode.com/problems/climbing-stairs/description/


Thinking in Dynammic programming way.


type of question: Combinatoric (finding ways)

steps 

1. Finding Objective
Are we going to do maximize or minimize

2. Breaking down problem in simple subproblem

n = 1
taking one step from 1.
F(1) = 1

suppose n = 2
so, distinct ways will be take two step from starting point or taking step from 1.
so, F(2) = 2

3rd recurrence relation

if we have staircase of size 3. n=3

from where we can get to staircase 3, as we are allowed to take either one step or two.

so it will be from either 2 or 1

for size 4 n =4
so it will be either from 3 or 2

so, for n it will either from n-1 or n-2


so, using rule of sum,
if we have A way to do something and if we have B ways to do something but they can't
be done at same time then there are A+B ways to do.

so 
way of n will be = ways of (n-1) + ways of (n-2)


recall.

# Indentify the base case:
T(0) = 1
T(1) = 1



# Recurrence Relation
f(n) = f(n-1) + f(n-2)


# Order of computation : what we need to calculate the answer
(n-1) and (n-2)


# execution of order
button up approach

location of answer: where is our final answer
at F(n)

'''


def stairs(n):
    '''
    n = number of staircase
    '''

    dp = [0] * (n+1)

    dp[0] = 1
    dp[1] = 1


    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]


    return dp[n]


print(stairs(4))


# optimization memory

# as we only need two values we can use just two variable and update the latter onedef stairs(n):

def stairs_st(n):
    dp = [0] * (n+1)

    p = 1
    q = 1


    for i in range(2,n+1):
        temp = p + q
        p,q = q,temp
    


    return q


print(stairs_st(4))



'''
suppose we are given that we can take upto 1 to kth step to solve
previously our constraint was we are allowed to take 1 or 2 step at a time.


so, reccurance function will be 
f(n) = f(n-1) + f(n-2) + ... f(n-k)

'''


def k_steps(n,k):
    '''
    n = number of stairs 
    k = number of step allowed
    '''


    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1


    for i in range(2,n+1):
        for j in range(1,k+1):
            if i-j<0:
                continue
            dp[i] += dp[i-j]

    return dp[n]




print(k_steps(4,2))



'''
space complexity up to kth element

'''

def op_k_steps(n,k):
    '''
    n = number of stairs 
    k = number of step allowed
    '''


    dp = [0]*(k)
    dp[0] = 1

    for i in range(1,n+1):
        for j in range(1,k):
            if i-j<0:
                continue

            dp[i%k] += dp[(i-j)%k]

    return dp[n%k]




print(op_k_steps(4,2))