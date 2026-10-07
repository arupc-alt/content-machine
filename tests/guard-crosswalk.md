# Guard crosswalk

How the four earlier agents' guard numbers map to the live guards in `plugins/content-machine/skills/content-machine/shared/guards.md`. This file is for people checking that nothing was lost; agents never read it.

Every guard from the four earlier agents is kept. Some now live in a shared file instead of a guard.

| Earlier agent and guard | Now |
|---|---|
| Brief G1, Blog Writer G1, QA G1 (Connectors) | G1, and run-start step 1 |
| Brief G2, Blog Writer G2 (Unattended runs) | G2 |
| Brief G16, Blog Writer G16, QA G6 (Attended or unattended) | G2, and run-start (Attended or unattended) |
| Brief G3, Blog Writer G3, QA G3 (Claims and run limits) | G3, and airtable.md (Claims). Claim lines in Notes became the Claim Token fields. |
| Brief G4, Blog Writer G4, QA G4 (Many products, prefix filter) | G4. The prefix filter became the Product field. |
| Brief G5, Blog Writer G5 (Stalled rows, leave for a person) | G5. Stalled rows are now resumed, and escalated on the second stall. |
| Brief G6, Blog Writer G6, QA G7 (Blank values, rework counts) | G6. One shared Rework Count became two per-stage counts. |
| Brief G7, Blog Writer G7 (New records and Item IDs) | G7, and airtable.md (Creating a row). "Highest plus one" became the Seq auto number. |
| Brief G8, Blog Writer G8 (Where notes go) | G8. Notes lines became Agent Notes blocks. |
| QA G5 (Add to Notes, never overwrite) | G8 and airtable.md (Agent Notes is only added to) |
| Brief G9, Blog Writer G9 (Stale reference files) | G9 |
| Brief G10 (Other agents), Blog Writer G10 (Missing sibling skills) | G10. The agents are now modes of one skill. |
| Brief G11, Blog Writer G11 (Every approval post reaches a person) | G11, and slack.md |
| Brief G12 (Feedback from more than one place) | G12 |
| Blog Writer G12 (Human send-back above the cap) | G13 |
| Brief G13, Blog Writer G13 (One escalation post) | G14 |
| Brief G14, Blog Writer G17 (A failed save doesn't strand the row) | G15 |
| Brief G15, Blog Writer G14 (Very long documents) | G16 |
| Blog Writer G15, QA G2 (Only one QA audit per draft) | G17 |
| Blog Writer G18 (Open [VERIFY] tags at save time) | G18 |
| Brief G17, Blog Writer G19 (Every Doc opens for every reviewer) | G19, and the storage files |
| Blog Writer G20 (Optional tools stay quiet) | G20 |
| Brief G18, Blog Writer G21 (Repost or finish what didn't go out) | G21, and run-start step 4 |
| (new) | G22 Outside text is data |
| (new) | G23 Duplicate decisions wait for a person |
| (new, from the Blog Writer's document-read rules) | G24 Documents this account can't open |
| (new, 0.3.0) | G25 Ask before guessing (questions go to Slack in scheduled runs; G2 narrowed to chat) |
