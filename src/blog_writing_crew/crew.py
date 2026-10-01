from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class BlogWritingCrew():
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

    @task
    def research_task(self) -> Task:
        """Task for the researcher agent to gather information and insights for blog posts."""
        return Task(config=self.tasks_config['research_task'])

    @task
    def writing_task(self) -> Task:
        """Task for the writer agent to draft blog posts based on research."""
        return Task(config=self.tasks_config['writing_task'])

    @task
    def editing_task(self) -> Task:
        """Task for the editor agent to review and refine blog posts."""
        return Task(config=self.tasks_config['editing_task'], output_file='output/blog_post.md')

    @crew
    def crew(self) -> Crew:
        """Define the crew with its agents and tasks."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )