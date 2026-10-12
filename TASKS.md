# Task queue

Work top to bottom. Mark each task done with the date, and update the relevant `status.md`. Read `CLAUDE.md` first; its hard rules apply to every task.

## Human prerequisites (do these before starting)
- [ ] Export the "First 100 Video Ideas" doc to `research/ideas.md`.
- [ ] Copy the Video 1 script, numbers and thumbnail brief into `videos/01-fee-drag/` as `script.md`, `numbers.md` and `thumbnail.md`.
- [ ] Run the YouTube searches for the Tier 1 ideas and paste the raw results into `research/validation-log.md` (the agent creates the template in task 1).

## Now
1. **Validation template and analysis.**
   Create `research/validation-log.md` with one row per Tier 1 idea: root query, autocomplete suggestions, the top 10 results (channel size, video age, views), a flag for any video with views above 10x its channel's subscribers from a channel under 10,000 subscribers, and whether one channel already owns the "modeled" style.
   Once the human has filled it in, rank the Tier 1 ideas on the evidence and propose the first 12.
   Done when: the first 12 are proposed with evidence, and you have said plainly whether fewer than 5 of the top 20 show a small-channel outlier (the re-rank trigger).

2. **Model check.**
   Run `python models/fee_model.py` and confirm it passes. Confirm that the CSVs it writes to `models/out/` import cleanly into a spreadsheet.
   Done when: assertions pass and you have noted any change needed.
   **Done 2026-10-12.** Assertions pass. Both CSVs imported into LibreOffice Calc with no errors: every header matches, every cell imported as a number, and all values match the CSVs. Google Sheets itself was not tested (no account access). No change needed.

3. **Video 1 fact-check.**
   Compare `videos/01-fee-drag/script.md` with `numbers.md` and the model output. List every sentence containing a number that is not in `numbers.md`, and every claim about fees or funds that has no source.
   Done when: `status.md` lists each problem, with nothing rewritten silently.
   **Done 2026-10-12.** Problems are listed in `videos/01-fee-drag/status.md`. U1-U3 are still UNVERIFIED because the SEC and FINRA pages are blocked by this environment's network policy.

4. **Rent vs buy model (Video 2 candidate, only if validation supports it).**
   Build `models/rent_vs_buy.py` with explicit inputs: home price, down payment, mortgage rate, property tax, insurance, maintenance, rent, rent growth, home price growth, and investment return on the down payment. Add assertions for a worked example, write CSV output, and document every assumption in the docstring.
   Done when: the break-even year is computed and a sensitivity table covers three mortgage rates.

5. **Scripts for Videos 2 and 3** using the template in `CLAUDE.md`. Pick the topics from the validated first 12, and write each `numbers.md` alongside its script.
   Done when: each script passes the quality gate except human voice and approval.

6. **Thumbnail briefs** for Videos 1-3: three variants each, text of 3 words or fewer, brand colors navy #0B1F3A, mint #2DD4A7, red #E5484D.

7. **Shorts cut lists** for Videos 1-3, with timestamps, a number in the first frame, and a 25-40 second target.

## Later
- Models for ideas 4 (debt vs invest break-even), 7 (credit card minimum payments), 10 (savings vs index fund after inflation), 11 (lump sum vs dollar-cost averaging) and 18 (rolling 10-year returns).
- A weekly review template: click-through rate, average percentage viewed and returning viewers per video, with one recommended change.

## Rules for this file
- Add a task only when the human asks, or when a task above is blocked and needs a new prerequisite.
- If a task depends on something missing, mark it blocked and say exactly what is missing.
