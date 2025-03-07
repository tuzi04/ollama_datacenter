#!/bin/bash
docker run --rm -d --init --security-opt=label=disable --mount=type=bind,src=.,dst=/mnt/workspace --device=nvidia.com/gpu=0 --hooks-dir=/usr/share/containers/oci/hooks.d/ -v ollama:/root/.ollama -p [PORT]:11434 --name ollama ollama/ollama
docker exec ollama ollama pull [MODEL]
docker stop ollama
