import os
import re


def token_bal_check():
    os.system("node uniswap_lp_balance.js") # run js script in terminal
    file = open('logresults.txt', mode = 'r', encoding = 'utf-8-sig')
    lines = file.readlines()
    file.close()

    seth = 0
    eth = 0
    count = 0
    for line in lines:
        count+=1
        if count <= 2:
            continue

        if count == 3:
            line = line.split(',')
            line = [i.strip() for i in line]
            eth = float(str(line).rsplit(':', 1)[1][:-2].strip())

        if count == 4:
            line = line.split(',')
            line = [i.strip() for i in line]
            seth = float(str(line).rsplit(':', 1)[1][:-2].strip())  

    min_req_token_bal = (seth + eth) * .1
    if seth < min_req_token_bal: # tokenBal shouldn't be under 10% of the entire LP amount
        print("sETH2 has a low balance.")
    elif eth < min_req_token_bal:
        print("ETH has a low balance.")
    else:
        print("sETH2 & ETH balances are not in danger zone.")
