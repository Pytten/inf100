
def clip_grass(heights, max_height):
    heights == []
    i = 0
    n = len(heights)
    for i in range(n):
        if heights[i] > max_height:
            heights[i] = max_height
            i +=1



