#!/bin/bash
singularity exec --writable --nv ~/ollama ollama pull $model
