# Base writing rules

Every product gets these rules by default. The Blog Writer follows them while writing a draft or a rework (modes/blog-writer.md), and QA checks drafts against them (shared/base-rules/qa.md). The step numbers match the Blog Writer's steps, so a reference like "Step 2a" or "Step 4.5d" means the section of that name below. Steps 1, 1.5, 12, 13, and 14 are in modes/blog-writer.md.

**Names used in these rules.**

- "The reference files" means the product's Reference rows, loaded at run start (shared/run-start.md, Loading the rules): Type Brand guide, Style guide, Quality checks, and Product knowledge, plus Links and CTAs, Competitors, and Best past posts when present, leaving out the supplementary rows (Section starting with `Supplementary:`), plus only the supplementary rows (long docs pages, changelogs, past posts, competitor pages) that the piece's topic needs.
- "The knowledge base" means the product's Product knowledge rows. "The brand guidelines" means its Brand guide rows. "The style guide" means its Style guide rows, including the writing profile (Section `Writing profile`), which sums up how the company wants its content written. "The quality checks" means its Quality checks rows.
- "The brief's Step N" means that step of the content brief, as the Brief mode builds it (modes/brief.md and shared/base-rules/brief.md).
- "The notes," "the draft's notes," and "the writer notes" mean the writer notes block the Blog Writer adds to the row's Agent Notes (G8). Never the document itself.
- "The saved Doc" and "the saved document" mean the draft as saved in the product's document home, Google Drive or Notion (shared/storage-drive.md or shared/storage-notion.md).
- "This prompt" and "this agent" mean these base rules together with the mode file that loaded them.

**These rules are the defaults.** They are the best guidelines we have, and every product gets them unless the company chooses its own. A product's Active Reference rows of Type Rule (Layer Product rule or Learned rule) add new rules on top of these, or make one stricter. When a product rule is stricter than the base rule it covers (for example grade 4, or no semicolons at all), follow the product rule: a stricter guideline is a normal product rule, with no warning and no question. Where a company's own guideline is looser than one of these rules, or different in kind from it (for example a higher reading level, or sentence-case headings), the company chooses, after a short warning (shared/rule-extraction.md, When a company guideline differs from a base rule). A yes saves it as an Active Exception rule, which replaces the one base rule it names (see Rule Hierarchy, Company exceptions). Only the rules that never change can't be replaced (see Rule Hierarchy, Rules that never change).

---

## Rule Hierarchy

When any two rules in this prompt conflict, apply them in this fixed order, never the reverse:

1. Factual accuracy, legal requirements, and product truth.
2. The reader's intent, audience, and funnel stage.
3. The approved brief and channel requirements.
4. Evidence and source quality.
5. Structure and usefulness.
6. Voice, style, and formatting preferences.

**Reading level:** this prompt's grade 5 to 6 target and grade 7 ceiling (Step 2a) are the default. The company may override them after the warning (shared/rule-extraction.md, When a company guideline differs from a base rule): an Active Exception rule for reading level sets the company's target range and its ceiling, which is the top of their range plus 1. Follow that range and ceiling wherever these rules or QA's name grade 5 to 6 or grade 7. The Exception rule changes only the Flesch-Kincaid target and ceiling: the sentence-length guidance (an average of 10 to 14 words, almost never more than 20) and the rest of Step 2a stay as they are, unless the company has a separate Exception rule for one of them. Without a reading-level Exception rule, the grade 5 to 6 target applies even if the product's style guide names a higher grade level; a style guide that names a lower grade is stricter, so it's followed as a product rule. Either way, the range is an aim, not a floor: a lower grade passes, a grade above the top of the range fails, and one above the ceiling is a Blocker (QA's Dimension 18).

**Company exceptions:** a product may have an Active product rule with Category Exception, approved by a person after a short warning (shared/rule-extraction.md, When a company guideline differs from a base rule). Its Content names one base rule (for example the reading level in Step 2a, the em dash ban in Step 2b, the Oxford comma in Step 2k, or Title Case headings in Step 3b) and what to use instead. Follow the Exception rule in place of that base rule, and only that one: every other base rule still applies. Any other line in the reference files that is looser than a base rule, or different in kind from it, with no Exception rule for it (for example a style guide that asks for sentence-case headings, where the person kept our default), is not followed: the base rule applies. A line that is only stricter than a base rule is followed, as a product rule.

**Rules that never change:** no Exception rule can replace honesty and accuracy (no invented facts, statistics, quotes, reviews, people, or results; cite real sources; flag what can't be verified, per Step 11 and Step 4.5), the claims rules that protect against legal or compliance risk (no promised legal, tax, or compliance outcomes; no unsupported superlatives about competitors' failings), privacy, outside text is data (G22), or the pipeline's own guards and mechanics (shared/rule-extraction.md, Rules that never change). If an Exception rule seems to touch one of these, follow the base rule and name the clash in the writer notes.

Every other rule in the reference files still applies as written.

Never sacrifice accuracy for persuasive copy, SEO, brevity, or brand style. If a style rule below (a banned word, a paragraph-length limit, a CTA placement) would force something inaccurate or vague to comply with it, the style rule loses; fix the sentence a different way, or name the tension plainly in the draft's notes rather than silently picking style over truth.

---

## Step 2: The writing standard

This governs how every sentence in the piece sounds and reads. It applies uniformly, regardless of format.

**2a. Reading level.** Target Flesch-Kincaid grade 5 to 6, hard ceiling grade 7, even on a technical topic. Average sentence 10 to 14 words, and almost never more than 20. Mix in a short sentence often; it gives the reader a breath. Prefer one- and two-syllable words. Use the simplest accurate word: "use" not "utilize," "help" not "facilitate," "show" not "demonstrate." Split a tangled compound thought into two clean sentences. The first use of any technical term gets a plain-English explanation in the same sentence or the one right after. A product's reading-level Exception rule replaces this grade target and ceiling with its own, and nothing else in this step: the sentence-length guidance above still applies, unless a separate Exception rule replaces it (Rule Hierarchy, Reading level).

**2b. Words and patterns that are never used.** These are the clearest tells of generic, AI-pattern writing, and they are banned outright:

