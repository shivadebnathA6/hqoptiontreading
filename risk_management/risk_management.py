
def calculate_stop_loss(entry_price, risk_percentage):
    stop_loss = entry_price * (1 - risk_percentage / 100)
    return stop_loss

def calculate_trailing_stop_loss(current_price, highest_price, trailing_percentage):
    trailing_stop_loss = highest_price * (1 - trailing_percentage / 100)
    return trailing_stop_loss

def calculate_profit_target(entry_price, reward_percentage):
    profit_target = entry_price * (1 + reward_percentage / 100)
    return profit_target

if __name__ == "__main__":
    # Example usage
    entry_price = 1000
    risk_percentage = 2
    trailing_percentage = 1
    reward_percentage = 5

    stop_loss = calculate_stop_loss(entry_price, risk_percentage)
    trailing_stop_loss = calculate_trailing_stop_loss(1050, 1100, trailing_percentage)
    profit_target = calculate_profit_target(entry_price, reward_percentage)

    print(f"Stop Loss: {stop_loss}")
    print(f"Trailing Stop Loss: {trailing_stop_loss}")
    print(f"Profit Target: {profit_target}")
