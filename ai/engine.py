from ai.planner import plan
from ai.thinking import think
from ai.reasoner import reason
from ai.decision_engine import decide


def process(user_message):

    planner_result = plan(user_message)

    if planner_result["action"] == "skill":
        return {
            "type": "skill",
            "data": planner_result
        }

    thought = think(user_message)

    decision = decide(user_message)

    return {
        "type": "response",
        "planner": planner_result,
        "thought": thought,
        "decision": decision
    }
