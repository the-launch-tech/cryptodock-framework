# CryptoDock Python Strategy Framework

CryptoDock Strategy Framework is a Python package used alongside the CryptoDock desktop iOS app, the CryptoDock remote API, and the CryptoDock Suite.

When bootstrapping a trading strategy in the CryptoDock desktop app the Framework is copied into the target local directory for your use in strategy development. It communicates with the remote API to pull historic and current trading data from multiple exchanges, and communicates with the Desktop app via websocket client as a NodeJS child process.

Additionally the Strategy Framework provides a Strategy Wrapper and Backtest Layer that is managed from the CryptoDock desktop interface.

Using this method we can normalize the structures of data from across the exchanges, run comprehensive and adaptable backtest, and provide a semantic interface, allowing for a much more efficient strategy development and research process.

## Installation

To install the SDK run: `pip install cryptodock-framework`, or `pip install cryptodock-framework==0.0.1`

This package will not work unless used alongside CryptoDock.

## Usage

### Import Package(s)

- `from cryptodock import CryptoDockSdk`
- `from cryptodock import CryptoDockApi, CryptoDockStrategy, CryptoDockBacktest`

### Initialize SDK

- `class Strategy(CryptoDockStrategy)`
- `class PortfolioManager(CryptoDockPortfolioManager)`
- `class DataHandler(CryptoDockDataHandler)`
- `class TradeExecutor(CryptoDockTradeExecutor)`
- `class FillStorage(CryptoDockFillStorage)`
- `backtest = CryptoDockBacktest(Strategy, args)`

## History

- Initial Release

## Credits

- Company: ©2019 The Launch
- Author: Daniel Griffiths
- Role: Founder and Engineer
- Project: ©2020 CryptoDock

## License

MIT Licence ©2020 Daniel Griffiths
