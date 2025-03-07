# How to run Ollama on Datacenter using docker, podman or singularity
## Overview
This library helps to use Ollama in your local computer or server using docker, podman or singularity.
Ollam is an API for prompting LLM easily. While it serves several useful functions, it is hard to find how to use it right away in server.
This library provides ready-made shell files and python files for inferencing LLMs using ollama.
For more details, you can check the official [**website**](https://ollama.com) and [**github**](https://github.com/ollama/ollama).
There will be the list of models and detailed guidelines for using ollama.

## Fast Start
Pull this repository first and choose which container platform to use.
Then, install the requirements on Anaconda using following commands.

```bash
conda create -n ollama python=3.10
conda activate ollama
pip install -r requirements.txt
```
Now follow the guidelines for each container platform.
Each of them contains [MODEL] and [PORT] as arguments.
You can choose models from official [**website**](https://ollama.com).
The default port is 11434 but you need to change it, if it is already in use.

## Docker

### Pulling Image
```bash
sh pull_image.sh
```

### Pulling Model
You need to change [MODEL] and [PORT].
```bash
sh pull_model.sh
```

### Running Model
You need to change [MODEL] and [PORT].
```bash
sh run.sh
```

## Podman

### Pulling Image
```bash
sh pull_image.sh
```

### Pulling Model
You need to change [MODEL] and [PORT].
```bash
sh pull_model.sh
```

### Running Model
You need to change [MODEL] and [PORT].
```bash
sh run.sh
```

## Singularity

### Pulling Image
```bash
sh build.sh
```

### Pulling Model
You need to change [MODEL] and [PORT].
```bash
sh pull_model.sh
```

### Running Model
You need to change [MODEL] and [PORT].
```bash
sh sbatch.sh
```
