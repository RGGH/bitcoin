# Bitcoin

## Script to set up bitcoin core
run `btc_test.sh`

###### Change { version }  to suit
---
#### Create a wallet

    bitcoin-cli -regtest createwallet my_wallet true
    bitcoin-cli -regtest createwallet moo
    bitcoin-cli -regtest -generate -rpcwallet="moo"
