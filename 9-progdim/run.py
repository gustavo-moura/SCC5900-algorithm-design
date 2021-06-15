import sys
data = sys.stdin.readlines()
content = [line.rstrip() for line in data]

#with open('1.in', 'r') as file:
#    content = file.readlines()
    
mx = 1005   

pointer = 0

n_cases = int(content[pointer]) #T
pointer += 1

for t in range(n_cases):

    n_objects = int(content[pointer]) #N

    pointer += 1

    price = []
    weight = []

    for i in range(pointer, pointer + n_objects):
        obj = [int(o) for o in content[i].split(' ')]
        price.append(obj[0])
        weight.append(obj[1])

    pointer += n_objects

    n_pep = int(content[pointer])

    pointer += 1

    people = []
    for i in range(pointer, pointer + n_pep):
        people.append(int(content[i]))
        
    pointer += n_pep


    # ---



    def shack(i, w):
        if i == n_objects:
            return 0

        if dp[i][w] != -1:
            return dp[i][w]

        res1 = 0 
        res2 = 0

        if (w + weight[i]) <= CAP:
            res1 = price[i] + shack(i + 1, w + weight[i])
        else:
            res1 = 0

        res2 = shack(i + 1, w)

        dp[i][w] = max(res1, res2)

        return dp[i][w]

    ans = 0
    pep = n_pep

    g = 0
    while pep > 0:
        
        dp = [[-1 for _ in range(mx)] for _ in range(mx)]

        CAP = people[g]
        ans += shack(0, 0)
        pep -= 1
        g += 1

    print(ans)
