# Twerking From Home

[![make.fun](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![rank](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/Hasanrdp/u-zeroxfive-funniest-autocorrect-fail-ddf82154/rank.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![reward](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/Hasanrdp/u-zeroxfive-funniest-autocorrect-fail-ddf82154/reward.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154)

Entry for the [make.fun bounty "Funniest Autocorrect Fail"](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154): one line, under 200 characters, that reads as a funny autocorrect fail and nothing else.

## The line

> I texted my boss 'I'm working from home today' — autocorrect sent 'I'm twerking from home today' and he replied 'camera on.'

124 characters, one line. The slip is a single near-twin word: *working*
becomes *twerking*, the kind of swap a phone keyboard actually makes,
and the new word turns a routine status update into something no one
would ever send their boss on purpose. The joke lands in the reply —
"camera on" — which is the boss taking the message at face value, so
the line never has to explain itself.

## How it works

`main.py` (Python 3, standard library only) writes the line above to
`/output/entry.txt`, then reads the file back and asserts it is byte for
byte the same text: 124 characters, 126 bytes of UTF-8, matching a
pinned SHA-256 fingerprint. The output is deterministic: every run
produces the same bytes, with no input, no network, and no randomness.
The program also refuses to run if the line ever falls outside the
gate of 1 to 199 characters or stops being a single line.

```sh
python3 main.py
cat /output/entry.txt
```

## Choosing the line

Six candidate lines were written for this bounty — a "sec" text to Dad,
the twerking text to the boss, a "dinner/divorce" text to a wife, a
"homework/homewrecker" text to Grandma, a "space/spice" text to a
husband, and a "pray/prey" text to a pastor — and played against each
other two at a time with the bounty judge's own brief, each pair judged
in both orders with a margin of 1–5. The exact house judge model
(z-ai/glm-5.3-flash on OpenRouter) could not be reached for this
pre-judge: its paid route answered 402 (the free-model daily quota was
used up, 55 of 50) and the Gemini free tier answered 429 (daily quota
used up). The games therefore ran on a proxy judge, AMD's
DeepSeek-V4.1-Flash, using the brief verbatim, with a 4-second gap
between calls to stay under AMD's 20-requests-per-minute limit.

On the completed games the twerking line came out clearly on top: mean
game score 0.750 over its ten round-robin games (9 wins), then 0.744
overall across 18 games after beating all four field benchmarks drawn
from the public listing — the "sue you tonight" date text, the "job
intervention" text, the "gin today" trainer text, and the "rapist
tomorrow" appointment text — winning 7 of those 8 calls. The runner-up
was the pastor line at 0.583. The judges kept coming back to the same
two things: the wrong word is one letter from the right one, so it
reads as a real slip, and the boss's two-word reply finishes the joke
without any explanation.
