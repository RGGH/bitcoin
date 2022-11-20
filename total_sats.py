""" calculate the total amount 
    of bitcoin that will be issued """

# Original block reward for miners was 50 BTC
start_block_reward = 50

""" 210000 is around every 4 years with 
    approx 10 minute block interval """

reward_interval = 210000

def max_money():
    # 50 BTC = 50 0000 0000 Satoshis
    current_reward = 50 * 10**8
    total = 0
    while current_reward > 0:
        total += reward_interval * current_reward
        current_reward /= 2
        print(str(current_reward))
    return total

print (f"total sats ever mined: {max_money()}")
