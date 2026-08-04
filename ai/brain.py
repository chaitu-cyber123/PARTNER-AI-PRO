import requests
from kernel.kernel import kernel
from config import (
    BASE_URL,
    MODEL,
    SYSTEM_PROMPT
)

from ai.planner import plan
from ai.correction import process_correction
from ai.memory_router import process_memory
from ai.knowledge import search_knowledge
from ai.memory import (
    smart_recall,
    add_context
)
from ai.context import (
    load_context,
    save_context
)
from ai.vision import analyze_image
from core.reference_resolver import resolve_reference
from core.manager import process
from core.context_tracker import update_context

def ask(prompt, image_path=None):

    add_context(
        "user",
        prompt
    )

    update_context(prompt)

    text = prompt.lower().strip()

    reference = resolve_reference(prompt)
    if reference:

        prompt = prompt.replace("it", reference)

        prompt = prompt.replace("that", reference)

        prompt = prompt.replace(
            "previous file",
            reference
        )

        prompt = prompt.replace(
            "last file",
            reference
        )

        text = prompt.lower()

    # -------------------------
    # IMAGE ANALYSIS
    # -------------------------

    if image_path:

        try:

            result = analyze_image(
                image_path,
                prompt
            )

            add_context(
                "partner",
                result
            )

            return result

        except Exception as e:

            return f"Vision Error: {e}"

    # -------------------------
    # INPUT CORRECTION
    # -------------------------

    correction = process_correction(prompt)

    if correction:

        add_context(
            "partner",
            correction
        )

        return correction

    # -------------------------
    # PLANNER
    # -------------------------

    planner = plan(prompt)

        # -------------------------
    # Memory Learning
    # -------------------------

    memory_result = process_memory(prompt)

    if memory_result:

        add_context(
            "partner",
            memory_result
        )

        return memory_result

    # -------------------------
    # Smart Memory Recall
    # -------------------------

    memory_answer = smart_recall(text)

    if memory_answer:

        reply = f"I remember that: {memory_answer}"

        add_context(
            "partner",
            reply
        )

        return reply

    # -------------------------
    # Skills
    # -------------------------

    if planner["action"] == "skill":

        result = process(prompt)

        if result:

            add_context(
                "partner",
                result
            )

            return result

    # -------------------------
    # Knowledge Search
    # -------------------------

    knowledge = search_knowledge(prompt)

    if knowledge:

        add_context(
            "partner",
            knowledge
        )

        return knowledge

    # -------------------------
    # Conversation Context
    # -------------------------

    context = load_context()

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }

    ]

    for item in context[-10:]:

        messages.append(
            {
                "role": item["role"],
                "content": item["content"]
            }
        )

         # -------------------------
    # OpenRouter AI
    # -------------------------

    try:

        response = requests.post(

            BASE_URL,

            headers={
                "Authorization": f"Bearer {MODEL if False else ''}",
                "Content-Type": "application/json"
            },

            json={

                "model": MODEL,

                "messages": messages

            },

            timeout=60

        )

        data = response.json()

        reply = data["choices"][0]["message"]["content"].strip()

        add_context(
            "partner",
            reply
        )

        return reply

    except Exception as e:

        return f"AI Error: {e}"
def ask(prompt, image_path=None):
    return kernel.run(prompt)
