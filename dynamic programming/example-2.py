'''
  In staircase question if we are given prices that we need to pay

'''




def op_stair_step(n,p):
    dp = [0] * (n+1)

    dp[0] = 0
    dp[1] = p[0]
    path = [0] * (n)

    for i in range(2,n):
        dp[i] = (min(dp[i-1],dp[i-2])) + p[i-1]

        if dp[i-1] < dp[i-2]:
            path[i] = i-1
        else:
            path[i] = i-2

    return path



prices = [1,2,3,4,5]
n = 5 

path = op_stair_step(n,prices)

curr = n-1

while curr > 0:
    
    curr = path[curr]
    print(curr)


