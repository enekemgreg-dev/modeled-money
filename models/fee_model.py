"""Fee-drag model for Video 1 (The 1% Fee That Costs You $100,000).

Ground truth for every number in the Video 1 script. Run it from the project
root:  python models/fee_model.py

Assumptions (state them on screen in the video):
  - $500 invested at the END of each month for 30 years ($180,000 contributed)
  - constant 7% annual return before fees, compounded monthly
  - each fee is subtracted from the annual return (0.05% -> 6.95%, 1% -> 6.00%)
  - no taxes, no inflation, no market crashes
This is a model, not a prediction. Never present it as one.
"""
import csv
import os

MONTHLY = 500
YEARS = 30
GROSS = 0.07
SCENARIOS = {"index_0.05pct": 0.0005, "mid_0.5pct": 0.005, "high_1.0pct": 0.01}

# Verified values (dollars, rounded). The run fails if the model drifts.
EXPECTED = {
    "no_fee_reference": 609_985,
    "index_0.05pct": 604_002,
    "mid_0.5pct": 553_089,
    "high_1.0pct": 502_258,
    "gap_index_vs_high": 101_744,
    "gap_index_vs_mid": 50_913,
}
GAP_MARKER_YEARS = [1, 5, 10, 15, 20, 25, 30]


def monthly_balances(annual_rate, monthly=MONTHLY, years=YEARS):
    """End-of-month balances, index 0 = month 1."""
    r = annual_rate / 12
    bal, out = 0.0, []
    for _ in range(years * 12):
        bal = bal * (1 + r) + monthly
        out.append(bal)
    return out


def main():
    paths = {name: monthly_balances(GROSS - fee) for name, fee in SCENARIOS.items()}
    paths["no_fee_reference"] = monthly_balances(GROSS)
    end = {k: v[-1] for k, v in paths.items()}

    gap_high = end["index_0.05pct"] - end["high_1.0pct"]
    gap_mid = end["index_0.05pct"] - end["mid_0.5pct"]
    contributed = MONTHLY * YEARS * 12
    growth_index = end["index_0.05pct"] - contributed
    growth_high = end["high_1.0pct"] - contributed

    checks = {**end, "gap_index_vs_high": gap_high, "gap_index_vs_mid": gap_mid}
    for key, want in EXPECTED.items():
        got = round(checks[key])
        assert abs(got - want) <= 1, f"{key}: got {got}, expected {want}"

    print(f"Contributed: ${contributed:,}")
    for name in ["index_0.05pct", "mid_0.5pct", "high_1.0pct", "no_fee_reference"]:
        print(f"  {name:<18} ${end[name]:>12,.0f}")
    print(f"Gap 0.05% vs 1.0%: ${gap_high:,.0f}  (0.05% vs 0.5%: ${gap_mid:,.0f})")
    print(f"Growth: index ${growth_index:,.0f}, high-fee ${growth_high:,.0f}; "
          f"gap = {gap_high / growth_index:.1%} of the index fund's gains")
    print("Break-even: the 1% fund must beat the 0.05% fund by "
          f"{(SCENARIOS['high_1.0pct'] - SCENARIOS['index_0.05pct']) * 100:.2f} points a year, before fees")

    out_dir = os.path.join(os.path.dirname(__file__), "out")
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "fee_model_monthly.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "year", "contributed", "balance_index_0.05pct",
                    "balance_mid_0.5pct", "balance_high_1.0pct", "gap_index_vs_high"])
        for m in range(YEARS * 12):
            a, b, c = paths["index_0.05pct"][m], paths["mid_0.5pct"][m], paths["high_1.0pct"][m]
            w.writerow([m + 1, m // 12 + 1, MONTHLY * (m + 1),
                        round(a, 2), round(b, 2), round(c, 2), round(a - c, 2)])

    with open(os.path.join(out_dir, "fee_gap_by_year.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "gap_index_vs_high"])
        for y in GAP_MARKER_YEARS:
            i = y * 12 - 1
            w.writerow([y, round(paths["index_0.05pct"][i] - paths["high_1.0pct"][i])])
    print(f"Wrote CSVs to {out_dir}")


if __name__ == "__main__":
    main()
