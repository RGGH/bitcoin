# Bitcoin

## Script to set up bitcoin core
###### download btc_test.sh
###### Change { version }  to suit
run `btc_test.sh`
---
##### Create a wallet

    bitcoin-cli -regtest createwallet my_wallet true
    bitcoin-cli -regtest createwallet moo
    bitcoin-cli -regtest -generate -rpcwallet="moo"
