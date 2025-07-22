# utils.py

def color(text, color_name):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "end": "\033[0m",
    }
    return f"{colors.get(color_name, '')}{text}{colors['end']}"

def log(message, color_name="green"):
    print(color(message, color_name))
