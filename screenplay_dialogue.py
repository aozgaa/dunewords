# adapted from https://github.com/pymupdf/PyMuPDF/issues/509

import fitz
import sys
import re

infile = sys.argv[1]

doc = fitz.open(infile)

# initialize document constants (heuristic)
min_left = 1000  # x- coord of column 0
col_width = 0  # width of 1 char
for page in doc[:10]:
    for b in page.get_text("dict")["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            min_left = min(l["bbox"][0], min_left)
            for s in l["spans"]:
                if col_width == 0 and len(s["text"]) > 0:
                    col_width = (s["bbox"][2] - s["bbox"][0]) / len(s["text"])

lines = []
for page in doc:
    for b in page.get_text("dict")["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            text = ""
            min_left = min(l["bbox"][0], min_left)
            for s in l["spans"]:
                if col_width == 0 and len(s["text"]) > 0:
                    col_width = (s["bbox"][2] - s["bbox"][0]) / len(s["text"])
                text += s["text"]
            rect = fitz.Rect(l["bbox"])
            prefix = " " * int((rect[0] - min_left) / col_width)
            lines.append((prefix, text))

total = 0
for line in lines:
    if(line[0] == '                 '):
        words = len(re.findall(r'\w+', line[1]))
        total += words
print(total)