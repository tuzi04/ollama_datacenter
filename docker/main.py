import sys
from datasets import load_dataset
from tqdm import tqdm
from ollama import Client
import timeout_decorator
from timeout_decorator.timeout_decorator import TimeoutError
import time
import os

# Generation using LLM with time constraint
@timeout_decorator.timeout(60) # You can change the time limit.
def call_LLM(client, model, prompt):
    return client.chat(
        model=model,
        messages=[{
            'role': 'user',
            'content': prompt,
        }]
        # ,
        # options = {
        #     "temperature": 0
        # }
    )

def restart_ollama():
    os.system("docker stop ollama") # It makes an error message when it runs for the first time.
    time.sleep(20)
    os.sytem(f"docker run --rm -d --init --security-opt=label=disable --mount=type=bind,src=.,dst=/mnt/workspace --device=nvidia.com/gpu=0 --hooks-dir=/usr/share/containers/oci/hooks.d/ -v ollama:/root/.ollama -p {sys.argv[2]}:11434 --name ollama ollama/ollama")
    client = Client(
        host=f'http://localhost:{sys.argv[2]}',
    )
    return client

# Initiating Ollama
client = restart_ollama()

# Preparing Model and Prompt
model = sys.argv[1] # Model must be pulled first from the ollama.com
prompt =""

# Inferencing
flag = True # flag for restarting ollama
for i in range(1000):
    if i%500 == 0 or flag:
        client = restart_ollama()
        flag = False
    try:
        response = call_LLM(client, model, prompt)
        print(f"{response.message.content}")
    except TimeoutError as error:
        print(f"TIME OUT")
        flag = True
