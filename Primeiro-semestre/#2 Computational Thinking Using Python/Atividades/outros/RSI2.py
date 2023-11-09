import ccxt
import pandas as pd
import ta
from ta.momentum import RSI
import time

# Função para obter dados de criptomoedas da Binance
def get_binance_data(symbol, timeframe):
    exchange = ccxt.binance()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# Função para calcular o RSI
def calculate_rsi(data, period):
    rsi = RSI(data['close'], window=period)
    return rsi

# Função para mostrar os valores do RSI
def show_rsi_data(symbol):
    print(f"Analisando a criptomoeda {symbol}...")
    for timeframe in ['1d', '4h', '1h', '30m']:
        data = get_binance_data(symbol, timeframe)
        rsi = calculate_rsi(data, 14)
        print(f"RSI ({timeframe}): {rsi.iloc[-1]:.2f}")

# Função principal
def main():
    while True:
        print("Selecione uma criptomoeda para análise:")
        print("1. Bitcoin (BTC)")
        print("2. Ethereum (ETH)")
        # Adicione outras criptomoedas aqui

        choice = input("Digite o número da criptomoeda desejada (ou 'q' para sair): ")
        if choice == 'q':
            break
        elif choice == '1':
            symbol = 'BTC/USDT'
            show_rsi_data(symbol)
        elif choice == '2':
            symbol = 'ETH/USDT'
            show_rsi_data(symbol)
        # Adicione outras opções para diferentes criptomoedas

if __name__ == "__main__":
    main()
