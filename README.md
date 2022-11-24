# Uniswap Balance Checker

Pull the Token A and B of your pool and check if one of them is below 10% of your total token balance.

Currently, this code only works for the StakeWise sETH2/ETH pool.

This code utilizes Alchemy, which you can get a free account for personal use here https://www.alchemy.com/.
You will need to put this into the `uniswap_lp_balance.py` on line 22 and you will need to update your `POOL_ID` on line 96.

# Future improvements
1. Implement functions into the JavaScript code, so you don't have to edit the code with your `alchemy_id` and `pool_id`.
2. Implement an alert system (i.e. Telegram).
