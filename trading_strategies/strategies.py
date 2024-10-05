
def suggest_straddle(symbol, current_price, strike_price, expiry_date):
    return {
        'strategy': 'Straddle',
        'symbol': symbol,
        'current_price': current_price,
        'strike_price': strike_price,
        'expiry_date': expiry_date,
        'entry_point': 'Buy Call and Put at strike price',
        'exit_point': 'Close positions before expiry'
    }

def suggest_strangle(symbol, current_price, lower_strike_price, upper_strike_price, expiry_date):
    return {
        'strategy': 'Strangle',
        'symbol': symbol,
        'current_price': current_price,
        'lower_strike_price': lower_strike_price,
        'upper_strike_price': upper_strike_price,
        'expiry_date': expiry_date,
        'entry_point': 'Buy Put at lower strike price and Call at upper strike price',
        'exit_point': 'Close positions before expiry'
    }

def suggest_iron_condor(symbol, current_price, lower_strike_price, upper_strike_price, expiry_date):
    return {
        'strategy': 'Iron Condor',
        'symbol': symbol,
        'current_price': current_price,
        'lower_strike_price': lower_strike_price,
        'upper_strike_price': upper_strike_price,
        'expiry_date': expiry_date,
        'entry_point': 'Sell Put at lower strike price, Buy Put at even lower strike price, Sell Call at upper strike price, Buy Call at even higher strike price',
        'exit_point': 'Close positions before expiry'
    }

if __name__ == "__main__":
    # Example usage
    straddle = suggest_straddle('RELIANCE', 2500, 2500, '2023-12-31')
    strangle = suggest_strangle('RELIANCE', 2500, 2400, 2600, '2023-12-31')
    iron_condor = suggest_iron_condor('RELIANCE', 2500, 2400, 2600, '2023-12-31')

    print(straddle)
    print(strangle)
    print(iron_condor)
