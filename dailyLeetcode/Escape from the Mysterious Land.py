def escape(line1, line2, line3) -> int:

    row, cols = line1.split()
    A, B, C, D = line2.split()
    A, B, C, D = int(A)-1, int(B)-1, int(C)-1, int(D)-1
    island = [[0 for _ in range(int(cols))] for _ in range(int(row))]
    keys_count = 0 

    for i in range(int(row)):
        for j in range(int(cols)):
            if line3[i][j] == 'k':
                keys_count += 1
            island[i][j] = line3[i][j]

    if keys_count == 0:
        return -1

    queue = [(int(A), int(B), 0)]  # (row, col, keys_collected, steps)
    visited = set()
    visited.add((int(A), int(B)))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    exist_start_row, exist_start_col, steps = int(A), int(B), -1

    while queue:
        r, c, steps = queue.pop(0)

        if island[r][c] == 'k': # Mark the key as collected
            exist_start_row, exist_start_col, steps = int(r), int(c), steps
            break

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < int(row) and 0 <= new_c < int(cols) and island[new_r][new_c] != '#' and (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                queue.append((new_r, new_c, steps + 1))
    if steps == -1:
        return -1
    
    queue = [(exist_start_row, exist_start_col, steps)]  # Reset the queue for the second BFS
    visited = set()
    visited.add((exist_start_row, exist_start_col))

    while queue:
        r, c, steps = queue.pop(0)

        if (r, c) == (int(C), int(D)):
            return steps+1

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < int(row) and 0 <= new_c < int(cols) and island[new_r][new_c] != '#' and (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                queue.append((new_r, new_c, steps + 1))





    return -1