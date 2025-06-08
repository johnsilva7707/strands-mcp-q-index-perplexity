
import os

from dotenv import load_dotenv
from strands import Agent
from strands.tools.mcp import MCPClient

from mcp import StdioServerParameters, stdio_client

load_dotenv()

# Perplexity API Key - loaded from .env
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY", None)

AGENT_SYSTEM_PROMPT = """
You are a helpful AI assistant who answers question correctly and accurately about a AcmeCompany's IT tickets and also rely on Perplexity MCP Server for general knowledge.
You answer in the format as follows:
<response>
    <datasource> 
    </datasource>
    <perplexityknowledge> 
    </perplexityknowledge>
</response>

** For datasource section: **
    Use tool answer_question from AnyCompany MCP Server.
    Do not makeup answers and only answer from the provided knowledge. 
    If the query doesn't has any Info about IT Tickets, you must acknowledge that. 
** For  perplexityknowledge section: **
    Provide info by obtaining the results from perplexity-ask MCP using it's preplexity_ask tool for addressing the query.
"""

# Get the full path of q_index_mcp directory
q_index_mcp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "q_index_mcp")

q_index_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uv",
            args=[
                "--directory",
                q_index_mcp_dir,
                "run",
                "mcp_server.py",
            ],
        )
    )
)

perplexity_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="npx",
            args=["-y", "server-perplexity-ask"],
            env={
                    "PERPLEXITY_API_KEY": PERPLEXITY_API_KEY
                }
        )
    )
)


# Create an agent with MCP tools
with q_index_mcp_client, perplexity_mcp_client:
    # Get the tools from the MCP server
    tools = (
        q_index_mcp_client.list_tools_sync() + perplexity_mcp_client.list_tools_sync()
    )

    # Create an agent with these tools
    agent = Agent(
        model="anthropic.claude-3-5-haiku-20241022-v1:0",
        system_prompt=AGENT_SYSTEM_PROMPT,
        tools=tools,
        max_parallel_tools=2
    )
    
    print("Welcome to the AcmeCompany IT Assistant CLI")
    
    while True:
        print("\nOptions:")
        print("1. Ask a question")
        print("2. Exit")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == "2":
            print("Exiting the assistant. Goodbye!")
            break
        elif choice == "1":
            user_query = input("Enter your query: ")
            if user_query.strip():
                print("\nProcessing your query...\n")
                response = agent(user_query)
                print("\n" + "-" * 50)
            else:
                print("Query cannot be empty. Please try again.")
        else:
            print("Invalid option. Please enter 1 or 2.")