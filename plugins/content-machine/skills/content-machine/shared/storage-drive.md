# Documents in Google Drive

Used when a piece's Doc Home is `Drive`. Every brief, draft, and QA report is a native Google Doc inside the product's Drive Folder (Settings). Never use Claude Docs, a `.docx` built by a script, or any other file type for pipeline documents.

## Where documents live

- The product's Drive Folder (Settings) holds every document. When the company uses Google Workspace, setup makes it a Shared Drive folder, which the company owns, so files survive when people leave.
- In a shared base without a Shared Drive, only the host's runs create documents (the host account owns the folder). A teammate's attended run that would create a document adds a Topic Requested row (or leaves the row for the next scheduled round) instead, and says so.

## Saving a document

Save in one call, with no files built on disk. The Drive connector turns HTML into a native Google Doc by itself.

1. **Turn the finished text into one clean HTML string, in memory.** Include everything, exactly as written. Use `<h1>`, `<h2>`, and `<h3>` for headings, so they arrive as real Google Docs headings, never bold text sized up to look like one. One `<p>` per paragraph. `<ul>`, `<ol>`, and `<li>` for lists, never a typed bullet character. `<table border="1">` with `<th>` and `<td>` for every table, so the borders survive. `<a href="...">` for every link, including links inside table cells; never write `[text](url)`. `<strong>` for bold. Each image-suggestion callout and each CTA block is its own `<p>` that starts with a bold label (`<p><strong>[IMAGE SUGGESTED]</strong> ...</p>`), never a leading `>` character. No emoji anywhere.
2. **Spacing.** Google Docs keeps no gap between imported paragraphs. Put exactly one empty spacer paragraph, `<p>&nbsp;</p>`, between any two blocks: between two paragraphs, before and after every list, table, and callout, and before every `<h2>` and `<h3>`. Never two spacers in a row.
3. **HTML only, never Markdown.** Never escape brackets with a backslash; write a tag as plain `[FRESHNESS_FLAG: verify before publishing]`. Don't use `---` or `***` as a divider. Escape `&`, `<`, and `>` inside text. Wrap it all as `<html><head><meta charset="utf-8"></head><body>...</body></html>`, and write every non-ASCII character as a numeric HTML entity (`&#215;` for the multiplication sign, `&#8594;` for an arrow, `&#8220;` and `&#8221;` for curly quotes), or Drive's conversion can garble it. No `<style>` blocks, no scripts, no embedded images.
4. **Check the structure before saving.** If a shell is available, run a short script over the HTML and fix every failure first; otherwise check by reading. This check doesn't count as a save attempt. It checks the mode's own structure rules (for a brief: exactly one `<h1>` and the twelve `<h2>` sections in order, the At a glance table right after the `<h1>`) plus: no `<ol>` with a single `<li>`; no `|` table text, no bare `http` text outside an `href`; no `#`, `**`, `->`, or lines starting with `* ` or `- `; every list of three or more items with the same labeled fields is a `<table>`; one spacer between blocks, never two.
5. **Create the Doc with one call:** `create_file` with `title`, `textContent` set to the HTML, `contentMimeType: "text/html"`, and `parentId` set to the Drive Folder's ID. Leave `disableConversionToGoogleType` unset.
6. **Confirm it from that call's own response.** The returned `mimeType` must be `application/vnd.google-apps.document`. The returned `viewUrl` is the document's link. Anything else counts as a failed attempt.
7. **Check access** (below). Only then does the link go into Airtable or Slack.

**At most three attempts** at `create_file` per document. If a call errors, read the error, fix the exact thing it names (malformed HTML, an unescaped character, a missing `contentMimeType`), and retry within the budget. After three failures, follow G15. Never fall back to another document type.

**Say what's happening as it happens.** Say briefly when the call is about to fire and when it comes back confirmed. Never go quiet for minutes at a time: a silent stall is much harder to catch. If a call is taking far longer than the run's other steps, stop, report what was in progress, and leave it for a person rather than waiting quietly.

**Once the call's own response confirms success, the save is done.** Don't read the Doc back to double check, and don't call it again.

## Titles

| Document | v1 | Rework N |
|---|---|---|
| Brief | `[Item ID]: [Working Title] - Brief` | `[Item ID]: [Working Title] - Brief (rework [N])` |
| Draft | `[Item ID]: [Working Title]` | `[Item ID]: [Working Title] (rework [N])` |
| QA report | `[Item ID]: QA Report (v1)` | `[Item ID]: QA Report (rework [N])` |
| Pasted brief copy | `[Item ID]: [Working Title] - Brief (pasted)` | |

## Reworks make a new Doc

The connector can't edit a Doc's text once it exists. Every rework is a new Doc, and the older Docs stay in the folder as the record of each earlier pass. So get each version right before saving. The row's link field always points to the newest version, and Rework History records the previous and new links.

## Reading a document

Take the file ID from the link (the part between `/d/` and the next `/`), and call `read_file_content` with `includeComments: true`, so any comment a reviewer left inside the Doc comes back with it. For QA's measurements, export the Doc as plain text and as HTML with `download_file_content` (or read it, when export isn't offered) so the scripts measure what the reviewer actually sees.

## Access check

The people who must be able to open every document: every Active member of Members (approvers and runners). Check with `get_file_permissions`. Anyone missing gets `share_file` with role `commenter` (role `writer` for runners on the folder itself). Skip the account that owns the Doc.

If creating inside the folder fails (the folder was deleted, or this account can't add to it), create the Doc without `parentId`, share it with every one of those people the same way, add one Agent Notes line saying the folder needs fixing, and post one alert. If a share still fails after one retry, the Doc still counts as saved, but name that person in Agent Notes and in the Slack post, so nobody is handed a link they can't open.

## Comments

Reviewers may leave comments in a Doc. Only the Orchestrator turns them into decisions (shared/run-start.md and modes/orchestrator.md). Only unresolved comments from an approver, left after the Doc was created, count. If a comment's resolved state or author can't be read, treat it as unresolved, match the author by name in Members, and say in the run summary that comments were matched by name.
