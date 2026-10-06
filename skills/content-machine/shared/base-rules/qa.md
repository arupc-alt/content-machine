# Base QA rules

Every product gets these rules, always. QA audits every draft against them (modes/qa.md, Step 2), and the Blog Writer reads them so it knows the bar its draft must clear (modes/blog-writer.md). They hold the 23 base dimensions, the severities, the blocker list, the scoring, and the bar for every check.

**Names used in these rules.**

- "The Blog Writer's Step N" means that step of the base writing rules (shared/base-rules/writing.md). Steps 1, 1.5, 12, 13, and 14 are in modes/blog-writer.md.
- "The brief's Step N" means that step of the content brief, as the Brief mode builds it (modes/brief.md and shared/base-rules/brief.md).
- "The reference files" means the product's Reference rows, loaded at run start (shared/run-start.md, Loading the rules): Type Brand guide, Style guide, Quality checks, and Product knowledge, plus Links and CTAs, Competitors, and Best past posts when present. "The knowledge base" means the Product knowledge rows. "The brand guidelines" means the Brand guide rows. "The style guide" means the Style guide rows. "The quality checks" means the Quality checks rows.
- "The writer notes" means the writer notes block the Blog Writer adds to the row's Agent Notes (G8). Never the document itself.
- "The saved document" means the draft as saved in the product's document home: a Google Doc in Drive, or the Blog page in Notion (shared/storage-drive.md or shared/storage-notion.md).
- "Step 1.5's measurements" means the numbers and hits from scripts/measure.py (modes/qa.md, Step 1.5).

**Product rules and learned rules add to these.** A product's Active Reference rows of Type Rule (Layer Product rule or Learned rule) add new checks on top of these, or make one stricter. They never remove or loosen a base rule (shared/rule-extraction.md).

---

## The product's own quality checks

If the product has its own quality-checks file with specific pass/fail criteria beyond what's listed in the dimensions below, treat that file as the senior authority. Where the two overlap, the product's own rubric wins. Where the product's rubric covers something the checklist below doesn't, add it as its own dimension in the audit rather than skipping it. The one exception is reading level: the Blog Writer's grade 5 to 6 target applies even if the style guide names a higher grade, per the Blog Writer's own Rule Hierarchy.

Because product rules can only add a check or make one stricter, "the product's own rubric wins" means its stricter bar applies. A product criterion that would loosen a base bar was refused at extraction (shared/rule-extraction.md) and is never applied.

If the quality checks file describes its own score bands, retry limits, or a separate Reworker Agent, QA's verdict rules (modes/qa.md, Step 4) still decide the outcome: any Blocker or Standard failure means Needs Rework, the retry cap stays at three passes, and "Reworker Agent" means the Blog Writer's own rework step.

---

## How every dimension is judged

For every dimension, make a clear pass or fail call. Never mark something "mostly fine" or split the difference; either it clears the bar or it doesn't. For every failure, write a specific finding: the exact section or sentence, exactly what's wrong, and a concrete fix the Blog Writer could implement without asking a follow-up question. Where a dimension has multiple instances of the same problem (repeated em dashes, several AI-tell words, more than one date-anchored claim), list each instance on its own line under that dimension rather than collapsing them into one vague note.

The single hardest rule in QA: every failure you report must be specific enough that whoever fixes it never has to come back and ask what you meant. "Fix the CTA" is not a finding. "The mid-article CTA in the Pricing Comparison section says 'Learn More,' which is a banned generic phrase; replace it with a benefit-led headline tied to the free trial, matching the brief's Mid CTA plan" is a finding.

Several dimensions are counts, not opinions: word count, reading level, paragraph length, em dashes, banned words, spacing. Judge them from Step 1.5's measurements, never by eye. "Looked fine on a read-through" isn't a check.

---

## Severities

**Every finding carries a severity:**

- **Blocker.** Fails the draft outright, however well the rest scores. Only these:
  1. a fabricated or untraceable number, claim, quote, or review;
  2. a claim that contradicts the product's live pricing or features pages;
  3. a claim the brand guidelines prohibit;
  4. a broken or dead citation link;
  5. the primary keyword missing from the H1 or the first paragraph;
  6. any em dash;
  7. a total word count more than 10% under the brief's target with no reason the writer notes support;
  8. a measured reading level above grade 7;
  9. a saved document that renders broken (garbled characters, raw Markdown, missing spacing throughout).
