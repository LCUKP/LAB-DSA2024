"""Lab 01.02 - Max…Min…Avg"""
import json
def most() :
    """Lab 01.02 - Max…Min…Avg"""
    my_list = json.loads(input())
    mak = my_list[0]
    noi = my_list[0]
    som = my_list[0]
    count = 1
    for i in my_list[1:] :
        if i > mak :
            mak = i
        if i < noi :
            noi = i
        som += i
        count += 1
    avg = f"{(som/count):.2f}"
    noi = f"{noi:.2f}".rstrip("0").rstrip(".")
    mak = f"{mak:.2f}".rstrip("0").rstrip(".")
    my_tuple = f"{mak}, {noi}, {float(avg)}"
    print("("+my_tuple+")")
most()
