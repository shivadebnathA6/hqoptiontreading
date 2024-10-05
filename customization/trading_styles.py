
class TradingStyle:
    def __init__(self, style, risk_appetite):
        self.style = style
        self.risk_appetite = risk_appetite

    def get_trading_style(self):
        return self.style

    def get_risk_appetite(self):
        return self.risk_appetite

    def set_trading_style(self, style):
        self.style = style

    def set_risk_appetite(self, risk_appetite):
        self.risk_appetite = risk_appetite

if __name__ == "__main__":
    # Example usage
    day_trading = TradingStyle('Day Trading', 'High')
    swing_trading = TradingStyle('Swing Trading', 'Medium')
    positional_trading = TradingStyle('Positional Trading', 'Low')

    print(f"Day Trading Style: {day_trading.get_trading_style()}, Risk Appetite: {day_trading.get_risk_appetite()}")
    print(f"Swing Trading Style: {swing_trading.get_trading_style()}, Risk Appetite: {swing_trading.get_risk_appetite()}")
    print(f"Positional Trading Style: {positional_trading.get_trading_style()}, Risk Appetite: {positional_trading.get_risk_appetite()}")
