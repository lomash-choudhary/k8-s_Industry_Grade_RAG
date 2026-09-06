# for HTML parsing we will use BeautifulSoup

from bs4 import BeautifulSoup
import logfire

def parse_html(file_path: str):
    """
    Parses HTMl content using BeautifulSoup.
    Cleans scripts, styles, extracts readable text for RAG.
    """

    # we will use log fire here because we are using to log what our python file is doing

    with logfire.span("📂 HTML Parsing", filename = file_path):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # html.parser is the parser which we are using to convert the data
            soup = BeautifulSoup(content, "html.parser")

            #1. Remove Junk (Scripts, Styles, Meta Data)

            for script in soup(["script", "style", "meta","noscript"]):
                script.decompose()

            # 2. Extract Text
            # beautifulSoup will put a new line character when it moves from one tag to another tag
            text = soup.get_text(separator="\n")

            #3. Clean white spaces and collaps multilple newlines
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text_clean = '\n'.join(chunk for chunk in chunks if chunk)

            return text_clean
        except Exception as e:
            logfire.error(f"Error parsing HTML: {e}")
            raise e