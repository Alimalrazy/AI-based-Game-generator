import streamlit as st
import httpx  # for HTTP requests

#API_KEY = "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" # mahmudul
API_KEY="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" #Reza
#API_KEY = "AIzaSyC35mil4vDAAmBkEVFVGyY8XEA5qGP3HSs" #Alim

BASE_URL="https://openrouter.ai/api/v1"
#MODEL ="gemini-2.0-flash:generateContent"
#BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
#MODEL = "anthropic/claude-3.5-sonnet"
#BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "deepseek/deepseek-chat-v3-0324:free"

# Streamlit UI
st.title("Game Code Generator")
user_prompt = st.text_area("Describe your game:", height=150)

if st.button("Generate Game Code"):
    if not user_prompt.strip():
        st.error("Please enter a game description!")
    else:
        with st.spinner("Generating code..."):
            ai_prompt = f"""
            Generate a complete, runnable game in HTML, CSS, and JavaScript based on this description:
            \"\"\"{user_prompt}\"\"\"
            Return ONLY the full HTML code including <html>, <head>, <body>, and <script>.
            Do NOT include any explanations or comments outside the code.
            """

            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            }

            payload = {
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": "You are a code generator that returns only runnable code."},
                    {"role": "user", "content": ai_prompt},
                ],
                "temperature": 0.7,
                "max_tokens": 15000,
            }

            try:
                # Call OpenRouter API
                with httpx.Client() as client:
                    response = client.post(f"{BASE_URL}/chat/completions", json=payload, headers=headers)
                    response.raise_for_status()
                    result = response.json()
                    code = result["choices"][0]["message"]["content"].strip()

                # Display code in an expandable box
                with st.expander("Generated Game Code", expanded=True):
                    st.code(code, language="html")

                # Preview the game in an iframe
                st.subheader("Game Preview")
                st.components.v1.html(code, height=500, scrolling=True)

            except Exception as e:
                st.error(f"Error generating code: {e}")