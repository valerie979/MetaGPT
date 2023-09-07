import os
from metagpt.roles import Role
from metagpt.actions import WriteContent
from metagpt.tools.prompt_writer import GPTPromptGenerator

class TutorialAssistant(Role):
    def __init__(self, language="en-us"):
        super().__init__(language)
        self.prompt_generator = GPTPromptGenerator()

    async def run(self, topic):
        # Generate a directory structure for the tutorial topic
        directory_structure = self.generate_directory_structure(topic)

        # Break down the directory structure into separate modules
        modules = self.break_down_into_modules(directory_structure)

        # Handle each module individually as a write content action
        for module in modules:
            await self.handle_module(module)

    def generate_directory_structure(self, topic):
        # Use GPT to generate a directory structure for the tutorial topic
        # This is a placeholder and should be replaced with actual GPT code
        return ["Introduction", "Setup", "Basic Concepts", "Advanced Concepts", "Conclusion"]

    def break_down_into_modules(self, directory_structure):
        # Break down the directory structure into separate modules
        # Each module is based on a first level title
        return directory_structure

    async def handle_module(self, module):
        # Generate a tailored prompt for GPT
        prompt = self.prompt_generator.gen(f"Write a tutorial section about {module}", style='instruction')

        # Create a write content action
        action = WriteContent(prompt)

        # Execute the action
        await self.execute(action)