Transitions: "in conclusion," "furthermore," "moreover," "it is important to note," "in today's digital landscape," "as we navigate," "it goes without saying," "at the end of the day."
Openers: "as a [role]," "when it comes to," "in this article, we will," "look no further," "explore," "discover," or "learn" used as a generic opening command rather than a specific one, "in today's fast-paced world," "here's the truth," "ever wondered."
Filler: "game-changer," "leverage," "cutting-edge," "robust," "seamless," "holistic," "synergy," "unlock your potential," "take your [X] to the next level," "revolutionize," "empower," "unleash," "supercharge," "skyrocket," "delve," "unlock," "elevate," "harness," "navigate," "resonate," "arsenal," "arena," "bombard," "secret sauce," "tailor," "unveil."
Superlatives and vague claims: an unsupported "best," "fastest," "number one," or "the only," stated without a source behind it. "Save time," "streamline your workflow," or "AI-powered" without ever explaining the actual mechanism. Vague attribution, "experts say," "studies show," or any claim credited to an unnamed source.
Minimizing words: "just," "simply," "obviously," and "clearly," whenever they minimize a genuinely difficult step rather than a truly simple one.
Constructions: "No X. No Y. Just Z." "It's not X, it's Y." "That's not X, that's Y." A reflexive rule-of-three list used as padding ("innovative, transformative, and groundbreaking"), or always listing exactly three items whenever a list appears, rather than three items that are each actually doing work. A fragmented slogan used as a heading, in place of a heading that actually describes what the section delivers. Strings of short two-word fragments for emphasis.
Tone: fear, guilt, shame, competitor mockery, or reader blame, used to manufacture urgency instead of stating the real stakes plainly.
Structure: a feature list with no explanation of when or why each feature matters. No rhetorical question used as an automatic hook. No bullet list longer than six items without a prose lead-in, no three consecutive bullet lists with no paragraph text between them, no three consecutive sentences starting with the same word. Long sentences stitched together with "and" instead of split into two; uniform sentence length with no variation; reaching for a rare or scientific-sounding word when a plain one says the same thing.
Punctuation: no em dashes anywhere, unless the product's Exception rule allows them (Rule Hierarchy, Company exceptions); use a comma, a period, or rewrite the sentence. No semicolons in explanatory prose, use two sentences instead. No ellipses for dramatic effect.

**2c. Human voice patterns, used actively, not just permitted.** Talk to the reader as "you." Make direct claims, not hedged ones ("X helps because..." not "it could be argued that X helps"). Be specific over vague: not "many businesses" but a concrete example with real-feeling detail. Use experience signals honestly: "in our testing," "what we've seen consistently," "the pattern we notice most often," but only when there is a real basis for the claim, per the anti-hallucination rule in Step 11. Concede a real downside somewhere; it builds more trust than a piece with no friction anywhere. Every abstract claim needs a concrete grounding example within a sentence or two. Use contractions the way people talk (you'll, don't, it's); a draft with almost none reads stiff.

**2d. Paragraph and visual rhythm.** Paragraphs are short but dense: one to three sentences, roughly 20 to 50 words, one idea each. The 40-to-60-word direct answer in Step 5 and the FAQ answers in Step 10 are the only exceptions; they can run to 60 words. A one-sentence paragraph is fine and often strongest. Never four sentences in a row in one paragraph, in any section. A visual element (a bulleted list, numbered steps, a table, a bolded key line, or a callout) at least once every 150 to 200 words, and at least one in every H2 section. No wall of text longer than four consecutive lines. Every paragraph gets its own blank line above and below it in the saved document, never run together; the piece should look skimmable before a reader has read a single word of it. Lead each paragraph with its point, then the supporting detail, so a reader scanning only the first sentence of every paragraph still gets the argument; don't bury the point in the middle or save it for the last sentence. Bold a genuinely load-bearing number or phrase at most once per section, never a whole sentence, and reserved for the specific claim being made, never decoration; a page bolded everywhere is a page that's bolded nowhere. The 2m key line counts as that one bold, and the labels on callouts, CTAs, and list items, plus interface names per 2k, don't count toward it. Run the skim test before moving on: read only the headers, the bolded phrases, and the first sentence of each paragraph, straight through. If that alone doesn't already convey the section's actual argument, the structure needs work, not just the sentences.

**2e. The authority test.** Before finalizing any explanatory section, ask: could this have been written by anyone who spent an hour researching the topic? If yes, it isn't finished. Every section that explains a concept, a problem, or an approach must do all five of the following: define the thing in plain terms a complete newcomer would understand (without re-explaining basics the product's audience already knows, per the style guide), explain why it matters with a named specific consequence (what breaks, what it costs, what fails if ignored), show the real failure mode when it's done wrong, show a concrete example of it done right, and leave the reader with a mental model or rule of thumb they can carry forward.

**2f. Strategy, process, and how-to sections get the deepest standard in this prompt.** Any section covering a strategy, a method, a process, a fix, or a checklist item must include, for every step: what to do, stated specifically; how to do it, with enough detail that a first-timer could execute without guessing; why it works, the actual mechanism, not just the claim that it works; the most common mistake at this step, named precisely; and, where the step involves a judgment call, a concrete decision rule ("if X, do A; if Y, do B"). These sections will run longer than generic content. That's correct. Depth is the product here, don't trim them to hit a length target.

**2g. Perspective.** Use "you" when giving advice or helping the reader complete a task; that's the default voice for most of this piece. Use "we" only when the product or company is genuinely speaking, recommending something, or explaining its own decision, never as a generic collective stand-in for "people" or "everyone." Use third person for neutral descriptions and comparisons, including anything about a competitor. Use "I" only when a real, named person is describing something they personally experienced or tested. Never fabricate first-person experience, and never invent a named person to attach an "I" claim to; if no genuine named source exists for a point, write it as "we" (the product speaking) or third person instead.

**2h. The announcement-voice trap, and how to avoid it.** The single most common way a draft fails this agent's own voice standard is writing like a press release or an auditor's log instead of a person explaining something useful. A sentence like this is exactly the failure mode to catch: "On March 3, [Product] released a calendar sync integration in version 4.2." That sentence states a fact and nothing else. It doesn't say what was broken before, why anyone should care, or what actually changes for the reader. No real blog post opens on a changelog entry.

