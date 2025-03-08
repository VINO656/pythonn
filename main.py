https://github.com/VINO656/pythonn
import random
import numpy
import pandasn njnj
hgvnhgcvdzfmjh
hello world
hello world
hello world
n nhb hn

commit this as api_core.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(_name_)

# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pythonn.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "super-secret-key")  # change for production

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# ------------------------------
# Database Models
# ------------------------------

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Stock(db.Model):
    stock_id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    pe_ratio = db.Column(db.Float)
    sentiment = db.Column(db.String(50))

# ------------------------------
# API Endpoints
# ------------------------------

# User Registration Endpoint
@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if not username or not password or not email:
        return jsonify({"msg": "Missing required fields"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400

    password_hash = generate_password_hash(password)
    new_user = User(username=username, password_hash=password_hash, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created successfully", "user_id": new_user.user_id}), 201

# User Login Endpoint
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=user.user_id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

# Fetch User Profile Endpoint (requires JWT)
@app.route("/api/profile", methods=["GET"])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user:
        return jsonify({
            "user_id": user.user_id,
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at.isoformat()
        }), 200
    else:
        return jsonify({"msg": "User not found"}), 404

# Update User Profile Endpoint (requires JWT)
@app.route("/api/profile", methods=["PUT"])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404

    data = request.get_json()
    if "username" in data:
        user.username = data["username"]
    if "email" in data:
        user.email = data["email"]
    db.session.commit()

    return jsonify({"msg": "Profile updated successfully"}), 200

# Fetch Stocks Endpoint
@app.route("/api/stocks", methods=["GET"])
def get_stocks():
    stocks = Stock.query.all()
    stocks_list = [{
        "stock_id": stock.stock_id,
        "symbol": stock.symbol,
        "price": stock.price,
        "pe_ratio": stock.pe_ratio,
        "sentiment": stock.sentiment
    } for stock in stocks]
    return jsonify(stocks=stocks_list), 200

# Admin/Utility Endpoint to Populate Stocks (for demo purposes)
@app.route("/api/populate_stocks", methods=["POST"])
def populate_stocks():
    # This is a simple demonstration to add sample stocks
    sample_stocks = [
        {"symbol": "AAPL", "price": 150.00, "pe_ratio": 30.0, "sentiment": "Positive"},
        {"symbol": "GOOGL", "price": 2800.50, "pe_ratio": 35.0, "sentiment": "Neutral"},
        {"symbol": "AMZN", "price": 3400.25, "pe_ratio": 60.0, "sentiment": "Negative"}
    ]
    for data in sample_stocks:
        if not Stock.query.filter_by(symbol=data["symbol"]).first():
            stock = Stock(**data)
            db.session.add(stock)
    db.session.commit()
    return jsonify({"msg": "Stocks populated successfully"}), 201

# ------------------------------
# Main Entry Point
# ------------------------------

if _name_ == "_main_":
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the Flask development server
    app.run(debug=True)
gvghgfcbfcvb


https://github.com/VINO656
import time
import numpy
import pandas
hello world

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
