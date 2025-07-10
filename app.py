import os
import gradio as gr
from groq import Groq
import json
from datetime import datetime

# Get API key from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Configuration
class ChatbotConfig:
    def __init__(self):
        self.model = "llama3-8b-8192"
        self.max_tokens = 1000
        self.temperature = 0.7
        self.system_prompt = "You are a helpful AI assistant. Be concise and informative."

# Chatbot class
class GroqChatbot:
    def __init__(self, api_key, config):
        self.config = config
        self.client = Groq(api_key=api_key) if api_key else None
        self.conversation_history = []
        self.add_system_message(config.system_prompt)
        
    def add_system_message(self, content):
        self.conversation_history.append({
            "role": "system",
            "content": content
        })
        
    def add_user_message(self, content):
        self.conversation_history.append({
            "role": "user", 
            "content": content
        })
        
    def add_assistant_message(self, content):
        self.conversation_history.append({
            "role": "assistant",
            "content": content
        })
        
    def get_response(self, user_input):
        if not self.client:
            return "❌ Error: API key not configured. Please set GROQ_API_KEY in environment variables."
        
        try:
            self.add_user_message(user_input)
            
            completion = self.client.chat.completions.create(
                messages=self.conversation_history,
                model=self.config.model,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                stream=False
            )
            
            response = completion.choices[0].message.content
            self.add_assistant_message(response)
            
            return response
            
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def change_model(self, model_name):
        self.config.model = model_name
        
    def set_temperature(self, temp):
        self.config.temperature = max(0.0, min(2.0, temp))
        
    def set_system_prompt(self, prompt):
        self.config.system_prompt = prompt
        if self.conversation_history and self.conversation_history[0]["role"] == "system":
            self.conversation_history[0]["content"] = prompt
        else:
            self.conversation_history.insert(0, {"role": "system", "content": prompt})

# Available models (updated to remove decommissioned models)
AVAILABLE_MODELS = [
    "llama3-8b-8192",
    "llama3-70b-8192",
    "llama-3.1-8b-instant",
    "llama-3.3-70b-versatile",
    "gemma2-9b-it"
]

# Initialize chatbot
config = ChatbotConfig()
chatbot = GroqChatbot(GROQ_API_KEY, config)

# Custom CSS - Fixed for proper layout
custom_css = """
.gradio-container {
    max-width: 1200px !important;
    margin: auto !important;
}
.chat-message {
    padding: 10px !important;
    margin: 5px !important;
    border-radius: 10px !important;
}
footer {
    visibility: hidden;
}
"""

# Gradio interface functions
def chat_with_bot(message, history, model, temperature, system_prompt):
    if not message.strip():
        return history, history, ""
    
    # Update chatbot settings
    chatbot.change_model(model)
    chatbot.set_temperature(temperature)
    if system_prompt.strip():
        chatbot.set_system_prompt(system_prompt)
    
    # Get response
    response = chatbot.get_response(message)
    
    # Update history
    history.append([message, response])
    
    return history, history, ""

# Create main interface
def create_interface():
    with gr.Blocks(css=custom_css, title="Groq AI Chatbot", theme=gr.themes.Soft()) as iface:
        # Header
        gr.Markdown(
            """
            # 🤖 Groq AI Chatbot
            Experience lightning-fast AI conversations powered by Groq's inference engine!
            """
        )
        
        # API Key Status
        if not GROQ_API_KEY:
            gr.Markdown(
                """
                ⚠️ **API Key Required**: This app requires a Groq API key to function. 
                The administrator needs to set the `GROQ_API_KEY` environment variable.
                """
            )
        
        with gr.Row():
            with gr.Column(scale=3):
                # Main chat interface
                chatbot_interface = gr.Chatbot(
                    label="💬 Chat with AI",
                    height=500,
                    show_label=True,
                    avatar_images=["🧑‍💻", "🤖"],
                    bubble_full_width=False,
                    show_copy_button=True
                )
                
                with gr.Row():
                    msg = gr.Textbox(
                        placeholder="Type your message here and press Enter...",
                        label="Your Message",
                        lines=2,
                        max_lines=10,
                        scale=4
                    )
                    submit_btn = gr.Button("Send 📤", variant="primary")
            
            with gr.Column(scale=1):
                # Settings panel
                gr.Markdown("## ⚙️ Settings")
                
                model_dropdown = gr.Dropdown(
                    choices=AVAILABLE_MODELS,
                    value="llama3-8b-8192",
                    label="🧠 AI Model",
                    info="Choose your preferred model"
                )
                
                temperature_slider = gr.Slider(
                    minimum=0.0,
                    maximum=2.0,
                    value=0.7,
                    step=0.1,
                    label="🌡️ Temperature",
                    info="0=Focused, 1=Balanced, 2=Creative"
                )
                
                system_prompt_box = gr.Textbox(
                    value="You are a helpful AI assistant. Be concise and informative.",
                    label="🎭 System Prompt",
                    lines=4,
                    info="Define the AI's personality and behavior"
                )
        
        # Example prompts section
        gr.Markdown("## 💡 Try These Prompts")
        
        example_prompts = [
            "Explain quantum computing in simple terms",
            "Write a Python function to sort a list",
            "Create a short story about AI",
            "Help me plan a healthy meal",
            "Explain the latest trends in technology"
        ]
        
        # Create example buttons in rows
        with gr.Row():
            for i in range(3):
                if i < len(example_prompts):
                    btn = gr.Button(example_prompts[i], size="sm")
                    btn.click(lambda p=example_prompts[i]: p, outputs=[msg])
        
        with gr.Row():
            for i in range(3, 5):
                if i < len(example_prompts):
                    btn = gr.Button(example_prompts[i], size="sm")
                    btn.click(lambda p=example_prompts[i]: p, outputs=[msg])
        
        # Chat history state
        state = gr.State([])
        
        # Event handlers
        def submit_message(message, history, model, temperature, system_prompt):
            return chat_with_bot(message, history, model, temperature, system_prompt)
        
        # Submit events
        submit_btn.click(
            submit_message,
            inputs=[msg, state, model_dropdown, temperature_slider, system_prompt_box],
            outputs=[chatbot_interface, state, msg]
        )
        
        msg.submit(
            submit_message,
            inputs=[msg, state, model_dropdown, temperature_slider, system_prompt_box],
            outputs=[chatbot_interface, state, msg]
        )
        
        # Footer
        gr.Markdown(
            """
            ---
            
            🔗 **Links:** [Groq API](https://console.groq.com/) 
            
            💡 **Tip:** Use different models for different tasks - Llama3-8B for speed, Llama3-70B for complex reasoning!
            """
        )
    
    return iface

# Launch the interface
if __name__ == "__main__":
    demo = create_interface()
    demo.launch()
