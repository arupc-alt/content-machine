# Reference files and product rules

Setup (and "update reference files") reads every reference file twice: once for content, and once for rules. Content is saved as Reference rows by section. Anything unique to the product becomes a short, testable rule, added on top of the base rules every product already gets.

## The three layers

1. **Base rules** apply to every product, always: everything in `shared/base-rules/`. The QA dimensions, the writing and SEO rules, the brief structure, no em dashes, grammar, the rework limits, and the honesty rules (no invented facts, stats, quotes, or reviews, and cite real sources).
2. **Product rules** come from the product's reference files. They add new rules or make a base rule stricter. They never remove one.
3. **Learned rules** come from repeated reviewer feedback, through the Orchestrator. Like product rules, they add on top, and go live only after a person's yes.

Every draft must pass all three layers.

## Collecting the files

| File | Required | What it holds | Reference Type |
|---|---|---|---|
| Product truth (knowledge base) | Yes | Audience, what the product does, plans and prices with live sources, trusted sources, proof points, facts that go stale | Product knowledge |
| Brand and voice | Yes | What the product is, positioning, exact names, claims allowed and prohibited, voice in a few words | Brand guide |
| Writing rules and best practices | Yes | Voice, point of view, reading level, punctuation, words to avoid, formatting, SEO habits | Style guide |
| Quality bar | No. The base QA rules apply either way. | What makes a draft good enough, what fails it, who approves | Quality checks |
| Internal links and CTAs | No | Pages to link to, and the calls to action to use | Links and CTAs |
| Competitors | No | Who they are, and what may and may not be said about them | Competitors |
| Best past posts | No | 2 or 3 links the writer can match for tone | Best past posts |

These are areas, not file names: a company's files rarely match them one to one. One file can cover several areas, and one area can come from several files. Any of these work, mixed freely: an uploaded file (PDF, Word, Markdown, or text), pasted text, a Google Doc or Notion link, or a public web page. If a company has no files yet, setup can draft starting files from its website and docs URL, marked "Draft, please review." Nothing drafted goes live until a person approves it.

## Saving the content

1. Read each file fully. A scanned PDF that can't be read is flagged, and setup asks for a text version. A private link that can't be opened is flagged, and setup asks the person to share it.
2. Sort the content into the standard sections from `products/_template/`, so every product's files have the shape the agents expect. Keep the company's own words. Never summarize, shorten, or rewrite a rule.
3. Show a short summary of each file, plus three lists: gaps ("no words-to-avoid list found"), conflicts ("style guide says sentence case, brand guide says title case"), and anything that looks private (emails, prices marked internal).
4. Fill gaps only with permission, from the public docs site, marked "Draft, please review." Never invent product claims.
5. If one product's saved content would pass about 150,000 characters in all, say so and ask which parts matter most for writing. Save those in full. For the rest (long docs pages, changelogs, old posts), save a short summary row with its Source URL, which an agent opens only when a piece needs it.
6. Save only after an explicit yes. Silence is not approval. Each section is one Reference row (Entry, Product, Type, Layer `File`, Section, Content, Status `Active`, Version, Approved By, Approved At). A long-text cell holds up to 100,000 characters; a longer section is split into numbered parts.
7. Facts that change (prices, limits, plan names) also get Source URL set to their live page. Agents read that page fresh when they use the fact.
8. Update the Team row's Reference Row Count for this product.

## Pulling out the rules

1. Find rule-like lines: "always," "never," "must," "avoid," "use X, not Y," checklists, do and don't examples, and approved-claims tables.
2. Rewrite each as one testable line, with its Category (Keywords and SEO, Writing style, Structure, Product truth, QA checks, Links and CTAs, Competitors, Visuals), the Agents it applies to (Brief, Blog Writer, QA), a Level (Must or Should), and a Check Method (Script for things that can be counted, like banned words, keyword spots, and word limits; Judged for the rest). Keep the exact Source Quote.
3. Compare it with the base rules:
   - Already covered by the base: skip it.
   - New, or stricter than the base: add it.
   - Clashing with the base or with another product rule: show both. The base stays unless the person approves an exception for a pure style choice, such as title case instead of sentence case in headings.
   - Lowering a quality bar or an honesty rule: refuse it, and say why.
4. A rule only seen in examples, never stated, is added as Suggested and stays off until someone approves it.
5. Show the list grouped by Category, each rule with the quote it came from. The person approves, edits, or drops each one. Nothing goes live without an explicit yes.
6. Save each as a Reference row: Entry (the Rule ID), Product, Type `Rule`, Layer `Product rule`, Rule ID (the product's prefix plus R and a number, like `ACME-R07`), Content (the testable line from item 2), Category, Agents, Level, Check Method, Source Quote, Status, Version.
7. If one agent would load more than about 60 rules for a product, ask the team to merge or drop overlapping ones, because a long list makes each rule easier to miss.

## Rule IDs

- Product rules: the product's Item ID Prefix, then R, then the next free number: `ACME-R07`.
- Learned rules: the product's Item ID Prefix, then L, then the next free number: `ACME-L03`. Read the product's Reference rows with Layer `Learned rule` (any Status) to find the next number. If two runs pick the same number at once, the later one adds a letter (`ACME-L03b`).

## Approving learned rules

Any mode may save a learned rule, always as Suggested. The Orchestrator asks the approvers about every Suggested learned rule it hasn't asked about yet, one line each, and records the answer: yes sets it Active, no sets it Retired. Nothing else makes a learned rule live.

## How each agent uses the rules

- **Brief Agent:** keyword, structure, product truth, link, and competitor rules shape the outline. Every brief gets a "Product rules for this piece" list inside its Brand and Asset Notes section, so the writer and the reviewers see what applies.
- **Blog Writer:** follows the rules while writing, then checks every Must rule itself before QA sees the draft.
- **QA:** runs its base checks plus one check per Active product and learned rule for its Agents. A failed Must rule sends the draft back, whatever the score. The report shows both numbers ("Base: 22 of 23. Product rules: 11 of 12") and quotes the line that broke each rule.
- **Orchestrator:** when an approver gives the same kind of feedback twice for a product, it adds a Suggested learned rule (Layer `Learned rule`) and posts one line asking whether to make it permanent. A Feedback Log row records what happened and the Rule ID. No agent can make a rule Active; only a person's yes does.

## Keeping them right over time

- "update reference files" runs the extraction again and shows what's new, changed, or removed before anything goes live. The Version goes up by 1.
- Edits made straight in Airtable are checked on the next run. A changed number of Active rows is handled as shared/airtable.md says (The batched read): more rows are used and the count is updated, fewer rows skip that product for the run with one alert. A rule with missing fields or vague wording ("make it engaging") is flagged in the run summary and skipped until it's fixed.
- Every brief and QA report records the reference version it used (Reference Version and Rules Loaded on the row).
