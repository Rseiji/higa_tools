import os


def load_prompt(name: str) -> str:
    path = os.path.join(os.path.dirname(__file__), f"../prompts/{name}.md")
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return None
