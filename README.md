# LangChain Sidekick

**A persistent AI co-worker that works on your tasks until they meet your success criteria.**

Sidekick is an AI agent built with **LangChain** and **LangGraph** that keeps iterating on a task — using tools, browsing the web, running code, searching, and more (15+ tools) — until an evaluator confirms that the user-defined success criteria are met or until it needs clarification from you.

It features a self-improving loop: after each attempt, an evaluator LLM reviews the response, provides feedback, and decides whether to accept the answer, ask you for input, or send the agent back to work.

The app includes a clean **Gradio** chat interface where you can provide a task and optional explicit success criteria.

## Features

- **Persistent task execution** via a LangGraph state machine (worker → tools → evaluator → loop or end)

- **Rich toolset**:
  - Browser automation (Playwright) for navigating and extracting web content
  - Multiple search engines (Google Serper, SerpAPI, SearchApi, DuckDuckGo)
  - Wikipedia, Wikidata, YouTube search, Arxiv, Semantic Scholar
  - Python REPL for code execution
  - DALL·E image generation
  - File management in a sandbox directory
  - Current weather lookup
  - Push notifications via Pushover

- **Evaluator node** that critically assesses progress against your success criteria
- **Memory** via LangGraph checkpointer (conversation history preserved across loops)
- **Gradio UI** with task input and optional success criteria field

## Demo Screenshot

![langchain_sidekick_screenshot](https://github.com/satyamnag/langchain_sidekick/blob/da1f8f7bec217fbc5d76d7c37a3ed1388343ba76/assets/langchain_sidekick_screenshot.png)
