import sys
import math
import copy
import itertools


def pro_out(n, pro_list):
    if n != len(pro_list):
        return 

    req_num = int(math.ceil(n*0.6))

    result = 0

    for i in range(req_num, n+1):
        iter_ = itertools.combinations(pro_list, i)

        for index in iter_:
            iter_not = copy.copy(pro_list)
            tmp_pro = 1

            for pro in index:
                if pro in iter_not:
                    iter_not.remove(pro)

            for pro in index:
                tmp_pro = tmp_pro*(pro/100.0)

            for pro in iter_not:
                tmp_pro = tmp_pro*(1.0-pro/100.0)
            print index
            print iter_not
            print tmp_pro

            result = result+tmp_pro
    print "%.5f" % result

if __name__ == '__main__':

    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    pro_list = map(int, line.split())

    pro_out(n, pro_list)
