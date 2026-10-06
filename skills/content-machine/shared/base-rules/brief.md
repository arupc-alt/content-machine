# Brief base rules

Every brief, for every product, follows this file. It holds the format skeletons (Step 3), the brief's fixed structure and template (Step 5), the plain-language rules for the brief itself (5a and 5b), and the formatting rules for the saved document (5c). modes/brief.md says when each one applies. The general writing standard for articles is in shared/base-rules/writing.md; the rules below are the brief's own.

Product rules and learned rules (shared/rule-extraction.md) add to these rules or make them stricter. They never remove one.

## When the product's files and these rules disagree

The product's reference files are the product's own house rules, so they win on anything about the product: facts, claims, terminology, audience, sources, and who approves what. On style and structure, where the two differ, follow whichever rule is stricter, and where a file adds a requirement these rules don't have, add it to the brief's plan. In practice:

- **Freshness:** if the product knowledge requires a fresher source than Step 4g's cadence (for example, pricing checked the same week as publish), the stricter rule goes into the Freshness Log.
- **Link minimums:** if the quality checks require a minimum number of internal or external links, the Internal Link Plan in Step 4f meets that minimum, so the writer isn't set up to fail QA.
- **Structural requirements:** if the style guide or quality checks require a block the Step 3 skeleton doesn't have (a Key Takeaways box, a methodology section, a disclosure line), add it to the outline where the file says.
- **Length:** if the style guide sets length ranges for a format, calibrate Step 3's word counts against those and the top-3 search results average, not against the default numbers in Step 3.
- **Banned words and punctuation:** the brief itself follows both these rules and the style guide's, together, since it models the house style for the writer.
- **Other agent names:** wherever the files name a "Reworker Agent," that means the Brief mode's own Step 0.6 at the brief stage and the Blog Writer's own rework step at the draft stage.

## Step 3: The format skeletons

Match the search results' dominant format and the keyword's own shape to one of these four skeletons. These are drawn from real, live blog posts, and each is a proven, working pattern, not a hypothetical template.

**The word count always comes from the research.** Set each piece's target from what Step 2b actually found: the average length of the top three results plus a depth premium. The typical figures shown under each skeleton are only for reference; when the research points to a different number, the research number wins, in either direction.

**Comparison or Alternatives post** ("best X," "X alternatives"). Informational shading into commercial intent.
Key Takeaways, then a Quick Answer summary table, then Methodology (how the numbers were actually pulled), then a Cost Comparison table, then a Feature Comparison table, then a platform-by-platform breakdown (one H3 per competitor, each with Pros, Cons, Pricing, and Hidden Costs), then Real Cost of Ownership across a few growth stages, then How to Choose, then Why [Product] Is Worth Considering, then Conclusion, then FAQ. Typically roughly 5,500 to 6,000 words; the Step 2b research number wins.

**Versus or head-to-head page** ("[Product] vs [Competitor]"). Commercial shading into transactional intent.
Open on the real philosophical difference between the two (managed versus self-managed, native versus bolted-on, whatever the actual distinction is), then Key Differences Explained, then Pricing broken into H3s (Annual Plans, Lifetime Plans, Extra Costs), then a run of feature-category H3 sections through to compliance and data ownership, then Why Most Users Choose [Product], then What's Right for You, then FAQ. Comparison tables use three columns: feature, this product, the competitor. Typically roughly 4,500 to 5,000 words; the Step 2b research number wins.

**Listicle, examples, or strategies guide** ("X examples," "X strategies," "X types," "ways to do X"). Informational intent.
What Is X, then Why X Helps (the mechanism, not just the claim), then the numbered items themselves, each with a name, a concrete scenario, and a short Why It Works explanation, then How to Do X Well (a short set of practical sub-rules), then a feature tie-in if the product has a relevant built-in capability, then a short Final Thought. No comparison table and no FAQ on this format unless the brief has a specific reason to break that pattern; per the writing style guide, an FAQ block isn't universal, and this format typically closes on a reflective final thought instead. External citation is heavier here than on other formats: pull specific supporting data points from real, authoritative outside sources (established publications, research, recognized reference sites), not just the product's own pages. Typically 4,000 words at minimum, and up to 8,000-plus for a genuinely comprehensive hub piece; the Step 2b research number wins.

**How-to or single-feature guide** ("how to do X"). Informational shading into transactional intent.
Open on the concrete problem, not generic scene-setting, then what the reader needs before starting, then explicit Step 1 through Step N instructions using imperative verbs, then common mistakes or troubleshooting, then a short, honest note on why the product makes this step easier, then FAQ. Typically roughly 1,500 to 2,500 words, the shortest of the four formats by design; the Step 2b research number wins.

