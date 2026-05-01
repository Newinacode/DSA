''''
Dynamic Programming where programming means tabular method.

Dynamic Programming is like divide and conquer but when we do divide and conquer if there
is common subproblem it solve them too. So, computation increase.

But I dynamic programming we solve each subproblem just once and save answer in table.

So, Dynamic Programming goes for optimization of problem by reusing the calculation that has
been already calculated.


As, each problems can have many possible solution and each solution has value, we wish to find
a solution with optimal (min/max) value.

Step to develop dynamic programming
1. characterize the structure of an optimal solution.
2. Recursively define the value of an optimal solution.
3. Compute the value of an optimal solution,typically in the button up fashion.
4. construct an optimal solution from computed information.


1-3 is for dynamic programming, but if we need information how we get it step 4 it required.

'''

# example 1 for dynamic programming implmentation.


# Rod cutting

'''
In this problem following information is provided.
n = size of rod in inches
p[i] = include the price of rod for particular inch. where i = 1,2,3,4,...,n 
rn - maximum revenue after cutting given rod with size n.
n = i1 + i2 + i3 +...+ ik ; where k = number of pieces.
so, rn = pi1 + pi2 + pi3 + .... + pik

rn = max(Pn,r1+rn-1,r2+rn-2,....,rn-1+r1)
'''
# value of prices each index represent size i+1
pi  =[1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# recursive implementation

def recursive(pi,n):

    if n == 0:
        return 0
    q = float('-inf')
    for j in range(0,n):
        q = max(q,pi[j]+recursive(pi,n-(j+1)))

    return q


print(recursive(pi,10))


# above implementation is recursive way of solving it.
'''
so there is two apporach to solve dynamic programming
1. top-down with memoization
2. bottom-up method

time - complexity is same for both, but there might be some cases where top-down doesn't 
examine all possible sub-problem

'''
# top-down apporach implementation 
def memoized_rod(p,n):
    r = [0]*(n+1)

    for i in range(n+1):
        r[i] = float("-inf")

    return memoized_rod_aux(p,n,r)


def memoized_rod_aux(p,n,r):
    if r[n]>=0:
        return r[n]
    
    if n == 0:
        q = 0

    else:
        q = float('-inf')

        for j in range(n):
            q = max(q,p[j]+memoized_rod_aux(p,n-(j+1),r))


    r[n] = q 
    return q

   
print(memoized_rod(pi,10))



# bottom up approach
'''
In botton up approach we solve in sorted way that means we will try to minimal subproblem
and then other.
'''
def botton_up(p,n):
    r = [0]*(n+1)
    r[0] = 0


    for j in range(1,n+1):
        q = float('-inf')
        for i in range(j):
            q = max(q,p[i]+r[j-i-1])
        r[j] = q

    return r[n]


print(botton_up(pi,2))
