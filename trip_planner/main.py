from crewai import Crew
from textwrap import dedent
from trip_agents import TripAgents
from trip_tasks import TripTasks
from langchain_openai import ChatOpenAI
import os
os.environ["OPENAI_API_KEY"] = "NA"

def host_llm():
    llm: ChatOpenAI = ChatOpenAI(
        base_url="http://10.0.192.75:8080/lm-studio/v1" ,
        #base_url="http://localhost:8001/v1",
        temperature=0,
        api_key="not-needed")
    return llm
llm =host_llm()
# llm = ChatOpenAI(
#     model = "crewai-llama3",
#     base_url = "http://localhost:11434/v1")
class TripCrew:

    def __init__(self, origin, cities, data_range, intrest):
        self.origin = origin,
        self.cities = cities,
        self.interest = intrest,
        self.date_range = data_range,

    def run(self):
        agents = TripAgents()
        tasks = TripTasks()
        city_selector_agent = agents.city_selection_agent(llm)
        local_expert_agent = agents.local_expert(llm)
        travel_concierge_agent = agents.travel_concierge(llm)

        identify_task  = tasks.identify_task(
            city_selector_agent,
            self.origin,
            self.cities,
            self.date_range,
            self.interest
        )

        gather_task = tasks.gather_task(
            local_expert_agent,
            self.origin,
            self.interest,
            self.date_range
            )
        plan_task = tasks.plan_task(
            travel_concierge_agent, 
            self.origin,
            self.interest,
            self.date_range
            )
        

        crew = Crew(
            agents=[
                city_selector_agent,
                local_expert_agent,
                travel_concierge_agent,
            ],
            tasks= [identify_task, 
                    gather_task,
                    plan_task],
            verbose=True
        )

        

        result = crew.kickoff()
        return result
    

if __name__ =="__main__":

    print("## Welcome to Trip Planner Crew")
    print('-------------------------------')
    location ="Delhi"
    # input(
    # dedent("""
    #   From where will you be traveling from?
    # """))
    cities = "Banglore or Goa"
    # input(
    # dedent("""
    #   What are the cities options you are interested in visiting?
    # """))
    date_range ="22 jun to 27 jun 2024"
    #input(
    # dedent("""
    #   What is the date range you are interested in traveling?
    # """))
    interests =  "Night Life and Cricket" #input(
    # dedent("""
    #   What are some of your high level interests and hobbies?
    # """))
    trip_crew = TripCrew(location, cities, date_range, interests)
    
    result = trip_crew.run()



