# Personal Assistant Agent

A personal AI assistant prototype based on RAG, tool calling, and LLM agents.

This project is designed to explore how large language models can be used to build a personal AI assistant that supports task planning, document understanding, retrieval-augmented generation, and tool-based execution.

## Features

- Task planning with LLM agents
- Retrieval-Augmented Generation for document QA
- Tool calling for external functions
- Modular agent architecture
- Long-context assistant workflow
- Future support for multi-agent collaboration

## Project Structure

```text
personal-assistant-agent/
├── main.py
├── config.py
├── requirements.txt
├── agents/
│   ├── planner_agent.py
│   └── executor_agent.py
├── rag/
│   ├── document_loader.py
│   ├── text_splitter.py
│   └── simple_retriever.py
├── tools/
│   └── calculator_tool.py
└── examples/
    └── demo_task.md
