import random
import time

# Mock stock data (normally fetched via API)
STOCK_DATA = {
    "AAPL": {"price": 175.0, "pe_ratio": 28, "sentiment": 0.8},
    "TSLA": {"price": 250.0, "pe_ratio": 50, "sentiment": 0.6},
    "GOOGL": {"price": 2900.0, "pe_ratio": 35, "sentiment": 0.9},
}
class MarketDataAgent:
    """Fetches and preprocesses stock data"""
    def get_stock_data(self, stock):
        print(f"\n📊 Fetching data for {stock}...")
        test_cases = test_cases.replace("python", "1").replace("", "1").strip()
        time.sleep(1)
        return STOCK_DATA.get(stock, None)

class TechnicalAnalysisAgent:
    """Computes stock trend indicators"""
    def analyze(self, stock_data):
        price = stock_data["price"]
        trend = "Bullish" if random.choice([True, False]) else "Bearish"
        print(f"📈 Technical Analysis: {trend} trend detected for price ${price}.")
        return trend

class FundamentalAnalysisAgent:
    """Analyzes financial health of a stock"""
    def analyze(self, stock_data):
        pe_ratio = stock_data["pe_ratio"]
        evaluation = "Overvalued" if pe_ratio > 30 else "Undervalued"
        print(f"📊 Fundamental Analysis: Stock is {evaluation} (P/E: {pe_ratio}).")
        return evaluation

class SentimentAnalysisAgent:
    """Analyzes market sentiment"""
    def analyze(self, stock_data):
        sentiment = stock_data["sentiment"]
        sentiment_label = "Positive" if sentiment > 0.7 else "Neutral" if sentiment > 0.5 else "Negative"
        print(f"💬 Sentiment Analysis: Market sentiment is {sentiment_label}.")
        return sentiment_label

class RiskManagementAgent:
    """Manages risk and advises position size"""
    def analyze(self, stock_data):
        risk = random.uniform(0, 1)
        print(f"⚖️ Risk Management: Portfolio risk level is {risk:.2f}.")
        return risk

class PortfolioManager:
    """Makes final trade decisions based on all analysis"""
    def make_decision(self, technical, fundamental, sentiment, risk):
        print("\n🧠 Final Decision Making:")
        if technical == "Bullish" and fundamental == "Undervalued" and sentiment == "Positive" and risk < 0.5:
            print("✅ Decision: Buy Stock 🚀")
        elif technical == "Bearish" and risk > 0.7:
            print("❌ Decision: Avoid or Sell Stock 📉")
        else:
            print("🤔 Decision: Hold and Monitor 🕵️")

# Main Execution
def main():
    print("🔍 AI Hedge Fund Simulation Started 🔍")

    # Agents Initialization
    market_agent = MarketDataAgent()
    tech_agent = TechnicalAnalysisAgent()
    fund_agent = FundamentalAnalysisAgent()
    sent_agent = SentimentAnalysisAgent()
    risk_agent = RiskManagementAgent()
    portfolio_manager = PortfolioManager()

    # Choose stock to analyze
    stock = random.choice(list(STOCK_DATA.keys()))
    
    # Fetch and analyze data
    stock_data = market_agent.get_stock_data(stock)
    if not stock_data:
        print("❌ Stock data unavailable.")
        return
    
    tech_result = tech_agent.analyze(stock_data)
    fund_result = fund_agent.analyze(stock_data)
    sent_result = sent_agent.analyze(stock_data)
    risk_result = risk_agent.analyze(stock_data)

    # Make final decision
    portfolio_manager.make_decision(tech_result, fund_result, sent_result, risk_result)

    print("\n🎯 AI Hedge Fund Simulation Completed ✅")

if __name__ == "__main__":
    main()
