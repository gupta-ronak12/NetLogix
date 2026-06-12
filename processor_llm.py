import os
import re
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from the .env file
load_dotenv()

# Explicitly initialize the client using the key from .env
# This ensures it never fails to find the key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is not set in the .env file.")

groq = Groq(api_key=api_key)

def classify_with_llm(log_msg):
    """
    Classifies a log message using Groq's LLM.
    """
    prompt = f'''Classify the log message into one of these categories: 
    (1) Workflow Error, (2) Deprecation Warning.
    If you can't figure out a category, use "Unclassified".
    Put the category inside <category> </category> tags. 
    Log message: {log_msg}'''

    try:
        chat_completion = groq.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="deepseek-r1-distill-llama-70b",
            temperature=0.5
        )

        content = chat_completion.choices[0].message.content
        match = re.search(r'<category>(.*)<\/category>', content, flags=re.DOTALL)
        
        return match.group(1).strip() if match else "Unclassified"
        
    except Exception as e:
        print(f"LLM Classification error: {e}")
        return "Unclassified"

if __name__ == "__main__":
    # Test cases
    test_logs = [
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active.",
        "The 'ReportGenerator' module will be retired in version 4.0.",
        "System reboot initiated by user 12345."
    ]
    for log in test_logs:
        print(f"{log} -> {classify_with_llm(log)}")