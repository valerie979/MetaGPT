import asyncio
from metagpt.roles import TutorialAssistant

def test_tutorial_assistant():
    # Create an instance of the Tutorial Assistant role
    tutorial_assistant = TutorialAssistant()

    # Run the Tutorial Assistant with a sample topic
    result = asyncio.run(tutorial_assistant.run("Sample Topic"))

    # Assert that the output is as expected
    assert result == ["Introduction", "Setup", "Basic Concepts", "Advanced Concepts", "Conclusion"]