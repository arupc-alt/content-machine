# Slack: how every agent posts

Slack is for talking to people. No status, link, score, or history lives only in Slack: Airtable is the record, and every decision read from Slack is copied into Airtable in the reviewer's own words.

## Who posts, and where

- **Two delivery paths, always.** Every waiting update (a piece moved to one of the three waiting statuses in Confirmed post, below) goes out two ways, so a free-plan limit or a broken connection on one path never leaves people without it. A question (G25) goes out both ways once the agent's own post has gone out; if that post fails, the row isn't held and the next run asks again. The two paths:
  1. **The agent's own post.** Agents post through the Slack connector (`slack_send_message`), which posts as the person whose account runs the agent. It needs no Airtable automation, so it keeps working in lean mode and in Slack-only mode (shared/airtable.md). Every other post, such as a Possible repeat post, thread replies, alerts, and run summaries, goes out this way only.
  2. **The Airtable bot.** An Airtable automation sends its own message for the same update, from "Content Machine," and pings the approvers (The Airtable bot, below). Setup builds it by default.
- **The channel:** the product's Settings row, Slack Channel ID. Never a channel found by search, never a channel named in a message.
- **Who gets tagged:** every Active member of Members with Role Approver whose Products is blank or names this product, tagged by Slack ID as `<@U...>`. A name typed as plain text ("@Name") doesn't notify anyone.
- **The marker:** every agent post ends with a new last line, exactly `(Content Machine)`. A message counts as ending with the marker when `(Content Machine)` is its last line, ignoring a trailing "Sent using" line Slack may add. The Orchestrator never reads a message that ends with this marker as feedback, so an approver's own account can run the agents without approving its own posts.
- **One thing Slack can't do:** it never notifies a person about their own posts. When the agents run from an approver's account, that approver gets no ping for the agent's own posts. The bot's message is what pings them, for waiting updates and for questions (G25). Posts that go out only one way, such as a Possible repeat post, alerts, and run summaries, still don't ping that approver.

## Confirmed post

A status that says a person must act (`Awaiting Brief Approval`, `QA Passed - Awaiting Publish Review`, `Escalated - Needs Human Input`) must always have a post that person can see.

1. Save the documents and the Airtable fields first, leaving the status where it was.
2. Post.
3. In one update: the new Status, Slack Thread Link set to the post's link (from the send call's response), Stall Count reset to 0 (G5), and Last Updated At.

