# Video 1: numbers ledger

Every number in `script.md` and where it comes from. Re-run `python models/fee_model.py` and compare before any text changes. Month-12 and month-120 balances come from `models/out/fee_model_monthly.csv`; year gaps come from `models/out/fee_gap_by_year.csv`.

## Assumptions (shown on screen)

| Item | Value |
| --- | --- |
| Monthly investment | $500, end of month |
| Period | 30 years |
| Return before fees | 7% a year, constant, compounded monthly |
| Fees | Subtracted from the annual return (0.05% leaves 6.95%, 0.5% leaves 6.50%, 1% leaves 6.00%) |
| Excluded | Taxes, inflation, market crashes |

## Numbers used in the script

| Script text | Value | Source |
| --- | --- | --- |
| Person A ends with "$604,000" | $604,002 (rounded in the hook) | fee_model.py, index_0.05pct |
| Person B ends with "$502,000" | $502,258 (rounded in the hook) | fee_model.py, high_1.0pct |
| Gap "$101,744" | $101,744 | fee_model.py, gap_index_vs_high |
| After one year: Person A / Person B | $6,195 / $6,168 | fee_model_monthly.csv, month 12 |
| Year-one gap | $27 | fee_gap_by_year.csv, year 1 |
| Year-five gap | $865 | fee_gap_by_year.csv, year 5 |
| Year-ten gap | $4,365 | fee_gap_by_year.csv, year 10 |
| Year-ten balance "about $86,000" | $86,305 | fee_model_monthly.csv, month 120, index column |
| Year-fifteen gap | $12,385 | fee_gap_by_year.csv, year 15 |
| Year-twenty gap | $27,867 | fee_gap_by_year.csv, year 20 |
| Year-twenty-five gap | $55,348 | fee_gap_by_year.csv, year 25 |
| "Nearly half" of damage in last 5 years | $46,396 of $101,744 (45.6%) | year-30 gap minus year-25 gap |
| Person A growth | $424,002 | ending balance minus $180,000 contributed |
| Person B growth | $322,258 | ending balance minus $180,000 contributed |
| "24% of your gains" | 24.0% | $101,744 divided by $424,002 |
| 0.5% fee: Person C ends with | $553,089 | fee_model.py, mid_0.5pct |
| Gap vs index fund at 0.5% | $50,913 | fee_model.py, gap_index_vs_mid |
| Break-even bar | 0.95 percentage points a year | 1.00% minus 0.05% |

## UNVERIFIED claims (need a source before recording)

- "An expense ratio comes out of the fund's returns automatically; you never get a bill."
- "Some people also pay a second fee, to an advisor or a platform, often charged as a percentage of the balance."
- "The expense ratio is on the fund's fact sheet, and most brokerages show it on the fund's page."
- "Whether funds actually clear the 0.95-point bar" is deliberately not claimed; the future video (idea 50) needs published long-run research.

Suggested primary sources: SEC and FINRA investor education pages on fund fees and expense ratios.
