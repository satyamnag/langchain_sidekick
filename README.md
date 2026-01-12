# 🚀 LangChain Sidekick

**A persistent AI co-worker that works on your tasks until they meet your success criteria.**

Sidekick is an AI agent built with **LangChain** and **LangGraph** that keeps iterating on a task — using tools, browsing the web, running code, searching, and more (15+ tools) — until an evaluator confirms that the user-defined success criteria are met or until it needs clarification from you.

It features a self-improving loop: after each attempt, an evaluator LLM reviews the response, provides feedback, and decides whether to accept the answer, ask you for input, or send the agent back to work.

## ✨ Features

- 🔁 **Persistent task execution** via a LangGraph state machine (worker → tools → evaluator → loop or end)

- 🧰 **Rich toolset**:
  - 🔎 Browser automation (Playwright) for navigating and extracting web content
  - 🌐 Multiple search engines (Google Serper, SerpAPI, SearchApi, DuckDuckGo)
  - 📚 Wikipedia, Wikidata, YouTube search, Arxiv, Semantic Scholar
  - 🐍 Python REPL for code execution
  - 🎨 DALL·E image generation
  - 📁 File management in a sandbox directory
  - ⛅ Current weather lookup
  - 📨 Push notifications via Pushover

- 🧠 **Evaluator node** that critically assesses progress against your success criteria
- 📝 **Memory** via LangGraph checkpointer (conversation history preserved across loops)
- 💬 **Gradio UI** with task input and optional success criteria field

## 🖼️ Demo Screenshot

![langchain_sidekick_screenshot](https://github.com/satyamnag/langchain_sidekick/blob/da1f8f7bec217fbc5d76d7c37a3ed1388343ba76/assets/langchain_sidekick_screenshot.png)

## 🔐 Environment Variables
#### PUSHOVER_USER=your pushover user ID
#### PUSHOVER_TOKEN=your pushover token
#### OPENAI_API_KEY=your openai api key
#### SERPER_API_KEY=your serper api key
#### YDC_API_KEY=your YDC api key
#### LANGSMITH_TRACING=true
#### LANGSMITH_ENDPOINT=https://api.smith.langchain.com
#### LANGSMITH_API_KEY=your langsmith api key
#### LANGSMITH_PROJECT=sidekick
#### SEARCHAPI_API=your searchapi api key
#### SERPAPI_API_KEY=your serpapi api key
#### OPENWEATHERMAP_API_KEY=your openweather api key
