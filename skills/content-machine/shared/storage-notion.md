# Documents in Notion

Used when a piece's Doc Home is `Notion`. The layout below was built and tested end to end: create, rework in place, tables, images, comments, and a second round of changes.

## Where documents live

- One top page, "[Company] Content Machine," in the host's Notion workspace (Settings: Notion Home), with a short "how to use this" note.
- A Content database under it, built by setup from `templates/notion-content-db.md`. One database row per piece.
- Three pages inside each piece's row: Brief, Blog, and QA Report. All three are edited in place on every rework, so their links never change.
- In a shared base, only the host's runs write to Notion. A teammate's attended run that would write a page leaves the row for the next scheduled round instead, and says so.

## Saving a document (first version)

1. Find or create the piece's row in the Content database (`notion-create-pages` with the database as parent). Properties: Title, Item ID, Status, Primary Keyword, Format, Product, Target Words, Airtable Record (the row's Airtable link), Slack Thread.
2. Create the page under that row (`notion-create-pages` with the row as parent), titled `Brief`, `Blog`, or `QA Report`, with the full content as Notion-flavored Markdown: real headings, real tables, bulleted and numbered lists, links, bold. A very long page is written in chunks of about 20 blocks: create the page with the first chunk, then add the rest in order.
3. Confirm from the call's own response that the page exists, and take its URL. That URL is the document link for Airtable and Slack.
4. Check access (below).

At most three attempts per document, the same as Drive. After three failures, follow G15.

## Reworks edit the same page

1. Fetch the page fresh (`notion-fetch`) right before editing. Never edit from an old copy: a person may have changed it.
2. **Small text changes** (a sentence, a heading, a table cell): `notion-update-page` with targeted `update_content` edits, each matching the exact current text.
3. **Big changes, or any image swap:** `notion-update-page` with `replace_content`, rewriting the whole page from the fresh fetch plus the changes. Comments and block IDs survive this.
4. Add one entry to a "What changed" toggle at the end of the Blog page: the rework number, the date, and one line per change. Notion's free plan keeps only 7 days of page history, so this log is the record.
5. Rework History records the same page link as both Previous Doc Link and New Doc Link, plus the "What changed" lines in Resolution Log.

## The QA Report page

One QA Report page per piece, edited in place each round: the newest round's full report at the top, and every earlier round inside an "Earlier rounds" toggle at the bottom, newest first. QA Report Link always points to this page. In Notion mode, QA also fills the database row's Word Count and Reading Grade from its measurements.

## Known quirks, and the fixes

| Quirk | Fix |
|---|---|
| Dollar signs come back as `\$` | Match the escaped form when editing, and re-read after every edit |
| An image line can't be matched by a targeted edit | Swap images with `replace_content` |
| PNG upload can be blocked in some sandboxes | Draw charts and diagrams as SVG and add them with `notion-create-attachment`; use public image links for photos |
| The connection drops mid-run | Retry once, then log it in Agent Notes and stop cleanly. Every step can be rerun without doing it twice |
| A page was deleted or moved | Log it on the Airtable row and post one alert. Never recreate it silently |
| 2 or more workspace members turn on a 1,000-block limit | Setup warns up front. Invite reviewers as guests, not members. If the limit error appears, post one plain alert |

## Reading a document

`notion-fetch` the page for its content, and `notion-get-comments` for its comments. For QA's measurements, the fetched Markdown is the text that gets measured, and its structure (headings, tables, lists, spacing) is checked from the same fetch.

## Access check

The Settings row's Doc Sharing says how reviewers open pages:

- **Notion web link:** the top page is published to the web with search engine indexing off. Every page under it is readable by anyone with its link. Setup warned that confidential plans don't belong under it. Setup confirms the public link opens (web fetch of the pasted public URL). Runs check it only during the weekly full check, with the web fetch tool, and post one alert if it no longer opens (shared/run-start.md, step 3).
- **Notion guests:** each approver is invited as a guest (up to 10 on the free plan). A new page under the top page inherits their access. If an approver isn't a guest yet, post one alert naming them.

## Comments

Reviewers give decisions in Slack. Comments left in Notion are read by the Orchestrator like Drive comments: only unresolved comments from an approver, left after the page was created, count.
