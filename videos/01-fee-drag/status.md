# Video 1: status

Last updated 2026-10-12 (task 3 fact-check). Nothing in `script.md` or `numbers.md` was changed; every fix below is for the human to decide.

## Overall

**Not ready for human review.** Every model number reproduces. However, the script has 2 factual problems, is about 375 words short of the template, and all 3 UNVERIFIED claims still lack confirmed wording from a source.

## 1. Model check

`python models/fee_model.py` passes. Every model figure in `numbers.md` matches the model output and the CSVs:

| Ledger item | Ledger value | Model / CSV value | Match |
| --- | --- | --- | --- |
| Person A end balance | $604,002 | 604,001.59 | Yes |
| Person B end balance | $502,258 | 502,257.52 | Yes |
| Gap, 0.05% vs 1% | $101,744 | 101,744.06 | Yes |
| Month 12, A / B | $6,195 / $6,168 | 6,194.86 / 6,167.78 | Yes |
| Gaps, years 1/5/10/15/20/25 | $27 / $865 / $4,365 / $12,385 / $27,867 / $55,348 | same (fee_gap_by_year.csv) | Yes |
| Month 120, index balance | $86,305 | 86,304.68 | Yes |
| Share of gap in final 5 years | 45.6% | 45.60% | Yes |
| Growth, A / B | $424,002 / $322,258 | same | Yes |
| Gap as share of A's gains | 24.0% | 23.996% | Yes |
| Person C (0.5%) end / gap | $553,089 / $50,913 | 553,089.04 / 50,913 | Yes |
| Break-even bar | 0.95 points | 1.00 - 0.05 | Yes |

## 2. Sentences containing a number that is not in `numbers.md`

| # | Where | Sentence | Problem | Severity |
| --- | --- | --- | --- | --- |
| N1 | Hook (0:00) | "That's $101,744 gone, and the only difference is one percentage point in fees." | **Inaccurate.** The two fees are 0.05% and 1%, a gap of 0.95 points, as the ledger's own break-even row and the 6:20 section state. "One percentage point" is not in the ledger. | High |
| N2 | Title (H1) | "The 1% Fee That Costs You $100,000" | $100,000 is not in the ledger; the model figure is $101,744. The quality gate requires the title's numbers to match `numbers.md`. Either add a ledger row for the rounding or change the title. The same applies to title options 1 and 3 in `thumbnail.md`. | Medium |
| N3 | Hook (0:00) | "...at the end I'll show you a two-minute check you can run on your own account." | "Two-minute" has no source. Nobody has timed the four-step check, and finding a fund's fees can take longer. | Low |
| N4 | 1:15 | "You never see a line that says you paid a thousand dollars." | "A thousand dollars" is not in the ledger or the model. It reads as a specific amount the viewer pays; no balance or year is tied to it. | Medium |
| N5 | 5:40 | "Still fifty thousand dollars." | This rounds $50,913. The ledger notes the hook's roundings ($604,000, $502,000) but not this one. Add a row. | Low |
| N6 | 8:40 | "...the answer depends on three numbers most people never plug in." | "Three" has no source. The rent-vs-buy model does not exist yet, and task 4 lists ten inputs. | Medium |
| N7 | Header (not spoken) | "Spoken length about 8 minutes at 150 words a minute." | **Wrong.** The spoken text is 825 words, about 5.5 minutes at 150 words a minute. The template requires 1,100-1,300 words, and the chapter markers run to 8:40, so they will not line up with the recording. | High |

## 3. Claims with no source

### Listed as UNVERIFIED in `numbers.md`

| # | Where | Claim | Status |
| --- | --- | --- | --- |
| U1 | 1:15 | "It comes out of the fund's returns automatically. You never get a bill." | UNVERIFIED (see section 4) |
| U2 | 1:15 | "Some people also pay a second fee, to an advisor or a platform, often charged as a percentage of the balance." The same claim appears at 7:10: "usually a percentage of your balance." | UNVERIFIED (see section 4). Note that "often" and "usually" are different claims. |
| U3 | 7:10 | "It's on the fund's fact sheet, and most brokerages show it right on the fund's page." | UNVERIFIED, and **likely conflicts with SEC wording** (see section 4). |
| U4 | 6:20 | Whether funds clear the 0.95-point bar | Deliberately not claimed; it is deferred to idea 50. However, see C5 below. |

### Not listed in `numbers.md`

