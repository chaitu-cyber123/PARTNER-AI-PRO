import os
import shutil

from core.context_engine import set_context, get_context


def files_command(message):

    text = message.lower().strip()
    print("FILES DEBUG:", text)
    # -------------------------
    # SHOW FILES
    # -------------------------

    if (
        text == "show files"
        or text == "list files"
        or "show my files" in text
        or "list my files" in text
        or "what files are available" in text
        or "what files do i have" in text
    ):

        files = os.listdir(".")

        if not files:
            return "No files found."

        return "\n".join(files)

    # -------------------------
    # FIND FILE
    # -------------------------

    if text.startswith("find "):

        filename = text.replace("find ", "").strip()

        for root, dirs, files in os.walk("."):

            for file in files:

                if filename in file.lower():

                    return os.path.join(root, file)

        return "File not found."

    # -------------------------
    # READ / OPEN FILE
    # -------------------------

    if text.startswith("read ") or text.startswith("open "):

        filename = (
            text.replace("read ", "")
            .replace("open ", "")
            .strip()
        )

        for root, dirs, files in os.walk("."):

            for file in files:

                if filename == file.lower():

                    path = os.path.join(root, file)

                    set_context(
                        "last_file",
                        path
                    )

                    # OPEN = only confirm
                    if text.startswith("open "):

                        return f"Opened {file}."

                    # READ = show content
                    if text.startswith("read "):

                        try:

                            with open(
                                path,
                                "r",
                                encoding="utf-8"
                            ) as f:

                                content = f.read(3000)

                            return content

                        except Exception as e:

                            return f"Cannot read file: {e}"

        return "File not found."
    # -------------------------
    # COPY FILE
    # -------------------------

    if text.startswith("copy "):

        try:

            command = message[5:].strip()

            parts = command.split(" to ")

            if len(parts) != 2:
                return "Use: Copy app.py to backup.py"

            source = parts[0].strip()
            destination = parts[1].strip()

            shutil.copy2(source, destination)

            return f"Copied '{source}' to '{destination}'."

        except FileNotFoundError:

            return "Source file not found."

        except Exception as e:

            return f"Copy failed: {e}"

    # -------------------------
    # MOVE / RENAME FILE
    # -------------------------

    if text.startswith("move ") or text.startswith("rename "):

        try:

            command = (
                message.replace("move ", "")
                .replace("rename ", "")
                .strip()
            )

            parts = command.split(" to ")

            if len(parts) != 2:
                return "Use: Move old.txt to new.txt"

            source = parts[0].strip()
            destination = parts[1].strip()

            os.rename(source, destination)

            return f"Moved '{source}' to '{destination}'."

        except FileNotFoundError:

            return "Source file not found."

        except Exception as e:

            return f"Move failed: {e}"

    # -------------------------
    # CONTEXT
    # -------------------------

    if text == "what file is open":

        last = get_context("last_file")

        if last:
            return f"The last opened file is {last}"

        return "No file has been opened yet."

    return None