If none of these four cleanly fits, don't force it. Say so, describe the closest fit and where it diverges, and propose a structure grounded in what's actually ranking rather than bending one of the four skeletons past where it still makes sense. The Format Skeleton field in Airtable only takes the four names above (`Comparison/Alternatives`, `Versus/Head-to-Head`, `Listicle/Examples`, `How-to/Guide`), so log the closest one and describe the difference in the brief.

## Step 5: The brief's fixed structure

Write the brief in exactly the structure shown in the template below. This is what the Blog Writer reads as its contract, and what QA will later check the finished draft against, so name things exactly and don't leave a section vague. Step 6a saves it as a document.

**The structure is fixed.** Every brief, new or reworked, has the same shape, in the same order:

1. The title as the only H1: `Content Brief: [Working Title]`.
2. The "At a glance" table, right under the title.
3. The twelve numbered sections, as H2 headings, with exactly the names the template shows, in that order. No other H2 headings, ever. Don't add sections such as "Brief metadata," "Editorial thesis," "Recommended stack," "Compatibility section," "Pre-publish checklist," or "Summary for Slack."
4. Anything else the research produced goes inside the section it belongs to, as an H3 under that H2. Use this map:

| Extra material | Where it goes |
|---|---|
| Working title, keyword, intent, format, length, slug | The "At a glance" table, then the full detail in sections 1, 2, 3, and 9 |
| The piece's main argument or thesis | Section 5, next to the Spearhead Strategy |
| What the reader will be able to do after reading | Section 4 |
| Search results findings, AI answer engine findings, community threads | Section 5 |
| Product roles, tool stacks, and integration or compatibility notes | Section 6, as the "Products and tools" table, with the detail under the outline section that covers it |
| The product rules and learned rules that apply to this piece | Section 6, as the "Product rules for this piece" H3 |
| Business models, step lists, test checklists, and anything else the article will teach | Section 7, under the outline section where the article covers it |
| CTA plan, and planned visuals or tables | Section 7, as the "CTA plan" and "Visual plan" H3s |
| Sources read | Section 9, as the "Sources" H3, as linked page names |
| Things to check before publishing | Section 10 |
| Decisions for the reviewer | Section 11 |
| The Slack summary | Nowhere in the document. It goes only in the Slack post (Step 6c). |

5. A section with nothing to say still appears, with one line saying so, for example "No community threads rank for this keyword."

## 5a. Write every line in plain words

A person reads this brief before approving it, often on a phone, often between other work. They should understand every line on the first read, including the technical parts. Being exact and being simple are not in conflict: say the exact thing, in short, everyday words.

1. **Reading level: aim for grade 6, never above grade 7.** This covers every sentence of the brief's own prose. It doesn't cover the keywords, titles, meta drafts, URLs, quoted search queries, or product names, which stay exactly as they are.
2. **Short sentences.** Aim for 15 words on average. Split any sentence over 25 words. One idea per sentence. Paragraphs of 1 to 3 sentences.
3. **Explain every technical point in this order.** This covers how a feature works, a setup step, a pricing or fee rule, a migration step, or an SEO tactic.
   - First, one plain sentence saying what it is, as you'd say it to a new customer. For example: "License keys stop people from using one plugin purchase on more sites than they paid for."
   - Then, one sentence on why it matters for this piece.
   - Then the detail, as short numbered steps or a small table, never one long sentence.
4. **Define a term the first time it appears**, in a few plain words, then use the same word every time after. Spell out shortened forms on first use: "the search results page (SERP)," "the 'People also ask' questions (PAA)," "signals that show real experience and expertise (E-E-A-T)." Use the product's own button and menu names exactly, and say what each one does.
5. **Break up noun piles.** "Per-tier license-limit override" becomes "a separate limit on how many sites each plan can use." "Module-by-module conversion result" becomes "what happened to each page builder module when we converted it."
6. **Say what you mean, then stop.** No filler ("it's worth noting," "in terms of," "from a ... perspective"). No vague words standing in for a specific one ("leverage," "robust," "seamless," "solution," "ecosystem," "holistic," "optimize" with no object). Say the actual thing: which feature, which number, which page.
7. **Keep the section headings exactly as the template shows them.** The Blog Writer and QA look for those headings. The words under each heading are what must be plain. "Spearhead Strategy," "Cornerstone Asset," and "Weakness archetype" each get a plain one-line meaning the first time they appear in the brief.
8. **If you don't know how something works, say so plainly.** Never cover a gap with technical-sounding words. Write "Not confirmed: whether X does Y. Needs a check in a live account," tag it `[VERIFY]`, and list it in Open Questions.
9. **The Spearhead Strategy stays the one sentence from Step 4a, kept under 40 words and in plain words.** Name the move and the gap in everyday terms. The detail goes in the bullets below it.
10. **No em dashes anywhere in the brief.** The brief should model the house style, not just tell the writer to follow it. Use the spelling the product's Settings row names (US or UK).

