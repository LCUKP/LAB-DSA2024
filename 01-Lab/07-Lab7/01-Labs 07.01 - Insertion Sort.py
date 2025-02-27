"""Labs 07.01 - Insertion Sort"""
import json
def insertion_sort(ulist, last) :
    current = 1
    comp = 0
    while current <= last :
        hold = ulist[current]
        walker = current - 1
        while walker >= 0 and hold < ulist[walker] :
            ulist[walker + 1] = ulist[walker]
            walker -= 1
            comp += 1
        if walker >= 0 and hold > ulist[walker] :
            comp += 1
        ulist[walker + 1] = hold
        current += 1
        print(ulist)
    print(f"Comparison times: {comp}")
insertion_sort(json.loads(input()), int(input()))
