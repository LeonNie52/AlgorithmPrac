import sys
if __name__ == '__main__':
    comd, consumer = sys.stdin.readline().strip().split()

    line = sys.stdin.readline().strip()
    values = map(int, line.split())

    price = min(values)
    profit = 0
    while True:
        numbers = int(comd)
        tmp_profit = 0
        for bid in values:
            if bid >= price and numbers > 0:
                tmp_profit = tmp_profit+price
                numbers = numbers-1
        if tmp_profit > profit:
            
            profit=tmp_profit
            
            price = price+1
            continue
        else:
            print price-1
            break

