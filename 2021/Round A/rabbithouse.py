def find_min_boxes(grid):
    rows, cols = len(grid), len(grid[0])
    
    def recompute_then_stack(r, new_r, c, new_c, grid, stack):
        delta = 0
        # If the element we are comparing against is larger, increase this element
        # and add it to the stack to recompute the values of neighbors.
        if (grid[new_r][new_c] - grid[r][c] > 1):
            delta += grid[new_r][new_c] - grid[r][c] - 1
            grid[r][c] = grid[new_r][new_c] - 1
            stack.append((r, c))
        # If the element we are comparing against is smaller, increase it and add to the
        # stack to recompute the values of its neighbors.
        elif (grid[r][c] - grid[new_r][new_c] > 1):
            delta += grid[r][c] - grid[new_r][new_c] - 1
            grid[new_r][new_c] = grid[r][c] - 1
            stack.append((new_r, new_c))
        return delta
    
    stack = []
    boxes = 0
    for i in range(rows):
        for j in range(cols):
            stack.append((i, j))
            while (len(stack) != 0):
                pair = stack.pop(-1)
                r, c = pair
                
                # Check the element above.
                if (r > 0): boxes += recompute_then_stack(r, r - 1, c, c, grid, stack)
                # Check the element below.
                if (r < rows - 1): boxes += recompute_then_stack(r, r + 1, c, c, grid, stack)
                # Check the element to the left.
                if (c > 0): boxes += recompute_then_stack(r, r, c, c - 1, grid, stack)
                # Check the element to the right.
                if (c < cols - 1): boxes += recompute_then_stack(r, r, c, c + 1, grid, stack)
 
    return boxes

num_cases = int(input())
for i in range(1, num_cases + 1):
    rows, cols = input().split(" ")
    rows = int(rows)
    cols = int(cols)
    
    grid = []
    for _ in range(rows):
        grid.append([])
        s = input().split(" ")
        for k in range(cols): grid[-1].append(int(s[k]))
    
    print("Case #" + str(i) + ": " + str(find_min_boxes(grid)))