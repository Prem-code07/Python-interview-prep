def rotateString(s, goal):
    return len(s) == len(goal) and goal in (s + s)
rotateString("hello")