"""Wiki import testing"""
import warnings
from bs4 import GuessedAtParserWarning
warnings.filterwarnings("ignore", category=GuessedAtParserWarning)

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError, RedirectError

print("Wikipedia viewer - blank to quit.")

while True:
    title = input("\nEnter page title: ").strip()
    if not title:
        print("Thank you.")
        break

    try:
        text = wikipedia.summary(title, sentences=2, auto_suggest=False, redirect=False)
        page = wikipedia.page(title, auto_suggest=False, redirect=False)

        print(page.title)
        print(text)
        print(page.url)

    except (PageError, RedirectError):
        print(f'Page id "{title}" does not match any pages. Try another id!')

    except DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print("(BeautifulSoup warning)")
        print(e.options[:8] + (['...'] if len(e.options) > 8 else []))
