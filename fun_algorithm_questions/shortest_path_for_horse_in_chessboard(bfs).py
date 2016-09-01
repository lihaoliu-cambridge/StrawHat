from collections import deque


def check_out_of_chessboard(step, n, m):
    if (0 <= step[0] <= n) and (0 <= step[1] <= m):
        return False
    else:
        return True


def bfs_step(n, m):
    G = {(x, y): False for x in range(0, n + 1) for y in range(0, m + 1)}
    step_size = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    path = deque()
    path.append((0, 0, 0))
    while len(path) > 0:
        now = path.popleft()
        for next_direction in step_size:
            next_step = (now[0] + next_direction[0], now[1] + next_direction[1], now[2] + 1)
            if check_out_of_chessboard(next_step, n, m):
                continue
            if G[next_step[0], next_step[1]]:
                continue
            G[next_step[0], next_step[1]] = True
            path.append(next_step)
            if next_step[0] == n and next_step[1] == m:
                return next_step[2]
    return -1


print bfs_step(1, 2)