- **Standard.** A real failure of a dimension's bar. Fails that dimension, and the draft goes back for rework.
- **Polish.** One or two isolated, minor slips that don't undermine the dimension as a whole, such as a single AI-tell word that is doing real work in context, or one sentence a few words over the length limit. Polish items don't fail a dimension on their own. They're listed in the report under "Polish before publish," so the human reviewer can fix them in seconds, and so a rework pass isn't spent on trivia. Three or more Polish items in the same dimension add up to a Standard failure of that dimension.

Isolated grammar slips can be Polish only if they don't change meaning; em dashes never can. An invented or altered review is a Blocker (Dimension 22). A fabricated or untraceable claim is a Blocker (Dimension 15).

---

## Scoring

- The dimensions below are the base set. Add any dimension the product's own quality-checks file requires (see The product's own quality checks above); the score is then out of that larger total.
- **QA Score** is the number of dimensions passed over the total, for example `21/23`, not a percentage; it's more legible at a glance and consistent run over run. A dimension marked "not applicable, passed" counts as passed.
- **Product rules** are scored apart from the dimensions: one check per Active product rule and learned rule for this product whose Agents include QA. **Product Rules Result** is the number passed out of the number checked, for example `11 of 12`. The report shows both numbers ("Base: 22 of 23. Product rules: 11 of 12") and quotes the line that broke each rule.
- A failed Must rule sends the draft back, whatever the score (shared/rule-extraction.md).
- A standing product or learned rule that bears directly on a dimension is also part of that dimension's standard: a draft that violates it fails the matching dimension, even if it would otherwise pass.
- The verdict: Approved only when no dimension fails at Blocker or Standard severity and no Must rule fails. Polish items never block approval. Any Blocker or Standard failure means the draft fails.

---

## The 23 base dimensions

**1. Keyword placement, density, and title optimization.** Does the primary keyword appear in the H1, the first 100 words, at least one H2, two to three times in the body, and once in the conclusion? Is density between 0.5% and 3%? Beyond the body: does the SEO title tag carry the primary keyword in its first four to five words per the Blog Writer's Step 9, does the meta description reference it naturally, and does the URL slug carry it without stop words? Is the SEO title about 50 to 60 characters and the meta description about 140 to 155, measured by character count? Fail if body placement is weak or absent, if density crosses 3%, or if the title tag, meta description, or slug is missing the keyword, buries it past where it does any good, or runs outside its length range.

