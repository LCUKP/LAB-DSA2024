"""Labs 07.04 - Seats Number (Insertion Sorting)"""
import json
def seatsNumber(num1, num2) :
    if num1[0] != num2[0] :
        return num1 >= num2
    return int(num1[1:]) >= int(num2[1:])
def insertion_sort(ulist, last) :
    current = 1
    comp = 0
    while current <= last :
        hold = ulist[current]
        walker = current - 1
        while walker >= 0 and not seatsNumber(hold, ulist[walker]) :
            ulist[walker + 1] = ulist[walker]
            walker -= 1
            comp += 1
        if walker >= 0 and hold[0] >= ulist[walker][0] :
            comp += 1
        ulist[walker + 1] = hold
        current += 1
        print(ulist)
    print(f"Comparison times: {comp}")
insertion_sort(json.loads(input()), int(input()))
