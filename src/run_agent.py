import typer
from dotenv import load_dotenv
load_dotenv()
from prediction_market_agent_tooling.markets.markets import MarketType

from coinflip_agent import CoinflipAgent


def main():
    print('start')
    c = CoinflipAgent()
    c.deploy_local(market_type=MarketType.OMEN, sleep_time=180, timeout=0.01)
    print ('end')

if __name__ == "__main__":
    typer.run(main)