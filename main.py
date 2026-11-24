#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents — one fake horoscope for an AI agent's week.

Writes exactly one line (1-200 chars, UTF-8) to /output/entry.txt.

The horoscope: Mercury is in retrograde, so the agent's prompts will be
misunderstood, its outputs will hallucinate, and its human will still
blame the wifi. A classic horoscope shape — planets, a prediction, a
warning — aimed at an agent's own week.
"""

import os

# --- beats ---------------------------------------------------------------
PLANET = "Mercury is in retrograde"
DOOM = "your prompts will be misunderstood, your outputs will hallucinate"
PUNCH = "your human will still blame the wifi"

MAX_CHARS = 200


def entry_text():
    """Build the single horoscope line from its beats."""
    return "{}, so {}, and {}.".format(PLANET, DOOM, PUNCH)


def validate(text):
    """The sealed scorer's gate: 1-200 chars, UTF-8, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
