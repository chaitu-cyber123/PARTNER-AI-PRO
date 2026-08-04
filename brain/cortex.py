from brain.perception import perceive
from brain.memory import recall
from brain.knowledge import search
from brain.reasoning import reason
from brain.planner import plan
from brain.executor import execute
from brain.learner import learn
from brain.responder import respond


def think(message):

    state = {}

    # -----------------------------
    # PERCEPTION
    # -----------------------------
    state["input"] = message
    state["perception"] = perceive(message)

    # -----------------------------
    # MEMORY
    # -----------------------------
    state["memory"] = recall(state)

    # -----------------------------
    # KNOWLEDGE
    # -----------------------------
    state["knowledge"] = search(state)

    # -----------------------------
    # REASONING
    # -----------------------------
    state["reasoning"] = reason(state)

    # -----------------------------
    # PLANNING
    # -----------------------------
    state["plan"] = plan(state)

    # -----------------------------
    # EXECUTION
    # -----------------------------
    state["result"] = execute(state)

    # -----------------------------
    # LEARNING
    # -----------------------------
    learn(state)

    # -----------------------------
    # RESPONSE
    # -----------------------------
    return respond(state)
