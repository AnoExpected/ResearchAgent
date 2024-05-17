from get_doc_tools import get_doc_tools
from pathlib import Path
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import FunctionCallingAgentWorker, AgentRunner
from llama_index.core import VectorStoreIndex
from llama_index.core.objects import ObjectIndex

def setup_agent(papers):
    # Prepare tools for each paper
    paper_to_tools_dict = {}
    for paper in papers:
        print(f"Getting tools for paper: {paper}")
        vector_tool, summary_tool = get_doc_tools(f"data/{paper}", Path(paper).stem)
        paper_to_tools_dict[paper] = [vector_tool, summary_tool]

    # Gather all tools
    all_tools = [t for paper in papers for t in paper_to_tools_dict[paper]]

    # Create object index and retriever
    obj_index = ObjectIndex.from_objects(
        all_tools,
        index_cls=VectorStoreIndex,
    )
    obj_retriever = obj_index.as_retriever(similarity_top_k=3)

    # Setup LLM
    llm = OpenAI(model="gpt-3.5-turbo")

    # Setup agent worker and agent
    agent_worker = FunctionCallingAgentWorker.from_tools(
        tool_retriever=obj_retriever,
        llm=llm, 
        system_prompt=""" \
        You are an agent designed to answer queries over a set of given papers.
        Please always use the tools provided to answer a question. Do not rely on 
        prior knowledge.\
        """,
        verbose=True
    )
    agent = AgentRunner(agent_worker)
    return agent
