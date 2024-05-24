import typer
from dotenv import load_dotenv

from src.llm_agent import LLMAgentAgent

load_dotenv()
from prediction_market_agent_tooling.markets.markets import MarketType


def main():
    print("start")
    # c = CoinflipAgent()
    c = LLMAgentAgent()
    c.deploy_local(market_type=MarketType.OMEN, sleep_time=180, timeout=0.01)
    print("end")


if __name__ == "__main__":
    typer.run(main)