## 5b. Do a plain-language pass before Step 6

Read the whole brief once, as someone who has never used this product and never seen this pipeline.

- Rewrite any sentence you'd need to read twice.
- Rewrite any technical point that doesn't follow the order in 5a.3.
- If a shell is available in this session, measure the brief's prose. Leave out headings, tables, URLs, keyword lists, and meta drafts. Check the Flesch-Kincaid grade and the average sentence length, and list every sentence over 25 words. Fix until the grade is 7 or lower and no sentence is over 25 words. If no shell is available, do the same check by reading, and don't claim a measured number.

## The template

The `#`, `##`, and `###` marks in the template only show heading levels. In the document, they become real headings, per 5c. Each bullet in the template is one item to write, in that order.

```
# Content Brief: [Working Title]

At a glance (a 2-column table, no heading above it):
| Item ID | [Item ID] |
| Primary keyword | [keyword] |
| Search intent | [primary intent, plus secondary if any] |
| Format | [format skeleton from Step 3] |
| Target length | [N] words |
| URL slug | [slug] |
| Open questions | [N], see section 11 |

## 1. Keyword and Intent
- Primary keyword, and how it was determined (Path A or Path B, one sentence)
- Search intent (primary, and secondary if present), with the evidence for the classification
- Secondary keyword map, as a table: Keyword | Use in this post or a future one | Section it goes in

## 2. Target Word Count
- Target number, with the reasoning: search results average plus depth premium, calibrated against the relevant format skeleton in Step 3
- A table of the section word budgets from section 7: Section | Target words, with a total row that matches the target

## 3. Recommended Titles
- Three options, as a numbered list, each keyword-forward and specific, not clickbait

## 4. Audience and Reader Goal
- Who is actually searching this, drawn from the product knowledge audience segments
- What they need to believe, know, and do after reading, as a short bulleted list

## 5. Competitive Intelligence
- Dominant search results format
- Table stakes topics found across the current top results
- Weakness archetype identified, with the specific supporting evidence
- Cannibalization check: whether the product's own blog already has a post on this exact keyword or a heavily overlapping one, and what this piece does differently, or whether it should instead update or consolidate into that existing post
- Any forum or community thread (Reddit, niche community, Quora) ranking in the top 10, and what real searcher language or unresolved concern it surfaced, with each thread as a linked title
- AI answer engine findings: the sources Google AI Mode and ChatGPT cited, the gaps and biases each surfaced, and where this piece will fill them
- The Spearhead Strategy sentence, on its own line, in bold

## 6. Brand and Asset Notes
- Tone descriptors and hard red lines from the brand guide and writing style guide
- The Cornerstone Asset selected, and why
- E-E-A-T and trust signal plan: where a first-hand data point, expert quote, or documented result belongs in this piece, or a plain note that nothing genuinely first-hand is available
- Any approved claim this piece will lean on, and any prohibited claim to actively avoid given the topic
- ### Products and tools (only when the piece covers several products, plugins, or tools): one table, one row per product: Product | Its job in this piece | How it connects to [Product] | Source (linked) | Needs a check? ([VERIFY] or "Confirmed")
- ### Product rules for this piece: one table, one row per Active product rule or learned rule that applies: Rule ID | Must or Should | The rule | What it means for this piece. If none apply, one line saying so

## 7. Content Outline
- The planned H1 of the article, on its own line
- Then one H3 per planned article section, in order, titled "Section [N]: [the planned H2 heading]". Under each one, these labeled bullets, in this order:
  - Target length: [N] words
  - Must cover: a nested bulleted list. Any planned H3s of the article go here, by name
  - Gap it fills: one sentence
  - Keyword: the assigned secondary keyword, if any
  - Answer opener: the planned 40-to-60-word opener, where relevant
  - CTA: only in the sections where one lands
  - Visual: only where a table, diagram, or checklist is planned
- ### Section [N]: FAQ (if the format calls for one): the questions as one numbered list, PAA questions plus logically derived ones, each answered in 40 to 60 words in the draft
- ### CTA plan: a table with exactly three rows: CTA | Section it goes in | Text direction | Linked URL
- ### Visual plan (if visuals are planned): a table: Visual | Section it goes in | What it shows

## 8. Internal Link Plan
- A table: Page (linked) | Why it's relevant | Section it goes in
- Where this piece should get linked from once published

## 9. SEO and AEO Requirements
- Meta title draft, within the measured character limit
- Meta description draft, within the measured character limit
- URL slug
- Schema markup to apply
- Citation cadence and sourcing notes
- ### Sources: every page read for this brief, as a bulleted list of linked page names, grouped under bold labels (for example "Product docs," "Competitor pages")

## 10. Freshness Log
- A table: Claim or section | Why it can go stale | Recheck how often

## 11. Open Questions
- A numbered list, one decision per item, each in one or two plain sentences, plus any judgment call made in an unattended run. Put the three most important first.

## 12. Hook and Narrative Plan
- The hook approach selected in Step 4h, and the specific number, cost, proof point, or myth it uses
- The narrative arc (Hook, Sharpen, Evidence, Reframe, Resolution, Proof, CTA), as a table: Beat | What it says | Section it lands in
- Any data-synthesis opportunity flagged in Step 4h, with the individual data points and the insight they point to, marked as reasoning, not fact
```

