import sys
from datasets import load_dataset
from tqdm import tqdm
from ollama import Client
import timeout_decorator
from timeout_decorator.timeout_decorator import TimeoutError
import time
import subprocess

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

def restart_ollama(sp):
    if sp != -1:
        sp = subprocess.Popen(f"kill -9 {sp.pid}" , stdout=subprocess.PIPE, shell=True)
        time.sleep(20)
    sp = subprocess.Popen(f"singularity exec --writable --nv --env OLLAMA_HOST=0.0.0.0:{sys.argv[2]},OLLAMA_LOAD_TIMEOUT=20m ~/ollama ollama serve 1>> /dev/null 2>&1 &" , shell=True)
    
    client = Client(
        host=f'http://localhost:{sys.argv[2]}', # sys.argv[2] is a port number which should not be currently used. ex) 11434
    )
    return client, sp

# Initiating Ollama
sp = -1
client, sp = restart_ollama(sp)

# Preparing Model and Prompt
model = sys.argv[1] # Model must be pulled first from the ollama.com
prompt =""

# Inferencing
flag = True # flag for restarting ollama
for i in range(1000):
    if i%500 == 0 or flag: 
        client,sp = restart_ollama(sp)
        flag = False
    try:
        response = call_LLM(client, model, prompt)
        print(f"{response.message.content}")
    except TimeoutError as error:
        print(f"TIME OUT")
        flag = True
