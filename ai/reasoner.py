from ai.thinking import think
from ai.response_generator import generate_response


def reason(user_message):

    thought = think(user_message)

    memory = thought["memory"]
    knowledge = thought["knowledge"]

    # Both memory and knowledge available
    if memory and knowledge:
        combined = (
            f"{knowledge}\n\n"
            f"I also remember: {memory}"
        )
        return generate_response(
            user_message,
            knowledge=combined
        )

    # Memory only
    if memory:
        return generate_response(
            user_message,
            memory=memory
        )

    # Knowledge only
    if knowledge:
        return generate_response(
            user_message,
            knowledge=knowledge
        )

    # Unknown
    return generate_response(user_message)
