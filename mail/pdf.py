import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# Load API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set up LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0.5)

# Function to generate email
def generate_email(purpose, recipient, tone, keywords):
    prompt = f"""
Generate an email based on the following inputs:
- Purpose: {purpose}
- Recipient: {recipient}
- Tone: {tone}
- Keywords: {keywords}

Structure the email with:
1. Subject
2. Greeting
3. Body
4. Closing
Keep it natural and appropriate for the context.
    """

    messages = [
        SystemMessage(content="You are a professional email writing assistant."),
        HumanMessage(content=prompt)
    ]

    response = llm(messages)
    return response.content

# Main app logic
if __name__ == "__main__":
    print("✉️ AI Email Generator ✉️")
    
    purpose = input("Enter the purpose of the email (e.g., internship request): ")
    recipient = input("Who is the email for? (e.g., professor, HR manager): ")
    tone = input("Tone? (formal / casual / friendly) [default: formal]: ") or "formal"
    keywords = input("Optional keywords to include (comma-separated): ")

    print("\n🔄 Generating email...\n")
    email = generate_email(purpose, recipient, tone, keywords)
    print("✅ Email Generated:\n")
    print(email)
