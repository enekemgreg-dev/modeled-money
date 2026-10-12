# Video 1: The 1% Fee That Costs You $100,000

Status: draft for human review. Spoken length about 8 minutes at 150 words a minute. Read it aloud once before recording and cut any sentence that makes you stumble. Every number must appear in `numbers.md`.

## 0:00 Hook

"Two people invest $500 a month for 30 years. Same market, same discipline, same 7% return before fees. One ends up with $604,000. The other, $502,000. That's $101,744 gone, and the only difference is one percentage point in fees. Here's the scary part: almost none of it happens at the end. It starts in year one, and by the time you can feel it, you can't get it back. I built the model so you can watch exactly where the money disappears, and at the end I'll show you a two-minute check you can run on your own account."

On screen: two curves drawing left to right, the end balances appearing, a counter for the gap.

## 0:35 The setup

"First, what this is and what it isn't. This is a model, not a prediction. Markets don't return 7% every single year. I'm holding the return constant on purpose, so the only thing that changes between these two people is the fee. $500 at the end of each month, 30 years, 7% before fees. Person A holds a low-cost index fund charging 0.05% a year. Person B holds a fund charging 1%. No taxes, no inflation, nothing else. Same everything, except the fee."

On screen: the assumptions as clean text, Person A as a mint dot, Person B as a red dot.

## 1:15 What a fee actually is

"So what is a 1% fee? It's called an expense ratio, and it comes out of the fund's returns automatically. You never get a bill. You never see a line that says you paid a thousand dollars. You just earn a little less than you should have. Some people also pay a second fee, to an advisor or a platform, often charged as a percentage of the balance. If both apply, they add together. So '1%' can be a perfectly honest description of someone's total cost."

On screen: a fund statement graphic: 7.00% return, minus 1.00% fee, equals 6.00%.

## 2:00 Year one

"Let's run it. Month one: both people put in $500. Watch the two balances. After one year, Person A has $6,195. Person B has $6,168. The difference is $27. Twenty-seven dollars. In a real account, you'd never notice, and you'd never complain. That's exactly why fees are so easy to ignore."

On screen: screen recording of the Sheets model running month by month, the gap cell highlighted.

## 2:50 Years five and ten

"Fast forward. After five years, the gap is $865. Annoying, but survivable. After ten years it's $4,365, on a balance of about $86,000. It looks like rounding error. This is the trap: the cost stays tiny for so long that most people never connect it to what they eventually lose. But watch what happens next."

On screen: the gap counter ticking up at each marker.

## 3:40 The curve bends

"Year fifteen: $12,385. Year twenty: $27,867. Year twenty-five: $55,348. And at year thirty: $101,744. Look at that last stretch. Nearly half of the entire damage lands in the final five years, after most people have stopped paying attention."

On screen: the gap-by-year chart (data in `models/out/fee_gap_by_year.csv`), with each year marked as it is spoken.

## 4:35 Why it happens

"Here's why. The fee doesn't take a slice once. Every dollar it takes is a dollar that stops working for you. That money would have earned returns, and those returns would have earned returns. You're not just losing the fee. You're losing everything the fee would have grown into. It's the same compounding that makes investing powerful, running against you. And here's the number that made me stop: Person A earns $424,002 in growth. Person B earns $322,258. Compared with the cheap fund, the 1% fee costs you 24% of your gains. One percent sounds small. Twenty-four percent of your gains doesn't."

On screen: the two growth totals side by side, the 24% revealed last.

## 5:40 Is half a percent still a problem?

"What about a smaller fee? At 0.5%, Person C ends with $553,089. That's still $50,913 less than the index fund. Half a percent. Still fifty thousand dollars."

On screen: a third curve appears between the first two.

## 6:20 Does a higher fee ever pay off?

"Now, the fair objection: maybe the expensive fund is better. Maybe it earns more. It might. So here's the question that actually matters: how much more does it need to earn just to break even? About 0.95 percentage points a year, every year, for 30 years, before fees. That's a high bar to clear for decades. Whether funds actually clear it is something I'll cover with real data in a future video, so I'm not going to guess here. For now, just know the bar exists, and most people never ask where it is."

On screen: a bar labeled "0.95 points a year" held over a timeline.

## 7:10 How to check your own fees

"So here's how to check yours. Step one: find the expense ratio of every fund you own. It's on the fund's fact sheet, and most brokerages show it right on the fund's page. Step two: look at your statements for any advisory or platform fee, usually a percentage of your balance. Step three: add them together. That's your real annual cost. Step four: plug it into the sheet linked below and see what 30 years does with it. This isn't advice on what to buy. It's the one number almost nobody checks."

On screen: four numbered steps, then the Sheets link on screen.

## 8:10 The rule

"So here's the rule to remember: before you compare returns, compare costs. Returns are a guess. Costs are certain. This whole video assumed a 7% return, and you can't count on that. But a 1% fee? That's the one number you know you'll pay."

On screen: the rule as one line of large text.

## 8:40 Disclaimer and close

"This video is education, not personal financial advice, and real returns will vary. Next up: rent versus buy. I built a calculator that shows the break-even point, and the answer depends on three numbers most people never plug in. If you want to see it, subscribe, and I'll see you in the next one."

On screen: a one-line disclaimer, then a preview frame of the rent-vs-buy model.

## Chapters (for the description)

0:00 Hook
0:35 The setup
1:15 What a fee actually is
2:00 Year one
2:50 Years five and ten
3:40 The curve bends
4:35 Why it happens
5:40 Is half a percent still a problem?
6:20 Does a higher fee ever pay off?
7:10 How to check your own fees
8:10 The rule
8:40 Close
