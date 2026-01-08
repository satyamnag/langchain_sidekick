import os
import requests
from dotenv import load_dotenv
from playwright.async_api import async_playwright

from langchain_core.tools import Tool
from langchain_experimental.tools import PythonREPLTool

from langchain_community.agent_toolkits import (
    FileManagementToolkit,
    PlayWrightBrowserToolkit,
)
from langchain_community.tools.arxiv.tool import ArxivQueryRun
from langchain_community.tools.openai_dalle_image_generation.tool import (
    OpenAIDALLEImageGenerationTool,
)
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.tools.youtube.search import YouTubeSearchTool
from langchain_community.tools import (
    DuckDuckGoSearchRun,
    DuckDuckGoSearchResults,
)
from langchain_community.tools.wikidata.tool import WikidataAPIWrapper, WikidataQueryRun
from langchain_community.tools.semanticscholar.tool import SemanticScholarQueryRun

from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain_community.utilities.google_serper import GoogleSerperAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_community.utilities import SearchApiAPIWrapper
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.utilities import OpenWeatherMapAPIWrapper

load_dotenv(override = True)

pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"

serper = GoogleSerperAPIWrapper()
wikipedia = WikipediaAPIWrapper()
dalle = DallEAPIWrapper(model = "dall-e-2")
searchapi = SearchApiAPIWrapper()
serp = SerpAPIWrapper()
weather = OpenWeatherMapAPIWrapper()
wikidata = WikidataAPIWrapper()

async def playwright_tools():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless = False)
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser = browser)
    return toolkit.get_tools(), browser, playwright

def push(text: str):
    """Send a push notification to the user"""
    response = requests.post(
        pushover_url,
        data = {
            "token": pushover_token,
            "user": pushover_user,
            "message": text,
        },
    )
    return (
        "success"
        if response.status_code == 200
        else f"failed: {response.text}"
    )

def get_file_tools():
    toolkit = FileManagementToolkit(root_dir = "sandbox")
    return toolkit.get_tools()

async def other_tools():
    push_tool = Tool(
        name = "push_tool",
        func = push,
        description = "Use this tool when you want to send a push notification",
    )

    file_tools = get_file_tools()

    serper_tool = Tool(
        name = "search",
        func = serper.run,
        description = (
            "Use this tool when you want to get the results of an "
            "online web search"
        ),
    )

    wiki_tool = WikipediaQueryRun(name = "wiki_tool", api_wrapper = wikipedia)

    python_repl_tool = PythonREPLTool(name = "python_repl_tool")

    youtube_tool = YouTubeSearchTool(name = "youtube_tool")

    arxiv_tool = ArxivQueryRun(name = "arxiv_tool")

    duckduckgo_run_tool = DuckDuckGoSearchRun(name = "duckduckgo_run_tool")
    
    duckduckgo_results_tool = DuckDuckGoSearchResults(name = "duckduckgo_results_tool")

    image_generation_tool = OpenAIDALLEImageGenerationTool(
        name = "image_generation_tool",
        api_wrapper = dalle
    )

    searchapi_tool = Tool(
        name = "searchapi_tool",
        func = searchapi.run,
        description = (
            "Use this tool to search the web using SearchApi and retrieve "
            "online information."
        ),
    )

    serp_tool = Tool(
        name = "serp_tool",
        func = serp.run,
        description = "Searches Google via SerpAPI. Returns rich, real-time results"
    )

    weather_tool = Tool(
        name = "weather_tool",
        func = weather.run,
        description = "Retrieves current weather conditions and short-term forecast via OpenWeatherMap."
    )

    wikidata_tool = WikidataQueryRun(name = "wikidata_tool", api_wrapper = wikidata)

    semanticscholar_tool = SemanticScholarQueryRun(name = "semanticscholar_tool")

    return file_tools + [
        push_tool,
        serper_tool,
        duckduckgo_run_tool,
        duckduckgo_results_tool,
        searchapi_tool,
        python_repl_tool,
        wiki_tool,
        youtube_tool,
        arxiv_tool,
        image_generation_tool,
        serp_tool,
        weather_tool,
        wikidata_tool,
        semanticscholar_tool,
    ]