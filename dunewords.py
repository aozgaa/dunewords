import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import re
import sys

epub_file = sys.argv[1]

def extract_paragraphs(epub_file) -> list[str]:
    paragraphs = []

    book = epub.read_epub(epub_file, {"ignore_ncx": True})

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content = item.get_content().decode('utf-8')
            soup = BeautifulSoup(content, 'html.parser')
            # Find all <p> elements and extract their text
            # paragraph_tags = soup.find_all('p')
            paragraph_tags = soup.find_all('p')
            for paragraph in paragraph_tags:
                paragraphs.append(paragraph.get_text())

    return paragraphs

def extract_dialogue_phrases(line: str) -> list[str]:
    # probably a slight oovercounting due to some block quote attributions (eg: to Princess Irulan)
    dialogue_phrases = re.findall(r'“([^”]+)”', line)
    return dialogue_phrases

def count_dialogue_words(paragraphs: list[str]) -> int:
    total = 0
    for line in paragraphs[:10000]:
        dialogue_phrases = extract_dialogue_phrases(line)
        for dialogue in dialogue_phrases:
            words = [w for w in dialogue.split(" ") if w]
            total += len(words)
    return total


paragraphs = extract_paragraphs(epub_file)
dialogue_words = count_dialogue_words(paragraphs)
print("Number of dialogue words:", dialogue_words)