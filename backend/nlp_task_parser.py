"""Very small NLP helper using spaCy to parse tasks and due dates."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import spacy
from dateutil.parser import parse as parse_date

nlp = spacy.load("en_core_web_sm")

@dataclass
class ParsedTask:
    """Result of task parsing."""

    title: str
    due_date: Optional[str] = None


def parse_task(text: str) -> ParsedTask:
    """Parse a natural language task description into components."""
    doc = nlp(text)
    for i, token in enumerate(doc):
        if token.text.lower() in {"by", "due"} and i + 1 < len(doc):
            date_text = doc[i + 1 :].text
            try:
                due = parse_date(date_text, fuzzy=True)
                return ParsedTask(title=doc[:i].text.strip(), due_date=due.isoformat())
            except Exception:
                break
    return ParsedTask(title=text.strip(), due_date=None)


if __name__ == "__main__":
    example = "Finish math homework by next Friday"
    print(parse_task(example))
