from langchain.agents import (
    AgentExecutor,
    create_openai_functions_agent,
)
from langchain_community.chat_models import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_openai import ChatOpenAI
from prediction_market_agent_tooling.deploy.agent import DeployableTraderAgent, Answer
from prediction_market_agent_tooling.markets.agent_market import AgentMarket


class LLMAgentAgentWithTools(DeployableTraderAgent):

    def ask_question_to_llm(self, question: str) -> Answer:
        llm = ChatOpenAI(temperature=0)
        tavily_tool = TavilySearchResults(max_results=3)
        tools = [tavily_tool]
        messages = [
            HumanMessagePromptTemplate.from_template("{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]

        prompt = ChatPromptTemplate.from_messages(messages)
        agent = create_openai_functions_agent(llm, tools, prompt)
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
        )
        answer = agent_executor.invoke(
            {
                "input": f"Answer the question below. \n QUESTION: {question}. \n You should output a single"
                f"integer answer, 0 if the answer to the question is NO and 1 if the answer if YES. "
            }
        )
        # We neglect p_yes and confidence for now.
        # Hacky way to extract Answer, defer to Pydantic output when more time available.
        try:
            decision = True if int(answer["output"]) else False
        except:
            decision = False

        return Answer(decision=decision, p_yes=0.5, confidence=0.5)

    def answer_binary_market(self, market: AgentMarket) -> Answer | None:
        """
        Asks an LLM for the answer of a market.
        """
        answer = self.ask_question_to_llm(market.question)
        return answer
