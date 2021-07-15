import sys

data = sys.stdin.readlines()
content = [line.rstrip() for line in data]

#with open('2.in', 'r') as file:
#    content = file.readlines()

coins = [0, 1, 5, 10, 25, 50]

mx = 7500

def solve(amount):
    #print(f'solving {amount}')
    
    dp = [0 for _ in range(mx)]
    dp[0] = 1

    for i in range(1, 6):
        c = coins[i]
        #print(f'c={c}')
        for j in range(amount+1):
            if j >= c:
                dp[j] += dp[j - c]
                #print(f'dp[{j}]={dp[j]}')
    return dp[amount]


for line in content:
    amount = int(line)
    ans = solve(amount)
    print(ans)

