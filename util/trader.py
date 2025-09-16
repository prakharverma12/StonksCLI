import time
import requests
import base64

def execute_trade(args, API_KEY, private_key):
    params = {
    'symbol':args.symbol,
    'side':args.side.upper(),
    'quantity':args.quantity,
    'type':args.order_type.upper(),
    }
    print("params :",params)

    # Timestamp the request
    timestamp = int(time.time() * 1000) # UNIX timestamp in milliseconds
    params['timestamp'] = timestamp

    # Sign the request
    payload = '&'.join([f'{param}={value}' for param, value in params.items()])
    signature =  base64.b64encode(private_key.sign(payload.encode('ASCII')))

    params['signature'] = signature

    # Send the request
    headers = {
        'X-MBX-APIKEY': API_KEY,
    }
    response = requests.post(
        'https://testnet.binance.vision/api/v3/order',
        headers=headers,
        data=params,
    )
    print(response.json())
    return response.json()

def execute_stoplimit_trade(args, API_KEY, private_key):
    params = {
    'symbol':args.symbol,
    'side':args.side.upper(),
    'quantity':args.quantity,
    'stopPrice':args.stop_price,
    'price':args.price,
    'type':args.order_type.upper(),
    'timeInForce':args.time_in_force.upper()
    }
    print("params :",params)

    # Timestamp the request
    timestamp = int(time.time() * 1000) # UNIX timestamp in milliseconds
    params['timestamp'] = timestamp

    # Sign the request
    payload = '&'.join([f'{param}={value}' for param, value in params.items()])
    signature =  base64.b64encode(private_key.sign(payload.encode('ASCII')))

    params['signature'] = signature

    # Send the request
    headers = {
        'X-MBX-APIKEY': API_KEY,
    }
    response = requests.post(
        'https://testnet.binance.vision/api/v3/order',
        headers=headers,
        data=params,
    )
    print(response.json())
    return response.json()

def execute_oco_trade(args, API_KEY, private_key):
    params = {
        'symbol': args.symbol,
        'side': args.side.upper(),
        'quantity': args.quantity,
        'abovetype':args.abovetype.upper(),
        'aboveprice':args.aboveprice,
        'aboveStopPrice':args.aboveStopPrice,
        'belowtype':args.belowtype.upper(),
        'belowprice':args.belowprice,
        'belowStopPrice':args.belowStopPrice,
        'type': 'OCO'
    }
    print("params :", params)

    # Timestamp the request
    timestamp = int(time.time() * 1000)  # UNIX timestamp in milliseconds
    params['timestamp'] = timestamp

    # Sign the request
    payload = '&'.join([f'{param}={value}' for param, value in params.items()])
    signature = base64.b64encode(private_key.sign(payload.encode('ASCII')))

    params['signature'] = signature

    # Send the request
    headers = {
        'X-MBX-APIKEY': API_KEY,
    }
    response = requests.post(
        'https://testnet.binance.vision/api/v3/order',
        headers=headers,
        data=params,
    )
    print(response.json())
    return response.json()