# 📈 StonksCLI
CLI-based trading bot for Binance Testnet with clean Python design, logging, and order management. nA **command-line trading assistant** for interacting with the **Binance Testnet API**.
Built in Python, this bot supports **market, limit, and stop-limit orders**, with a modular structure for easy extension.

---

## 🚀 Features

* Connects to **Binance Testnet** securely with API keys
* Place **MARKET** and **LIMIT** trades
* Supports **STOP-LOSS-LIMIT** orders
* Modular design: easy to extend for **OCO** and **TWAP** trades
* Logs requests, responses, and errors for transparency
* CLI interface with argument parsing for flexibility

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/prakharverma12/StonksCLI.git
cd StonksCLI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

1. **API Key**

   * Register on [Binance Testnet](https://testnet.binance.vision/).
   * Generate API credentials.
   * Save your API key in `secret.txt` as:

     ```ini
     [DEFAULT]
     api_key = YOUR_API_KEY
     ```

2. **Private Key**

   * Save your private key in a file named `Private_key.pem`.
   * Ensure it matches the format expected by the Binance signing process.

---

## ▶️ Usage

Run the bot with desired arguments:

```bash
python main.py --symbol BTCUSDT --side BUY --quantity 0.01 --order_type MARKET
```

### Available Arguments

| Argument          | Type  | Default | Description                                   |
| ----------------- | ----- | ------- | --------------------------------------------- |
| `--symbol`        | str   | None    | Trading pair (e.g., `BTCUSDT`)                |
| `--side`          | str   | BUY     | Order side: `BUY` or `SELL`                   |
| `--quantity`      | float | None    | Order quantity                                |
| `--price`         | float | None    | Limit price (for `LIMIT` / `STOP_LOSS_LIMIT`) |
| `--testnet`       | bool  | True    | Use Testnet (`True`) or Live (`False`)        |
| `--order_type`    | str   | MARKET  | `MARKET`, `LIMIT`, `STOP_LOSS_LIMIT`          |
| `--time_in_force` | str   | GTC     | Time in force: `GTC`, `IOC`, `FOK`            |
| `--stop_price`    | float | None    | Stop price for stop-limit orders              |
| `--trailingDelta` | float | None    | Trailing stop delta                           |

---

## 📊 Examples

* **Market Order (Buy)**

  ```bash
  python main.py --symbol BTCUSDT --side BUY --quantity 0.01 --order_type MARKET
  ```

* **Limit Order (Sell at \$30,000)**

  ```bash
  python main.py --symbol BTCUSDT --side SELL --quantity 0.01 --price 30000 --order_type LIMIT
  ```

* **Stop-Loss Limit Order**

  ```bash
  python main.py --symbol BTCUSDT --side SELL --quantity 0.01 --price 28000 --stop_price 28500 --order_type STOP_LOSS_LIMIT
  ```



---

## 🧑‍💻 Author

**Prakhar Verma**
📌 IIT Kharagpur | AI/ML & Trading Automation Enthusiast

