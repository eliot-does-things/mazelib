def to_box_string(maze, entrances=False, solutions=False):
    """Return a string representation of the maze.
    This can also display the maze entrances/solutions IF they already exist.
    Args:
        entrances (bool): Do you want to show the entrances of the maze?
        solutions (bool): Do you want to show the solution to the maze?
    Returns:
        str: string representation of the maze
    """
    if maze.grid is None:
        return ""

    # build the walls of the grid
    txt = []
    for row in range(m.grid.shape[0]):
        wall = ''
        for col in range(m.grid.shape[1]):
            me = m.grid[row][col]
            # Connect up?
            if row == 0: up=0
            else: up = m.grid[row-1][col]
            # Connect down?
            if row == row == m.grid.shape[0]-1: dn=0
            else: dn = m.grid[row+1][col]
            # Connect left
            if col == 0: lft=0 
            else: lft = m.grid[row][col-1]
            # Connect right?
            if col == m.grid.shape[1]-1: rgt=0 
            else: rgt = m.grid[row][col+1]

            # Choose shape
            if me and up and dn and lft and rgt: wall = wall + u'\u253C'
            elif me and up and dn and lft and not rgt: wall = wall + u'\u2524'
            elif me and up and dn and not lft and rgt: wall = wall + u'\u251C'
            elif me and up and not dn and lft and rgt: wall = wall + u'\u2534'
            elif me and up and not dn and lft and not rgt: wall = wall + u'\u2518'
            elif me and up and not dn and not lft and rgt: wall = wall + u'\u2514'
            elif me and not up and dn and lft and not rgt: wall = wall + u'\u2510'
            elif me and not up and dn and not lft and rgt: wall = wall + u'\u250C'
            elif me and not up and dn and lft and rgt: wall = wall + u'\u252C'
            elif me and not up and not dn and (lft or rgt): wall = wall + u'\u2500'
            elif me and (up or dn) and not lft and not rgt: wall = wall + u'\u2502'
            elif not me: wall = wall + ' '
            else: wall = wall + '?'
        txt.append(wall)

    # insert the start and end points
    if entrances and maze.start and maze.end:
        r, c = maze.start
        txt[r] = txt[r][:c] + "S" + txt[r][c + 1 :]
        r, c = maze.end
        txt[r] = txt[r][:c] + "E" + txt[r][c + 1 :]

    # if extant, insert the solution path
    if solutions and maze.solutions:
        for r, c in maze.solutions[0]:
            txt[r] = txt[r][:c] + "+" + txt[r][c + 1 :]

    return "\n".join(txt)
