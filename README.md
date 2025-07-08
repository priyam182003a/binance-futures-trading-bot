# 🚀 Binance Futures Testnet Trading Bot

This is a **simplified crypto trading bot** built as part of an application task for the **Junior Python Developer – Crypto Trading Bot** position at Bajarangs & PrimeTrade.

It connects to the **Binance Futures Testnet** to safely simulate **Market**, **Limit**, and **Stop-Limit** orders.

---

## ✅ Features

- 📌 **Market Orders** — Place real or simulated BUY/SELL market orders
- 📌 **Limit Orders** — Place real or simulated BUY/SELL limit orders
- 📌 **Stop-Limit Orders** — *Bonus:* Supports third order type
- 📌 **Testnet Base URL** — Uses `https://testnet.binancefuture.com` for safe testing
- 📌 **Official `python-binance` Library** — Interacts with Binance REST API
- 📌 **Input Validation** — Takes input via **enhanced CLI** with **Questionary**
- 📌 **Logging** — Logs API requests, responses, and fallback DRY-RUNs to `futures_bot.log`
- 📌 **KYC-Safe Dry-Run** — Runs safely without live credentials for testing
- 📌 **Bonus UI** — CLI upgraded with **Questionary** for a user-friendly prompt experience

---

## ⚙️ Requirements

- Python 3.8+
- `python-binance`
- `python-dotenv`
- `questionary`

Install all dependencies:

```bash
pip install -r requirements.txt
