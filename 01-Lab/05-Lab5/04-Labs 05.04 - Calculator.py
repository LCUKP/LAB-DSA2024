"""Labs 05.04 - Calculator"""
import time
def calculator(num) :
    """Calculator"""
    if num == 1 :
        return 1
    som = 0
    for i in range(1,num+1) :
        som += len(str(i))+1
    return som
def main() :
    """main"""
    stime = time.time()
    print(calculator(int(input())))
    etime = time.time()
    elapsed = etime - stime
    print("execution time : " + str(elapsed), stime, etime)
main()