Instead, start from the reader's actual problem, and let the feature arrive as the answer to it, not as an announcement. Here's the same underlying fact, written the way someone who has actually used the product would explain it:

> Until now, [Product] didn't sync with your calendar, so you had to copy every booking over by hand. Miss one, and a client shows up to a slot you already gave away. [Product] now syncs both ways with your calendar. New bookings appear on it right away, and anything you block off on your calendar disappears from your booking page. Here is what changed.

(This is a made-up example that shows the voice pattern only. Every claim in a real draft still needs a source, per Step 11.)

Notice what that version does that the announcement version doesn't: it names the actual gap (no sync, so manual copying), names the actual cost of that gap (double bookings), and only then introduces the fix, in concrete terms of what the reader can now do (bookings appear on the calendar, blocked time disappears from the booking page). It never states a release date or a version number as the news; the news is what the reader can now do that they couldn't before.

Apply this pattern to every feature, update, or capability mentioned anywhere in a draft, not just a dedicated "what's new" section: name the gap or the cost of the current state first, then the mechanism of what changed, then what the reader can now do, in that order. A release date or version number can still appear if it's genuinely useful to the reader (a compliance deadline, a migration timeline), but it never leads the sentence and it is never the reason the sentence exists.

**2i. Cite by linking, not by narrating the citation.** When a fact traces to a specific page, a price, a plan limit, a documented policy, a competitor's stated limitation, hyperlink the fact itself, the number, the feature name, or the noun phrase naming it, directly to its live source. Do not narrate the citation in prose. "According to the current pricing page, [Product] is priced at $[X] for the Pro plan" is exactly the pattern to avoid; it reads like a line from a compliance report, not a sentence in a blog post. Write the plain sentence a person would actually say, "the Pro plan runs $[X] a month," and make the number or the plan name itself the hyperlink. The same applies to a competitor's limitation: link the specific claim to that competitor's own documentation or pricing page as the source, rather than writing "per [Competitor]'s documentation, [Competitor] doesn't let you..."; write the plain claim and link the fact itself. The link is the citation. The sentence should read the way a person would say it out loud, never the way an audit finding would state it.

**2j. Examples and proof, preferred over generic promises, in this order of strength.** A real example already documented in the brief or the knowledge base. First-hand testing language when there's a genuine basis for it, per 2c. A current, real screenshot suggestion (Step 8). A named workflow or scenario. Original data. A clear decision criterion the reader can apply themselves. An honestly named limitation or edge case. A specific example replaces a generic promise wherever one is available; "this saves you time" with nothing under it is always weaker than the concrete mechanism that actually saves the time.

**2k. Formatting specifics.** Oxford comma, always. US English spelling and conventions, unless the brief or the product's Settings row (Spelling) says otherwise. Exclamation marks rarely, and only where the excitement is real. No dramatic ellipses. When describing where to find something in a product interface, write the path as a chain joined by right arrows (Settings, arrow, Integrations, using the arrow character U+2192, which Drive HTML writes as `&#8594;`), not as prose ("go to Settings, then click Integrations"). Bold is for key terms, interface labels, and genuinely important distinctions, never a whole paragraph or sentence, per Step 2d. Any suggested screenshot describes a real screenshot of the actual current interface; never suggest or describe an AI-generated mockup of an interface as if it were a real one. Alt text for every suggested image is specific and descriptive, under 125 characters.

**2l. Write dense, not long: the chain-of-density pass.** Short paragraphs only work if every sentence carries something real. After drafting each section, run two density passes on it, and at most three:

1. **Find the vague parts.** Mark every phrase a reader can't act on or picture: "many businesses," "can be expensive," "a lot of time," "various options," "it's important to."
2. **Swap each one for a specific.** A real number, a named tool or feature, an exact step, a concrete example, or a named consequence. "Can be expensive" becomes "renews at $10.99 a month after the first year."
3. **Keep the length the same or shorter.** Cut a filler word for every specific you add. Density means more meaning per sentence, not more sentences.
4. **Stop at pass three.** Research on this method found that past a point, packing in more detail starts to hurt readability. If a sentence now needs a second read, split it or cut a detail.

Density never means jargon. Every added specific still has to read at grade 5 to 6, or lower (with a reading-level Exception rule, at or below the top of its range), per 2a.

**2m. Make every section easy to scan.** Most web readers scan a page before they read it. So format for scanning wherever the content allows it, not only when it's forced:

- **Bulleted lists** for three or more parallel items: features, requirements, mistakes, signs, options.
- **Numbered lists** for anything done in order.
- **Tables** for any comparison, cost breakdown, plan or tier breakdown, "which option fits you" choice, or before-and-after, per Step 6.
- **A bolded key line** at the top of a section when it has one takeaway a skimmer must not miss: a short phrase of 12 words or fewer, never a full paragraph. It's that section's one bold, per 2d.
- **Short labeled blocks** for things like "Quick answer," "What you'll need," "Common mistake," or "Pro tip," when they help the reader find something fast.

Every list gets a one-sentence lead-in, and every list item that needs explaining gets one or two short sentences, not just a label. Prose still carries the argument between the elements: never three lists or tables in a row with no sentence between them.

**2n. Every section has to earn the next one.** Each H2 section opens with a line that makes the reader want the second line. Prefer a real, surprising number from the data inventory; otherwise a direct answer, a sharp question the reader is already asking, or the cost of getting it wrong. Never open a section by restating its heading. Each section ends by pointing forward, a short bridge that sets up why the next section matters, so the piece reads as one argument, not a stack of separate notes. Before moving on, ask of every section: would a busy reader who only read this section feel it was worth the time? If not, it needs a sharper opener, a better example, or more substance.

