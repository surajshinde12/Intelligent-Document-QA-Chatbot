#!/bin/bash

set -e

echo "======================================"
echo "Starting Ollama..."
echo "======================================"

# Start Ollama server in background
ollama serve > /tmp/ollama.log 2>&1 &

# Wait for Ollama server
echo "Waiting for Ollama..."

until curl -s http://localhost:11434/api/tags > /dev/null 2>&1
do
    sleep 2
done

echo "Ollama is ready."

echo "======================================"
echo "Checking Llama 3.2..."
echo "======================================"

# Download model if it does not already exist
if ! ollama list | grep -q "llama3.2"; then

    echo "Llama 3.2 not found."
    echo "Downloading Llama 3.2..."

    ollama pull llama3.2

else

    echo "Llama 3.2 already exists."

fi

echo "======================================"
echo "Starting Streamlit..."
echo "======================================"

streamlit run app.py \
    --server.address=0.0.0.0 \
    --server.port=8501