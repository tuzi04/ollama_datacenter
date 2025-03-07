#!/bin/bash
sbatch -p [PARTITION] -q [QOS] --gres=gpu:[GPUS] -J [JOBNAME] --time=3-00:00:0 run.sh
