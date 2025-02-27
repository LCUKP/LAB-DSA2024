"""Labs 07.06 - Seats Number (Bubble Sorting)"""
import json
def seatsNumber(num1, num2) :
    if num1[0] != num2[0] :
        return num1 >= num2
    return int(num1[1:]) >= int(num2[1:])
def bubbleSort(ulist, last) :
    current = 0
    ssorted = False
    comp = 0
    while current <= last and ssorted == False :
        warlker = last
        ssorted = True
        while warlker > current :
            if not seatsNumber(ulist[warlker], ulist[warlker-1]) :
                ssorted = False
                ulist[warlker], ulist[warlker-1] = ulist[warlker-1], ulist[warlker]
            comp += 1
            warlker -= 1
        current += 1
        print(ulist)
    print(f"Comparison times: {comp}")
bubbleSort(json.loads(input()), int(input()))
