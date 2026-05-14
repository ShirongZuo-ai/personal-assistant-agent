class PlannerAgent:
    """
    PlannerAgent decomposes a user task into executable steps.
    """

    def create_plan(self, user_task: str) -> list[str]:
        return [
            "Analyze the user's task and identify the main goal.",
            "Retrieve relevant documents or background knowledge.",
            "Break the task into smaller executable steps.",
            "Select suitable tools or modules for each step.",
            "Generate a final response based on the execution results."
        ]
