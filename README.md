# 🎮 AI Game Generator

Create amazing interactive games with AI! Just describe your game idea and watch as AI generates complete, playable HTML games with embedded CSS and JavaScript.

## ✨ Features

- 🤖 **Dual AI Support**: Choose between OpenRouter (Claude, GPT-4, DeepSeek) and Google Gemini
- 🎯 **Simple Game Creation**: Describe your game in plain English
- 🎮 **Instant Play**: Generated games run immediately in your browser
- 💾 **Download Games**: Save generated games as standalone HTML files
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- 🔑 **Easy API Setup**: Simple API key configuration
- 🎨 **Beautiful UI**: Modern, intuitive interface
- ⚡ **Fast Generation**: Get your game in seconds

## 🚀 Quick Start

### Option 1: HTML Version (Recommended - No Installation)

1. **Download the files**
2. **Open `simple_game_generator.html`** in any web browser
3. **Get your API key** from [OpenRouter](https://openrouter.ai/keys) or [Gemini](https://makersuite.google.com/app/apikey)
4. **Start creating games!**

### Option 2: Streamlit Version

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python -m streamlit run backend.py
   ```

3. **Open your browser** to `http://localhost:8501`

## 🔑 API Setup

### OpenRouter API (Recommended for beginners)
1. Visit [openrouter.ai/keys](https://openrouter.ai/keys)
2. Sign up for a free account
3. Get your API key (free credits included)
4. Choose from models like:
   - DeepSeek Chat (Free)
   - Claude 3.5 Sonnet
   - GPT-4o
   - Llama 3.1 (Free)

### Gemini API
1. Visit [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Choose from models:
   - Gemini 2.0 Flash (Latest)
   - Gemini 1.5 Flash
   - Gemini 1.5 Pro

## 🎯 How to Use

### Step 1: Choose Your AI Provider
- Click **"🤖 OpenRouter"** or **"🌟 Gemini"**
- Enter your API key in the designated field

### Step 2: Describe Your Game
Write a clear description of the game you want to create. Here are some examples:

#### 🐍 Snake Game
```
A simple snake game where you control a snake to eat food and grow longer. 
Use arrow keys to move. The game ends if you hit the walls or yourself.
```

#### 🃏 Memory Card Game
```
A memory card game where you match pairs of cards. 
Click cards to flip them and find matching pairs. 
Track your score and time.
```

#### 🎯 Clicker Game
```
A clicker game where you click a button to earn points. 
Buy upgrades to increase points per click and auto-clickers.
```

#### 🏃 Platformer
```
A simple platformer where you jump over obstacles. 
Use spacebar to jump and avoid falling into pits.
```

#### ❌ Tic-Tac-Toe
```
A tic-tac-toe game for two players. 
Click squares to place X or O. 
First to get three in a row wins.
```

### Step 3: Generate and Play
1. Click **"🚀 Generate Game"**
2. Wait for AI to create your game (usually 10-30 seconds)
3. Play your game immediately in the preview
4. Download the HTML file to share or play offline

## 📁 Project Structure

```
AI-based-Game-generator-main/
├── backend.py                 # Streamlit web application
├── simple_game_generator.html # Standalone HTML version
├── requirements.txt           # Python dependencies
├── index.html                # Original frontend (legacy)
└── README.md                 # This file
```

## 🛠️ Installation (Streamlit Version)

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup
1. **Clone or download** the project files
2. **Navigate** to the project directory:
   ```bash
   cd AI-based-Game-generator-main
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**:
   ```bash
   python -m streamlit run backend.py
   ```
5. **Open your browser** to `http://localhost:8501`

## 🎮 Game Examples

The AI can generate various types of games:

### Simple Games
- **Snake Game**: Classic snake with food collection
- **Memory Cards**: Match pairs of cards
- **Tic-Tac-Toe**: Two-player strategy game
- **Clicker Game**: Idle game with upgrades
- **Platformer**: Jump and avoid obstacles
- **Racing Game**: Avoid obstacles while racing
- **Puzzle Game**: Logic puzzles and brain teasers
- **Quiz Game**: Interactive questions and answers

### Advanced Games
- **RPG Elements**: Character stats and progression
- **Multi-level Games**: Increasing difficulty levels
- **Scoring Systems**: Points, high scores, and achievements
- **Sound Effects**: Audio feedback and music
- **Animations**: Smooth visual effects
- **Responsive Design**: Works on all screen sizes

## 🔧 Customization

### Modifying Game Generation
You can customize the AI prompts in both versions:

**Streamlit Version** (`backend.py`):
- Edit the `ai_prompt` variable to change generation instructions
- Modify model parameters like `temperature` and `max_tokens`

**HTML Version** (`simple_game_generator.html`):
- Edit the prompt text in the `generateGame()` function
- Adjust API parameters in the request body

### Adding New AI Providers
The modular design makes it easy to add new AI providers:

1. Add provider selection UI
2. Implement API call function
3. Handle response parsing
4. Add error handling

## 🐛 Troubleshooting

### Common Issues

**"API key not recognized"**
- Verify your API key is correct
- Check if you have sufficient credits
- Ensure the API key is for the correct provider

**"Game generation failed"**
- Check your internet connection
- Verify API key permissions
- Try a different AI model

**"Streamlit not found"**
- Install Streamlit: `pip install streamlit`
- Use: `python -m streamlit run backend.py`

**"Game doesn't work properly"**
- Try regenerating with a clearer description
- Check browser console for JavaScript errors
- Ensure browser supports modern JavaScript

### Getting Help
1. Check the browser console for error messages
2. Verify your API key and credits
3. Try a simpler game description
4. Test with different AI models

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Report bugs** by creating an issue
2. **Suggest features** for new game types
3. **Add new AI providers** (OpenAI, Anthropic, etc.)
4. **Improve the UI/UX** with better designs
5. **Add more game examples** and templates

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **OpenRouter** for providing access to multiple AI models
- **Google Gemini** for their powerful AI capabilities
- **Streamlit** for the amazing web app framework
- **The AI community** for inspiration and support

## 📞 Support

- **Issues**: Create an issue on GitHub
- **Questions**: Check the troubleshooting section
- **Feature Requests**: Open a discussion

## 🎉 What's Next?

Future features we're planning:
- 🎨 **Visual Game Builder**: Drag-and-drop interface
- 🎵 **Sound Library**: Built-in sound effects and music
- 🌐 **Multiplayer Games**: Real-time multiplayer support
- 📱 **Mobile Apps**: Convert games to mobile apps
- 🎭 **Game Templates**: Pre-built game templates
- 🔄 **Game Export**: Export to various formats (Unity, Godot, etc.)

---

**Happy Game Creating! 🎮✨**

*Made with ❤️ by the AI Game Generator team*
