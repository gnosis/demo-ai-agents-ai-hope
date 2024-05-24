import typer
from dotenv import load_dotenv

load_dotenv()

from llm_agent_with_tools import LLMAgentAgentWithTools

from prediction_market_agent_tooling.markets.markets import MarketType


def main():
    print("start")
    # c = CoinflipAgent()
    # c = LLMAgentAgent()
    c = LLMAgentAgentWithTools()
    c.deploy_local(market_type=MarketType.OMEN, sleep_time=180, timeout=0.01)
    print("end")


if __name__ == "__main__":
    typer.run(main)
