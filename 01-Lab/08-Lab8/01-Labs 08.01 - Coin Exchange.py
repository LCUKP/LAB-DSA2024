"""Labs 08.01 - Coin Exchange"""
def coinExchange(amount, coins) :
    count = 0
    print("Coin exchange result:")
    for k,v in coins.items() :
        tmp = 0
        if (amount // k) < v :
            count += amount // k
            tmp = amount // k
            amount -= k*(amount // k)
        else :
            count += v
            tmp = v
            amount -= k*v
        print(f"  {k} baht = {tmp} coins")
    print(f"Number of coins: {count}")

def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def main():
    import json
    sumc = 0
    amount = int(input())
    data = convert_key(json.loads(input()))
    for k,v in data.items() :
        sumc += k*v
    print(f"Amount: {amount}")
    if sumc < amount :
       print("Coins are not enough.")
       return
    coinExchange(amount, data)
main()
