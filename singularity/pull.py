import subprocess
import sys

model = sys.argv[1]
port = sys.argv[2]

sp = subprocess.Popen(f"singularity exec --writable --nv --env OLLAMA_HOST=0.0.0.0:{port} ~/ollama ollama serve 1>> /dev/null 2>&1 &", shell=True)
sp2 = subprocess.Popen(f"singularity exec --writable --nv ~/ollama ollama pull {model}", shell=True)
subprocess.Popen(f"kill -9 {sp.pid}", stdout=subprocess.PIPE, shell=True)