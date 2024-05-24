# demo-ai-agents-ai-hope

This projects illustrates how to get started with the [PMAT](https://github.com/gnosis/prediction-market-agent-tooling) (prediction-market-agent-tooling) repository, in order to create AI agents able to interact with prediction markets.

## Getting started

- Clone this repo
- Install dependencies using Poetry (Python 3.11 recommended)
```shell
poetry install
```
- Rename `.env.local` to `.env`
- Fill dependencies on `.env` (we suggest using the Gnosis Fork from the `.env.example`)
- Run an agent locally
```
poetry run src/run_agent.py
```