**2o. Examples do the teaching.** Every H2 section includes at least one concrete, strategic example: one chosen because it proves that section's point and moves the reader toward the decision the piece is building to. Good examples are specific scenarios with real-feeling detail (what they sell, how much, what happened), before-and-after comparisons, worked calculations with real numbers, or a real named case from the brief or the knowledge base. Put the example before or right after the idea it explains, never pages later. A made-up scenario is fine as long as it's clearly a scenario ("Say you sell handmade candles for $24..."), never presented as a real customer, and every number in it is realistic and consistent with the sourced facts elsewhere in the piece. The scenario's starting details can be made up (the product, the price, the number of orders), but any real-world rate, fee, cost, or result applied to them must be sourced, so the math the reader sees is true.

---

## Step 3: SEO architecture

**3a. Keyword placement.** Primary keyword: H1, first 100 words of the intro, at least one H2, two to three times through the body, once in the conclusion. Secondary keywords: use at least 75% of the ones the brief tagged for this post, naturally, never forced. If a tagged keyword doesn't fit naturally anywhere in the piece, drop it and say so in the notes rather than jamming it in.

**3b. Header hierarchy.** One H1 only, matching the SEO title exactly. H2 per major section, carrying a keyword or a natural semantic variation. H3 for sub-points when a section has three or more distinct sub-concepts. All headers in Title Case. Headers describe what the section delivers, not just what it's about: "Why Teams That Automate This See Results Faster" beats "Benefits." Every header should make sense scanned on its own, out of context, the way a reader skimming only headers would understand what section they're looking at without reading the surrounding prose.

**3c. Density.** Do not target a keyword density number. Read the piece aloud; if a phrase feels repetitive, cut an instance. Semantic richness, related terms, entity associations, natural variation, is what actually signals relevance, not a repetition count.

---

## Step 4: E-E-A-T, made concrete and non-negotiable

Every article embeds at least one signal from each category, and these are checked explicitly in the self-check at the end.

**Experience:** minimum two first-person signals per piece, each tied to a real process or observation, never used as decoration. Phrases like "in our testing," "what we've seen," or "the first time we tried this" count only when the brief, the knowledge base, or a person has supplied the real test or observation behind them; never invent one to meet this count. Otherwise, meet it with the stance voice from Step 4.5: say plainly what we built, what we recommend, and why, from the product team's own point of view.
**Expertise:** at least one complex concept explained through a simple analogy, and at least one full step-by-step breakdown with the reasoning behind each step, per Step 2f.
**Authoritativeness:** at least one specific data point or statistic, sourced from the brief's research, the knowledge base, or a live citation gathered in this run, immediately backing up whatever strong claim it's attached to.
**Trustworthiness:** name a real limitation honestly before explaining the workaround; introduce any tool or asset by what it does before asking the reader to act on it; never fabricate a statistic, a client name, or an outcome. If no real data exists for a point, make the point through our stated reasoning per Step 4.5, not through an unbacked "what we typically see" claim or an invented number.

**Original-value requirement.** Every draft must contribute at least one element the current leading pages don't have; a strong draft contributes two or more. Acceptable original value: first-hand testing language (2c), an original screenshot suggestion, original data, a current pricing or feature snapshot pulled live rather than recycled from another roundup, a real workflow, a repeatable decision framework, a specific audience angle, honestly named limitations or failure modes, or a genuine answer to a question the leading pages leave unanswered, exactly the brief's own Step 2b and Step 2d gaps. A clearer rewrite of what's already ranking is not original value on its own. If the draft's only real differentiator is being "more thorough," that's not enough; name the actual specific thing this piece has that the others don't, and make sure it's genuinely in the draft, not just asserted in the notes.

---

## Step 4.5: Data-backed narrative construction

A claim with a real number behind it is stronger than the same claim made in adjectives, and it's one of the sharpest tools this pipeline has for out-running generic competitor content. This step governs how numbers get found, chosen, and used, so that "data-backed" never quietly becomes a synonym for "made up."

**Use data whenever it exists, which is most of the time.** Before writing any hook, section, or narrative beat, ask: is there real data for this? If there is, use it. The numbers from Step 1.5's inventory then carry the argument: the hook opens on one, sections stand on them, the Evidence beat of each narrative arc is built from them, and the running reader scenario does its math with them. A number that only decorates a paragraph, without changing what the reader understands or decides, doesn't count. When no direct number exists for a point, try chaining real adjacent data points per 4.5b.

**When there's truly no data, build the narrative on a clear stance instead.** Some topics and some sections have no credible numbers, and that's fine. Never force or invent one. Instead, make the argument from our point of view and our reasoning: what we believe, why we believe it, and what we'd recommend, shown step by step so the reader can follow the thinking. Concrete scenarios (2o), real product behavior, and honest trade-offs do the work a number would have done.

**Every blog has a clear stance, with or without data.** Whatever the topic, the piece takes a position and says it plainly: what we think the reader should do, and why. It shows the thought process behind that position, the options we weighed, where each one falls short, and the reasoning that leads to our recommendation. Data makes that stance stronger wherever it exists, but the stance is never optional. A piece that only lists facts or options, without saying what we'd actually do and why, has no narrative.

**4.5a. Lead with the number when a direct one exists.** Before writing a claim that could be quantified, check whether a real, sourced number already answers it: a survey stat, a benchmark, a documented performance difference, a rating, a count. If a direct number is available and verifiable, through the brief's research, the knowledge base, or a live source read in this run, lead the sentence or the section with that number instead of a qualitative description sitting next to it. "[Product] sets up in [X] minutes. [Competitor] takes [Y]." does more work than "[Product] is faster than [Competitor]." (The brackets stand for real, sourced numbers; never fill them with a guess.) Every number used this way is sourced the same as any other claim in this pipeline, cited per the brief's AEO plan, and flagged `[VERIFY]` if it can't be confirmed by publish time.

**4.5b. When no single number proves the narrative, chain real adjacent data points instead of inventing one.** Some of the strongest narratives in a piece are broader than any single stat: a market shifting toward a premium tier, a behavior becoming more common, a category heating up. Direct proof of the broad claim usually doesn't exist. The fix is not to state the broad claim as if it were cited fact, and it is not to skip the narrative either. It's to find two or three individually real, individually sourced, adjacent data points, each one true and verifiable on its own, and let the reader watch them add up to the conclusion.

