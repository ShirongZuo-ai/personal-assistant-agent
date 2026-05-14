from agents.planner_agent import PlannerAgent
from agents.executor_agent import ExecutorAgent
from tools.calculator_tool import CalculatorTool


def main():
    user_task = "Help me plan how to build a RAG-based personal assistant."

    planner = PlannerAgent()
    executor = ExecutorAgent()
    calculator = CalculatorTool()

    plan = planner.create_plan(user_task)
    result = executor.execute_plan(plan)

    print("User Task:")
    print(user_task)

    print("\nGenerated Plan:")
    for step in plan:
        print(f"- {step}")

    print("\nExecution Result:")
    print(result)

    print("\nTool Calling Demo:")
    print("2 + 3 =", calculator.add(2, 3))


if __name__ == "__main__":
    main()
