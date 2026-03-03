# 加密货币访问优化规则

## 用途
优化访问加密货币交易所、钱包、数据网站的线路，提升访问速度。

## 生成文件

| 文件 | 说明 |
|------|------|
| crypto.mrs | 二进制规则文件 |
| cryptocurrency.txt | Geosite纯文本格式 |
| dlc.dat | Geosite二进制格式 |
| rules.yaml | Clash/SingBox规则 |
| domains.txt | 纯域名列表 |

## 使用方法

### Clash / SingBox
直接使用 `rules.yaml`

### RouterOS
使用 `crypto.mrs` 或 `dlc.dat`

### 自行编译
```bash
# 安装工具
go install github.com/v2fly/domain-list-community@latest

# 编译
domain-list-community -exportlists=cryptocurrency -outputdir=.
```

## 包含内容

- 交易所: Binance, Coinbase, OKX, Kraken等
- 钱包: MetaMask, Trust Wallet等
- 数据网站: CoinMarketCap, CoinGecko等
- API: 各大交易所API

## 更新
- 2026-03-04: 使用 domain-list-community 生成