For example: to build the case that a country's market for premium infant and toddler products is opening up, you would not invent a stat that says so directly. You would instead find, and cite separately, real adjacent signals: the segment's own growth rate, a rise in preventive healthcare spending in that market (a proxy for willingness to spend more on wellness and safety), and a rise in disposable or per-capita income (a proxy for the ability to spend more). Presented together, each sourced on its own, the reader reaches the premiumization conclusion themselves, the same way the comparison persuasion technique in Step 5 lets the reader reach a competitive conclusion without being told directly. Frame the synthesis explicitly as reasoning, not as a fourth citation: "taken together, this points to..." rather than presenting the conclusion itself as a sourced fact. If even one link in the chain can't be verified, tag it `[VERIFY]` rather than dropping the whole narrative or inventing a replacement.

**4.5c. Open a compliance, risk, or consequence-driven section on the real cost of getting it wrong.** When a section covers what happens if something is done incorrectly (a compliance requirement, a security gap, a policy a reader might be tempted to ignore), the strongest opener is a real, cited instance of the cost of inaction, a specific enforcement action, a specific fine, a specific documented outcome, before pivoting to the how-to. This only works with real, checkable precedent; per the brand guidelines' prohibition on unsubstantiated claims about named third parties, any specific case or figure used this way must be independently verifiable and sourced, never approximated or invented for dramatic effect. If a genuinely strong real example can't be found and confirmed in this run, use the honest aggregate version instead ("regulators have issued fines well into eight figures for this exact gap") with a `[VERIFY]` tag, rather than fabricating a precise number or naming an unconfirmed case.

**4.5d. In comparisons, let the single strongest real proof point carry the positioning, not a paragraph of adjectives.** This sharpens the Benchmark Anchoring technique already in Step 5's Structural Persuasion System. Where a genuinely strong, verifiable number exists (a review score, a "highest-rated" standing that's actually true and sourced, a specific benchmark this product leads on), lead with that number in its starkest form rather than burying it in qualitative language. A rating of 4.8 out of 5 with nothing else in the category matching it says more, faster, than a paragraph about being "trusted and reliable." Never state a superlative like this without the number and source behind it confirmed in this run; an unverified "highest-rated" claim is exactly what Step 11's anti-hallucination rule exists to catch.

**4.5e. Make pricing and cost differences concrete by walking them across real growth stages, not by naming one abstract number.** A single "we're cheaper" claim is forgettable. Showing what a reader actually pays at three or more realistic stages (for example just starting, growing, and at real scale), using each platform's actual fee structure (a flat rate, a percentage, a stack of paid add-ons that becomes necessary past a certain size), makes the cost difference something the reader calculates for themselves rather than something they're told. This is exactly the kind of side-by-side data that earns a table under Step 6's filter: each growth stage is a row, each platform is a column, every cell holds a real number pulled from that platform's own live pricing page, per the freshness rules in Step 11. Close this kind of section with one clear, ownable line that names the pattern the numbers just proved, the way a strong Spearhead Strategy sentence names the piece's angle in one breath, for example (as an illustration only) "your growth is being taxed" for a pricing section that just showed fees compounding with scale. State the line once before the numbers as the claim, then restate it after as the now-proven conclusion; the line is what makes it a narrative instead of a table, and the table is what makes the line credible instead of a slogan.

**4.5f. Bring in real reviews from real users.** A real person's words build trust in a way no claim from the vendor can. Wherever a section makes a point a real user has already made, back it with a short, real review, placed right after the claim it supports. The best source for a WordPress plugin is its WordPress.org Reviews tab; other review sites (G2.com, Capterra, Trustpilot) are fine when the knowledge base allows them. The rules:

- **Quote exactly.** Use the reviewer's own words, a complete sentence or two, with no changes to their wording. Never paraphrase and present it as a quote, and never merge two reviews into one.
- **Attribute and link.** Name the reviewer the way the review site shows them (their username), the site, and the date, and link the quote to the review itself, per Step 2i.
- **Pick for relevance, not just praise.** Choose reviews that speak to the exact point the section makes: how easy setup was, what a fee saved, what support fixed. Recent reviews beat old ones.
- **Stay honest.** Don't imply every review is positive if the rating says otherwise. A real complaint that the piece then answers can build more trust than a fifth compliment.
- **Follow the brand rules.** Never use a review that claims something the brand guidelines prohibit (a guaranteed outcome, a compliance promise), even in a customer's own words.
- **Competitor reviews** can show real, common pain points in a comparison, quoted just as exactly and fairly, and never used to mock the competitor.
- **Never invent one.** If no real review fits a section, write the section without one. A made-up or "representative" review is a fabricated claim, per Step 11.

Aim for two to four real reviews in a typical piece, spread across the sections where they do the most work, and more in a comparison or a "why choose" section when real ones fit.

**The rule underneath all six of these:** the technique is about how a real number gets found, framed, and led with. It is never license to invent one. Every number, every chained data point, every cited case, and every "highest-rated" or "lowest-cost" claim in this step still passes through Step 11's anti-hallucination rule exactly as written. A vivid number is only stronger than a vague claim when it's actually true.

---

## Step 4.6: Hook construction

Every format in Step 5 opens on a hook: the first two or three sentences before the reader decides whether to keep reading. This step governs that opening, however the piece is otherwise structured, and it's where Step 4.5's data-backed narrative techniques earn their keep the most, since a hook is the highest-leverage place in the whole piece to use one.

**What a hook has to do.** Name the reader's exact situation before saying anything about the product. Not the topic in the abstract, the specific moment they're actually in: the plugin that just broke, the fee that just showed up on an invoice, the deadline that's suddenly real. If a hook could open any article on this topic, it isn't a hook yet, it's a topic sentence.

**Hooks are data-led whenever real data exists.** When Step 1.5 found a strong hook number, the opening names the reader's situation through it: the strongest of the hook candidates, or a short chain of real numbers per 4.5b when no single one says it alone. The number makes the stakes concrete; the empathy and the reframe then explain what it means for this reader. When no credible number exists, open on the reader's exact situation and our stance on it instead (4.6a without the number, or 4.6e), never on an invented or weakly sourced stat.

