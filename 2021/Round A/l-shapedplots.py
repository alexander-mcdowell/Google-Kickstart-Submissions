def get_num_l_shapes(grid):
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    # Pre-compute up, left, right, down distances.
    up_len, down_len, left_len, right_len = [], [], [], []
    for i in range(rows):
        up_len.append([0 for _ in range(cols)])
        down_len.append([0 for _ in range(cols)])
        left_len.append([0 for _ in range(cols)])
        right_len.append([0 for _ in range(cols)])
    up_len[0] = grid[0]
    down_len[-1] = grid[-1]
    for i in range(rows):
        left_len[i][0] = grid[i][0]
        right_len[i][cols - 1] = grid[i][cols - 1]
    for i in range(rows):
        for j in range(cols):
            if (grid[i][j] == 1):
                if (i != 0): up_len[i][j] = up_len[i - 1][j] + 1
                if (j != 0): left_len[i][j] = left_len[i][j - 1] + 1
            if (grid[rows - i - 1][cols - j - 1] == 1):
                if (i != 0): down_len[rows - i - 1][cols - j - 1] = down_len[rows - i][cols - j - 1] + 1
                if (j != 0): right_len[rows - i - 1][cols - j - 1] = right_len[rows - i - 1][cols - j] + 1
    
    for i in range(rows):
        for j in range(cols):
            if (grid[i][j] == 0): continue
            
            # Check if this is a corner
            up, down, left, right = False, False, False, False
            if (i > 0):
                up = bool(grid[i - 1][j])
            if (i < rows - 1):
                down = bool(grid[i + 1][j])
            if (j > 0):
                left = bool(grid[i][j - 1])
            if (j < cols - 1):
                right = bool(grid[i][j + 1])
            
            if ((up or down) and (left or right)):
                # Check if we form an L-shape.
                for a in [up_len[i][j], down_len[i][j]]:
                    for b in [left_len[i][j], right_len[i][j]]:
                        if (a != 1 and b != 1):
                            x = max(a, b)
                            y = min(a, b)
                            count += min(int(x/2), y) + min(int(y/2), x) - 2
                
    return count

num_cases = int(input())
for i in range(num_cases):
    rows, cols = input().split(" ")
    rows = int(rows)
    cols = int(cols)
    
    # Construct grid
    grid = []
    for j in range(rows):
        grid.append([])
        elements = input().split(" ")
        for k in range(cols): grid[j].append(int(elements[k]))
        
    print("Case #" + str(i + 1) + ": " + str(get_num_l_shapes(grid)))