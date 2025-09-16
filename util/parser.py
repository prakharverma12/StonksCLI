import argparse
def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument('--symbol', type=str, help='[STRING] : The symbol of the stock you wish to trade')
    parser.add_argument('--side', type=str,default = 'BUY', help='[STRING] : The action to perform (buy/sell)')
    parser.add_argument('--quantity', type=float, help='[FLOAT] :The quantity of stocks to trade')
    parser.add_argument('--price', type=float, help='[FLOAT] :The price at which to trade')
    parser.add_argument('--testnet', type=bool, default=True, help='[BOOL] :Use testnet or live trading. True if testnet, False if live trading.')
    parser.add_argument('--order_type', type=str, default='MARKET', help='[MARKET/LIMIT/STOP_LOSS_LIMIT] :Type of order (market/limit/stop_loss_limit)')
    parser.add_argument('--time_in_force', type=str, default='GTC', help='[GTC/IOC/FOK] :Time in force for the order (gtc/ioc/fok)')
    parser.add_argument('--stop_price', type=float, help='[FLOAT] :The stop price for stop-limit orders')
    parser.add_argument('--trailingDelta', type=float, help='[FLOAT] :The limit price for stop-limit orders')
    args = parser.parse_args()
    return args