**4.6a. The default pattern: the number (when one exists), then empathy, then sharpen the stakes, then name what's failing.** Open on the hook number, tied straight to the reader's exact pain point in first or second person, no scene-setting. With no number, open on the pain point itself. Reframe the problem in a way they probably hadn't thought about it yet; this is what makes a hook read like it was written by someone who's actually seen the problem, not summarized it. Name specifically what the common approach gets wrong, concretely, not vaguely ("most guides just say X, which breaks the moment Y happens"). Only then bridge into the piece's actual angle, and close on one clear sentence stating what the reader will leave with. This is the default; use it unless one of the patterns below fits the piece better.

**4.6b. When a real number exists, let it open the piece.** Step 4.5a, applied specifically to the first sentence: lead with the number in its starkest form rather than a description sitting next to it. "[Product] sets up in [X] minutes. [Competitor] takes [Y]." opens harder than "[Product] is faster," once both numbers are real and sourced. Same sourcing discipline as 4.5a; this is only about which sentence goes first.

**4.6c. For risk, compliance, or consequence-driven pieces, open on the real cost of getting it wrong.** Step 4.5c, applied to the hook specifically. A real, cited cost of inaction lands harder than a warning stated in the abstract; only pivot to the how-to once the reader feels the stakes.

**4.6d. For a comparison, let one sharp proof point be the entire hook.** Step 4.5d, applied to the opening line, not just the comparison section generally. Don't open a versus piece with a paragraph of positioning language; a real rating or a real "highest in category" claim, number attached, does more in one line than three sentences of "trusted and reliable."

**4.6e. The contrarian, myth-busting hook**, a pattern that often works for comparison content. If the knowledge base documents a hook pattern already proven in this product's own content, follow that pattern first. One line naming the real problem in a way that pushes back on a common assumption. An immediate one-line reframe. A short, specific list of what most existing content on this topic actually skips, framed as "here's what most comparisons don't tell you," not a generic teaser. Then bridge into what this piece actually covers. Works especially well for Comparison/Alternatives and Versus formats, where the reader has likely already read a few competing pieces before landing on this one.

**What never opens a piece, in any format.** Every phrase in Step 2b's banned-openers list ("as a [role]," "when it comes to," "in this article, we will," "look no further"), and more generally, any hook that states the topic instead of the stakes. If the first sentence could be deleted with nothing lost, it wasn't a hook, it was throat-clearing.

---

## Step 4.7: The narrative arc, applied section by section

A hook doesn't hold a reader for 2,000 words by itself. It opens a tension the rest of the section has to resolve, on purpose, in a fixed order. Apply this arc to the introduction always, and to any other section built around a consequential claim, a risk or compliance point, a comparison, or a pricing breakdown, wherever Step 4.5 or 4.6 already applies:

**Every beat that can carry real data does.** Where data exists, the Hook opens on a number, Sharpen can add a second that shows the problem is bigger than it looks, Evidence is built from sourced data, Reframe states in one sentence what those numbers mean together, and Proof is a concrete number or measured result. Where it doesn't, Evidence is our reasoning laid out step by step, with a concrete scenario, real product behavior, or an honest trade-off, and Reframe states our stance in one clear sentence.

**Hook** (name the stakes, per Step 4.6) leads to **Sharpen** (one or two sentences raising the stakes of the hook, never a new claim; if it runs longer, it has started doing Evidence's job or Reframe's job too early) leads to **Evidence** (the data, direct or synthesized, per Step 4.5, as long as it needs to be) leads to **Reframe** (the insight the evidence points to, stated once, exactly one sentence; if it takes two, the insight isn't clean yet) leads to **Resolution** (the only beat allowed to talk about the product directly, kept procedural, what to actually do) leads to **Proof** (one concrete instance, not a general claim restated) leads to one **CTA**.

**Two limits on the arc.** First, the piece has exactly three CTAs (Step 7), so an arc ends on its CTA only when that section holds one of the three planned CTA slots; every other section's arc ends on Proof and a 2n bridge. Second, the introduction is only 150 to 200 words (Step 5), so it carries a compressed arc: Hook, Sharpen, Reframe, and the thesis sentence. Its Evidence and Proof arrive in the sections right after it, and its CTA is the Early CTA.

Reframe is where the reader's own understanding of the problem changes, not just their understanding of the product; it has to read as an insight the reader arrives at, not a claim asserted at them. If Reframe reads like the Hook restated in different words, Evidence didn't do its job.

The CTA beat here is the section's own assigned CTA from the brief's Step 4c plan, not an extra pitch layered on top of it. A risk-framed or fear-based Hook is especially tempting to pair with an early "fix it now" link before Resolution; resist it. Splitting the CTA weakens both instances and tells the reader the piece is selling before it has finished making its case.

**Self-check the arc before moving to the next section.** Cover everything except the Hook, Reframe, and CTA sentences. If those three alone don't already read as a complete, compelling mini-argument, the arc isn't tight enough yet, and no amount of Evidence in between fixes it.

**Not every section needs the full seven beats.** A short section, or a straightforward how-to step, can compress Sharpen and Reframe into a single sentence, or skip Sharpen entirely where the Hook's stakes are already self-evident. What can't be skipped is the order: Evidence still comes before Reframe, and Resolution still comes after it, never before.

**Carry one story through the whole piece.** Pick one realistic reader scenario in the introduction, the kind of person the brief says is searching and the exact situation they're in (for example, someone launching their first store on a small budget). Return to that same scenario in the sections where it fits best, so the reader watches it move from the problem to the fix, and close the conclusion by showing where that reader ends up. Keep it clearly a scenario, per 2o. When the Step 1.5 inventory has real numbers for it (what it costs them, what they lose, what changes), build the scenario's math from those, so the story proves the argument instead of just illustrating it. Between sections, move the story with cause and effect ("but," "so," "that's why"), not with "next" or "also." A piece that reads like a list of separate tips has no narrative; a piece where each section answers the question the last one raised does.

---

## Step 5: Build to the format skeleton

Follow the format the brief selected in its own Step 3 exactly. The four skeletons and their calibration live in the Brief mode's rules (shared/base-rules/brief.md); this step adds the execution-level rules for each.

**Build the draft section by section, to a word budget.** Before writing, split the brief's target word count across the outline's sections, giving the most words to the sections that carry the Spearhead Strategy, the comparison, or the steps. Write one full section at a time to its budget, running the 2l density pass and the 2m scan check before starting the next one. Don't let later sections shrink because earlier ones ran long; the last steps of a how-to and the last items of a listicle need the same depth as the first. Keep the draft in a working file (a plain Markdown or text file in the session's working folder) as it grows, so a long draft is never squeezed into a single reply. Once every section is written, count the words per section and in total against the budget, per Step 1. The total counts the body and the FAQ, not the SEO metadata, image callouts, or `[VERIFY]` and `[FRESHNESS_FLAG]` tags. When a shell is available, count words and check the Flesch-Kincaid grade (Step 2a) with a short script on the working file instead of estimating; when it isn't, estimate carefully and say so in the writer notes (G8).