| # | Where | Claim | Problem | Severity |
| --- | --- | --- | --- | --- |
| C1 | Hook (0:00) | "Here's the scary part: almost none of it happens at the end." | **Contradicts the model and the script itself.** 45.6% of the gap lands in the final 5 years, and 3:40 says "Nearly half of the entire damage lands in the final five years." | High |
| C2 | 1:15 | "If both apply, they add together." | No source. It is only approximately true: the fund fee is charged on fund assets and the advisory fee on the account balance. | Low |
| C3 | 1:15 | "So '1%' can be a perfectly honest description of someone's total cost." | No source. It also blurs the model: the model treats 1% as a single fund fee subtracted from returns. | Low |
| C4 | 2:00 | "In a real account, you'd never notice, and you'd never complain." | An unsourced claim about behavior. | Low |
| C5 | 6:20 | "That's a high bar to clear for decades." | This implies funds usually fail to clear the bar, which is the claim the script says it will not make until idea 50. It needs a source or should be softened. | Medium |
| C6 | 2:50, 3:40, 6:20, 7:10 | "most people never connect it...", "after most people have stopped paying attention", "most people never ask where it is", "the one number almost nobody checks" | Four unsourced claims about what most people do. | Medium (as a group) |
| C7 | 8:10 | "Costs are certain." / "a 1% fee? That's the one number you know you'll pay." | Overstated. A fund can change its expense ratio, and advisory fees can change. | Low |
| C8 | 7:10 | "plug it into the sheet linked below" | Not a factual claim, but the public Sheets link does not exist yet. | Dependency |
| C9 | 8:40 | "Next up: rent versus buy." | Video 2 depends on validation (TASKS.md task 4), so this promise may not hold. | Dependency |
| C10 | 8:40 | "If you want to see it, subscribe" | Departs from the CLAUDE.md template ("a promise of the next video (not 'please subscribe')"). | Template |

## 4. Primary sources for U1-U3: links found, exact wording NOT retrieved

**Blocked:** this environment's network policy denies www.sec.gov, www.investor.gov and www.finra.org, so I could not open any of these pages. The notes below come from search-engine summaries. **They are paraphrases, not quotes. Do not put them in the script or `numbers.md` until you have opened each page and copied the exact wording.** All three claims stay UNVERIFIED.

### U1: expense ratio comes out of fund assets; no bill
- SEC Investor.gov, glossary, "Expense Ratio": https://www.investor.gov/introduction-investing/investing-basics/glossary/expense-ratio
  - Search summary (paraphrase): defines the expense ratio as the percentage of a fund's average net assets used each year to pay the fund's operating expenses.
- SEC Investor.gov, "Mutual Fund and ETF Fees and Expenses" (Investor Bulletin): https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/mutual-fund-and-etf-fees-and-expenses-investor-bulletin
  - Search summary (paraphrase): operating expenses are paid out of fund assets, so investors pay them indirectly.
- SEC, "How Fees and Expenses Affect Your Investment Portfolio" (PDF): https://www.sec.gov/investor/alerts/ib_fees_expenses.pdf
- Assessment: "paid out of fund assets" / "indirectly" would support the substance of U1. "You never get a bill" is the script's own framing; check that the source supports something that strong.

### U2: advisory or platform fee charged as a percentage of the balance
- SEC Investor.gov, "Subscription-based Advisory Fees" (Investor Bulletin): https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/subscription-based-advisory-fees
  - Search summary (paraphrase): the most common way to pay an investment adviser is an asset-based fee, calculated as a percentage of the assets in your account, usually quoted as a yearly rate.
- Assessment: if the exact wording says "most common", it supports "often" at 1:15 and probably "usually" at 7:10. It covers advisers only, not "platforms"; a platform-fee source is still needed, or that word should go.

### U3: expense ratio on the fact sheet and the brokerage's fund page
- SEC Investor.gov, glossary, "Total Annual Fund Operating Expenses": https://www.investor.gov/introduction-investing/investing-basics/glossary/total-annual-fund-operating-expense
- FINRA, "Mutual Funds": https://www.finra.org/investors/investing/investment-products/mutual-funds
- SEC, "Mutual Fund Fees and Expenses" (PDF): https://www.sec.gov/files/ib_mutualfundfees.pdf
  - Search summary (paraphrase): SEC sources place the expense ratio in the fee table of the fund's prospectus, on the line "Total Annual Fund Operating Expenses". The FINRA page reportedly also mentions the fund's website and financial publications, and FINRA's Fund Analyzer for comparing fund costs.
- **Possible conflict (CLAUDE.md: stop and ask the human).** None of these sources appear to mention a "fact sheet" or say that "most brokerages" show the figure. The sourced location is the prospectus fee table. Decide whether to change the wording to match the source or to find a source for the current wording.

### To close U1-U3
1. Either allow the three domains in the environment's network settings and ask me to retrieve the exact wording, or open the links yourself.
2. Paste the exact sentence and the page's date into a "Sources" column in `numbers.md` for each claim.
3. Move each claim out of UNVERIFIED only when the exact wording supports the script's sentence as written.

## Still UNVERIFIED (quality gate)
- U1, U2, U3 (section 4)
- All of section 2 except N5 (N5 needs only a ledger row)
- C1-C7 in section 3

## Quality-gate snapshot (not part of task 3; listed for completeness)
- [ ] `numbers.md` lists every number in the script: no (N1-N7)
- [x] Re-running the model reproduces the numbers and passes
- [x] Assumptions appear within the first 90 seconds (0:35-1:15)
- [ ] Disclaimer in the script and the description: in the script; `description.md` does not exist
- [x] No claims about specific funds or brokers, and no promises
- [ ] Title is 60 characters or fewer and its numbers match `numbers.md`: 34 characters, but $100,000 is not in the ledger (N2)
- [x] Three thumbnail variants, each with 3 words or fewer (A "-$102K", B "$604K vs $502K", C "1% = 24%"). Note that "-$102K" also needs a ledger row.
- [x] `status.md` lists everything still UNVERIFIED (this file)