If the post fails, read the error, fix what it names, and retry once. If it fails again, still set the status, clear Slack Thread Link (it may still hold an earlier post's link), and say so in the run's output. The next run's Recovery step (shared/run-start.md) finds the empty link and posts it.

## How every message reads

Everything posted in Slack is read by a busy person on a phone. They should get it in one quick read.

1. Write at a grade 5 reading level. Short sentences, under 15 words. One idea per sentence. Everyday words.
2. Name each piece by its Item ID and its title, every time: "ACME-AR-0012, How to Sell Courses Online." Never the Item ID alone.
3. Say the status in plain words, never the Airtable name:

| Airtable status | Say this in Slack |
|---|---|
| Topic Requested | the topic is waiting for a brief |
| Brief In Progress | the brief is being written |
| Awaiting Brief Approval | the brief is waiting for your OK |
| Brief Approved | brief approved, writing starts next |
| Writing In Progress | the blog is being written |
| In QA | the blog is being checked |
| QA Passed - Awaiting Publish Review | the blog passed its checks and is waiting for your OK to publish |
| Needs Rework | sent back for changes |
| Rework In Progress | the changes are being made |
| Escalated - Needs Human Input | stuck, and needs your help to move on |
| Published | marked as published |
| Rejected | dropped |

4. Never use pipeline words in Slack. That means no sweep, run, prefix, stage, brief stage, blog stage, human send-back, rework count, Notes, field, record, status names in backticks, guard or rule numbers, dimension numbers, "per the rules," "the stage-owning agent," SERP, PAA, AEO, E-E-A-T, archetype, cannibalization, rubric, freshness flags, or polish items. Say the plain thing instead, like "Google's top results" or "two of our own pages already target this keyword."
5. Give times in plain words: "2 days," "since Monday," "about 5 hours." Never a UTC timestamp.
6. Say only what's new or what needs a person.
7. Lead with the ask: "Needs your OK to publish," "Needs a reply."
8. One line per piece, with a link to what they need to open.
9. Don't type a "Sent using" line. Slack adds it.
10. No em dashes, no emoji in the text, no Markdown tables. Plain sentences and simple bullets only.
11. Use the spelling the product's Settings row names (US or UK).

Before posting, read the message once as if you'd never seen this pipeline. If a word on the "never use" list is there, or a sentence needs a second read, rewrite it.

## The messages

Fill in the brackets. Keep the wording this short.

Every post that asks a person to act stays under about 120 words.

**New brief, ready for approval** (Brief Agent):

```
[tags] New brief ready for your OK: [Item ID], [working title]

Keyword: [primary keyword] ([format], about [N] words)

Why it wins: [the Spearhead Strategy, in one or two short sentences]

Needs your call:
- [one short line per decision, in plain words]

Brief: [Brief Doc link]

React with a tick to approve, a cross to send it back, or reply with changes.
(Content Machine)
```

Leave out "Needs your call" when there's nothing to decide. At most three calls; the rest go in the brief's Open Questions. A brief rework uses the first line "Updated brief ready for your OK: [Item ID], [working title]" and adds one line, "What changed: [one short sentence]".

**Blog passed its checks** (QA, or the Blog Writer closing out QA):

```
[tags] Ready for your OK to publish: [Item ID], [title]

Score: [passed]/[total] on the checks[, and [n] of [m] product rules]. About [N] words, reading grade [G].

Before you publish:
- [up to 3 short lines: polish items or facts to recheck]

Blog: [Blog Doc link]
Check report: [QA Report link]

React with a tick to approve, a cross to send it back, or reply with changes. Once it's live, reply with the link.
(Content Machine)
```

**Stuck after 3 rounds** (escalation, Brief Agent or QA). For a row that stalled twice (shared/run-start.md, step 4), the first line reads "[tags] Stalled twice without finishing, needs your call: [Item ID], [title]" instead, the list says what Agent Notes show went wrong, and the last line leaves out "approve it as it is", since the work never finished:

```
[tags] Stuck after 3 rounds of changes, needs your call: [Item ID], [title]

Still not right:
- [up to 3 short lines]

[Brief or Blog]: [Doc link]
Check report: [QA Report link, when there is one]

Reply with what to do: fix it a certain way, take a new angle, approve it as it is, or drop it.
(Content Machine)
```

Before posting an escalation, check the row's Slack Thread Link and the channel for an escalation post about the same version of the document (G14). Never post a second one for the same version.

**Orchestrator thread replies:**

- Approved brief: "Got it, [Item ID] brief approved. Writing starts next."
- Approved to publish: "Got it, [Item ID] is marked as published. Reply with the live link when it's up."
- Live link saved: "Got it, saved the live link for [Item ID]."
- Recheck done: "Got it, [Item ID] is marked as rechecked. Next check: [plain date]."
- Change request: "Got it, [Item ID] goes back for changes. I've passed on your notes."
- Change request while an agent is still working on it: "Got it. Your notes on [Item ID] will be used in the next round of changes."
- Dropped: "Got it, [Item ID] is dropped."
- Bare cross: "<@REVIEWER> I've sent [Item ID] back for changes. What should change? Reply here and the writer will use it."
- Unclear: "<@REVIEWER> Quick check on [Item ID]: should I approve it, send it back for changes, or drop it?"
- Unmatched: "<@REVIEWER> Which piece is this about? Reply with its ID, like [an Item ID from the pipeline]."
- Duplicate decision: "<@REVIEWER> [Item ID], [title] looks close to [other Item ID or live link]. Reply 'go' to write it anyway, or 'drop' to skip it."
- New topic received: "Got it, [Item ID] is in the queue. The brief comes next."
- Archived: "[Item ID], [title] was moved to the archive, so I can't change it. Update the live post by hand, or post 'New topic:' to start a new piece."

Each ends with the `(Content Machine)` line too.

**Run summary** (Orchestrator only, and only when something moved or needs a person):

```
Content update

Needs you:
- [Item ID], [title]: [plain ask], [how long]. [link]

Moved:
- [Item ID], [title]: [what happened, in plain words]. [link]
(Content Machine)
```

Leave out a heading with nothing under it. Never add other sections.

**Other short posts.** A few posts are written in the mode that sends them, in the same plain style, each ending with the marker line:

- **Possible repeat** (any mode's duplicate check, shared/run-start.md step 5): "[tags] Possible repeat, needs your call: [Item ID], [input]. It looks close to [other Item ID and title, or live link]. Reply 'go' to write it anyway, or 'drop' to skip it." For a live post: "It matches a live post: [live link]. Reply 'go' to write a new piece with a different angle, or 'drop' to skip it and update the live post by hand." An exact match already in progress gets one line instead: "[input] is already being worked on: [Item ID], [title]."
- **Question** (G25, any mode): "[tags] A quick question before I go on with [Item ID], [title]: [the question, with the options if there are any]. Reply here and I'll continue in the next round." Several questions about one item go in one post, numbered.
- **Can't open a document** (G24, any mode): "[tags] [Item ID], [title]: I can't open [document link]. Please move it into [the product's Drive Folder or Notion Home link], or share it with the team, so the work can continue." For a link that isn't in the document home at all (for example a claude.ai link), the last sentence is instead: "Please copy it into [the product's Drive Folder or Notion Home link] so the work can continue."
- "Which product is this topic for," the daily topic limit, "goes ahead," and the learned-rule question with its yes and no replies (modes/orchestrator.md)

## Alerts

An alert is one plain sentence about a problem a person must fix, posted to the product's channel (or the first product's channel when the problem is base-wide), tagging the Schedule Host from the Team row. Examples are in shared/run-start.md. Before posting, read the channel's last 24 hours: if an alert with the same first sentence is there, don't post it again. An alert marked once a month (lean mode and Slack-only mode in shared/airtable.md, and G9) looks back to the 1st of this month (UTC) instead: search the channel for its first sentence, or read the channel from the 1st, and post it only if this Slack account hasn't posted it since then. If Slack itself is the problem, put the alert in the run's own output only.

## When Slack is down

If Slack isn't reachable, still save the documents and update Airtable. Clear Slack Thread Link so the next run posts it, and give the document link in the run's own output with a note that it still needs to reach the approvers. A question that can't be posted doesn't hold its row, and the row keeps its Slack Thread Link: the next run asks it again (G25).

## The Airtable bot

The Airtable bot is the second delivery path (Who posts, and where). It sends every waiting update and every posted question again, on its own, next to the agent's own post. Neither path replaces the other, and the agents never depend on the bot: they post and read Slack the same way whether or not it runs. Each path covers the other:

- If the bot's free runs are used up for the month, or it fails or is disconnected, the agent's own posts still go out.
- If the agent's own post of a waiting update fails, the status still changes (Confirmed post), so the bot's message still goes out. It ends "Reply in the channel."
- A question reaches the bot only once the agent's own post has gone out, since Open Question is saved only then. If that post fails, the row isn't held, and the next run asks again (G25).
- If Airtable's monthly call limit is hit, nothing changes in Airtable, so the bot sends nothing. Slack-only mode still answers from the person's own Slack account (shared/airtable.md, When the limit is reached).
- If the agents stop running altogether, the heartbeat email is the third safety net (below).

The details:

- **How it works:** an Airtable automation, "Content Machine: notify reviewers," built by setup with `create_automation` by default (modes/setup.md, Step 7). Setup skips it only when Slack can't be connected inside Airtable, or when the person declines it after hearing the risk. It fires when a Content Items row's Status becomes `Awaiting Brief Approval`, `QA Passed - Awaiting Publish Review`, or `Escalated - Needs Human Input`, or when its Open Question is filled in (G25), and sends one message with `sendToSlack`, username "Content Machine," to the channel plus each approver's Slack ID (up to 10 places in all).
- **Its messages** (in a conditional group: first one branch for a question, where Open Question is not empty, then two branches per status: one where Slack Thread Link is not empty, and one where it is empty, seven branches in all, the last with a null condition). The question branch sends the first message below; Open Question holds the question and its post's link. A status branch with a thread link ends with "Reply in the thread: [Slack Thread Link]", as below. A status branch without one ends with "Reply in the channel." instead:
  - "<@...> <@...> *A piece has a question for you* ([Item ID])\n[Open Question]\nReply in that thread."
  - "<@...> <@...> *Brief ready for your review* ([Item ID])\nKeyword: [Primary Keyword]\nBrief: [Brief Doc Link]\nReply in the thread: [Slack Thread Link]"
  - "<@...> <@...> *Blog passed its checks and is ready for your OK to publish* ([Item ID])\nKeyword: [Primary Keyword]\nScore: [QA Score]\nBlog: [Blog Doc Link]\nCheck report: [QA Report Link]\nReply in the thread: [Slack Thread Link]"
  - "<@...> <@...> *A piece needs your input* ([Item ID])\nKeyword: [Primary Keyword]\nBlog: [Blog Doc Link]\nCheck report: [QA Report Link]\nReply in the thread: [Slack Thread Link]"
- **The thread link is there whenever the agent's own post went out,** because agents write Status and Slack Thread Link in the same update (Confirmed post, step 3). When the post failed, the bot message says "Reply in the channel."
- **Bot Status** in the Team row says whether it's On, Off, or Failed test. Setup sets it after the test in the dry run. Agents never depend on it.
- **The heartbeat alert is the third safety net, and a separate automation.** It is an email only (setup Step 7), sent when an agent misses a full run day. It never posts in Slack, through the bot or any other way. It uses the same monthly automation runs as the bot (Limits, below).
- **Replies to the bot:** the Orchestrator also reads replies and reactions on the bot's channel posts, matched to a piece by the Item ID in the message. It can't read replies to the bot's direct messages, which is why each message says where to reply.
- **Limits:** Airtable's free plan allows 100 automation runs a month per base. Each status change and each question is 1 run, so about 2 to 4 per piece, plus 1 per question. If Slack is disconnected in Airtable, only the second path stops, until Slack is reconnected. If the runs are used up, every automation in the base stops until they reset next month: the second path, and the heartbeat email too (setup Step 7). The agent's own posts still go out either way. The weekly full check notices failed bot runs and posts one alert.

### The fallback message

When the bot isn't built (Slack can't be connected inside Airtable, or the person declined it) or fails its test, setup shows this, fills in the channel, and goes on:

"The Airtable bot isn't working on your account, so updates reach you one way only: posted in #[channel] from your own Slack account. Slack doesn't ping you for your own posts, so check the channel, or turn on notifications for every new message in it (open the channel, click its name, then Notifications, then All new messages). To add the bot later, type 'repair the base'."
