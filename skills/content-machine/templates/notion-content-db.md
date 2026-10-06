# Notion layout

Built by setup in the host's Notion workspace when a team picks Notion. Setup checks what exists first and never makes a second copy.

## Top page

Title: `[Company] Content Machine`

Body:

```
This is where the content machine keeps its briefs, blogs, and check reports.

- Every piece has a row in the Content database below.
- Open a row to find its Brief, Blog, and QA Report pages.
- Give feedback in the Slack channel, in the piece's thread. The pipeline reads it from there.
- Don't move or delete pages. The pipeline edits them in place.
```

## Content database

Under the top page. Properties:

| Property | Type | Notes |
|---|---|---|
| Title | title | The working title |
| Item ID | text | |
| Status | select | The same 12 statuses as Airtable |
| Primary Keyword | text | |
| Format | select | Comparison/Alternatives, Versus/Head-to-Head, Listicle/Examples, How-to/Guide |
| Product | select | One choice per Settings row |
| Target Words | number | From the brief |
| Word Count | number | From QA |
| Reading Grade | number | From QA |
| QA Score | text | Like 21/23 |
| Rounds of Changes | number | Draft passes |
| Airtable Record | url | The Content Items row |
| Slack Thread | url | |
| Created | created time | |
| Last Edited | last edited time | |

The host's Orchestrator copies Status, QA Score, and Rounds of Changes from Airtable each run for rows that changed, so Notion never shows an old status. QA fills Word Count and Reading Grade when it saves its report.

## Views

1. All pieces: table, newest first.
2. Board: grouped by Status.
3. Needs your OK: filtered to Awaiting Brief Approval, QA Passed - Awaiting Publish Review, and Escalated - Needs Human Input.
4. Published: filtered to Published.

## Pages inside each row

- **Brief**, **Blog**, and **QA Report**, created when each first exists, and edited in place after that.
- The Blog page ends with a "What changed" toggle that logs every rework.

## Sharing

Chosen at setup and saved in Settings (Doc Sharing):

- **Notion web link:** publish the top page to the web, search engine indexing off. Anyone with a link can read every page under it, so keep confidential plans out.
- **Notion guests:** invite each approver as a guest (up to 10 free). Each needs a Notion account.

Never invite reviewers as workspace members: 2 or more members turns on a 1,000-block limit on the free plan.
