# How to run Ollama on Datacenter using Docker, Podman or Singularity
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

Now, follow the guidelines for each container platform.

Each of them contains [MODEL] and [PORT] as arguments.

You can use 11434 as a default for [PORT] but you need to change it if port is already in use.

I recommend you to use a number from 11380 to 11750.

If you or other people use several containers with the same port number, it will cause an error.

You can choose models from official [**website**](https://ollama.com).

## Docker

#### Pulling Image
It pull the official docker image of ollama from the [**Docker Hub**](https://hub.docker.com/r/ollama/ollama).
```bash
sh pull_image.sh
```

#### Pulling Model
It pulls a model(e.g. phi) using the container.
```bash
sh pull_model.sh [MODEL] [PORT]
```

#### Running Model
It runs main.py using the ollama client.

If you want to use more GPUs, you can change the option --device=nvidia.com/gpu=0 into --device=nvidia.com/gpu=all in main.py file.
```bash
sh run.sh [MODEL] [PORT]
```

## Podman
It pull the official docker image of ollama from the [**Docker Hub**](https://hub.docker.com/r/ollama/ollama).
#### Pulling Image
```bash
sh pull_image.sh 
```

#### Pulling Model
It pulls a model(e.g. phi) using the container.
```bash
sh pull_model.sh [MODEL] [PORT]
```

#### Running Model
It runs main.py using the ollama client.

If you want to use more GPUs, you can change the option --device=nvidia.com/gpu=0 into --device=nvidia.com/gpu=all in main.py file.
```bash
sh run.sh [MODEL] [PORT]
```

## Singularity
It pull the official docker image of ollama from the [**Docker Hub**](https://hub.docker.com/r/ollama/ollama) and build it into singularity image.

A directory named ollama will be created in your $HOME directory as a singularity image.
#### Pulling Image
```bash
sh build.sh
```

#### Pulling Model
You can download models from ollama.com by using the following command. (e.g. phi)
```bash
sh pull_model.sh [MODEL] and [PORT]
```

#### Running Model
It runs main.py using the ollama client.

You need to change [MODEL] and [PORT] in run.sh and [PARTITION], [QOS], [GPUS] and [JOBNAME] in sbatch.sh manually.
```bash
sh sbatch.sh
```
