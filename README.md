# 加密货币访问优化规则

## 用途
优化访问加密货币交易所、钱包、数据网站的线路，提升访问速度。

## 文件说明

| 文件 | 说明 | 用途 |
|------|------|------|
| dlc.dat | Geosite二进制 | 通用 |
| proxy.yaml | Clash规则 | Clash/SingBox |
| sing-box | 工具 | 生成mrs |

## 生成 .mrs

1. 下载 geosite.db:
```
wget https://github.com/SagerNet/sing-box-geosite/releases/download/20240302/geosite.db
```

2. 生成 mrs:
```
./sing-box geosite export cryptocurrency -f geosite.db -o crypto.mrs
```

## 包含内容
- 交易所: Binance, Coinbase, OKX等
- 钱包: MetaMask, Trust Wallet等
- 数据网站: CoinMarketCap, CoinGecko等

## 更新
- 2026-03-04: 初始版本
