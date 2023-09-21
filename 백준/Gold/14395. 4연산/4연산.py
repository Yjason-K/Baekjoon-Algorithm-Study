from collections import deque

def bfs(s, t):
    visited = []
    queue = deque([(s, "")])
    visited.append(s)
    
    while queue:
        cur, op = queue.popleft()
        
        if cur == t:
            return op if op else "0"
        
        for next_op, next_val in [('*', cur * cur), ('+', cur + cur), ('-', cur - cur), ('/', cur // cur if cur != 0 else 0)]:
            if 0 < next_val <= 10**9 and next_val not in visited:
                visited.append(next_val)
                queue.append((next_val, op + next_op))
                
    return "-1"

s, t = map(int, input().split())
print(bfs(s, t))