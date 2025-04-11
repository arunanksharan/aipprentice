# src/latest_ai_development/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai_tools import SerperDevTool
from datetime import datetime


@CrewBase
class LinkedinMarketingCrew():
  """Linkedin Marketing Crew"""

  @before_kickoff
  def before_kickoff_function(self, inputs):
    print(f"Before kickoff function with inputs: {inputs}")
    return inputs # You can return the inputs or modify them as needed

  @after_kickoff
  def after_kickoff_function(self, result):
    print(f"After kickoff function with result: {result}")
    return result # You can return the result or modify it as needed


  @agent
  def linkedin_marketing_specialist(self) -> Agent:
    return Agent(
      config=self.agents_config['linkedin_marketing_specialist'],
      verbose=True,
      tools=[]
    )

  @task
  def linkedin_marketing_specialist_task(self) -> Task:
    return Task(
      config=self.tasks_config['linkedin_marketing_specialist_task'],
      output_file=f'output/post_{datetime.now()}.md' # This is the file that will be contain the final report.
    )

  @crew
  def crew(self) -> Crew:
    """Creates the Linkedin Marketing crew"""
    return Crew(
      agents=self.agents, # Automatically created by the @agent decorator
      tasks=self.tasks, # Automatically created by the @task decorator
      process=Process.sequential,
      verbose=True,
    )