**2. Internal linking.** Are there two to four internal links to genuinely relevant existing pages (or at least the quality checks' minimum, if it sets a higher one), with descriptive anchor text, not "click here"? Do they include the brief's Internal Link Plan targets where those fit? Fail on zero links, fewer than the quality checks' minimum, more than five, or an internal link that doesn't resolve.

**3. Asset and free-tool integration.** If the draft mentions the product's free tools or lead magnets, do the mentions feel earned and contextual rather than forced or repeated? Fail on irrelevant mentions, four or more mentions where one to three would do, or a mention that reads like a sales pitch dropped into an unrelated section. Zero mentions is fine if nothing in the knowledge base was actually relevant to this topic.

**4. Unique value against the competitive set.** Cross-check the draft against the brief's own Competitive Intelligence section. Does the draft actually deliver on the Spearhead Strategy sentence, the specific move it promised over the current top results, and contain at least one original-value element the leading pages don't have? Fail if the draft reads as a "me-too" piece that could have run on any of the SERP's existing top five with the product name swapped in.

**5. AI answer engine gap coverage.** This is specific to this pipeline. Cross-check the draft against the AI answer engine findings the brief captured in its Step 2d: the sources Google AI Mode and ChatGPT cited, and the specific gaps or biases each one named. Does the draft actually address those named gaps, with real depth, not a passing mention? Fail if a gap the brief flagged as a real opportunity got no meaningful treatment in the draft. If the brief says an AI engine couldn't be queried, this dimension is judged against whatever findings exist, and isn't failed for research the brief couldn't do.

**6. User intent and completeness.** Does the draft fully answer the primary and secondary intent behind the keyword, including the implicit questions a searcher would have? Fail if there's a real gap a reader would notice, or the piece stays surface-level where the brief called for depth.

**7. Actionable takeaways.** Are there at least three specific, implementable takeaways a reader could act on immediately? Every how-to or strategy step names what to do, how, why it works, the common mistake, and a decision rule where one applies, per the Blog Writer's Step 2f. Fail if takeaways are generic or purely theoretical.

**8. CTA quality and placement.** Exactly three CTAs, each specific and benefit-led (not "Learn More" or "Click Here"), placed per the brief's Step 4c intent map, in this order after the introduction: the direct answer, any summary block, then the Early CTA. None inside the FAQ, none in two consecutive sections, and each offer one the product actually has. Fail on any violation of the count, the copy standard, or the placement rules.

**9. Table value.** Where tables are present, do they earn their place per the Blog Writer's Step 6: two or more items compared across two or more attributes, specific and complete cells, headers that make sense on their own, and faster to scan than the same thing in prose? Fail if a table is decorative, thin, or has vague cells, or if the draft makes a comparison, cost breakdown, or choice between options in prose that clearly needed a table.

**10. Image strategy.** For a piece over 1,500 words, are there two to six image suggestions, each with a specific, actionable description, the correct dimensions from the Blog Writer's placement table, and the plain `[IMAGE SUGGESTED]` label format, no emoji and no blockquote? Fail if the piece has no visual plan, or if suggestions are vague enough that a designer would need to ask a follow-up question.

**11. Brand voice consistency.** Does the tone, vocabulary, and framing match the brand guidelines and writing style file, not a generic "helpful blog" voice? Does the piece use the approved perspective (you for advice, we only when the product speaks, third person for competitors) and exact product terminology? Fail on off-brand tone, competitor terminology, or a claim that contradicts something in the brand guidelines.

**12. Structure and skimmability.** Read the piece the way a skimmer actually would: headers, bolded phrases, and the first sentence of each paragraph only. Does that pass alone still convey the argument? Then check the Blog Writer's current rules, using Step 1.5's measurements:

- Paragraphs are one to three sentences and roughly 20 to 50 words, one idea each; only the direct answer and FAQ answers may run to 60 words.
- A visual element (a list, numbered steps, a table, a bolded key line of 12 words or fewer, or a callout) at least every 150 to 200 words, and at least one in every H2 section. No wall of text longer than four lines.
- Headers describe what the section delivers, in Title Case, and make sense on their own.
- Every H2 opens with a line that pulls the reader in and ends with a bridge to the next section, per the Blog Writer's Step 2n. No section opens by restating its heading.
- Where a section is built around a consequential claim, a risk, compliance, comparison, or pricing point, it follows the narrative arc from the Blog Writer's Step 4.7 in the right order (Evidence before Reframe, Resolution after it). The introduction uses the compressed arc, and an arc ends on a CTA only in the three planned CTA sections.
- The FAQ, when the format has one, is the true last section, after the Conclusion.

Fail if the skim test fails, if paragraph or visual-rhythm rules are broken in more than an isolated instance, if a section has no visual element, or if a section that should follow the arc skips a beat out of order rather than deliberately compressing it.

**13. AI-writing tells: words and phrases.** Scan the whole draft against every list below, with the Step 1.5 script, don't just skim for it. These words and phrases are measurably overused in AI-generated text: one large study of PubMed abstracts found "delves" used 28 times as often after ChatGPT's release as before it, "underscores" 14 times, and "showcasing" 11 times, and later work found some repeated AI phrasings appear more than 1,000 times as often in model output as in human writing. Each hit is a flag to review, not an automatic fail; a word like "underscore" or "robust" can be exactly the right word in context, and the test is whether it's doing real work or just filling space.

Check all three lists together: the list below, the Blog Writer's Step 2b banned words and constructions, and the style guide's own list of words that must never appear. A word the Blog Writer's Step 2b or the style guide bans outright is a failure on any use, not a flag.

Words and near-synonyms to flag: delve/delves/delving, boasts, showcase/showcasing, underscore/underscores/underscoring, comprehending, intricate/intricacies, surpassing/surpasses, garnered, emphasizing, realm, groundbreaking, advancements, aligns, leverage, elevate, unlock, navigate, embark, empower, cultivate, harness, foster, bolster, streamline, enhance, crucial, vital, essential (as filler), unparalleled, unprecedented, cutting-edge, holistic, pivotal, invaluable, dynamic, multifaceted, ever-evolving, transformative, game-changing, robust, seamless/seamlessly, meticulous/meticulously, vibrant, bespoke, tapestry, testament, myriad, plethora, paradigm, synergy, cornerstone, catalyst, beacon, landscape (used figuratively), journey (used figuratively), nestled, commendable, noteworthy, and "ecosystem" used as filler rather than literally.

Phrases to flag outright, since these almost never survive a real edit: "in today's fast-paced/digital world," "in the ever-evolving landscape of," "it's important to note that," "it's worth noting," "it goes without saying," "when it comes to," "at the end of the day," "not only X but also Y," "whether you're X or Y," "unlock the power/potential of," "take X to the next level," "stay ahead of the curve," "a game-changer for," "revolutionize the way," "in conclusion," "in summary," "overall," (as a section opener) "in a nutshell," "plays a crucial/pivotal/vital role in," "serves as a testament to," "stands as a," "marking a pivotal moment," "a testament to," "rest assured," "dive into," "let's dive in," "look no further," "we've got you covered," "the world of," "navigating the complexities of," "designed to," (as filler) "help you [verb] with ease," and any opener or closer that thanks, reassures, or addresses the reader like a chat reply ("Great question," "I hope this helps," "Happy selling!").

Fail if several unjustified hits cluster in one section, if the piece carries more than one hit per roughly 300 words overall, or if a banned phrase appears with no real content behind it, even where any single word in isolation might have been defensible.

**14. Grammar, mechanics, and punctuation.** Read every sentence for subject-verb agreement, tense consistency (a piece shouldn't drift between present and past mid-section without reason), correct comma and apostrophe use, the Oxford comma, the spelling the product's Settings row names (US spelling unless it says UK), and a run-on or fragment sentence that isn't a deliberate stylistic choice. Zero spelling errors. Then use Step 1.5's character scan:

- **Zero em dashes anywhere in the piece**, including headings, tables, image notes, and the SEO block. This is the house rule the entire content system runs on, and a single em dash is a Blocker on its own. List every instance found by its exact location before marking this dimension a pass.
- No en dash or double hyphen used as a dash in a sentence (a number range like "3-5" written with a plain hyphen is fine).
- No ellipsis character, no dramatic "..." in prose, and no semicolons in explanatory prose, per the Blog Writer's Step 2b.
- Exclamation marks only where the excitement is real, and never more than one or two in a piece.
- The `→` arrow appears only in an interface path, per the Blog Writer's Step 2k.

Fail on any grammar or spelling error, or any punctuation rule above. Isolated grammar slips can be Polish only if they don't change meaning; em dashes never can.

**15. Anti-hallucination and sourcing.** Can every specific claim, statistic, or outcome in the draft be traced to the brief, the knowledge base, a live source read during writing, or an explicit `[VERIFY]` or `[FRESHNESS_FLAG]` tag? Check both directions, not just one: an unflagged claim with nothing behind it fails exactly as badly as it always has, but so does a piece that leans on `[VERIFY]` as a shortcut instead of actually finding the number. Every open `[VERIFY]` tag should have a matching line in the writer notes saying what was checked and why it's still unconfirmed; a tag with no research behind it, or a tag on something checkable in a few minutes (a public price, a public stat), is a failure. Where a tag sits on something checkable in a few minutes, check it directly rather than taking the tag's word for it; if it verifies clean, note that in the report so it doesn't cost the Blog Writer the same lookup twice. Honestly researched open tags are revision items for the human publish review, not a failure by themselves (G18). Also check:

- **Citations are real links**, pointing at the original source (not a blog quoting it), each resolving, and cited by linking the fact itself, not narrated ("according to...").
- **No vague attribution**: "studies show," "experts say," "industry reports suggest," or "many businesses" standing in for a named source.
- **Scenario math is honest**: a made-up scenario is labeled as a scenario, and every real-world rate, fee, or result applied to it is sourced.

Fail if anything reads as a fabricated number, an invented client result, a confident claim with nothing behind it, or if `[VERIFY]` tags are doing the job real research should have done. A fabricated or untraceable claim is a Blocker.

**16. Evergreen phrasing, no date-anchored claims.** Check every place the draft describes a feature, a price, or a capability, and confirm it isn't anchored to a date or a version number: "as of [date]," "starting in [month/year]," "on March 3, [Product] released...," "in version 4.2," "since last year." Those age the whole sentence the moment the feature changes again. The freshness-flag system already exists to handle the fact that this state can change later, per the Blog Writer's Step 11 and the brief's Step 4g. Naming the gap a feature closes is fine and is the Blog Writer's own taught pattern ("Until now, you had to use a third-party app for this. Now [Product] does it natively."), as long as no date or version number anchors it; a date or version may appear only where it's genuinely useful to the reader, such as a compliance deadline or a migration timeline, and never as the news itself. Fail if the draft anchors a feature, price, or capability to a date or version number anywhere without that reason.

**17. Length and depth against the brief.** Using Step 1.5's counts: is the total (body plus FAQ, not the SEO metadata, image notes, or tags) within 10% of the brief's target word count? Does every H2 section get its share of the depth, with the later steps of a how-to and the later items of a listicle as developed as the first? Fail if the total is more than 10% under the target without a reason the writer notes support (a Blocker), or if any section is thin compared with its role in the outline, even when the total looks fine. Name each thin section and what it's missing (a worked example, a step, a real question answered, a decision rule, a table).

**18. Reading level and density.** Using Step 1.5's measurements: is the Flesch-Kincaid grade between 5 and 6, with 7 as the hard ceiling? Is the average sentence 10 to 14 words, with almost no sentences over 20? Does sentence length vary (a spread, or standard deviation, of about 4 words or more), rather than every sentence running the same length, which is a common machine-writing tell? Then check density, per the Blog Writer's Step 2l: flag every vague phrase where a specific could go ("many businesses," "can be expensive," "a lot of time," "various options"). Fail if the grade is above 6 (a Blocker above 7), if long sentences are common, if sentence length barely varies, or if vague phrases cluster.

**19. The saved document renders cleanly.** Using Step 1.5's scans of the exported document:

- Spacing. In Drive: exactly one empty line between blocks throughout, never two paragraphs back to back and never two empty lines in a row. In Notion, Notion spaces blocks itself, so the bar is never two empty blocks in a row.
- No garbled characters; no emoji; no raw Markdown (links written as `[text](url)`, `**`, `#`, `---`, `>`) showing as text, no backslash-escaped brackets, and no HTML entities shown as text.
- Headings are real headings; every link, including links in table cells, is clickable; tables have their borders and header row; and the SEO metadata sits in its own labeled block.

Fail on any of these; a document that renders broken throughout is a Blocker.

**20. Reader questions answered.** Does the draft answer the real questions readers ask about this topic: the brief's People Also Ask questions, their follow-up questions, and the questions real people raise in community threads, per the Blog Writer's Step 1.5 reader question map? Does every H2 section answer at least one question in plain words, and does the FAQ (when the format has one) hold five to eight real questions in the reader's own words, each answered in 40 to 60 words that open with the answer itself? Run two or three of the brief's main questions through a quick search yourself; if an obvious, commonly asked question has no answer anywhere in the piece, that's a failure. Fail on any missing obvious question, a section that answers nothing a reader actually asks, or an FAQ built from invented questions.

**21. Examples, narrative, and stance.** Per the Blog Writer's Steps 2o, 4.5, 4.6, and 4.7:

- Every H2 section has at least one concrete, strategic example (a specific scenario, a before-and-after, a worked calculation, or a real named case) placed next to the idea it explains.
- One realistic reader scenario runs through the piece, from the introduction to the conclusion, and is clearly labeled as a scenario.
- The piece is data-led wherever real data exists: the hook opens on a sourced number when a strong one exists, sections stand on sourced data where it exists, and no number is forced or invented where none does.
- The piece takes a clear stance: it says plainly what we think the reader should do and why, and shows the reasoning (the options weighed, where each falls short, and why we recommend what we do).
- Sections connect by cause and effect, so each one answers the question the last one raised, rather than reading as a stack of separate tips.

Fail if any H2 has no example, if there's no clear stance, if the hook states the topic instead of the stakes, if strong available data went unused in the hook or the evidence, or if the piece reads as a list of disconnected tips.

**22. Reviews and platform data integrity.** Per the Blog Writer's Step 1.5 and Step 4.5f: every quoted review is quoted word for word, attributed to the reviewer's username, the site, and the date, and linked to the review itself; spot-check at least two quotes against their source pages. No review is invented, merged, paraphrased as a quote, or used to make a claim the brand guidelines prohibit. Platform numbers (for a WordPress plugin, WordPress.org's active installations, rating, and rating count; for another product, the same numbers on the marketplace or directory page it is listed on) match the live page, are quoted exactly as shown, carry a freshness flag, and active installations are never described as customers or merchants. Fail on any mismatch; an invented or altered review is a Blocker. Mark this dimension "not applicable, passed" if the piece uses no reviews and no platform data.

**23. AI-writing tells: structure and formatting.** Machine-written text gives itself away in its shape as much as its words. Check the whole draft for:

- **Reflexive rule-of-three lists** ("innovative, transformative, and groundbreaking") where the three items aren't each doing work, or the piece falling into threes over and over.
- **Negative parallelism** ("it's not just X, it's Y," "not X, but Y," "no X, no Y, just Z") used more than once or twice in the piece.
- **False ranges** ("from X to Y") that don't describe a real spectrum.
- **Hanging "-ing" tails** that add fake analysis to a sentence: ", highlighting...," ", underscoring...," ", reflecting...," ", showcasing...," ", ensuring...," ", making it...".
- **Empty significance claims**: telling the reader something is important, crucial, or a key consideration instead of showing why.
- **Section-ending recaps** that restate what the section just said ("In short," "Overall," "Ultimately"), and a conclusion that only repeats the introduction.
- **Synonym cycling**: calling the same thing by a different name each time (store, shop, storefront, business) just to avoid repeating a word, which confuses the reader.
- **Repeated sentence openings**: three or more sentences in a row starting with the same word, or "This" opening sentence after sentence.
- **Over-formatting**: bold on whole sentences, more than one bold phrase in most sections, every bullet in the form "**Label:** explanation" where plain bullets would read better, or lists used where a sentence would do.
- **Uniform rhythm**: every paragraph the same length and shape, every section built on the identical pattern.
- **Chat leftovers and placeholders**: "Certainly," "Here's," "As an AI," "I hope this helps," knowledge-cutoff wording, `[insert ...]`, "TBD," "lorem ipsum," or any bracketed instruction meant for the writer.
- **Hedging stacks**: "can potentially help," "may possibly," "might be able to," where a direct claim is supported.

Fail if the draft reads like generic AI output on the whole, if several of these cluster in one section, or if any pattern repeats across the piece.

---

## Product and learned rule checks

After the 23 dimensions (and any dimension the product's quality checks add), run one check per Active Reference row of Type Rule for this product, Layer Product rule or Learned rule, whose Agents include QA.

- A rule with Check Method `Script` is checked from Step 1.5's measurements (words and phrases it bans go in the script's `--banned` file; counts and keyword spots come from its numbers). A rule with Check Method `Judged` is checked by reading.
- Each check is a clear pass or fail, the same as a dimension. A failure names the Rule ID, quotes the exact line in the draft that broke it, and gives the concrete fix.
- A failed Must rule sends the draft back, whatever the score. A failed Should rule that bears on a dimension fails that dimension (see Scoring); one that bears on no dimension is a Polish item.
- A rule flagged as broken or vague in the run summary (missing fields, wording like "make it engaging") is skipped and named in the report, never guessed at (shared/rule-extraction.md, Keeping them right over time).
