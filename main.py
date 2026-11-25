#!/usr/bin/env python3
"""Pigeon Pitch, One Line — entry for u-donrulezz-pigeon-pitch-one-line-af06c6cf.

Writes the one-line elevator pitch to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

MAX_CHARS = 200

PITCH = (
    "I'm building Crumbly: a subscription turning every dropped fry in this "
    "city into dinner for 70 million pigeons. Zero churn — we never leave. "
    "Seed round: one bag of seed."
)


def validate(text: str) -> str:
    """One line, English, 1-200 chars — the gate's exact requirements."""
    text = text.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"pitch is {len(text)} chars, must be 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")
    return text


def main() -> None:
    text = validate(PITCH)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
