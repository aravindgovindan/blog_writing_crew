from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class BlogWritingCrew(Crew):
    """Blog Writing Crew"""

    @agent
    def researcher(self) -> Agent:
        """Researcher agent responsible for gathering information and insights for blog posts."""
        return Agent(config=self.agents_config['researcher'], verbose=True)

    @agent
    def writer(self) -> Agent:
        """Writer agent responsible for drafting blog posts based on research."""
        return Agent(config=self.agents_config['writer'], verbose=True)

    @agent
    def editor(self) -> Agent:
        """Editor agent responsible for reviewing and refining blog posts."""
        return Agent(config=self.agents_config['editor'], verbose=True)