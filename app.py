from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

async def main():
    # Create the agent with GPT-4 Vision
    agent = Agent(
        task="""
        1. Go to google.com, click accept, go to x.com, click login. click signin with google
        """,
        llm=ChatOpenAI(
            model="gpt-4o",
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
    os.system("pip install --upgrade browser-use langchain-openai python-dotenv")
    
    # Run the main function
    asyncio.run(main())