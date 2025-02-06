"""Labs 05.03 - isIntersect(A, B, C)"""
import json, time
def isIntersect(a, b, c) :
    """isIntersect"""
    for i in a :
        if i in b and i in c :
            return True
    return False

def main() :
    stime = time.time()
    print(isIntersect(json.loads(input()), json.loads(input()), json.loads(input())))
    etime = time.time()
    elapsed = etime - stime
    print("execution time : " + str(elapsed), stime, etime)
main()
