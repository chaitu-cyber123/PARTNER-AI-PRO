from ai.planner import plan
from ai.thinking import think
from ai.reasoner import reason
from ai.action_engine import execute


def run(user_message):

    # Step 1
    plan_result = plan(user_message)

    # Step 2
    thought = think(user_message)

    # Step 3
    reasoning = reason(user_message)

    # Step 4
    action = execute(
        plan_result,
        user_message
    )

    return {
        "plan": plan_result,
        "thought": thought,
        "reasoning": reasoning,
        "action": action
    }
