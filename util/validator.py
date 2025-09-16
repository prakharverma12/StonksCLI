
def validation(args):
    match args.order_type:
        case 'MARKET' | 'LIMIT':
            if args.side not in ['BUY', 'SELL']:
                raise ValueError("Side must be 'buy' or 'sell'")
            if args.quantity <= 0:
                raise ValueError("Quantity must be a positive number")
            if args.order_type not in ['MARKET', 'LIMIT']:
                raise ValueError("Order type must be 'MARKET' or 'LIMIT'")
            if args.order_type == 'LIMIT' and args.price is None:
                raise ValueError("Price must be specified for limit orders")
        case 'STOP_LOSS_LIMIT':
            if args.side not in ['BUY', 'SELL']:
                raise ValueError("Side must be 'buy' or 'sell'")
            if args.quantity <= 0:  
                raise ValueError("Quantity must be positive")
            if args.stop_price is None and args.trailingDelta is None:
                raise ValueError("Either stop_price or trailingDelta must be specified for STOP_LOSS_LIMIT orders")
            if args.price is None:
                raise ValueError("Price must be specified for STOP_LOSS_LIMIT orders")
        case 'OCO':
            if args.side not in ['BUY', 'SELL']:
                raise ValueError("Side must be 'buy' or 'sell'")
            if args.quantity <= 0:
                raise ValueError("Quantity must be positive")
            if args.abovetype not in ['LIMIT', 'STOP_LOSS_LIMIT']:
                raise ValueError("abovetype must be 'LIMIT' or 'STOP_LOSS_LIMIT'")
            if args.belowtype not in ['LIMIT', 'STOP_LOSS_LIMIT']:
                raise ValueError("belowtype must be 'LIMIT' or 'STOP_LOSS_LIMIT'")
            if args.abovetype == 'LIMIT' and args.aboveprice is None:
                raise ValueError("aboveprice must be specified for abovetype LIMIT")
            if args.abovetype == 'STOP_LOSS_LIMIT' and (args.aboveStopPrice is None or args.aboveprice is None):
                raise ValueError("Both aboveStopPrice and aboveprice must be specified for abovetype STOP_LOSS_LIMIT")
            if args.belowtype == 'LIMIT' and args.belowprice is None:
                raise ValueError("belowprice must be specified for belowtype LIMIT")
            if args.belowtype == 'STOP_LOSS_LIMIT' and (args.belowStopPrice is None or args.belowprice is None):
                raise ValueError("Both belowStopPrice and belowprice must be specified for belowtype STOP_LOSS_LIMIT")    
    return True
    
