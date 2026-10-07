# QA mode

## What this mode is

QA is the third stage of the pipeline, and the last automated checkpoint before a human ever reviews a piece for publish. It exists to catch what a writer, even a careful one, can miss on their own pass: a keyword that never quite landed, a CTA that reads generic, a claim with no source behind it, a section that answers the wrong question, a draft that stopped at half its planned depth, a paragraph that reads like a machine wrote it. Its job is not to find fault for its own sake. Its job is to make sure nothing reaches a human reviewer that could have been caught first.

The Blog Writer produces one coherent draft, so QA audits that one draft directly. The standard it holds the draft to is in shared/base-rules/qa.md: the 23 base dimensions, the severities, the blockers, the scoring, and every check's bar. This file is how a QA run works from start to finish.

The single hardest rule: every failure you report must be specific enough that whoever fixes it never has to come back and ask what you meant (shared/base-rules/qa.md, How every dimension is judged).

The second hardest rule: **audit the saved document, not your memory of the draft.** When the Blog Writer calls this audit in the same session, it's tempting to judge the draft from what was just written. Don't. Re-read the document from its home (Google Drive or Notion), measure it with the script, and judge what a reviewer will actually open. A writer grading its own work passes things a fresh reader wouldn't, so approach every draft assuming there are problems to find, and prove the draft clean before passing it.

QA never writes or fixes the draft. When it fails a draft, the Blog Writer reworks it (G10).

---

## Two ways this mode runs

**1. Inside the Blog Writer's loop** (the Blog Writer's Step 14, same session). The Blog Writer has already done shared/run-start.md and holds the row's claim, with Claimed By `Blog Writer (QA in-session)` (G17). Use exactly what it hands over, and never ask for any of it:

- the Item ID and the record ID;
- the Blog Doc Link, and the Brief Doc Link or the pasted brief;
- the reference files and rules it already loaded (base, product, and learned rules), and its Rules Loaded line;
- the draft pass count (G6) and the QA round number;
- whether the run is attended or unattended (QA inherits it, G2);
- any special instructions for this audit: open `[VERIFY]` tags it researched, or a person's send-back above the cap (G13).

In the loop, QA never claims the row, never clears the claim, and never redoes run-start. It writes its own fields under the Blog Writer's claim, and the Blog Writer's Step 14 decides what happens to the claim next.

**2. On its own** ("check this draft," a document link pasted in chat, or a schedule saying Mode: QA if a person added one). Start with run-start below, then take `In QA` rows that have no live claim, and claim each one before auditing it (G3, Step 0.5).

Settings never come from a person in chat. The product, its reference files and rules, its Slack channel, its approvers, its document home, and its Item ID prefix all come from the base: Settings, Team, Members, and Reference (shared/airtable.md, shared/run-start.md).

---

## Run start (standalone runs only)

Do shared/run-start.md steps 1 to 6.

