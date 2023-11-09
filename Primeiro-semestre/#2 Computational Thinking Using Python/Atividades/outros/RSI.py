import pandas as pd
from binance.client import Client
from ta.momentum import RSIIndicator

# Substitua 'your_api_key' e 'your_api_secret' pelas suas chaves da API Binance
client = Client('1GHoM3qOfUhZGYqfQ0BRSJLTnelQL3ecc2PjhFYU37bRkIo3WXTWHXH1fprLTMmF', '5tAgZlM60wdmiUV1uqlN6ELNBkmhe1E6aJH4eaA7BnHU8JB1kt9FqmgALi3Zupee')


def calculate_rsi(data, period):
    rsi = RSIIndicator(data['close'], period)
    return rsi.rsi()


def get_crypto_data(symbol, interval):
    klines = client.get_klines(symbol=symbol, interval=interval)
    data = pd.DataFrame(klines,
                        columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av',
                                 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'])
    data['close'] = pd.to_numeric(data['close'])
    return data


def main():
    cryptos = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'ADAUSDT', 'XRPUSDT', 'SOLUSDT', 'DOTUSDT', 'DOGEUSDT', 'AVAXUSDT',
               'LUNAUSDT']
    print("Selecione uma das seguintes criptomoedas para análise:")
    for i, crypto in enumerate(cryptos):
        print(f"{i + 1}. {crypto}")

    choice = int(input("Digite o número correspondente à sua escolha: ")) - 1
    symbol = cryptos[choice]

    intervals = ['1d', '4h', '1h', '30m']

    for interval in intervals:
        data = get_crypto_data(symbol, interval)
        rsi = calculate_rsi(data, 14).iloc[-1]
        print(f"RSI {interval} para {symbol}: {rsi}")

    another_choice = input("Deseja selecionar outra cripto? (s/n): ")
    if another_choice.lower() == "s":
        main()


if __name__ == "__main__":
    main()
