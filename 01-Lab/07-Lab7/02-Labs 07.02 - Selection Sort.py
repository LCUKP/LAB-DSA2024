"""Labs 07.02 - Selection Sort"""
import json
def selectionSort(ulist, last) :
    current = 0
    comp = 0
    while current < last :
        smallest = current
        walker = current + 1
        while walker <= last :
            if ulist[walker] < ulist[smallest] :
                smallest = walker
            walker += 1
            comp += 1
        ulist[current], ulist[smallest] = ulist[smallest], ulist[current]
        current += 1
        print(ulist)
    print(f"Comparison times: {comp}")

selectionSort(json.loads(input()), int(input()))