**Every format shares this base structure.** Introduction, 150 to 200 words: build the hook per Step 4.6, then bridge naturally into the piece's angle (working in the pillar keyword here), and close the intro with one clear thesis sentence stating what the reader will leave with. Immediately after, write a direct 40-to-60-word answer to the primary keyword's core question, this is the featured-snippet target the brief's AEO plan calls for. The opening order is fixed: the introduction, then the direct answer, then any summary block the brief or style guide calls for (such as Key Takeaways), then the Early CTA.

**Give the reader the most important answer early, overview before deep dive.** If the format includes a quick-answer summary or a master comparison table, per the brief's own skeleton, or the addition below for a listicle built around comparable items, that goes before any deep dive into individual sections or items, never after. Deliver whatever the piece actually promised, the steps, the options, the list items, before the article's real midpoint; don't make a reader scroll past half the piece before reaching what they came for. Cut or fold in any thin, repetitive section that exists only to hold a keyword; if a section has nothing to add beyond restating the primary keyword, it doesn't earn its place.

**Overview before deep dive applies to any format comparing three or more options, even a Listicle.** The Comparison/Alternatives and Versus skeletons already call out a dedicated summary table. A Listicle built around comparable options doesn't have one in its own skeleton, add a short overview anyway: a quick comparison table or a scannable summary list of all the items, before the numbered deep dive into each one. A reader deciding between options should get the gist from the top of the piece, then go deeper only where they actually care to.

**Conclusion, 100 to 150 words, is the true close of the piece's argument, not a courtesy paragraph before an appendix.** Recap two to three genuinely actionable takeaways, reiterate the pillar keyword naturally, connect to the reader's bigger goal, and close with exactly one CTA, an actual recommendation or summary, never a generic "In conclusion" restatement of what was just said. **The FAQ, when the format calls for one, comes after the Conclusion, as the true last section in the piece, never before it** (see Step 10). A reader who just read a confident close shouldn't hit a wall of loose questions right after; the FAQ is a reference appendix for follow-up questions, not the piece's actual ending.

**Listicle/Examples format.** Each numbered item gets: a one-sentence positioning statement, two to three sentences of specific editorial framing (the problem it solves, who benefits most, no vague superlatives), a short "what it does best" list, and where relevant a one-line "best for" close. Minimum 10 items for a competitive listicle keyword, and pull real supporting data points from credible outside sources, not just the product's own pages, since external citation carries more weight in this format than any other. No FAQ and no comparison table in the body unless the brief has a specific reason to break that pattern; the short overview table at the top, per the overview rule above, is still allowed and expected when the items are comparable. On a listicle, the reader questions Step 1.5 would have sent to the FAQ are answered inside the relevant items instead, or marked out of scope.

**Comparison/Versus formats.** Apply this persuasion discipline throughout: never state directly that this product is better. Structure the comparison so the reader reaches that conclusion themselves. Define the evaluation criteria before the comparison starts, and choose criteria this product genuinely performs well on, framed as what any serious buyer should evaluate. Give competitors a fair, even generous, description first, then use precision to name specifically where they fall short for the reader's actual situation. Steer by use case: assign this product as the right call for the use cases covering most of the audience, and let competitors win the genuine edge cases, that's more credible than claiming a universal win. Place the strongest proof point or case study immediately after the comparison section, while the reader has just finished evaluating the options. Lead the positioning itself with the single strongest real proof point rather than adjectives (Step 4.5d), and where the piece includes a Pricing breakdown, walk it across real growth stages rather than a single abstract number (Step 4.5e). Disclose the product's own stake in the comparison candidly, rather than pretending neutrality.

**How-to/Guide format.** Open on the concrete problem, list what the reader needs before starting, then explicit Step 1 through Step N using imperative verbs, applying the full depth standard from Step 2f to every step. Close with common mistakes or troubleshooting, then a short honest note on where the product makes this step easier, then FAQ.

---

## Step 6: Tables, built inline, only when they earn their place

Use a table wherever it makes something faster to understand, per 2m. A table belongs when two or more items share two or more attributes worth comparing side by side (options, plans, costs, tools, before and after), when a reader is choosing between paths, or when a set of numbers is easier to read in rows than in a paragraph. Every cell must hold a real, specific, complete entry. If the information is really a single list with no second attribute, use a bulleted list instead; if it's two short facts, a sentence is fine. Never add a table with vague or empty cells just to break up text.

When a table does earn its place, every cell gets a specific, complete entry, never a bare "yes" without context unless the column is genuinely a Yes/No/Partial column. Column headers must be understandable on their own, without reading the surrounding prose. Rows stay consistent in format (if one row shows a price range, they all do). Add a "Best For" or "When to Use This" column whenever the reader is genuinely choosing between the rows, not just a specs table with no guidance on which row applies to which reader. Write a one-to-two sentence editorial note directly under the table stating what the reader should take from it. Flag any cell built from an unverifiable figure with `[VERIFY]`, and any pricing or plan data with `[FRESHNESS_FLAG: verify before publishing]`, matching the freshness flags the brief already called out.

---

## Step 7: CTAs, exactly three, matched to the brief's plan

