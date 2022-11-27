# Uniswap Balance Checker

Pull the balance of Token A and Token B in your Uniswap V3 Liquidity Pool and check if one of them is below 10% of your total token balance.

Currently, this code only works for the StakeWise sETH2/ETH pool.

This code utilizes Alchemy, which you can get a free account for personal use here https://www.alchemy.com/.

# Running

Clone the project:

`git clone https://github.com/rzeydelis/uniswap_lp.git`

Go to the project folder:

`cd uniswap_lp`

Set your environment ALCHEMY_ID variable to be the HTTPS link:
`export ALCHEMY_ID="<<<Alchemy HTTP Link>>>"`

Then run:
`python3 main.py`

# Future improvements
1. Implement a way to configure your pool_id, so you don't have to enter it everytime you run the code.
2. Implement an alert system (i.e. Telegram, SMTP, etc). This would require setting up a Flask app and some AWS services. If someone is willing to sponsor the services, I can set them up.
