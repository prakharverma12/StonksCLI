from util.logging import logger
from util.parser import parsing
from util.validator import validation
from util.trader import execute_trade , execute_stoplimit_trade
import configparser
from cryptography.hazmat.primitives.serialization import load_pem_private_key # type: ignore

def main():
    args = parsing()
    validation(args)
    config = configparser.ConfigParser()
    config.read("secret.txt")
    api_key = config["DEFAULT"]["api_key"]
    with open("Private_key.pem", "rb") as f:
        private_key = load_pem_private_key(data=f.read(), password=None)
    print(private_key)
    match args.order_type:
        case "MARKET" | "LIMIT":
            response = execute_trade(args, api_key, private_key)
        case "STOP_LOSS_LIMIT":
            response = execute_stoplimit_trade(args, api_key, private_key)
        case "OCO":
            print("OCO trade type is not yet implemented.")
        case "TWAP":
            print("TWAP trade type is not yet implemented.")
    logger(args, response)


if __name__ == "__main__":
    main()