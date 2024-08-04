def find_best_photo_side(n, heights):
    # Check from the left
    visible_from_left = True
    max_height = heights[0]
    for i in range(1, n):
        if heights[i] < max_height:
            visible_from_left = False
            break
        max_height = heights[i]
    
    # Check from the right
    visible_from_right = True
    max_height = heights[-1]
    for i in range(n-2, -1, -1):
        if heights[i] < max_height:
            visible_from_right = False
            break
        max_height = heights[i]
    
    if visible_from_left:
        return "L"
    elif visible_from_right:
        return "R"
    else:
        return "N"

# Input handling
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    heights = list(map(int, input().strip().split()))
    print(find_best_photo_side(n, heights))
