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


''''
How do know what kind of problem do we use dynamic programming


Normally dp is used for problem like combinatoric and optimization problem.

example of combinatoric problem -
  # How many ways to make a change ?
  # How many ways to traverse a graph ?
  # How many steps needed to get from point A to point B?

example of optimization problem (maximum or minimum)-
  # what is the minimum/maximum number of steps needed to get from point A to point B?
  # what is the maximum profit selling and buying stock?
  # what is the shortest path to get from India to China ?


We can say that DP is a algorithm way to solve combinatoric or optmization problem


$$$ Basic Understanding of DYNAMIC PROGRAMMING "

example 1:
sum of n number.



1 + 2 + 3 + 4 + ..... + n 

#base case 
F(1) = 1

F(2) = F(1) + 2
F(3) = F(2) + 3

representing above process in equation.
F(n) = f(n-1) + n
'''

# why n+1 here we are doing 1-indexing
# here we are using top down approach

def n_sum(n):
    # time memory trade off we are using more memory resources to cache our previous solved data
    dp = [0]*(n+1)


    dp[0] = 0
    dp[1] = 1


    for i in range(1,n+1):
        dp[i] = dp[i-1] + i

    return dp[n]



# writing test case for n_sum


def test_n_sum():
    # tuple are parameter and result
    test_val = [(3,6),(10,55)]

    for idx,val in enumerate(test_val):
        par,res = val
        
        try:
            assert(n_sum(par)) == res
            print(f"test #{idx} = PASSED")
        
        except:
            print(f"test.#{idx} = FAILED for {par}")



test_n_sum()










