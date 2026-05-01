# 🚀 Trading Bot (Binance Futures Mock Engine)

A Python-based command-line trading bot that simulates order execution for Binance Futures (USDT-M).  
Built with a clean modular architecture, logging system, and extensible design for future real exchange integration.

---

## 📌 Project Overview

This project implements a simplified trading bot that supports:

- Market Orders (BUY / SELL)
- Limit Orders (BUY / SELL)
- CLI-based order execution
- Structured logging of all trading activity
- Modular architecture (client, order service, CLI)

The system is designed so it can be easily upgraded to real Binance API integration by replacing the mock client layer.

---

## 🏗️ Architecture
CLI (cli.py)
↓
Order Service (orders.py)
↓
Client Layer (client.py)
↓
Mock Exchange Engine
↓
Response + Logging System

## 📁 Project Structure
trading_bot/
│
├── cli.py # CLI entry point (argparse)
├── bot/
│ ├── client.py # Mock Binance client (no API required)
│ ├── orders.py # Order execution logic
│ └── logging_config.py # Logging setup using loguru
│
└── trading_bot.log # Auto-generated logs file

---

## ⚙️ Features

### ✔ Order Types
- MARKET order (instant execution simulation)
- LIMIT order (price-based simulated execution)

### ✔ Supported Actions
- BUY / SELL
- Symbol-based trading (e.g., BTCUSDT)
- Quantity-based execution

### ✔ Engineering Features
- Clean modular architecture
- Separation of concerns (CLI / Service / Client)
- Structured logging using loguru
- Error handling and validation
- Easily extendable to real API integration

---

## 🧪 How to Run

### 1️⃣ Clone Repository
```bash
git clone https://github.com/rishika6-star/trading_bot.git
cd trading_bot

📦 Sample Output
📦 ORDER REQUEST SUMMARY
Symbol     : BTCUSDT
Side       : BUY
Order Type : MARKET
Quantity   : 0.01

✅ ORDER EXECUTED SUCCESSFULLY
{
  "orderId": 397075,
  "symbol": "BTCUSDT",
  "side": "BUY",
  "type": "MARKET",
  "status": "FILLED",
  "executedQty": 0.01,
  "avgPrice": "market_price",
  "timestamp": 1777626468732
}


