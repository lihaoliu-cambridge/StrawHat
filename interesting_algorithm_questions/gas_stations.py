limit = [2, 1, 3]
cost = [3, 3, 3]
n = len(limit)

residual = [limit[i] - cost[i] for i in range(n)]

start_position, steps, residual_sum = 0, 0, 0
for position in range(n<<1):
    if n == steps:
        break
    residual_sum += residual[position%n]
    if residual_sum >= 0:
        steps += 1
    else:
        residual_sum, steps, start_position = 0, 0, (position+1)%n

print start_position if steps == n else -1
