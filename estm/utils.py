def get_neighbours(i,j,height,width):
    return [(x,y) for x, y in [
            (i-1, j),   # n
            (i, j-1),   # w
            (i+1, j),   # s
            (i, j+1),   # e
        ]
        if 0 <= x < width and 0 <= y < height]