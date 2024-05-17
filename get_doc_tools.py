from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, SummaryIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.tools import FunctionTool, QueryEngineTool
from llama_index.core.vector_stores import MetadataFilters, FilterCondition
from typing import List, Optional

def get_doc_tools(file_path: str, name: str):
    """Get vector query and summary query tools from a document."""
    # Load documents
    documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
    
    # Split documents into nodes
    splitter = SentenceSplitter(chunk_size=1024)
    nodes = splitter.get_nodes_from_documents(documents)
    
    # Create a VectorStoreIndex
    vector_index = VectorStoreIndex(nodes)
    
    # Define the vector query function
    def vector_query(query: str, page_numbers: Optional[List[str]] = None) -> str:
        """Perform a vector search over an index."""
        page_numbers = page_numbers or []
        metadata_dicts = [{"key": "page_label", "value": p} for p in page_numbers]
        
        query_engine = vector_index.as_query_engine(
            similarity_top_k=2,
            filters=MetadataFilters.from_dicts(metadata_dicts, condition=FilterCondition.OR)
        )
        response = query_engine.query(query)
        return response

    # Create a vector query tool
    vector_query_tool = FunctionTool.from_defaults(
        name=f"vector_tool_{name}",
        fn=vector_query
    )

    # Create a SummaryIndex
    summary_index = SummaryIndex(nodes)
    
    # Create a summary query engine
    summary_query_engine = summary_index.as_query_engine(
        response_mode="tree_summarize",
        use_async=True,
    )
    
    # Create a summary query tool
    summary_tool = QueryEngineTool.from_defaults(
        name=f"summary_tool_{name}",
        query_engine=summary_query_engine,
        description=(
            f"Useful for summarization questions related to {name}"
        ),
    )
    
    return vector_query_tool, summary_tool
