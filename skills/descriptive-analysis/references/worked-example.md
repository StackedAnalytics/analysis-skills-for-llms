# Worked Example: The Monthly Channel Performance Report

A compressed run of the descriptive-analysis skill on the most routine deliverable in analytics — which is exactly why it's the right test. The instructive beats: the triage strips narration from nine of twelve movements, one "alarming" drop turns out to be routine variation while one quiet drift turns out to be the real signal, and the lede leads with the thing the dashboard order buries.

**Prompt:** "Can you write up the June channel performance summary for the client? Same as usual — sessions, conversion, leads by channel. They read it Monday morning."

---

## Stage 1 — Frame

- **Audience & use:** client's VP Marketing + agency lead, Monday review; they act on channel budget nudges and flag items for the analytics backlog. Altitude: channel level, not campaign level.
- **Materiality:** budget nudges happen on sustained ±15% channel movements or lead-volume swings > ~50/month; smaller moves are watch-only.
- **Open loops from May:** (1) paid search CPL spike flagged — vendor attributed to a competitor's bid surge; (2) email list-cleaning project expected to depress send volume in June (announced, verified context).

## Stage 2 — Expectation frames (fixed per metric)

Leads and CPL: vs. prior month **and** vs. same month last year (seasonal — June softens ~8% historically). Sessions: vs. seasonal norm only (prior-month comparisons of traffic were generating monthly noise-narration; frame fixed and announced two reports ago). Conversion rates: vs. trailing-6-month band. Definitions: no tracking or definition changes in the window (checked — stated once in the table notes).

## Stage 3 — Variation triage

Twelve tracked movements. Natural limits from 18 months of month-over-month deltas per metric (XmR-style). Results:

- **ROUTINE (9 of 12):** organic sessions −4% (limits: ±9%), paid social leads +11% (limits: ±18%), referral, direct, display, email conversion, site-wide CVR, blog sessions, LinkedIn leads — all inside their bands. **The headline-grabber is here:** paid social leads *fell 14% from April to May and rose 11% in June* — two consecutive "stories" in past reports, both inside a ±18% natural band. Narration: one collective sentence.
- **SIGNAL #1 — paid search CPL, third consecutive month above its natural band** (+21%, +26%, +24% vs. trailing norm; run pattern + limit breach). May's "competitor bid surge" explanation predicted a *reversion* that has not come. Signal status: persistent, material (CPL drives the budget-nudge decision). **Handed to RCA** as falsifiable entries: (a) auction pressure is structural, not episodic (checkable via impression-share/auction-insights history); (b) the June search-terms mix shifted toward expensive non-brand queries (checkable in query reports). *Not narrated as either — that's RCA's job.*
- **SIGNAL #2 — organic-to-lead conversion, seven consecutive months of small declines** (each individually routine; the run is the signal — cumulative −18% from the September peak). Invisible to month-over-month reporting by construction; this is what run rules exist to catch. Material at the threshold. Handed to RCA with a verified-context note: three of the seven months coincide with the blog's shift toward top-of-funnel topics (known editorial decision — labeled as context, not cause).
- **Email leads −31%: NOT a signal** — the announced list-cleaning (open loop #2) fully accounts for the send-volume drop; per-send conversion is inside its band. Reported as a closed loop with the verified context labeled.

## Stages 4–5 — The report (as delivered)

> # June channel report: [Client]
>
> ## Bottom line
> 1. **Paid search CPL is now a confirmed trend, not an episode — up ~24% vs. norm for a third straight month.** May's competitor-surge explanation predicted a reversion that hasn't come. This crosses your budget-review threshold; we've opened a structured investigation (auction pressure vs. query-mix shift) and will bring the answer, not a guess, next week. Recommend holding the June budget nudge until it reports.
> 2. **Organic lead conversion has drifted down seven months running — small steps, now −18% cumulative from September.** No single month looked notable; the streak is the story. Partial context: the blog's deliberate move up-funnel covers some of the window. Investigation opened; worth two minutes Monday because it's the quiet kind of decline that gets discovered a year late.
> 3. **Everything else is normal — including two things that may look otherwise:** email leads are down 31% *entirely* per the announced list-cleaning (per-send conversion is healthy; loop closed), and paid social's June "rebound" is routine variation, as was May's "drop." No action on either.
>
> ## Open loops
> May's paid-search flag: **persisting — escalated** (item 1). Email list-cleaning: **resolved as expected** (item 3).
>
> ## Within normal ranges
> Organic sessions, paid social, referral, direct, display, email conversion, site CVR, blog sessions, LinkedIn all moved within their historical bands. Full figures in the table.
>
> ## Metric table
> [12 rows: value · frames · deltas · ROUTINE/SIGNAL — complete, unnarrated. Note: no tracking or definition changes in June.]

---

**What the process bought us:** the untrained version of this report narrates all twelve metrics in dashboard order, celebrates paid social's +11% "recovery" (noise), attaches a fresh guess to the email drop (already explained), repeats the vendor's competitor-surge story for CPL (now three months stale and failing its own prediction), and never sees the organic conversion drift at all — because no single month of it was ever worth a sentence. The scaffolded version delivered a Monday briefing with three items, two honest investigations instead of two inline guesses, one loop closed, one escalated, and — the quiet achievement — nine metrics *not* narrated, which is what makes the three that were impossible to miss.
