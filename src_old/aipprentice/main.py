import sys
from aipprentice.crew import LinkedinMarketingCrew
from .prompts import rule_set, style_guide, template_set, emotion_set, previous_posts, linkedin_profile

def run():
  """
  Run the crew.
  """
  inputs = {
    'topic': """I watched this movie and it changed what I needed my future to be. 
It was 2019 when I stumbled across Ready, Player One. The movie, as a piece of entertainment, by itself is a 7/10. But the concept hooked me in - a globally networked virtual reality most of humanity used - a world with endless possibilities. Back then I felt limited by technology. But now """,
    'linkedin_profile': linkedin_profile,
    'rule_set': rule_set,
    'style_guide': style_guide,
    'template_set': template_set,
    'previous_posts': previous_posts,
    'emotion_set': emotion_set,
  }
  LinkedinMarketingCrew().crew().kickoff(inputs=inputs)
