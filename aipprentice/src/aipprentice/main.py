#!/usr/bin/env python
import sys
import warnings

from aipprentice.crew import LinkedinMarketingCrew
from .prompts import rule_set, style_guide, template_set, emotion_set, previous_posts, linkedin_profile


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

topic = """I watched this movie and it changed what I needed my future to be. 
It was 2019 when I stumbled across Ready, Player One. """

def run():
    """
    Run the crew.
    """
    inputs = {
    'topic': topic,
    'linkedin_profile': linkedin_profile,
    'rule_set': rule_set,
    'style_guide': style_guide,
    'template_set': template_set,
    'previous_posts': previous_posts,
    'emotion_set': emotion_set,
  }
    LinkedinMarketingCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        LinkedinMarketingCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        LinkedinMarketingCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        LinkedinMarketingCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
