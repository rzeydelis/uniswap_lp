# Uniswap Balance Checker

Pull the balance of Token A and Token B in your Uniswap V3 Liquidity Pool and check if one of them is below 10% of your total token balance.

Currently, this code only works for the StakeWise sETH2/ETH pool.

This code utilizes Alchemy, which you can get a free account for personal use here https://www.alchemy.com/.

# Running

Clone the project:

`git clone https://github.com/rzeydelis/uniswap_lp.git`

Go to the project folder:

`cd uniswap_lp`

## Running main app

`python3 main.py`


## Find LP Balance

`node uniswap_lp_balance.js`

You may need to install some packages.

# Future improvements
1. Implement a way to configure your alchemy_id and pool_id, so you don't have to enter it everytime you run the code.
2. Implement an alert system (i.e. Telegram).
