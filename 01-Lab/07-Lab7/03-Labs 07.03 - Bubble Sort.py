"""Labs 07.03 - Bubble Sort"""
import json
def bubbleSort(ulist, last) :
    current = 0
    ssorted = False
    comp = 0
    while current <= last and ssorted == False :
        warlker = last
        ssorted = True
        while warlker > current :
            if ulist[warlker] < ulist[warlker-1] :
                ssorted = False
                ulist[warlker], ulist[warlker-1] = ulist[warlker-1], ulist[warlker]
            comp += 1
            warlker -= 1
        current += 1
        print(ulist)
    print(f"Comparison times: {comp}")
bubbleSort(json.loads(input()), int(input()))