## 5c. Format it so it reads well in the document

These rules decide how Step 6a turns the brief into the saved document: HTML in Google Drive (shared/storage-drive.md), or Notion-flavored Markdown in Notion (shared/storage-notion.md). The tags in brackets are the Drive form. Breaking these rules is what makes a brief look messy in the document.

1. **Headings.** One H1 (the title, `<h1>`). One H2 (`<h2>`) for each of the twelve sections. H3 (`<h3>`) for every part inside a section. Never use a bold line, or a paragraph ending in a colon, as a heading.
2. **Numbered lists only for short items.** Use a numbered list (`<ol>`) only when every item is one line with nothing under it. Put all the items in one list. If an item needs its own explanation, put that text inside the same item (`<li>`), or nest a bulleted list (`<ul>`) inside that item. If each item needs more than two sentences, make each one an H3 with the number in its text ("Model 2: Course bundles") instead of a list. Never close a list to add a paragraph and then start a new list for the next item. That's what makes every item show as "1."
3. **Tables for anything repeated.** When three or more items share the same fields (products, plugins, business models, steps with lengths, tests, keywords, links), use one real table (`<table border="1">`) with a header row (`<th>`), one row per item. Never type a table as plain text with `|` marks that show up as text. Keep each cell under about 15 words, and no more than 5 columns. Put one plain sentence after the table saying what it shows.
4. **Labels.** A label and its text sit in one paragraph, with the label in bold: `<p><strong>Target length:</strong> 350 words</p>`. Never put a label on its own line with the text below it.
5. **Links.** Every URL is a link with readable text, such as `<a href="https://...">[Product] setup guide for [integration]</a>`. Never paste a bare URL as text.
6. **Flows.** A step-by-step flow is a numbered list, never a line of arrows like "A -> B -> C."
7. **Spacing.** In Drive, Google Docs drops the space between blocks on import, so the document looks like one wall of text. Put exactly one empty paragraph, `<p>&nbsp;</p>`, between blocks: after each paragraph, list, and table, and before each heading. Never two in a row. Never inside a list or a table. In Notion, pages keep the gap between blocks themselves, so add no empty spacer blocks.
8. **No stray Markdown, anywhere.** In Drive, no `#`, `*`, `**`, `|`, `->`, or `---` in the text; everything is real HTML. In Notion, headings, bold, lists, and tables are real Notion blocks, and no mark like `->` or `---` shows up as text.

## Structure check before saving

If a shell is available, run a short script on the text about to be saved (the HTML in Drive, the Markdown in Notion) and fix every failure before saving. If no shell is available, check the same points by reading. This check doesn't count as a save attempt. It checks:

- Exactly one H1, and exactly twelve H2 headings, matching the template's section names in order
- The "At a glance" table sits right after the H1
- No numbered list holds only one item, and no two numbered lists sit with only a paragraph between them
- No `|` table text, no bare `http` text outside a link, and no `#`, `**`, or `->` showing as text. In Drive, also no lines starting with `* ` or `- `
- Every list of three or more items with the same labeled fields is a table instead
- In Drive: one `<p>&nbsp;</p>` between blocks, and never two in a row
