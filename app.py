from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os

# Hardcode OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

async def main():
    # Create the agent with GPT-4 Vision
    agent = Agent(
        task="""
        1. Go to google.com, click accept, go to x.com, click login. click signin with google
        """,
        llm=ChatOpenAI(
            model="gpt-4o",
            api_key="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",
            max_tokens=4096
        )
    )
    
    try:
        print("Starting browser automation...")
        result = await agent.run()
        print("Task completed!")
        print("Result:", result)
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    # Make sure you have the latest versions
    os.system("pip install --upgrade browser-use langchain-openai")
    
    # Run the main function
    asyncio.run(main())