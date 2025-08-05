import streamlit as st
import httpx
import json
import os

# Page configuration
st.set_page_config(
    page_title="AI Game Generator",
    page_icon="🎮",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        font-size: 3rem;
        margin-bottom: 2rem;
    }
    .api-section {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .game-preview {
        border: 2px solid #1f77b4;
        border-radius: 10px;
        padding: 1rem;
        margin-top: 1rem;
    }
    .stButton > button {
        background-color: #1f77b4;
        color: white;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        font-size: 1.1rem;
    }
    .api-provider {
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
    }
    .api-provider.active {
        border-color: #1f77b4;
        background: #f8f9ff;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🎮 AI Game Generator</h1>', unsafe_allow_html=True)

# API Key Management
st.markdown('<div class="api-section">', unsafe_allow_html=True)
st.subheader("🔑 API Configuration")

# Check if API keys are already set
if 'openrouter_api_key' not in st.session_state:
    st.session_state.openrouter_api_key = ""
if 'gemini_api_key' not in st.session_state:
    st.session_state.gemini_api_key = ""
if 'selected_provider' not in st.session_state:
    st.session_state.selected_provider = "OpenRouter"

# API Provider Selection
st.markdown("**Choose your AI provider:**")
col1, col2 = st.columns(2)

with col1:
    if st.button("🤖 OpenRouter", use_container_width=True, 
                 type="primary" if st.session_state.selected_provider == "OpenRouter" else "secondary"):
        st.session_state.selected_provider = "OpenRouter"

with col2:
    if st.button("🌟 Gemini", use_container_width=True,
                 type="primary" if st.session_state.selected_provider == "Gemini" else "secondary"):
        st.session_state.selected_provider = "Gemini"

# API key inputs based on selection
if st.session_state.selected_provider == "OpenRouter":
    st.markdown('<div class="api-provider active">', unsafe_allow_html=True)
    st.subheader("🤖 OpenRouter API")
    openrouter_key = st.text_input(
        "Enter your OpenRouter API Key:",
        value=st.session_state.openrouter_api_key,
        type="password",
        help="Get your API key from https://openrouter.ai/keys"
    )
    if openrouter_key:
        st.session_state.openrouter_api_key = openrouter_key
        st.success("✅ OpenRouter API key saved!")
    
    # OpenRouter model selection
    openrouter_model = st.selectbox(
        "Choose AI Model:",
        [
            "deepseek/deepseek-chat-v3-0324:free",
            "anthropic/claude-3.5-sonnet",
            "openai/gpt-4o",
            "meta-llama/llama-3.1-8b-instruct:free"
        ],
        index=0
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
else:  # Gemini
    st.markdown('<div class="api-provider active">', unsafe_allow_html=True)
    st.subheader("🌟 Gemini API")
    gemini_key = st.text_input(
        "Enter your Gemini API Key:",
        value=st.session_state.gemini_api_key,
        type="password",
        help="Get your API key from https://makersuite.google.com/app/apikey"
    )
    if gemini_key:
        st.session_state.gemini_api_key = gemini_key
        st.success("✅ Gemini API key saved!")
    
    # Gemini model selection
    gemini_model = st.selectbox(
        "Choose Gemini Model:",
        [
            "gemini-2.0-flash",
            "gemini-1.5-flash",
            "gemini-1.5-pro"
        ],
        index=0
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Game Description Input
st.subheader("🎯 Describe Your Game")
st.markdown("""
**Examples:**
- "A simple snake game where you control a snake to eat food and grow longer"
- "A memory card game where you match pairs of cards"
- "A clicker game where you click a button to earn points and buy upgrades"
- "A simple platformer where you jump over obstacles"
""")

user_prompt = st.text_area(
    "Describe your game in detail:",
    height=150,
    placeholder="Describe the game you want to create..."
)

# Game generation button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate_button = st.button("🚀 Generate Game", use_container_width=True)

# Game generation logic
if generate_button:
    if st.session_state.selected_provider == "OpenRouter":
        api_key = st.session_state.openrouter_api_key
        if not api_key:
            st.error("❌ Please enter your OpenRouter API key first!")
        elif not user_prompt.strip():
            st.error("❌ Please enter a game description!")
        else:
            with st.spinner("🤖 AI is generating your game..."):
                # Enhanced prompt for better game generation
                ai_prompt = f"""
                Create a complete, interactive game in HTML, CSS, and JavaScript based on this description:
                "{user_prompt}"
                
                Requirements:
                1. Make it fully playable and interactive
                2. Include proper game mechanics, scoring, and user feedback
                3. Use modern CSS for attractive styling
                4. Add sound effects or visual feedback where appropriate
                5. Make it responsive and work on different screen sizes
                6. Include clear instructions for the player
                
                Return ONLY the complete HTML code with embedded CSS and JavaScript.
                Do NOT include any explanations outside the code.
                The code should be ready to run immediately.
                """

                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                }

                payload = {
                    "model": openrouter_model,
                    "messages": [
                        {
                            "role": "system", 
                            "content": "You are an expert game developer. Generate only complete, runnable HTML games with embedded CSS and JavaScript. Focus on creating engaging, interactive experiences."
                        },
                        {"role": "user", "content": ai_prompt},
                    ],
                    "temperature": 0.7,
                    "max_tokens": 8000,
                }

                try:
                    # Call OpenRouter API
                    with httpx.Client(timeout=30.0) as client:
                        response = client.post(
                            "https://openrouter.ai/api/v1/chat/completions", 
                            json=payload, 
                            headers=headers
                        )
                        response.raise_for_status()
                        result = response.json()
                        code = result["choices"][0]["message"]["content"].strip()

                    # Store the generated code in session state
                    st.session_state.generated_code = code
                    st.session_state.game_generated = True

                    st.success("🎉 Game generated successfully!")

                except Exception as e:
                    st.error(f"❌ Error generating game: {str(e)}")
                    st.info("💡 Make sure your API key is valid and you have sufficient credits.")

    else:  # Gemini
        api_key = st.session_state.gemini_api_key
        if not api_key:
            st.error("❌ Please enter your Gemini API key first!")
        elif not user_prompt.strip():
            st.error("❌ Please enter a game description!")
        else:
            with st.spinner("🤖 Gemini is generating your game..."):
                # Enhanced prompt for better game generation
                ai_prompt = f"""
                Create a complete, interactive game in HTML, CSS, and JavaScript based on this description:
                "{user_prompt}"
                
                Requirements:
                1. Make it fully playable and interactive
                2. Include proper game mechanics, scoring, and user feedback
                3. Use modern CSS for attractive styling
                4. Add sound effects or visual feedback where appropriate
                5. Make it responsive and work on different screen sizes
                6. Include clear instructions for the player
                
                Return ONLY the complete HTML code with embedded CSS and JavaScript.
                Do NOT include any explanations outside the code.
                The code should be ready to run immediately.
                """

                headers = {
                    "Content-Type": "application/json",
                }

                payload = {
                    "contents": [
                        {
                            "parts": [
                                {
                                    "text": f"You are an expert game developer. Generate only complete, runnable HTML games with embedded CSS and JavaScript. Focus on creating engaging, interactive experiences.\n\n{ai_prompt}"
                                }
                            ]
                        }
                    ]
                }

                try:
                    # Call Gemini API
                    with httpx.Client(timeout=30.0) as client:
                        response = client.post(
                            f"https://generativelanguage.googleapis.com/v1beta/models/{gemini_model}:generateContent?key={api_key}",
                            json=payload, 
                            headers=headers
                        )
                        response.raise_for_status()
                        result = response.json()
                        code = result["candidates"][0]["content"]["parts"][0]["text"].strip()

                    # Store the generated code in session state
                    st.session_state.generated_code = code
                    st.session_state.game_generated = True

                    st.success("🎉 Game generated successfully with Gemini!")

                except Exception as e:
                    st.error(f"❌ Error generating game: {str(e)}")
                    st.info("💡 Make sure your Gemini API key is valid and you have sufficient credits.")

# Display generated game
if 'game_generated' in st.session_state and st.session_state.game_generated:
    st.markdown('<div class="game-preview">', unsafe_allow_html=True)
    st.subheader("🎮 Your Generated Game")
    
    # Tabs for code and preview
    tab1, tab2 = st.tabs(["🎮 Play Game", "📝 View Code"])
    
    with tab1:
        st.markdown("**Instructions:** Use the controls below to play your generated game!")
        st.components.v1.html(st.session_state.generated_code, height=600, scrolling=True)
    
    with tab2:
        st.code(st.session_state.generated_code, language="html")
        
        # Download button
        st.download_button(
            label="💾 Download Game",
            data=st.session_state.generated_code,
            file_name="generated_game.html",
            mime="text/html"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🎮 AI Game Generator | Powered by OpenRouter & Gemini</p>
    <p>Get your API keys at <a href='https://openrouter.ai/keys' target='_blank'>openrouter.ai/keys</a> or <a href='https://makersuite.google.com/app/apikey' target='_blank'>makersuite.google.com</a></p>
</div>
""", unsafe_allow_html=True)