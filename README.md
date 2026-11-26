# What the Elevator Would Say

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/Djebrix/elevator-line/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/Djebrix/elevator-line/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958)

The funniest one line a talking elevator could say, spoken in the elevator's own voice.

## The line

> Stop mashing the button — I heard you the first time. I'm slow, not deaf.

(73 characters — within the 120-character limit.)

## How it works

`main.py` (Python stdlib only) writes exactly that one line to `/output/entry.txt` — no trailing newline, no extra output. It asserts the line is 1–120 characters and not only whitespace, so an over-long line fails loudly instead of shipping invalid. Two runs produce byte-identical output.

Run it:

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py out.txt    # writes to a path of your choice
```

## License

MIT — see [LICENSE](LICENSE).