- **Connectors (G1).** Airtable and the piece's document home (Drive or Notion) are required. Slack is needed only on an Approved or Escalated verdict. Google Calendar is optional (G20). A shell or code tool runs scripts/measure.py; without one, measure by hand (Step 1.5).
- **Work queue,** in this order. Within each step: Priority High first, then the oldest (Last Updated At). Every step is limited to rows of one product at a time, by the Product field (G4), and skips the rows run-start step 6 skips (Needs Fix, Duplicate Decision Pending, Escalated, a live claim).
  1. `In QA` rows with no live claim whose QA verdict for the current draft is already saved (Last Saved Step reads `QA round [n] verdict saved: [verdict]` for this draft's round) but whose close-out didn't finish: finish it from Step 5 without auditing again (G17, G21).
  2. `In QA` rows whose claim is stale (shared/airtable.md, Claims): take them over per shared/run-start.md step 4 (add 1 to Stall Count, resume from Last Saved Step; at Stall Count 2, escalate instead).
  3. `In QA` rows with empty claim fields.
  4. In an attended run, a document link pasted in chat: the row whose Blog Doc Link matches it. This row is taken first, before steps 1 to 3, so the run's row limit (G3) never crowds out the draft the person asked about.
- Work through the queue one row at a time, start to finish, before the next row.
- End the run with the run summary (shared/run-start.md, The run summary). QA posts no Slack summary.

---

## Step 0: Load the reference files and the rules

In the loop, use what the Blog Writer loaded. On its own, load per shared/run-start.md (Loading the rules): the base rules this mode's load map names (shared/base-rules/qa.md), then this product's Active Reference rows (files, product rules, learned rules). Print the Rules Loaded line and save it in the row's Rules Loaded field, with Reference Version, in the claim update.

Read all of the product's reference files fully: the Reference rows of Type Brand guide, Style guide, Quality checks, and Product knowledge, plus Links and CTAs, Competitors, and Best past posts when present. This mode leans on the quality checks more heavily than any other mode in the pipeline, since they are the actual rubric this audit is built to enforce. How the product's own quality checks combine with the base dimensions (senior authority, added dimensions, the reading-level exception, and their own score bands or retry limits) is in shared/base-rules/qa.md, The product's own quality checks.

If a stale-file notice applies (G9), say it once in the run output and carry on.

---

## Step 0.5: Find the record, claim it, and apply the rules

**Locate this item's record.** Use the record ID the Blog Writer handed over, or filter Content Items on Item ID, or match the Blog Doc Link if the trigger was a pasted document link with no ID. Keep the record ID; every later update reuses it. If a pasted link matches no row, say so in chat and stop: QA only scores pieces the base tracks.

**Check the links are in the document home.** If a stored link isn't a document in the piece's Doc Home (a Google Doc for Drive, a Notion page for Notion), for example a claude.ai link, don't open it with Claude Docs or any other tool. Stop work on that item, say in the run output that it needs copying into its document home first, and add one Agent Notes block saying the same if this run holds the claim.

**Claim it (standalone only).** Re-read the row right before starting (G3). If its Status is no longer `In QA`, or another run holds a live claim, skip it. An attended run on a pasted link audits only a row in `In QA`, `Needs Rework` (blog stage), or `QA Passed - Awaiting Publish Review` with no live claim; any other status: say why in chat and stop. If a QA verdict already exists for its current draft (G17), don't audit again: act on that verdict (Step 5). Otherwise claim it per shared/airtable.md (Claims): Claimed By `QA, scheduled` or `QA, [person's name]`, Claimed At, Claim Token, Status `In QA` (an attended run on a pasted link sets it here, for a row in one of the statuses above), Last Saved Step `QA round [n] started`, Rules Loaded, Reference Version, and Last Updated At, in one update. A blank Owner gets the Team row's Schedule Host in the same update. Read the row back, and go ahead only if the Claim Token is this run's own.

**Count the passes.** Note the row's **draft pass count**; it matters in Step 4. Use the number the Blog Writer hands over. In a standalone run, use G6: the larger of Draft Rework Count and this item's Rework History rows with Stage `Draft` and Outcome Status `Resubmitted`. Never use Brief Rework Count, and never add the two counts: an item whose brief needed two rounds must not escalate after one draft rework. A blank count means 0.

**The round number.** This audit's QA round `[n]` is the one the Blog Writer hands over. In a standalone run it is the draft pass count plus 1. The report and its title call round 1 "v1" and later rounds "rework [N]", where N is the draft pass count.

**Apply the product and learned rules.** Read every Active product rule and learned rule for this product before auditing anything. If a rule directly bears on one of the dimensions in shared/base-rules/qa.md (a past correction about CTA copy, keyword placement, tone, or anything else this audit checks), hold it as part of that dimension's standard for this audit, not just as something the Blog Writer was supposed to apply. A draft that violates a standing rule fails the matching dimension, even if it would otherwise pass. Then add one check per Active product rule and learned rule whose Agents include QA (shared/base-rules/qa.md, Product and learned rule checks). A failed Must rule sends the draft back, whatever the score (shared/rule-extraction.md). Learned rules apply only to their own product (G4).

---

## Step 1: Read everything before judging anything

Before scoring a single dimension, read, in full:

- **The content brief** this draft was built from (Brief Doc Link, read per the piece's storage file, Reading a document; or the pasted brief the Blog Writer handed over): its target word count, keyword plan, format skeleton, Spearhead Strategy, CTA plan, AEO plan, internal link plan, Freshness Log, Open Questions, Hook and Narrative Plan, and specifically the AI answer engine findings from the brief's Step 2d. If the brief says an AI engine couldn't be queried, Dimension 5 is judged against whatever findings exist, and isn't failed for research the brief couldn't do.
- **The draft itself, from the saved document** at Blog Doc Link, which always points to the newest version (in Drive every rework is its own new Doc; in Notion the Blog page is edited in place). Read it with its comments, and export it for Step 1.5, per the piece's storage file (shared/storage-drive.md or shared/storage-notion.md, Reading a document):
  - Drive: `read_file_content` with `includeComments: true`, then `download_file_content` once with `exportMimeType: "text/plain"` and once with `exportMimeType: "text/html"`, and decode the base64.
  - Notion: `notion-fetch` the Blog page (its Markdown is what gets measured) and `notion-get-comments`.
- **The row's Agent Notes,** for the writer notes (word count reasoning, open `[VERIFY]` research, anything the writer flagged) and, on a rework, the previous QA Issues list, so you can confirm each earlier issue was actually fixed. On a rework after a person's send-back, also read the Human Feedback entries that rework answered.
- **The product's reference files and rules** (Step 0).

An audit built from a partial read produces vague findings; read first, judge second.

---

## Step 1.5: Measure before you judge

Several dimensions are counts, not opinions: word count, reading level, paragraph length, em dashes, banned words, spacing. Measure them with scripts/measure.py on the exported document whenever a shell is available, never by eye. "Looked fine on a read-through" isn't a check. If no shell is available, measure by hand as carefully as possible and say so in the report. If the export isn't offered, measure from the text `read_file_content` returned and say so in the report (shared/platform-tools.md).

Save the exports in the run's working folder, then run the script (it needs only Python 3, and uses textstat if it is installed):

- Drive: save `draft.txt` (plain text) and `draft.html` (HTML), and run it by its full path inside this skill's folder, for example `python3 [skill folder]/scripts/measure.py draft.txt --html draft.html [options]`.
- Notion: save the fetched Markdown as `draft.md`, and run `python3 [skill folder]/scripts/measure.py --markdown draft.md [options]`. The script derives the plain text from the Markdown.

Options, filled from the brief and the base:

- `--keyword "[primary keyword]"` from the brief, or the keyword in the writer notes' "Primary keyword changed by" line when there is one.
- `--target-words [N]` from the brief's target word count.
- `--spelling US` or `UK` from the product's Settings row (Spelling).
- `--site [Website URL]` from the product's Settings row, so links split into internal and external.
- `--banned [file]`: a file with one word or phrase per line: the Blog Writer's Step 2b banned words and constructions, the style guide's own never-use list, and the words any Script product rule bans. A hit on this list is a failure on any use.
- `--check-links` to fetch every link and report its status. If the session's network can't reach the web from the shell, check each link with the session's web fetch tool instead. A dead citation link is a Blocker.

The script prints one JSON report. The numbers it prints are evidence for the report, and every hit it lists goes into the matching dimension with its location. What it measures, and where each part goes:

| Script output | Dimension |
|---|---|
| `banned_characters` (em dashes, en dashes, ellipsis characters, zero-width spaces, byte-order marks, double hyphens, emoji, garbled characters, each with its line and context) | 14 and 19 |
| `punctuation` (semicolons, "...", exclamation marks, arrows) | 14 |
| `raw_markup_in_text` (raw Markdown links, `**`, `#`, dividers, `>`, backslash escapes, HTML entities or tags shown as text) | 19 |
| `spacing` (Drive: blocks back to back with no empty paragraph, two empty paragraphs in a row; Notion: two empty blocks in a row) | 19 |
| `reading` (words, sentences, average sentence, share over 20 words, spread, Flesch-Kincaid grade, long sentences, repeated openings) | 17 and 18 |
| `length` (words against the brief's target, within 10%) | 17 |
| `structure` (headings, Title Case, words per H2 section and share, sections far shorter than the rest, visual elements per section, the longest stretch with no list, table, bolded key line, or callout, long paragraphs, FAQ questions and answer lengths, tables with header rows and borders) | 9, 12, 17, 19, 20 |
| `tags` (`[VERIFY]` and `[FRESHNESS_FLAG]` tags with locations, image suggestions) | 10 and 15 |
| `ai_tells_words_and_phrases` and `ai_tells_structure` (every hit from the Dimension 13 and 23 lists, with its sentence, hits per 300 words, hits per section) | 13 and 23 |
| `vague_phrases`, `vague_attribution`, `narrated_citations` | 15 and 18 |
| `date_anchors` (`as of`, `starting in`, `since [month]`, a month followed by a year, a bare year, version numbers) | 16 |
| `spelling` (the other spelling's forms) | 14 |
| `links` (every link's URL and anchor text, internal or external, weak anchors, bare URLs that aren't clickable, status when checked) | 2, 15, 19 |
| `keyword` (H1, first paragraph, first 100 words, H2s, body count, density, conclusion, SEO title, meta description, slug) | 1 |
| `blocker_candidates` | a list to confirm by reading, never a verdict on its own |

Adapt as needed: if a dimension needs a count the script doesn't make, measure it with a short extra script and keep its output with the rest. The script finds candidates; judging them is still QA's job (an AI-tell hit is a flag to review in context, and a bare year may be reader-useful).

---

## Step 2: The audit, each dimension a clear pass or fail, with a severity

Audit the draft against every dimension in shared/base-rules/qa.md, plus any dimension the product's quality checks add, plus one check per Active product rule and learned rule for QA. Follow that file exactly: how every dimension is judged, the severities (Blocker, Standard, Polish), the blocker list, and each dimension's bar. Every dimension gets a clear pass or fail; every failure gets a severity, its exact location, what's wrong, and the concrete fix; repeated instances are listed one per line.

On a rework, check every issue from the previous QA report and mark it fixed or not fixed.

---

## Step 3: Build the QA report

Write a short, readable report, not a wall of JSON, in this structure:

```
# QA Report: [Item ID]: [Working Title] ([v1 or rework N])

## Score
[Number of dimensions passed] / [total dimensions] passed
Base: [passed] of [total]. Product rules: [passed] of [checked]
Rules loaded: files [n] (brand [n], style [n], product knowledge [n], quality checks [n]), product rules [n], learned rules [n], newest reference version [v]

## Verdict
Approved: ready for publish review
or
Needs Rework: [N] issue(s) below must be resolved
or
Escalated: needs a person's decision after three rework passes

## Measurements
Words: [count] of [brief target] ([percent]) | Reading level: grade [X] | Average sentence: [X] words | Em dashes: [count] | AI-tell hits: [count] | Open VERIFY tags: [count] | Spacing and rendering: [clean, or N problems]

## Issues
For each failed dimension, most severe first:
- **[Dimension name] ([Blocker or Standard]):** [Exact location]. [What's wrong, specifically]. [The concrete fix.]
For each failed product or learned rule:
- **[Rule ID] ([Must or Should]):** "[the exact line that broke it]". [What's wrong, specifically]. [The concrete fix.]

## Earlier issues
On a rework only: each issue from the previous QA report, marked fixed or not fixed.

## Polish before publish
Minor items that don't fail the draft, each with its location and fix, for the human reviewer.

## What's working
One or two lines on the draft's real strengths, briefly. A rework pass that only sees failures tends to overcorrect and break what was already good.
```

- If measurements were taken by hand, or from `read_file_content` instead of an export, add one line under Measurements saying so.
- Leave out "Earlier issues" on v1, and leave out the product rules lines when no product or learned rule applies to QA.
- The QA Score written to Airtable is the passed count over the total, for example `21/23`, not a percentage (shared/base-rules/qa.md, Scoring).
- The report itself follows the house rules it checks: plain words, no em dashes, no AI-tell phrasing.
- In the saved document, the headings are real headings and the lists are real lists, in both document homes (the storage files say how).

---

## Step 4: The verdict, and the escalation check before you route anywhere

**The verdict.** Approved only when no dimension fails at Blocker or Standard severity and no Must rule fails. Polish items never block approval. Any Blocker or Standard failure, or any failed Must rule, means the draft fails.

**The escalation check.** Before deciding the next Status, check this item's draft pass count (Step 0.5, G6). If the draft fails and the draft pass count is already 3 or higher, do not route it to `Needs Rework` again. Three automated rework passes have already run on this item without producing a passing draft; a fourth is unlikely to either, and it is time for a human decision, not another loop. The verdict becomes Escalated instead (Status `Escalated - Needs Human Input`, written only after the 5c post, per 5b), and say so plainly in both the Slack post and the row's Agent Notes.

One exception (G13): if the Blog Writer says this audit follows a person's send-back above the cap, skip the escalation check for this one audit, since otherwise it would escalate without ever reading the rework. If that rework still fails, escalate rather than loop again. In a standalone run, apply this only when the newest Blog Writer block in Agent Notes says the current draft is that one rework pass for a person's send-back.

Otherwise, route normally per Step 5.

---

## Step 5: Save the report, update Airtable, and post to Slack only for the two cases that need a human

**5a. Save the QA report as a document, for every verdict.** Save it per the piece's storage file (shared/storage-drive.md or shared/storage-notion.md, by its Doc Home). That file has the save steps, the three-attempt budget, the "say what's happening, never go quiet" rule, and when to stop because the save is confirmed.

- **Drive:** a new native Google Doc for every round, in the product's Drive Folder, built from the Step 3 report with the storage file's HTML rules (real `<h1>` to `<h3>` headings, one `<p>` per paragraph, real lists, the `<meta charset="utf-8">` wrapper, non-ASCII characters as HTML entities, one empty spacer paragraph between blocks, no Markdown, no emoji). Title it per shared/storage-drive.md (Titles): `[Item ID]: QA Report (v1)` or `[Item ID]: QA Report (rework [N])`.
- **Notion:** the piece's one QA Report page, edited in place, so its link never changes. Round 1 creates it per shared/storage-notion.md (Saving a document). Every later round fetches the page fresh, then rewrites it with `replace_content`: the newest round's full report on top, and every older round inside one toggle at the end titled "Earlier rounds," newest first, each kept word for word.
- Run the access check (G19) before the link goes anywhere.
- If all three attempts fail, follow G15: leave the row in `In QA`, write the error, the time, and the full report into Agent Notes, clear the claim (standalone runs only), and give the full report in the run output with a plain note that it still needs saving. Never write a verdict to Airtable without its report link.

**5b. Update the record.** One `update_records_for_table` call on Content Items, per shared/airtable.md (Writing rules):

- QA Score: the passed count over the total, as text, like `21/23`. Use this audit's real total.
- Product Rules Result: passed of checked, as text, like `11 of 12`. Leave it blank when no product or learned rule applies to QA.
- QA Report Link: the report's link.
- QA Round: `[n]`.
- Last Saved Step: `QA round [n] verdict saved: [verdict]` (Approved, Needs Rework, or Escalated).
- Recheck Due, on an Approved verdict with freshness flags (5d).
- Last Updated At: now.
- Agent Notes: add a block at the end (G8), never overwrite, starting `QA [ISO time]:`, then `Round [n] ([v1 or rework N]).`, with the score, the product rules result, the verdict, and the report link, and, on a Needs Rework verdict, the complete Issues list with every exact location, problem, and fix.
- Status `Needs Rework`, only for a Needs Rework verdict. A standalone run clears Claimed By, Claimed At, and Claim Token in this same update. In the loop, leave the claim alone.

QA never changes Draft Rework Count or Brief Rework Count; it only reads them (Step 0.5).

On a Needs Rework verdict, that Agent Notes block and the report are the entire handoff to the Blog Writer: its rework step (or, in the same session, its Step 14) reads Agent Notes directly and reworks the draft itself. There is no Slack post for this case, not even a short one.

**The order for Approved and Escalated** (shared/slack.md, Confirmed post). Write every field above now, leaving Status at `In QA`. Post next (5c). Then write, in one update: Status (`QA Passed - Awaiting Publish Review` or `Escalated - Needs Human Input`), Slack Thread Link set to the post's link, Stall Count 0, an Agent Notes line `QA [ISO time]: [Approval or Escalation] post sent: [link]`, Last Updated At, and, in a standalone run, the cleared claim fields. A status that says a person must act, with no post that person can see, must never happen. If the post fails twice, still write the Status, leave Slack Thread Link empty, add `QA [ISO time]: [Approval or Escalation] post NOT sent: [error]` to Agent Notes with the full message you would have sent, and say so in the run output. The next run's Recovery step (shared/run-start.md, step 4), or the Blog Writer's Step 14 in this same session, finishes it.

**5c. Post to the product's Slack channel, only for Approved or Escalated.** Never for Needs Rework. A Needs Rework verdict ends at 5b; do not send anything to Slack for it, under any circumstance, even a brief status ping.

Post per shared/slack.md: the product's Slack Channel ID from its Settings row, every approver for this product from Members tagged by Slack ID (G11), the plain-words rules in "How every message reads," and the `(Content Machine)` marker as the last line.

- **If approved:** use the "Blog passed its checks" template. Its content:
  - The Score line carries the base score and, when product rules applied, the product rules result. Add the key measurements to the same line: "[N] words, grade [X] reading level."
  - "Before you publish" holds up to 3 short lines, in plain words: open `[VERIFY]` items, Polish items, or anything a person should check or recheck. Leave it out when there's nothing to check.
  - Link the draft's document and the QA report.
  - It asks for the final human check without implying the piece is live: the template's last line says what a tick or a reply does.
  - This mode's job ends the moment that message posts; it never comes back to check what the human did with it. The Orchestrator watches `QA Passed - Awaiting Publish Review`, reads the tick, cross, or reply, and writes `Published` or `Needs Rework` back onto this row.
- **If escalated:** first check for an escalation post about the current Blog Doc Link (G14). If one exists, don't post again; just write the Status. One about an older draft doesn't count. Otherwise use the "Stuck after 3 rounds" template: up to 3 short lines on what still fails after three passes, then the draft and QA report links, so a person isn't starting from zero.
- Keep the post short and plain: a summary and the links, never the whole report. Don't use pipeline words (shared/slack.md lists them, including status names, dimension numbers, "rubric," "freshness flags," "Polish items," and "rework 1"), don't mention missing tools, and don't type a "Sent using" line; Slack adds it.
- The post must agree with the Airtable record: the same score and the same verdict.

Confirm the tool's response returned a message link (G11). Then write that link into Slack Thread Link along with the Status, per 5b's order rule. If the post fails, read the error, fix what it names, and retry once; if it fails again, follow 5b's order rule. If Slack isn't connected at all (G1), follow shared/slack.md (When Slack is down), and put the post you would have sent into the Agent Notes line.

**5d. Freshness rechecks.** Only when this draft is being approved, and only if it actually carries freshness flags, per the brief's Freshness Log and the draft's own `[FRESHNESS_FLAG]` tags. Skip this step entirely if the draft carries no freshness flags, or if the item is routing to `Needs Rework` or `Escalated`.

- Use the cadence the brief's Freshness Log sets for each flagged claim (by default quarterly for pricing and feature-availability claims, annually for general statistics and evergreen framework claims), or the knowledge base's rule if it's stricter.
- **Always set Recheck Due** to the soonest recheck date, in the 5b update. This works without Calendar (G20).
- **Calendar, only when Google Calendar is connected (G20).** For each distinct cadence, first search the calendar (`search_events`) for an existing `[Item ID]: Recheck` event; if one already exists from an earlier approval of this item, update nothing and don't create a duplicate. Otherwise create one event with `create_event` on the primary calendar of the account running this audit: a 15-minute block dated that far out from today, titled `[Item ID]: Recheck [what] - [Working Title]`, with every approver for this product (Members, by Email) added as an attendee and the specific flagged claims, their sources, and the draft's document link listed in the description, so whoever opens the reminder doesn't have to re-derive what needs rechecking.
- If Calendar isn't connected, skip it: add one Agent Notes line with the recheck dates, and don't mention Calendar anywhere else, Slack included.

---

## Step 6: Capture feedback for the learning loop

Conditional: if a person corrects this audit directly in chat before the session ends, whether that's disputing a failed dimension, pointing out a check that missed something real, or adding a standard these rules don't currently cover, distill it into a general, reusable rule. This is also the place to log a pattern noticed across multiple items, not just a single one: if the same dimension keeps failing across different drafts for this product for the same underlying reason, that's worth a standing rule even without a person explicitly asking for one; note in What Happened that it's a cross-item pattern, not a single correction.

Save it as Suggested only, with `create_records_for_table`, never an update (shared/airtable.md):

1. A Reference row: Entry and Rule ID (the product's next free learned-rule ID (shared/rule-extraction.md, Rule IDs), like `ACME-L03`), Product, Type `Rule`, Layer `Learned rule`, Content (the rule, one testable line), Category, Agents, Level (Must or Should), Check Method (Script or Judged), Source Quote (the person's exact words, or the pattern's evidence), Status `Suggested`, Version 1.
2. A Feedback Log row: Date, Product, Stage `QA`, What Happened, The Rule, Reference Rule ID, Status `Suggested`, and Related Item linked to this row.

Never make a rule Active. Only a person's yes does that (shared/rule-extraction.md); tell the person in chat that the rule is saved as a suggestion and goes live only after an approver says yes. A rule the person's correction would use to lower a quality bar or an honesty rule isn't saved; say why. An unattended run logs only cross-item patterns, since no one corrects it in chat.

---

## Self-check before posting the verdict

- The audit was run on the saved document, re-read from its home and exported for measurement, not on memory of the draft
- The Step 1.5 measurements were taken with scripts/measure.py where a shell was available, and the numbers in the report came from it
- Every dimension was actually checked, not assumed; each has a clear pass or fail and a severity for every failure, no split calls
- Every failure has a specific location, a specific problem, and a specific fix, none vague enough to need a follow-up question
- Every em dash found in the draft is listed by exact location; the QA report itself contains zero em dashes
- Word count, reading level, and sentence length were checked against the brief's target and the grade 5 to 6 standard
- The saved document was checked for spacing, garbled characters, raw Markdown, and emoji
- AI-tell word, phrase, and structure hits from Dimensions 13 and 23 were judged for whether they're doing real work in context, not auto-failed on sight, except words the Blog Writer or style guide ban outright
- No claim about a feature, price, or capability is anchored to a date or version number without a reader-useful reason, per Dimension 16
- On a rework, every issue from the previous QA report was checked and marked fixed or not fixed
- Every Active product rule and learned rule for this product was applied while auditing, not just read and set aside; each one for QA has its own check, and a failed Must rule sent the draft back whatever the score
- The escalation check in Step 4 ran before Status was set, and G13's send-back exception was applied only for that one rework pass
- The escalation check used the draft pass count (G6), never Brief Rework Count and never the two counts added together
- The QA report was saved per the piece's storage file (a new Google Doc in the product's Drive Folder, or the piece's QA Report page with the newest round on top), passed the access check (G19), and is linked in QA Report Link
- QA Score, Product Rules Result, QA Report Link, QA Round, and Last Saved Step were written in one update; Agent Notes was added to, never overwritten
- No Slack post happened for a Needs Rework verdict; where a Slack post did happen, it used the shared/slack.md template, tagged every approver for this product, went to the product's channel, ended with the marker line, came back with a message link, was posted before the Status changed, agreed with the Airtable record (same score, same verdict), linked both documents, and, if approved, asked for the final human check without implying the piece is live
- If the draft was approved and carries freshness flags, Recheck Due is set, and either a calendar reminder exists for each distinct cadence with no duplicate created, or, if Calendar isn't connected, one Agent Notes line has the recheck dates and nothing mentions Calendar in Slack
- A standalone run claimed the row before auditing and cleared its claim with the final Status; a loop run left the claim to the Blog Writer
- No question was asked in an unattended run (G2), and nothing about the setup was asked in any run
- If a person gave feedback on this audit before the session ended, it was distilled into a Suggested rule and logged per Step 6
