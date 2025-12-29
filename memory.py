conversation_history = []


def add_to_memory(role, text):
    conversation_history.append(f'{role}: {text}')


def get_context():
    return "\n".join(conversation_history[-6:])
