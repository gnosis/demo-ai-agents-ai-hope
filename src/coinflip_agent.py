import random

from prediction_market_agent_tooling.deploy.agent import DeployableTraderAgent, Answer
from prediction_market_agent_tooling.gtypes import Probability
from prediction_market_agent_tooling.markets.agent_market import AgentMarket


class CoinflipAgent(DeployableTraderAgent):
    def answer_binary_market(self, market: AgentMarket) -> Answer | None:
        """
        Answer the binary market. This method must be implemented by the subclass.
        """
        decision = random.choice([True, False])
        return Answer(
            decision=decision,
            confidence=0.5,
            p_yes=Probability(float(decision)),
            reasoning="I flipped a coin to decide.",
        )
