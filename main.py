import nest_asyncio
from agent_setup import setup_agent
from pathlib import Path 
from app import app


nest_asyncio.apply()

def main():
    # Define the papers
    papers = ["metagpt.pdf", "longlora.pdf", "selfrag.pdf"]
    
    # Setup the agent
    agent = setup_agent(papers)
    
    # Example queries
    response = agent.query(
        "Tell me about the evaluation dataset used in LongLoRA, "
        "and then tell me about the evaluation results"
    )
    print(response)
    
    response = agent.query("Give me a summary of both Self-RAG and LongLoRA")
    print(response)

if __name__ == "__main__":
    main()
