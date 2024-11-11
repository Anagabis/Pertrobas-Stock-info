import yfinance as yf

# Função para obter os dados de ações da Petrobras
def get_petrobias_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")  # Últimos dados de 1 dia
    if data.empty:
        return None

    # Extrair algumas informações relevantes
    stock_data = {
        "symbol": ticker,
        "open": data["Open"].iloc[0],
        "close": data["Close"].iloc[0],
        "high": data["High"].iloc[0],
        "low": data["Low"].iloc[0],
        "volume": data["Volume"].iloc[0],
        "date": data.index[0].strftime("%Y-%m-%d %H:%M:%S")
    }
    return stock_data

# Função para exibir as informações no terminal
def display_stock_info(ticker):
    stock_data = get_petrobias_stock_data(ticker)
    if stock_data:
        print(f"\nInformações sobre as ações de {ticker}:")
        print(f"Data: {stock_data['date']}")
        print(f"Abertura: R${stock_data['open']:.2f}")
        print(f"Fechamento: R${stock_data['close']:.2f}")
        print(f"Máxima: R${stock_data['high']:.2f}")
        print(f"Mínima: R${stock_data['low']:.2f}")
        print(f"Volume: {stock_data['volume']}")
    else:
        print(f"\nNão foi possível obter os dados para o ticker {ticker}.")

# Exibir as informações para PETR3 e PETR4
if __name__ == "__main__":
    display_stock_info('PETR3.SA')
    display_stock_info('PETR4.SA')
