#!/usr/bin/env python3
"""Entry for make.fun bounty u-xvader-tell-a-whole-story-in-32-characters-f86dd978.

Writes a single Wi-Fi network name (32 characters or fewer) to
/output/entry.txt. The name is a fixed, deterministic string: no input,
no randomness, no network, standard library only.

The name: "MyExTookTheRouterAndTheDog" (26 characters).

Why this name: a passer-by reading it in a phone's network list gets the
whole story in one line -- a break-up, an ex who walked out, and the
double loss of both the router and the dog. The router is the Wi-Fi
itself, so the joke is about the very network broadcasting it; the dog
is the twist that makes the loss sting. It is a situation, a character,
and something that happened, in 26 characters, with no stock Wi-Fi joke
("FBI Surveillance Van", "Pretty Fly for a Wi-Fi") in sight.
"""

import os

NAME = "MyExTookTheRouterAndTheDog"


def main() -> None:
    assert 1 <= len(NAME) <= 32, "name must be 1-32 characters"
    assert NAME.strip() == NAME and NAME, "name must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NAME)


if __name__ == "__main__":
    main()
