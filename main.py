from fastapi import FastAPI, HTTPException, Depends
from prometheus_fastapi_instrumentator import Instrumentator
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
import httpx
import os

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost/crypto")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Models
class TrackedCoin(Base):
    __tablename__ = "tracked_coins"
    id = Column(Integer, primary_key=True)
    coin_id = Column(String, unique=True, nullable=False)
    symbol = Column(String, nullable=False)
    name = Column(String, nullable=False)

class PriceHistory(Base):
    __tablename__ = "price_history"
    id = Column(Integer, primary_key=True)
    coin_id = Column(String, nullable=False)
    price_usd = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# FastAPI
app = FastAPI(title="Crypto Price Tracker", version="1.0.0")
scheduler = AsyncIOScheduler()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Instrumentator().instrument(app).expose(app)
# CoinGecko API
async def fetch_prices(coin_ids: list[str]) -> dict:
    ids = ",".join(coin_ids)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

# Background task
async def update_prices():
    db = SessionLocal()
    try:
        coins = db.query(TrackedCoin).all()
        if not coins:
            return
        coin_ids = [c.coin_id for c in coins]
        prices = await fetch_prices(coin_ids)
        for coin_id, data in prices.items():
            history = PriceHistory(
                coin_id=coin_id,
                price_usd=data["usd"]
            )
            db.add(history)
        db.commit()
        print(f"✅ Prices updated at {datetime.utcnow()}")
    except Exception as e:
        print(f"❌ Error updating prices: {e}")
    finally:
        db.close()

TOP_20_COINS = [
    {"id": "bitcoin", "symbol": "BTC", "name": "Bitcoin"},
    {"id": "ethereum", "symbol": "ETH", "name": "Ethereum"},
    {"id": "tether", "symbol": "USDT", "name": "Tether"},
    {"id": "binancecoin", "symbol": "BNB", "name": "BNB"},
    {"id": "solana", "symbol": "SOL", "name": "Solana"},
    {"id": "usd-coin", "symbol": "USDC", "name": "USD Coin"},
    {"id": "ripple", "symbol": "XRP", "name": "XRP"},
    {"id": "dogecoin", "symbol": "DOGE", "name": "Dogecoin"},
    {"id": "toncoin", "symbol": "TON", "name": "Toncoin"},
    {"id": "cardano", "symbol": "ADA", "name": "Cardano"},
    {"id": "avalanche-2", "symbol": "AVAX", "name": "Avalanche"},
    {"id": "shiba-inu", "symbol": "SHIB", "name": "Shiba Inu"},
    {"id": "polkadot", "symbol": "DOT", "name": "Polkadot"},
    {"id": "chainlink", "symbol": "LINK", "name": "Chainlink"},
    {"id": "bitcoin-cash", "symbol": "BCH", "name": "Bitcoin Cash"},
    {"id": "near", "symbol": "NEAR", "name": "NEAR Protocol"},
    {"id": "matic-network", "symbol": "MATIC", "name": "Polygon"},
    {"id": "litecoin", "symbol": "LTC", "name": "Litecoin"},
    {"id": "internet-computer", "symbol": "ICP", "name": "Internet Computer"},
    {"id": "uniswap", "symbol": "UNI", "name": "Uniswap"},
]

@app.on_event("startup")
async def startup():
    db = SessionLocal()
    try:
        for coin_data in TOP_20_COINS:
            existing = db.query(TrackedCoin).filter(
                TrackedCoin.coin_id == coin_data["id"]
            ).first()
            if not existing:
                coin = TrackedCoin(
                    coin_id=coin_data["id"],
                    symbol=coin_data["symbol"],
                    name=coin_data["name"]
                )
                db.add(coin)
        db.commit()
        print("✅ Top 20 coins initialized")
    finally:
        db.close()

    scheduler.add_job(update_prices, "interval", minutes=5)
    scheduler.start()
    await update_prices()

@app.on_event("shutdown")
async def shutdown():
    scheduler.shutdown()

# Endpoints
@app.get("/")
def root():
    return {"app": "Crypto Price Tracker", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy", "version": "1.0.0"}

@app.get("/prices")
async def get_all_prices(db: Session = Depends(get_db)):
    coins = db.query(TrackedCoin).all()
    if not coins:
        return []
    coin_ids = [c.coin_id for c in coins]
    prices = await fetch_prices(coin_ids)
    result = []
    for coin in coins:
        price_data = prices.get(coin.coin_id, {})
        result.append({
            "coin_id": coin.coin_id,
            "symbol": coin.symbol,
            "name": coin.name,
            "price_usd": price_data.get("usd", 0)
        })
    return result

@app.get("/price/{coin_id}")
async def get_price(coin_id: str, db: Session = Depends(get_db)):
    coin = db.query(TrackedCoin).filter(TrackedCoin.coin_id == coin_id).first()
    if not coin:
        raise HTTPException(status_code=404, detail=f"Coin '{coin_id}' not tracked")
    prices = await fetch_prices([coin_id])
    price = prices.get(coin_id, {}).get("usd", 0)
    return {
        "coin_id": coin_id,
        "symbol": coin.symbol,
        "name": coin.name,
        "price_usd": price,
        "timestamp": datetime.utcnow()
    }

@app.get("/price/{coin_id}/history")
def get_history(coin_id: str, db: Session = Depends(get_db)):
    coin = db.query(TrackedCoin).filter(TrackedCoin.coin_id == coin_id).first()
    if not coin:
        raise HTTPException(status_code=404, detail=f"Coin '{coin_id}' not tracked")
    history = db.query(PriceHistory)\
        .filter(PriceHistory.coin_id == coin_id)\
        .order_by(PriceHistory.timestamp.desc())\
        .limit(100)\
        .all()
    return [{"price_usd": h.price_usd, "timestamp": h.timestamp} for h in history]

@app.post("/track/{coin_id}")
async def track_coin(coin_id: str, db: Session = Depends(get_db)):
    existing = db.query(TrackedCoin).filter(TrackedCoin.coin_id == coin_id).first()
    if existing:
        raise HTTPException(status_code=400, detail=f"Coin '{coin_id}' already tracked")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.coingecko.com/api/v3/coins/{coin_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail=f"Coin '{coin_id}' not found on CoinGecko")
        data = response.json()
    coin = TrackedCoin(
        coin_id=coin_id,
        symbol=data["symbol"].upper(),
        name=data["name"]
    )
    db.add(coin)
    db.commit()
    db.refresh(coin)
    return {"message": f"Now tracking {coin.name} ({coin.symbol})", "coin": coin_id}

@app.delete("/track/{coin_id}")
def untrack_coin(coin_id: str, db: Session = Depends(get_db)):
    coin = db.query(TrackedCoin).filter(TrackedCoin.coin_id == coin_id).first()
    if not coin:
        raise HTTPException(status_code=404, detail=f"Coin '{coin_id}' not tracked")
    db.delete(coin)
    db.commit()
    return {"message": f"Stopped tracking {coin_id}"}
