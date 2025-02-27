"""Labs 07.05 - Seats Number (Selection Sorting)"""
import json
def seatsNumber(num1, num2) :
    if num1[0] != num2[0] :
        return num1 >= num2
    return int(num1[1:]) >= int(num2[1:])
def selectionSort(ulist, last) :
    current = 0
    comp = 0
    while current < last :
        smallest = current
        walker = current + 1
        while walker <= last :
            if not seatsNumber(ulist[walker], ulist[smallest]) :
                smallest = walker
            walker += 1
            comp += 1
        ulist[current], ulist[smallest] = ulist[smallest], ulist[current]
        current += 1
        print(ulist)
    print(f"Comparison times: {comp}")

selectionSort(json.loads(input()), int(input()))
