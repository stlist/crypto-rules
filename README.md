# 加密货币访问优化规则

## 用途
优化访问加密货币交易所、钱包、数据网站的线路，提升访问速度。

## 包含内容

### 交易所
- Binance, Coinbase, OKX, Kraken, Huobi, Bybit, Gate, KuCoin等

### 钱包
- MetaMask, Trust Wallet, Phantom, Solflare, Uniswap等

### 数据网站
- CoinMarketCap, CoinGecko, TradingView等

### API
- 各大交易所API域名

## 格式

### Clash / SingBox 规则
`rules.yaml` - 可直接用于 Clash / SingBox

### 域名列表
`domains.txt` - 纯域名列表

## 生成 .mrs 文件

需要安装 MetaRules 工具：
```bash
# 安装 Go
sudo apt install golang

# 安装 metrules
go install github.com/ko1nksm/metrules@latest

# 编译
metrules -i rules.yaml -o telegram.mrs
```

## 更新日志
- 2026-03-03: 初始版本
