#!/usr/bin/env python3
"""生成简单的.mrs/geosite文件"""

domains = [
    "binance.com",
    "coinbase.com", 
    "okx.com",
    "kraken.com",
    "huobi.com",
    "bybit.com",
    "gate.io",
    "kucoin.com",
    "bitfinex.com",
    "bittrex.com",
    "gemini.com",
    "crypto.com",
    "bitget.com",
    "mexc.com",
    "metamask.io",
    "trustwallet.com",
    "rainbow.me",
    "phantom.app",
    "solflare.com",
    "uniswap.org",
    "pancakeswap.finance",
    "coinmarketcap.com",
    "coingecko.com",
    "tradingview.com",
    "api.binance.com",
    "api.okx.com",
    "ws.binance.com",
    "etherscan.io",
    "bscscan.com",
]

output = """! name: cryptocurrency
! description: Cryptocurrency websites
"""

for d in domains:
    output += f"domain:{d}\n"

with open("crypto_geosite.txt", "w") as f:
    f.write(output)

print(f"生成 {len(domains)} 个域名到 crypto_geosite.txt")