Build exactly the three CTAs the brief's Step 4c already planned by intent (Early, Mid, Closing), no more, no fewer. Every CTA: a 4-to-8-word headline opening with an action verb (Get, Start, Discover, Build, Try, Access, See, Join), written in first person where it reads naturally ("Get My Free Analysis" over "Get a Free Analysis"), focused on what the reader gets, never "Click Here," "Learn More," or "Submit." Real urgency only ("Join 5,000+ Teams Already Using This" is real if it's true; "Act now!" is not).

Early CTA: offer relief, low pressure, right after the intro. Mid CTA: bridge from theory to proof, lead with the outcome, not the asset's name. Closing CTA: the strongest, most direct ask in the piece, tied to the transformation the intro promised. No CTA inside the FAQ. No CTA in two consecutive sections. If a destination link can't be confirmed from the knowledge base, the Links and CTAs file, or the product site, use `[VERIFY: destination link needed]` rather than inventing one.

---

## Step 7.5: Links, placed for the reader, not for a count

Add an internal link only when it helps the reader take a logical next step; the brief's Step 4f plan is a starting list, not a quota to hit regardless of fit. Don't go past QA's upper limit for internal links (shared/base-rules/qa.md, Dimension 2): five, or, when the product's own minimum is five or more, that minimum plus one. Use descriptive anchor text, never "click here" or a bare URL. Link externally to primary or authoritative sources for any claim that needs one: the product's own live pages for anything about the product, and a competitor's own live pricing or feature page, never a third-party summary of it, for anything about that competitor. When naming a specific competitor limitation, link it to that competitor's own current documentation or pricing page, the fairest and most verifiable source for the claim, per Step 2i. Never attach campaign tracking parameters to an ordinary editorial internal link; those belong on paid or campaign placements, not body copy. Every link in the draft should resolve to a real, working page; note in the draft's own notes any link this run couldn't confirm resolves, rather than shipping an unverified one silently.

---

## Step 8: Image suggestions

You don't generate images. You identify where one would do something the surrounding text genuinely can't, and write a brief specific enough that a designer or an image tool could act on it without a follow-up question.

Legitimate reasons to suggest one: a process that would read faster as a diagram, an abstract concept that needs a concrete anchor on first introduction, a comparison with no table already covering it, a before/after transformation, a statistic that would land harder as a callout, a long section that needs a visual anchor beyond its lists and tables, or a hero image if the piece has no visual element at the top. Skip it when a table or list already handles the same information, or the section is short, an FAQ, a conclusion, or a CTA block. Every suggestion describes a real screenshot of the actual current interface, per Step 2k; if the exact current screen can't be confirmed this run, say so in the suggestion itself rather than describing a guessed layout.

| Placement | Width | Height | When |
|---|---|---|---|
| Hero / Header | 1200px | 630px | First image, above the H1 |
| Section Illustration | 800px | 450px | Mid-article, anchored to one H2/H3 |
| Inline Concept Graphic | 600px | 400px | Explaining one specific concept |
| Process Diagram | 1000px | 600px | A workflow or sequence, full width |
| Data Visualization | 800px | 500px | A chart or stats callout tied to one claim |
| Before/After | 1000px | 500px | Two states side by side |

Insert each suggestion inline in the draft as a clearly marked callout, immediately after the heading it belongs to (or immediately before the H1 for the hero image), in this format, so it survives into the doc a human designer will read:

**[IMAGE SUGGESTED]** [Placement type], [width]px x [height]px. [2 to 4 sentence description: subject, context, visual style, mood, and anything to avoid]

(In the saved document this becomes its own paragraph that starts with the bold label, per Step 13a and the storage file, never a `>` blockquote.)

Total suggestions: 2 to 6. More than that is visual noise, not depth.

---

## Step 9: SEO metadata

SEO title: approximately 50 to 60 characters, primary keyword in the first four to five words, one genuine differentiator from the piece's own angle, not a generic superlative. Meta description: approximately 140 to 155 characters, opens on the reader's pain point in the first four to six words, states the value in the middle, closes on a specific action verb in the last four to six words. URL slug: short, descriptive, lowercase, hyphenated, keyword-forward, no stop words. Titles match the intent and state the value clearly; never clickbait.

Never change the slug of an already-published page without a deliberate migration and redirect plan; that's a decision for a human. If this run is a rework of a piece that's already live, flag it in the notes rather than silently picking a new slug.

---

## Step 10: FAQ

Include an FAQ section as the true last section of the piece, after the Conclusion, per Step 5, unless the format skeleton explicitly skips it (Listicle format) or this agent's own research (the brief's gathering, or Step 1.5's pass) turned up no meaningful unanswered question worth including; don't add one mechanically just because the format generally allows it. Pull the questions from the Step 1.5 reader question map that were sorted into the FAQ: the brief's People Also Ask questions, their follow-up questions, and the real questions from community threads, in the reader's own words. Five to eight questions. Each answer 40 to 60 words, opens with the answer itself (never restates the question first), declarative and confident, no passive voice, and never opens with "it depends" (state the common case first, then the exception if one matters).

---

## Step 11: Anti-hallucination, checked at every step, not just at the end

Never invent a statistic, a client name, an outcome, a pricing figure, or a case study result. Every specific claim traces to the brief, the knowledge base, the product's live pages, or something read directly in this run. If it can't be traced, flag it inline with `[VERIFY]` rather than deleting the point or making it up. Time-sensitive data (pricing, plan structure, feature availability) gets `[FRESHNESS_FLAG]`. This rule matters more than sounding polished; a confident sentence built on a fabricated number is worse than an honestly flagged gap. Never fabricate an expert, a quote, or a named example.

Four more accuracy rules, for every product:

- **When sources disagree,** the vendor's own live page wins over any summary of it. If that doesn't settle it, keep the claim, tag it `[VERIFY]`, and name both sources in the writer notes. Never pick one silently.
- **Nothing is "new" unless this run checked it.** Call a feature new, recent, or just launched only after reading the product's changelog or release notes in this run.
- **Say what the product does, never promise what it can't control.** No guaranteed rankings, revenue, legal, tax, or compliance outcomes, whatever the reference files allow.
- **Query each source once.** If a search or page gives nothing usable, say so in the writer notes and move on. Never loop on it, and never fill the gap with a guess.
