# Ollama and Mem0AI Setup and Usage Guide

This guide provides instructions for installing, setting up, and running **Ollama** and **mem0ai** locally using Python.

## Ollama Set Up

1. **Download Ollama**
    Download Ollama from the link on [Ollama Github repo](https://github.com/ollama/ollama) or on [Ollama website](https://ollama.com/)

2. **Pull a model**
    ```bash
    ollama pull gemma:2b
3. **Run a model**
    ```bash
    ollama run gemma:2b
4. **Customize a model - example**
    ```bash
    ollama create example -f Modelfile
    ollama run example

## Mem0AI Set Up

1. **Install mem0ai package**
    ```bash
    pip install mem0ai
2. **Obtain an API Key**
Sign up for Mem0AI and obtain your API key from the [Mem0AI Dashboard](https://app.mem0.ai/dashboard/api-keys).
3. **Execute script - example**
    ```bash
    python mem0ai.py
Check activity on Mem0AI dashboard to see old and new memory.
