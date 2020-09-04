def prisonAfterNDays(cells, N):
    if len(cells) == 0 or N == 0:
        return []
    
    if N == 1:
        return cells
    
    prev = [cell for cell in cells]
    for i in range(2, N + 1):
        cells[0] = cells[len(cells) - 1] = 0
        for j in range(1, len(cells) - 1):
            
            cells[j] = 1 if prev[j - 1] == prev[j + 1] else: 0
        print("cells", cells)
        prev = [cell for cell in cells]
    return cells
            


prisonAfterNDays([0,1,0,1,1,0,0,1], 7)