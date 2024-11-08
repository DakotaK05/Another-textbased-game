import time
def slow_text(text, delay=0.5):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # for new line after the text