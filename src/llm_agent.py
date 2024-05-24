from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from prediction_market_agent_tooling.deploy.agent import DeployableTraderAgent, Answer
from prediction_market_agent_tooling.markets.agent_market import AgentMarket


class LLMAgentAgent(DeployableTraderAgent):

    def ask_question_to_llm(self, question: str) -> Answer:
        model = ChatOpenAI(temperature=0)
        parser = PydanticOutputParser(pydantic_object=Answer)

        prompt = PromptTemplate(
            template="Answer the question.\n{format_instructions}\n{question}\n",
            input_variables=["question"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        chain = prompt | model | parser

        answer = chain.invoke({"question": question})
        return answer

    def answer_binary_market(self, market: AgentMarket) -> Answer | None:
        """
        Asks an LLM for the answer of a market.
        """
        answer = self.ask_question_to_llm(market.question)
        return answer
