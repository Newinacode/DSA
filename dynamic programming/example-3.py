'''
Dynamic Programming : Example 3


leetcode: https://leetcode.com/problems/unique-paths/description/


How many unique path we have to reach at end of matrix of n*m if n and m is given you are 
only allowed to go down or right:

Input: m = 3, n = 7
Output: 28



# base case that computer don't have to calculate:
In our case base case will when there is only one grid is given n =1 and m=1
ans = 1


dp[0][0] = 1
# reccurance relation
When we want to see reccurance relationship we see after the problem is finish.
to end up in last. 
As to get we can get from two places from top or from left
so, at m and n
it will  be
F(n,m) = F(n-1,m) + F(n,m-1)


'''


def unique_path(n,m):
        dp = [[0]*n]*m


        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i>0 and j>0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif j>0:
                    dp[i][j] = dp[i][j-1]
                elif i>0:
                    dp[i][j] = dp[i-1][j]

        return dp[m-1][n-1]

print(unique_path(3,7))  #28




# question 2
# leetcode https://leetcode.com/problems/unique-paths-ii/

'''
In this question it will be same, but here we are given extra information.
Here, we might have obstacle if we have obstacle. We can just let that grid dp value to 0

'''



def unique_path_obstacle(obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        
        dp[0][0] = 1 

  

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
            
                    if i > 0 and j>0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    elif i>0:
                        dp[i][j] = dp[i-1][j]
                    elif j>0:
                        dp[i][j] = dp[i][j-1]


        return dp[m-1][n-1]



obs = [[0,0,0],[0,1,0],[0,0,0]]



print(unique_path_obstacle(obs)) #2



'''
Example to find maximum profit in grid if each grid consist of value.
'''


def unique_path_obstacle(profitGrid):
        m = len(profitGrid)
        n = len(profitGrid[0])

        dp = [[0] * n for _ in range(m)]

        
        dp[0][0] = 1 

  

        for i in range(m):
            for j in range(n):
               
                if i > 0 and j>0:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + profitGrid[i][j]
                elif i>0:
                    dp[i][j] = dp[i-1][j] + profitGrid[i][j]
                elif j>0:
                    dp[i][j] = dp[i][j-1] + profitGrid[i][j]


        return dp[m-1][n-1]


profitGrid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]


print(unique_path_obstacle(profitGrid)) #12




'''
As previous question finding maximum profit but here we are going to print out the path we
took get maximum profit.
'''


def unique_path_obs(profitGrid):
        m = len(profitGrid)
        n = len(profitGrid[0])

        dp = [[0] * n for _ in range(m)]

        
        dp[0][0] = profitGrid[0][0]

  

        for i in range(m):
            for j in range(n):
                if i > 0 and j>0:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + profitGrid[i][j]
                elif i>0:
                    dp[i][j] = dp[i-1][j] + profitGrid[i][j]

                elif j>0:
                    dp[i][j] = dp[i][j-1] + profitGrid[i][j]



        return dp


profitGrid = profitGrid = [
    [2, 5, 1, 8, 3, 1, 4, 2],
    [1, 3, 2, 5, 1, 4, 6, 1],
    [6, 1, 8, 2, 3, 2, 1, 5],
    [1, 4, 1, 6, 7, 1, 3, 2],
    [2, 1, 5, 2, 4, 5, 8, 1],
    [3, 2, 1, 1, 2, 8, 4, 3],
    [1, 6, 2, 4, 1, 5, 2, 7],
    [4, 1, 3, 2, 6, 1, 3, 5]
]



dp = unique_path_obs(profitGrid)


m = len(dp)-1
n = len(dp[0])-1




path = []
path.append((m,n))
while m !=0 or n !=0:
    if m == 0:
        path.append((m,n-1))
        n -= 1
    elif n == 0:
        path.append((m-1,n))
        m-=1
    elif m>0 and n>0:
        if dp[m-1][n]>dp[m][n-1]:
            path.append((m-1,n))
            m -= 1
        else:
            path.append((m,n-1))
            n-=1

print(list(reversed(path)))




        
     






