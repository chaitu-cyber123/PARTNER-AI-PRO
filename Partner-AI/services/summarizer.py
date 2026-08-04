def summarize_news(headlines):

    try:

        if isinstance(headlines, list):

            return "\n".join(
                f"• {item}"
                for item in headlines[:5]
            )

        return str(headlines)

    except Exception:

        return str(headlines)
