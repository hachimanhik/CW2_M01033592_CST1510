from openai import OpenAI
import streamlit as st

def ask_ai(domain, question):
    # Create client using the key from secrets
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # Simple text prompt
    full_prompt = f"Domain: {domain}\nQuestion: {question}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": full_prompt}
        ]
    )

    answer = response.choices[0].message.content
    return answer
