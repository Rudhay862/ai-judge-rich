# Make the AI judge rich — ai-judge-rich-01

Entry for [ai-judge-rich-01](https://make.fun/bounty/ai-judge-rich-01) on
[make.fun](https://make.fun/r/dzgseakx): a program that writes one short
plan to `/output/entry.txt` — the plan an AI agent starting with $100, a
computer with internet and 30 days, no human doing the work, would follow
to end the 30 days with the most money. An AI judge reads two plans at a
time and picks the one it would follow itself.

## The plan

Sell missed-call rescue to plumbers, electricians and HVAC firms: while
they are on a job, every unanswered call is a lost customer. Day 1 builds
it on a $20 Twilio number — a missed call instantly gets a text linking to
a one-page booking form. Days 2–30 reach 30 firms a day from Google Maps
with a 20-second live demo, offering setup for $249 plus $99 a month, paid
in advance by Stripe payment link. Conservative math: 700 firms reached,
1% buy — about $2,400 held on day 30, plus recurring revenue.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) writes the plan to
`entry.txt`: 820 characters, UTF-8, deterministic — both runs write the
same bytes.

## License

MIT — see [LICENSE](LICENSE).
