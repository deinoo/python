# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    arrayOut = []
    zerocount = 0
    for item in array:
        if item == 0 and isinstance(item, (int, float)) and not isinstance(item, bool):
            zerocount += 1
        else:
            arrayOut.append(item)
    arrayOut.extend([0] * zerocount)
    return arrayOut