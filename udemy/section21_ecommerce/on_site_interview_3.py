# Given two rectangles, determine if they overlap. The rectangles are defined as a
# Dictionary, for example:
# r1 = {'x': 2, 'y': 4, 'w': 5, 'h': 12}

def calc_overlap(coor1, dim1, coor2, dim2):
    
    greater = max(coor1, coor2)
    lower = min(coor1+dim1, coor2+dim2)

    if greater >= lower:
        return (None, None)
    
    overlap = lower - greater

    return (greater, overlap)

def calc_rect_overlap(rect1, rect2):
    x_overlap, w_overlap = calc_overlap(rect1['x'], rect1['w'], rect2['x'], rect2['w'])
    y_overlap, h_overlap = calc_overlap(rect1['y'], rect1['h'], rect2['y'], rect2['h'])

    if not w_overlap or not h_overlap:
        return None
    
    return {'x': x_overlap, 'y': y_overlap, 'w': w_overlap, 'h': h_overlap}

