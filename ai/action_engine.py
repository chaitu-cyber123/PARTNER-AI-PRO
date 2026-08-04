from core.manager import process


def execute(plan_result, user_message):

    if plan_result["action"] == "skill":

        result = process(user_message)

        return {
            "success": result is not None,
            "result": result
        }

    return {
        "success": False,
        "result": None
    }
