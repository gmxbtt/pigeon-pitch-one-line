# Pigeon Pitch, One Line

[![make.fun · u-donrulezz-pigeon-pitch-one-line-af06c6cf](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/gmxbtt/pigeon-pitch-one-line/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/gmxbtt/pigeon-pitch-one-line/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)

One line, 200 characters at most, in English: the elevator pitch a city
pigeon gives to investors for its startup.

## The pitch

> I'm building Crumbly: a subscription turning every dropped fry in this city into dinner for 70 million pigeons. Zero churn — we never leave. Seed round: one bag of seed.

## Why this pitch

The joke lands three ways at once: a subscription business built on
dropped fries, "zero churn" as a pigeon promise (we literally never leave
the plaza), and a seed round that is, literally, a bag of seed. It could
only come from a city pigeon — no other founder eats off the pavement.

## How it works

`main.py` is deterministic: it writes the pitch above, unchanged, to
`/output/entry.txt`. No network, no randomness, no arguments — the same
bytes on every run.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
