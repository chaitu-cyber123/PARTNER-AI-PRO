def plan(state):

    intent = state["perception"]["intent"]

    plan = []

    if intent == "conversation":
        plan.append("Generate conversational response")

    else:
        plan.append("Execute matching skill")

    return {
        "intent": intent,
        "steps": plan
    }

