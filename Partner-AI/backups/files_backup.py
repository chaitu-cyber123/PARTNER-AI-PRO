import os
import shutil

def files_command(message):

    text = message.lower().strip()

    if text == "show files" or text == "list files":

        files = os.listdir(".")

        if not files:
            return "No files found."

        return "\n".join(files)

    if text.startswith("find "):

        filename = text.replace("find ", "").strip()

        for root, dirs, files in os.walk("."):
            for file in files:
                if filename in file.lower():
                    return os.path.join(root, file)

        return "File not found."

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

                    try:
                        with open(path, "r", encoding="utf-8") as f:
                            return f.read(3000)

                    except Exception as e:
                        return f"Cannot read file: {e}"

        return "File not found."

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

    return None
