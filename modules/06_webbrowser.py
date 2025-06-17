from typing import overload
import webbrowser


# Open the specified website in a default browser.
def open_web_default(url: str) -> None:
    webbrowser.open(url)


def open_web_specific(url: str) -> None:
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    # %s is placeholder for the url we want to open
    chrome = webbrowser.get(f'"{chrome_path}" %s')
    chrome.open(url)


# ------------------ Test

# open_web_default("https://www.kemper-amps.com/")

open_web_specific("https://www.kemper-amps.com/")
