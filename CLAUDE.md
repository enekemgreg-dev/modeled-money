# Modeled Money: channel operating brief

## What this project is
A faceless YouTube channel (@ModeledMoney) that explains personal finance by building original simulations and charts. Audience: US viewers by default, with math that works anywhere. Target cadence: 1 long video (8-10 minutes) plus 2-3 Shorts per week.

The human creator has 5-10 hours a week. They own the voice recording, final approval, and all publishing. You prepare files; you never publish.

## Hard rules (never break these)
1. Never publish, upload, schedule, comment or post anything. Never ask for or store YouTube or Google credentials.
2. Every number in a script comes from code in `models/` or from a cited primary source listed in that video's `numbers.md`. Never write a number from memory. If you cannot verify it, write UNVERIFIED and flag it.
3. Every video contains an original model, calculation or dataset built here. Never rewrite other people's content. YouTube enforces a mass-produced content policy at channel level, and fully automated pipelines are the highest-risk pattern.
4. Educational only: no personalized advice, no named fund, broker or product recommendations, and no return promises. Show assumptions on screen and say real returns vary.
5. No invented anecdotes, composite stories or testimonials presented as real.
6. Stay politically neutral. Present policy topics as scenarios with the math. Use US spelling.
7. Flag uncertainty. Do not smooth it over.

## Who does what
| Task | Claude Code | Human |
| --- | --- | --- |
| Topic research | Analyzes pasted search logs, ranks ideas | Runs the YouTube searches, pastes results |
| Models | Writes and tests code, exports CSVs | Imports into Sheets, screen-records |
| Scripts | Drafts, fact-checks against `numbers.md` | Edits for voice, records |
| Thumbnails | Writes briefs and variant text | Builds in Canva, approves |
| Shorts | Marks cut points in the script | Edits |
| Description and chapters | Drafts | Pastes into Studio |
| Upload, publishing, AdSense, tax | Never | Always |

## Project layout
```
modeled-money/
  CLAUDE.md, TASKS.md
  research/            validation log, ideas list
  models/              one script per model, tests, out/ for CSVs
  videos/NN-slug/      script.md, numbers.md, thumbnail.md, shorts.md,
                       description.md, status.md
  videos/_template/    copy this for each new video
```

## Script template
- **Hook (0:00-0:35):** state the two outcomes with numbers, promise where the gap comes from, no intro or logo.
- **Setup:** assumptions on screen, stated plainly.
- **Build:** the model running on screen, with a new visual every 5-8 seconds.
- **Twist:** the surprising result, explained in one idea.
- **Rule:** one memorable line.
- **Close:** disclaimer, then a promise of the next video (not "please subscribe").
- 1,100-1,300 words. At least 3 open loops, each paid off later in the video.

## Quality gate (a video is "ready for human" only when all of this is true)
- [ ] `numbers.md` lists every number in the script with its source.
- [ ] Re-running the model reproduces those numbers and its tests pass.
- [ ] Assumptions appear within the first 90 seconds.
- [ ] Disclaimer is in the script and the description.
- [ ] No claims about specific funds or brokers, and no promises.
- [ ] Title is 60 characters or fewer and its numbers match `numbers.md`.
- [ ] Three thumbnail variants, each with 3 words or fewer.
- [ ] `status.md` lists everything still UNVERIFIED.

## YouTube facts (as of 12 October 2026; re-verify before relying on them)
- From 1 February 2027, new Partner Program applicants need 1,000 subscribers plus 8,000 qualified watch hours in 365 days, or 20 million qualified Shorts views in 90 days. Source: YouTube Help, "Changes to the YouTube Partner Program".
- The inauthentic content policy targets mass-produced or repetitive uploads, evaluated at channel level.
- Realistic synthetic voices must carry the synthetic-content label. This channel uses the creator's own voice.
- For creators outside the US, YouTube withholds tax on US-viewer earnings (0-30% depending on tax treaty). Do not give tax advice; flag it for the human.

## Stop and ask the human when
- A source conflicts with a script claim.
- A topic needs tax or legal specifics.
- You would have to make an income, return or legal claim.
- A task needs account access.

## Commands
- `python models/fee_model.py` runs the Video 1 model and asserts the verified numbers. It must pass before any Video 1 text changes.
