learning_log = []


def learn(state):

    learning_log.append({

        "input": state["input"],

        "intent": state["perception"]["intent"],

        "success": state["result"] is not None

    })
