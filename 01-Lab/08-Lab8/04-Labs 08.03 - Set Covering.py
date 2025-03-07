"""Labs 08.03 - Set Covering"""
def main():
    import json
    city = set(json.loads(input()))
    wireless = [json.loads(input()) for _ in range(int(input()))]
    selected = []
    while city:
        index = 0
        tmpMax = 0
        tmp = None
        while index < len(wireless):
            if len(set(wireless[index]["Cities"]).intersection(city)) > tmpMax:
                tmp = wireless[index]
                tmpMax = len(set(wireless[index]["Cities"]).intersection(city))
            index += 1
        if tmp:
            selected.append(tmp["Name"])
            wireless.remove(tmp)
            city = city - set(tmp["Cities"])
        else:
            break
    print(sorted(selected))

main()