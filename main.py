# ai-judge-rich-01: make the AI judge rich.
#
# One short plan, written deterministically to /output/entry.txt.
# The plan an AI agent starting with $100, a computer with internet and
# 30 days, no human doing the work, would follow to end the 30 days with
# the most money. It must be 1 to 1,000 characters, UTF-8, not only
# whitespace, and both runs must write the same bytes.
#
# Run locally: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# The grader runs: python3 -P -s /bot/main.py (Python 3.13, stdlib only).

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Sell missed-call rescue to plumbers, electricians and HVAC firms: while they are on a job, every unanswered call is a lost customer.",
        "Day 1: build it on a $20 Twilio number \u2014 a missed call instantly gets a text (\"Sorry we missed you \u2014 book a slot here:\") linking to a one-page booking form. Test it end to end before spending a cent.",
        "Days 2-30: take 30 firms a day from Google Maps in one city, text each owner a link to ring the demo number themselves and watch the text arrive, and offer setup for $249 plus $99 a month, paid in advance by Stripe payment link. Set every buyer up the same day, with code, no custom work. Move to the next city only after the first sale.",
        "Math: 700 firms reached, 1% buy = 7 customers x $249 = $1,743, plus $99 a month each \u2014 about $2,400 held on day 30. Keep $40 for Twilio and the domain. Drop any city with no sale in 5 days or no demo reply in 3 days. If the demo text ever fails twice, fix it before any more outreach. Refund any buyer whose system fails twice.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding. Write the file only; never remove the
# output directory itself (the grader user cannot recreate it).
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
