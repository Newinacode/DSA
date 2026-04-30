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


'''