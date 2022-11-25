import os
import re


def token_bal_check():
    os.system("node uniswap_lp_balance.js") # run js script in terminal
    file = open('logresults.txt', mode = 'r', encoding = 'utf-8-sig')
    lines = file.readlines()
    file.close()

    tokenA = 0
    tokenB = 0
    count = 0
    for line in lines:
        count+=1
        if count <= 2:
            continue

        if count == 3:
            line = line.split(',')
            line = [i.strip() for i in line]
            # tokenA = (["'])(?:(?=(\\?))\2.)*?\1
            tokenA = float(str(line).rsplit(':', 1)[1][:-2].strip())
            # print("tokenA:", tokenA)

        if count == 4:
            line = line.split(',')
            line = [i.strip() for i in line]
            # tokenA = (["'])(?:(?=(\\?))\2.)*?\1
            tokenB = float(str(line).rsplit(':', 1)[1][:-2].strip())
            # print("tokenB:", tokenB)        

        # print(line)
        # count+=1

    min_req_token_bal = (tokenA + tokenB) * .1
    if tokenA < min_req_token_bal: # tokenBal shouldn't be under 10% of the entire LP amount
        print("Token 1 has a low balance.")
    elif tokenB < min_req_token_bal:
        print("Token 2 has a low balance.")
    else:
        print("Token 1 & 2 balances are not in danger zone.")