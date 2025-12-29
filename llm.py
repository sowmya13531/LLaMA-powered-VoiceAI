import subprocess

MODEL = 'llama3.2'


def ask_llama(prompt, context=" "):
    full_prompt = f'''
{context}
User: {prompt}
Assistant:
'''
    result = subprocess.run(
        ['ollama', 'run', MODEL],
        input=full_prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()
