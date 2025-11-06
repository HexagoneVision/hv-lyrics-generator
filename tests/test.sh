#!/bin/bash

# Get current directory path
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_DIR="$SCRIPT_DIR/.."

cd $PROJECT_DIR

mkdir -p ./output
python3 script.py --input ./docs/example.slrc --output ./output/song.luau --name "La Marseillaise" --author "Rouget de Lisle" --id 120439399722201
