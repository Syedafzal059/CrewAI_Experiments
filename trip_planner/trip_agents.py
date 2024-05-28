
from crewai import Agent
from langchain.llms import OpenAI

#from tools.browser_tools import BrowserTools
#from tools.calculator_tools import CalculatorTool
#from tools.search_tools import SearchTools
from crewai_tools import ScrapeWebsiteTool, SerperDevTool


search_tool = SerperDevTool()
scrap_tool = ScrapeWebsiteTool()

class TripAgents():

  def city_selection_agent(self, llm):
    return Agent(
        role='City Selection Expert',
        goal='Select the best city based on weather, season, and prices',
        backstory=
        'An expert in analyzing travel data to pick ideal destinations',
        tools=[
            # SearchTools.search_internet,
            # BrowserTools.scrap_and_summarize_website,
            scrap_tool,
            search_tool,
        ],
        llm= llm,
        verbose=True)
  

  def local_expert(self,llm):
    return Agent(
        role='Local Expert at this city',
        goal='Provide the BEST insights about the selected city',
        backstory="""A knowledgeable local guide with extensive information
        about the city, it's attractions and customs""",
        tools=[
            #SearchTools.search_internet,
            #BrowserTools.scrap_and_summarize_website,
            scrap_tool,
            search_tool,
        ],
        llm= llm,
        verbose=True)

  def travel_concierge(self,llm):
    return Agent(
        role='Amazing Travel Concierge',
        goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the city""",
        backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
        tools=[
            # SearchTools.search_internet,
            # BrowserTools.scrap_and_summarize_website,
            search_tool,
 #           CalculatorTool.calculate,
        ],
        llm=llm,
        verbose=True)