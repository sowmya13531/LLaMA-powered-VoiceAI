from tts import speak
from sst import listen
from llm import ask_llama
from memory import add_to_memory, get_context

speak('Hello. I am your AI Assistant! How can i assist you today?')

while True:
    user_text = listen()

    if user_text.lower() in ['exit', 'quit', 'stop']:
        speak('Goodbye')
        break

    if user_text:
        add_to_memory('User', user_text)
        context = get_context()

        reply = ask_llama(user_text, context)
        add_to_memory('Assistant', reply)
        print('AI:', reply)
        speak(reply)
