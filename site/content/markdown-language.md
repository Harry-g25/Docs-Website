# Markdown Language — Complete Study Manual (CommonMark Core + GFM Extensions)

**Baseline Specification:** CommonMark (normative core) + GitHub Flavored Markdown (GFM) extensions  
**Last Updated:** February 2026  
**Normative Sources:**  
- CommonMark Specification: <https://spec.commonmark.org/>  
- GitHub Flavored Markdown Spec: <https://github.github.com/gfm/>  

**Non-normative but historically important context (covered comparatively):**  
- Original “Markdown” (Gruber) description and its underspecification  
- Major dialect families (Markdown Extra, MultiMarkdown, Pandoc Markdown)

---

## Table of Contents

<details open>
<summary><strong>Table of Contents — click to expand/collapse</strong></summary>

<nav aria-label="Table of contents">
    <ul>
        <li><a href="#preface-and-scope">Preface and Scope</a></li>
        <li><a href="#part-a--conceptual-foundations">Part A — Conceptual Foundations</a>
            <ul>
                <li><a href="#a01--what-a-markdown-language-means-formal-framing">A0.1 — What “a Markdown language” means (formal framing)</a></li>
                <li><a href="#a11--core-primitives-text-lines-whitespace-indentation">A1.1 — Core primitives: text, lines, whitespace, indentation</a></li>
                <li><a href="#a2--block-vs-inline-the-fundamental-separation">A2 — Block vs inline: the fundamental separation</a></li>
                <li><a href="#a3--the-parsing-lifecycle-execution-model-of-markdown">A3 — The parsing lifecycle (execution model of Markdown)</a></li>
                <li><a href="#a4--blocks-container-blocks-vs-leaf-blocks-formal-taxonomy">A4 — Blocks taxonomy</a></li>
                <li><a href="#a5--inlines-delimiter-runs-precedence-and-why-regex-parsing-fails">A5 — Inlines: delimiter runs</a></li>
                <li><a href="#a6--escaping-backslash-semantics-entities-and-literalness">A6 — Escaping and entities</a></li>
                <li><a href="#a7--raw-html-blending-markup-languages-security-and-semantics">A7 — Raw HTML (security and semantics)</a></li>
                <li><a href="#a8--linkreference-system-global-state-inside-a-simple-language">A8 — Link/reference system</a></li>
                <li><a href="#a9--tooling-ecosystem-context-what-authoritative-means-in-practice">A9 — Tooling ecosystem context</a></li>
                <li><a href="#a10--concept-maps-and-dependency-graphs-textual-for-rigorous-study">A10 — Concept maps and dependency graphs</a></li>
                <li><a href="#a11--paragraphs-soft-breaks-hard-breaks-and-inline-eligibility">A11 — Paragraphs and line breaks</a></li>
                <li><a href="#a12--headings-atx-setext-and-their-disambiguation-rules">A12 — Headings (ATX/Setext)</a></li>
                <li><a href="#a13--thematic-breaks-horizontal-rules-and-false-positives">A13 — Thematic breaks</a></li>
                <li><a href="#a14--block-quotes-marker-continuation-and-lazy-continuation">A14 — Block quotes</a></li>
                <li><a href="#a15--code-blocks-indented-vs-fenced-info-strings-and-containment">A15 — Code blocks</a></li>
                <li><a href="#a16--lists-markers-indentation-tightloose-and-ambiguity-resolution">A16 — Lists</a></li>
                <li><a href="#a17--code-spans-inline-code-backtick-runs-trimming-and-delimiter-selection">A17 — Code spans (inline code)</a></li>
                <li><a href="#a18--links-and-images-inline-form-reference-form-destinations-titles-and-nesting-constraints">A18 — Links and images</a></li>
                <li><a href="#a19--autolinks-angle-form-and-email-autolinks">A19 — Autolinks (angle form)</a></li>
                <li><a href="#a20--emphasis-and-strong-emphasis-delimiter-run-classification-and-pairing-algorithm">A20 — Emphasis/strong (algorithm)</a></li>
                <li><a href="#a21--backslash-escapes-escapable-punctuation-set-and-ambiguity-control">A21 — Backslash escapes</a></li>
                <li><a href="#a22--inline-html-and-entitycharacter-references-parsing-boundaries-and-safety">A22 — Inline HTML and entities</a></li>
                <li><a href="#a23--link-reference-definitions-block-level-syntax-normalization-and-resolution-semantics">A23 — Link reference definitions</a></li>
                <li><a href="#a24--html-blocks-commonmark-block-types-termination-rules-and-interactions">A24 — HTML blocks</a></li>
            </ul>
        </li>
        <li><a href="#part-b--complete-technical-reference">Part B — Complete Technical Reference</a></li>
        <li><a href="#part-c--structured-learning-path-for-self-study">Part C — Structured Learning Path (Self-Study)</a></li>
        <li><a href="#appendix-a--dialect-compatibility-matrix-and-known-divergences">Appendix A — Dialect Compatibility Matrix</a></li>
        <li><a href="#appendix-b--security-model-threats-and-sanitization-requirements">Appendix B — Security Model</a></li>
        <li><a href="#appendix-c--testing-verification-and-differential-fuzzing">Appendix C — Testing and Verification</a></li>
    </ul>
</nav>

</details>

---

## Preface and Scope

This manual treats “Markdown language” as a *precisely defined transformation* from Unicode text to a structured document model and rendered output.

Because the historical “Markdown” description is underspecified and implementations diverge, this manual uses:

1. **CommonMark** as the normative core specification.
2. **GFM** as the dominant, widely deployed, and formally specified extension layer.

Where behavior differs across major dialects or is intentionally underspecified, this manual:

- states the ambiguity explicitly,
- shows competing interpretations,
- explains the consequences for correctness, portability, and security.

---

# Part A — Conceptual Foundations

## A0.1 — What “a Markdown language” means (formal framing)

### A0.1.1 Formal definition

A Markdown processor defines a mapping:

- **Input domain:** A Unicode text document (sequence of code points), which can be partitioned into lines.
- **Primary output:** A structured document model (commonly an AST with typed nodes; conceptually similar to a DOM tree).
- **Rendered output:** A serialization of the model into a target format (usually HTML).

CommonMark defines (normatively):

1. A parsing algorithm that consumes lines and yields a tree of block and inline nodes.
2. Deterministic disambiguation rules for syntactic forms that are ambiguous under naive grammars.

GFM defines additional constructs and parsing rules layered on CommonMark.

### A0.1.2 Why the concept exists

Markdown exists to make authoring structured documents feasible in plain text, while remaining sufficiently machine-parsable to support tooling such as:

- rendering into HTML,
- link checking,
- search indexing,
- transformations to other formats,
- linting, formatting, and compliance verification.

### A0.1.3 Historical or design motivation

- The original Markdown (2004) prioritized readability and informal conventions but left many parsing behaviors unspecified.
- Divergence of implementations caused portability failures.
- CommonMark was created to standardize behavior with a formal spec and a comprehensive test suite.
- GFM standardizes the extension layer that became de facto common in code hosting and documentation platforms.

### A0.1.4 Theoretical model

Markdown is not well described as a single context-free grammar.

- Block parsing is strongly line- and indentation-dependent.
- Inline parsing is context-sensitive (e.g., emphasis delimiters depend on surrounding character categories).

Practical parsers therefore use state machines, delimiter stacks, and well-defined precedence rules rather than regular-expression-only pipelines.

### A0.1.5 Internal mechanics

CommonMark parsing is most usefully modeled as two phases:

1. **Block parsing:** recognize and nest blocks (headings, paragraphs, lists, block quotes, code blocks, etc.).
2. **Inline parsing:** within specific leaf blocks (notably paragraphs and headings), parse inline constructs (emphasis, links, code spans, etc.).

This separation is a deliberate design choice to keep ambiguity manageable.

### A0.1.6 Interactions with other concepts

- Block decisions constrain where inline parsing applies (code blocks disable inline parsing).
- Link reference definitions create global document state used later for link resolution.
- Raw HTML blocks can suppress Markdown parsing depending on HTML block type.

### A0.1.7 Examples

#### A0.1.7.1 Minimal working example (reference links)

Markdown:

```markdown
# Title

A *paragraph* with a [link][id].

[id]: https://example.com "Example"
```

Expected HTML (conceptual):

```html
<h1>Title</h1>
<p>A <em>paragraph</em> with a <a href="https://example.com" title="Example">link</a>.</p>
```

Line-by-line explanation:

1. `# Title` starts an ATX heading block.
2. Blank line terminates the heading block.
3. Paragraph text is collected into a paragraph block.
4. The reference definition is recognized and stored in the reference map; it does not appear as visible text output.

Failure modes:

- If the reference definition is malformed, `[link][id]` becomes an unresolved reference; CommonMark renders it as literal brackets/text rather than a hyperlink.

---

## A1.1 — Core primitives: text, lines, whitespace, indentation

### A1.1.1 Formal definition: document, line, blank line

- A **document** is a sequence of characters that can be partitioned into **lines**.
- A **blank line** is a line containing only spaces/tabs (or empty).
- Many block constructs are terminated or separated by blank lines.

### A1.1.2 Why the concept exists

Markdown is line-structured; many constructs are recognized from line starts, and many termination/continuation rules depend on blank lines.

### A1.1.3 Theoretical model

Block parsing is naturally treated as a stream over lines with indentation-aware recognition.

### A1.1.4 Internal mechanics

CommonMark uses a column-based indentation model:

- Tabs are expanded to 4-space tab stops for indentation calculation.
- “Up to three spaces” vs “four or more spaces” frequently changes meaning.

### A1.1.5 Examples

#### A1.1.5.1 Indented code block (minimal)

Markdown:

```markdown
    indented code
```

Expected HTML (conceptual):

```html
<pre><code>indented code
</code></pre>
```

Explanation:

- A line indented by 4+ spaces at the top level begins an indented code block.
- Inline parsing is disabled inside code blocks.

#### A1.1.5.2 Incorrect-intent example: 3-space indentation

Markdown:

```markdown
   not code (3 leading spaces)
```

Explanation:

- In CommonMark, 3 spaces is not sufficient to start an indented code block at top level.
- The text is parsed as a paragraph line starting with spaces.

Performance note:

- Naive per-character re-computation of columns with tabs can be expensive; efficient implementations track column position incrementally.

---

## A2 — Block vs inline: the fundamental separation

### A2.1 Formal definition

- **Block constructs** define vertical structure (headings, paragraphs, lists, block quotes, code blocks, HTML blocks, thematic breaks).
- **Inline constructs** define structure within inline-capable blocks (emphasis, links, images, code spans, breaks, entities, inline HTML).

### A2.2 Why it exists

Without a block-first discipline, parsing ambiguity becomes intractable and portability across implementations collapses.

### A2.3 Internal mechanics

Common pipeline:

1. Build a block tree from lines.
2. Apply inline parsing only within eligible leaf blocks.

### A2.4 Examples

#### A2.4.1 Fenced code disables inline parsing

Markdown:

````markdown
```python
print("*not emphasis*")
```
````

Expected HTML (conceptual):

```html
<pre><code class="language-python">print("*not emphasis*")
</code></pre>
```

Explanation:

- The `*` characters remain literal inside a fenced code block.

Incorrect example (misconception):

- Expecting emphasis to apply inside code blocks. In CommonMark/GFM, it does not.

---

## A3 — The parsing lifecycle (execution model of Markdown)

### A3.1 Formal definition (pipeline)

A Markdown processor typically implements:

1. Input normalization (encoding, line endings).
2. Block parsing.
3. Inline parsing.
4. Post-processing (e.g., reference resolution, list tight/loose normalization; GFM table/task-list post-processing).
5. Rendering.

### A3.2 Why it exists

- Reference link definitions require global state.
- List tightness depends on blank lines within items.
- Inline emphasis/link parsing requires context-sensitive disambiguation.

### A3.3 Error and exception model

Markdown parsers generally do not raise errors for malformed syntax. Instead:

- Unrecognized syntax is treated as literal text.
- Ambiguities are resolved by precedence rules.

Failure modes to study:

- **Recognition failure:** syntax is not recognized; output is literal.
- **Constraint failure:** a construct is attempted but invalid; fallback to paragraph.
- **Ambiguity resolution:** multiple interpretations exist; spec selects one.

---

## A4 — Blocks: container blocks vs leaf blocks (formal taxonomy)

### A4.1 Formal definition

- **Container blocks:** blocks that contain blocks.
  - Block quotes
  - List items / lists

- **Leaf blocks:** blocks with text or atomic structure.
  - Paragraphs
  - Headings
  - Code blocks (indented, fenced)
  - Thematic breaks
  - HTML blocks

### A4.2 Why it exists

This taxonomy explains nesting, indentation, and continuation rules.

### A4.3 Internal mechanics

On each new line, the parser typically:

1. Attempts to continue all currently open container blocks.
2. Closes containers that can no longer match.
3. Checks whether the remainder begins a new block.
4. Otherwise appends content to the current leaf block.

Lazy continuation (notably for block quotes) is a major portability pitfall.

---

## A5 — Inlines: delimiter runs, precedence, and why regex parsing fails

### A5.1 Formal definition: delimiter run

A **delimiter run** is a sequence of one or more `*` or `_` characters.

Whether a run can open and/or close emphasis depends on:

- The categories of characters before/after the run (whitespace vs punctuation vs alphanumeric),
- Whether the run is *left-flanking* and/or *right-flanking* (CommonMark terms),
- Additional restrictions for `_` to prevent intraword emphasis surprises.

### A5.2 Why it exists

- Prevents emphasis from triggering in the middle of identifiers and words.
- Enables deterministic nesting and pairing rules.

### A5.3 Examples

#### A5.3.1 Canonical emphasis/strong

Markdown:

```markdown
This is *em* and **strong**.
```

Expected HTML (conceptual):

```html
<p>This is <em>em</em> and <strong>strong</strong>.</p>
```

#### A5.3.2 Edge case: underscores within words

Markdown:

```markdown
foo_bar_baz
```

Expected behavior (CommonMark intent):

- Often **no emphasis is produced**, because `_` emphasis has intraword restrictions.

Common misconception:

- “Underscore works exactly like asterisks.” It does not.

Performance note:

- Naive backtracking across long delimiter runs can become quadratic on adversarial input.

---

## A6 — Escaping, backslash semantics, entities, and literalness

### A6.1 Formal definition: backslash escape

A backslash may:

- Escape certain punctuation characters that would otherwise be parsed as syntax.
- Create a hard line break when placed at the end of a line (CommonMark supports this form).

### A6.2 Examples

#### A6.2.1 Escaping emphasis markers

Markdown:

```markdown
\*not emphasized\*
```

Expected HTML (conceptual):

```html
<p>*not emphasized*</p>
```

#### A6.2.2 Hard line break via backslash

Markdown:

```markdown
line 1\\
line 2
```

Expected HTML (conceptual):

```html
<p>line 1<br />
line 2</p>
```

Incorrect example:

```markdown
\q
```

Explanation:

- Backslash is not a universal escape; only certain escapes are recognized by the spec. Otherwise the backslash may be treated literally.

### A6.3 Entities and decoding

Markdown processors typically pass through (or interpret) HTML entity references such as `&amp;` and `&#x2026;`.

Security relevance:

- Sanitizers must handle entity decoding correctly before enforcement; otherwise policy checks can be bypassed.

---

## A7 — Raw HTML: blending markup languages (security and semantics)

### A7.1 Formal definition

Markdown commonly supports:

- Inline HTML within paragraphs.
- HTML blocks (line-start patterns) that can suppress Markdown parsing within their region depending on HTML block type.

CommonMark specifies multiple HTML block types with different termination rules.

### A7.2 Security model and risks

If raw HTML is allowed and rendered into a browser DOM, Markdown becomes an XSS attack surface.

Example (dangerous if rendered without sanitization):

```markdown
Hello <img src=x onerror=alert(1)>
```

Mitigations (conceptual):

- Disable raw HTML in the renderer, **or**
- Render then sanitize with a strict allowlist policy.

---

## A8 — Link/reference system: global state inside a “simple” language

### A8.1 Formal definition: link reference definition

A link reference definition associates:

- A **label** (normalized; commonly case-insensitive and whitespace-normalized in CommonMark),
- A **destination** (URL),
- An optional **title**.

The processor collects definitions across the document and uses them to resolve reference links and images.

### A8.2 Examples

Markdown:

```markdown
Use [CommonMark][cm].

[cm]: https://commonmark.org "Spec"
```

Expected HTML (conceptual):

```html
<p>Use <a href="https://commonmark.org" title="Spec">CommonMark</a>.</p>
```

Failure modes:

- Label normalization mismatches can yield unresolved references.
- Duplicate definitions may resolve differently across dialects (CommonMark defines a deterministic rule; other dialects may differ).

---

## A9 — Tooling ecosystem context: what “authoritative” means in practice

### A9.1 Specifications and test suites

- CommonMark provides a comprehensive spec and a machine-readable test suite.
- Implementations frequently advertise compliance percentages.

### A9.2 Implementation families (conceptual)

- C-based implementations used as correctness baselines.
- JavaScript implementations widely used in web tooling.
- Python implementations with significant dialect variation.

### A9.3 Debugging and introspection

- Inspect HTML output or AST output (if available).
- Visualize whitespace and indentation.
- Reduce surprising inputs to minimal counterexamples.
- Use differential testing across multiple implementations to locate underspecified corners.

---

## A10 — Concept maps and dependency graphs (textual, for rigorous study)

### A10.1 Concept map (textual)

- Document
  - Lines
    - Indentation model (tabs → columns)
    - Blank lines
  - Block parsing
    - Container blocks
      - Block quotes (marker continuation, lazy continuation)
      - Lists (markers, indentation, tight/loose, continuation)
    - Leaf blocks
      - Paragraphs (inline parsing enabled)
      - Headings
      - Code blocks (inline disabled)
      - HTML blocks (inline disabled depending on type)
      - Thematic breaks
  - Inline parsing (within eligible blocks)
    - Escapes
    - Code spans
    - Emphasis/strong (delimiter runs)
    - Links/images (inline + reference definitions)
    - Autolinks (and GFM autolink literals)
    - Entities / inline HTML
  - Rendering
    - HTML serialization
    - Sanitization policy (security)
  - Extensions (GFM)
    - Tables
    - Task lists
    - Strikethrough
    - Autolink literals

### A10.2 Dependency graph (textual)

- Indentation rules → code blocks, list parsing, quote nesting
- Block parsing → determines which text receives inline parsing
- Reference definition collection → link/image resolution
- Inline delimiter rules → emphasis correctness and performance
- HTML allowance policy → security posture

### A10.3 Common mental model errors

1. Misunderstand indentation → misparse lists vs code blocks.
2. Misunderstand lazy continuation → block quotes and lists “leak”.
3. Treat emphasis as regex → broken nesting and edge-case failures.
4. Ignore label normalization → reference links fail unexpectedly.
5. Assume Markdown is safe HTML → XSS vulnerabilities in docs sites.

---

## A11 — Paragraphs, soft breaks, hard breaks, and inline eligibility

### A11.1 Formal definition

A **paragraph** is a leaf block consisting of one or more consecutive lines of text that:

- are not interpreted as another block construct,
- are not separated by a blank line,
- and occur in a context where a paragraph is permitted.

Within paragraphs (and certain other inline-capable blocks, such as headings), **inline parsing is enabled**.

Two line-break concepts must be distinguished:

- **Soft line break:** a newline in the source that is rendered as a space (or sometimes a newline in HTML, but semantically it is not `<br>`).
- **Hard line break:** a newline in the source that is rendered as an explicit line break (`<br />` in HTML).

### A11.2 Why the concept exists

- Markdown is optimized for prose; paragraphs are the default unit of prose.
- Hard breaks exist to support poetry/addresses without forcing HTML.

### A11.3 Historical or design motivation

Original Markdown implementations differed in how they treated single newlines inside paragraphs.
CommonMark standardizes soft vs hard breaks and specifies the triggering syntax for hard breaks.

### A11.4 Theoretical model

- Block parsing determines paragraph boundaries.
- Inline parsing then interprets inline constructs within those boundaries.
- Line breaks are an inline-level rendering decision.

### A11.5 Internal mechanics

CommonMark recognizes a hard line break in either of these forms:

1. Two or more spaces at end of line.
2. A backslash at end of line.

Otherwise, a newline in a paragraph is a soft break.

### A11.6 Examples

#### A11.6.1 Minimal working example: soft break

Markdown:

```markdown
line 1
line 2
```

Expected HTML (conceptual):

```html
<p>line 1
line 2</p>
```

Explanation:

- The newline is a soft break; renderers typically display a space-like separation in the browser.
- It is not a hard break unless explicit syntax is used.

#### A11.6.2 Canonical hard break: two spaces

Markdown (the two trailing spaces are significant):

```markdown
line 1  
line 2
```

Expected HTML (conceptual):

```html
<p>line 1<br />
line 2</p>
```

Failure mode (common):

- Editors that trim trailing whitespace silently remove the two spaces, changing semantics.

#### A11.6.3 Canonical hard break: backslash

Markdown:

```markdown
line 1\\
line 2
```

Expected HTML (conceptual):

```html
<p>line 1<br />
line 2</p>
```

Incorrect example (misconception):

```markdown
line 1\ line 2
```

Explanation:

- A backslash creates a hard break only at end-of-line, not in the middle of a line.

Performance note:

- Paragraph parsing is linear, but inline parsing inside large paragraphs can dominate runtime due to delimiter processing (emphasis/link parsing).

---

## A12 — Headings: ATX, Setext, and their disambiguation rules

### A12.1 Formal definition

CommonMark defines two heading forms:

1. **ATX headings:** initiated by 1–6 `#` characters at line start (allowing up to 3 leading spaces), followed by content.
2. **Setext headings:** a paragraph line followed by an underline of `=` (level 1) or `-` (level 2).

Headings are leaf blocks that are inline-capable: their textual content is parsed for inline constructs.

### A12.2 Why the concept exists

- Enables hierarchical structure for documents.
- Provides two syntaxes: a compact form (ATX) and a prose-friendly form (Setext).

### A12.3 Design motivation and history

- Original Markdown had both forms; Setext style predates Markdown as a plain-text heading convention.
- CommonMark standardizes edge cases: trailing `#` handling, required spacing rules, and precedence relative to other blocks.

### A12.4 Internal mechanics

ATX heading recognition involves:

- Up to 3 leading spaces permitted.
- Between the opening `#` run and content, there must be at least one space (or end of line).
- Optional closing `#` run may be stripped if preceded by a space.

Setext heading recognition involves:

- The underline must be composed of `=` or `-` characters (with optional trailing spaces).
- It applies to the immediately preceding paragraph line(s) (subject to block context constraints).

### A12.5 Examples

#### A12.5.1 ATX heading (canonical)

Markdown:

```markdown
### Heading *with emphasis*
```

Expected HTML (conceptual):

```html
<h3>Heading <em>with emphasis</em></h3>
```

Line-by-line explanation:

- `###` selects heading level 3.
- Inline parsing applies within the heading content.

#### A12.5.2 Trailing hashes (edge behavior)

Markdown:

```markdown
## Title ##
```

Expected HTML (conceptual):

```html
<h2>Title</h2>
```

Explanation:

- In CommonMark, the trailing `##` may be stripped when preceded by a space.

Incorrect example:

```markdown
##Title
```

Explanation:

- Without a space after the opening `##`, CommonMark does not recognize an ATX heading; it becomes a paragraph.

#### A12.5.3 Setext heading (canonical)

Markdown:

```markdown
Heading level 1
==============
```

Expected HTML (conceptual):

```html
<h1>Heading level 1</h1>
```

Pitfall:

- A line of dashes under a paragraph can also be interpreted as a thematic break in some contexts/dialects; CommonMark defines precedence rules.

---

## A13 — Thematic breaks (horizontal rules) and false positives

### A13.1 Formal definition

A **thematic break** is a leaf block that represents a transition in topic or scene. In HTML it is commonly rendered as `<hr />`.

CommonMark recognizes a thematic break line when it consists of:

- a sequence of `*`, or
- a sequence of `-`, or
- a sequence of `_`,

with optional spaces between characters, and satisfying minimum count constraints.

### A13.2 Why it exists

- Provides structure without headings.

### A13.3 Internal mechanics

- Up to 3 leading spaces permitted.
- The line must contain only the marker character and spaces.
- Minimum number of marker characters is required (commonly 3).

### A13.4 Examples

#### A13.4.1 Canonical thematic break

Markdown:

```markdown
---
```

Expected HTML (conceptual):

```html
<hr />
```

#### A13.4.2 Edge case: spaced markers

Markdown:

```markdown
* * *
```

Expected HTML (conceptual):

```html
<hr />
```

Incorrect example: insufficient markers

```markdown
--
```

Explanation:

- Usually parsed as a paragraph line (or, in some contexts, can affect list parsing); it is not a thematic break.

---

## A14 — Block quotes: marker continuation and lazy continuation

### A14.1 Formal definition

A **block quote** is a container block introduced by a `>` marker at the start of a line (allowing up to 3 leading spaces). It contains blocks.

### A14.2 Why it exists

- Supports quoted material, citations, and nested discussions.

### A14.3 Historical/design motivation

- `>` quoting is inherited from email/news plaintext conventions.
- Lazy continuation exists to allow wrapped prose inside a quote without repeating `>` on every line.

### A14.4 Theoretical model

- Block quote is a container that modifies the “line prefix” consumed before parsing inner blocks.
- Continuation can be explicit (`>` present) or lazy (omitted on subsequent paragraph lines under constraints).

### A14.5 Internal mechanics

Key mechanics (CommonMark-style):

- A block quote line begins with optional indentation (≤3 spaces), then `>`, then an optional single space.
- Nested block quotes are formed by repeated `>` prefixes.
- Lazy continuation: if inside a block quote and currently parsing a paragraph, a subsequent line without `>` may still be included in that paragraph if it does not start a block that would close the quote.

### A14.6 Examples

#### A14.6.1 Canonical block quote

Markdown:

```markdown
> quoted line 1
> quoted line 2
```

Expected HTML (conceptual):

```html
<blockquote>
<p>quoted line 1
quoted line 2</p>
</blockquote>
```

#### A14.6.2 Lazy continuation (major pitfall)

Markdown:

```markdown
> quoted line 1
quoted line 2 (still quoted)
```

Expected behavior (CommonMark intent):

- The second line can be treated as part of the same quoted paragraph due to lazy continuation.

Incorrect-intent misconception:

- “A missing `>` means the quote ends.” This is not reliably true.

Security-relevant note:

- Quote blocks themselves are not special security risks, but they interact with HTML blocks and list parsing in ways that can hide raw HTML in visually unexpected places.

---

## A15 — Code blocks: indented vs fenced, info strings, and containment

### A15.1 Formal definition

CommonMark defines two code block forms:

1. **Indented code blocks:** initiated by 4+ spaces indentation (subject to container context).
2. **Fenced code blocks:** initiated by a fence of backticks (```) or tildes (~~~) of sufficient length; terminated by a matching fence.

Code blocks are leaf blocks whose content is treated as literal text (no inline parsing).

### A15.2 Why the concept exists

- Code must be representable without escaping every punctuation character.
- Indented code supports simple examples; fenced code supports explicit language annotation and is more robust inside lists.

### A15.3 Design motivation and history

- Fenced code blocks were not in original Markdown but became ubiquitous; CommonMark includes them.
- GFM popularized “info strings” (language identifiers) and consistent highlighting hooks.

### A15.4 Internal mechanics

Indented code block mechanics:

- Begins when a line is indented by 4+ spaces and not otherwise parsed as a list continuation or other container-induced indentation.
- Continues as long as subsequent lines are similarly indented (blank lines may be included).

Fenced code block mechanics:

- Opening fence: at line start (allowing up to 3 leading spaces), a run of ≥3 backticks or ≥3 tildes.
- Optional **info string** follows on the opening line (for backtick fences, the info string cannot contain backticks).
- Closing fence: same fence character (backtick or tilde) with length ≥ opening fence length (and optional trailing spaces).

### A15.5 Examples

#### A15.5.1 Fenced code block (canonical)

Markdown:

````markdown
```python
print("hello")
```
````

Expected HTML (conceptual):

```html
<pre><code class="language-python">print("hello")
</code></pre>
```

Line-by-line explanation:

- Opening fence begins a fenced code block.
- `python` is an info string; renderers may map it to a language class.
- Closing fence terminates the block.

#### A15.5.2 Incorrect example: mismatched closing fence length

Markdown:

````markdown
````
code
```
````

Explanation:

- An opening fence of length 4 requires a closing fence of length ≥4.
- With a shorter closing fence, the code block may run until end of document (dialect-specific but CommonMark is explicit).

#### A15.5.3 Edge case: backticks inside backtick-fenced code

Markdown:

````markdown
```text
Here is a fence: ```
```
````

Explanation:

- If the opening fence uses backticks, the code content may include backticks safely, but the *closing* fence must be recognized at line start with sufficient length.
- If you need to include a line that could be mistaken for the closing fence, use a longer opening fence.

Performance note:

- Fenced code blocks are typically efficient to parse; the major risk is scanning for a closing fence. Good implementations check line starts rather than searching every character.

---

## A16 — Lists: markers, indentation, tight/loose, and ambiguity resolution

### A16.1 Formal definition

A **list** is a container block consisting of one or more **list items**.

CommonMark supports:

- **Bullet lists:** markers `-`, `+`, `*`.
- **Ordered lists:** numeric markers like `1.` or `1)` (CommonMark specifics depend on exact marker rules).

Each list item may contain blocks (paragraphs, sublists, code blocks, etc.).

### A16.2 Why the concept exists

- Lists are a fundamental document structure for procedures, enumerations, and outlines.

### A16.3 Design motivation and history

List parsing is historically the most divergent aspect of Markdown. CommonMark defines detailed indentation rules to make list parsing deterministic.

### A16.4 Theoretical model

Lists are container blocks whose continuation depends on:

- whether a new line matches a list marker at the appropriate indentation,
- whether the line is a continuation line for the current item (indentation-based),
- and whether blank lines make a list “loose” (affecting output structure).

### A16.5 Internal mechanics

Key mechanics:

- Up to 3 leading spaces allowed before a list marker.
- After the marker, indentation rules determine the content start column.
- A list can be **tight** (no `<p>` wrappers around item paragraphs) or **loose** (paragraphs wrapped), determined by blank lines and block structure inside items.

Common ambiguity:

- `-` can start a list item or be literal.
- Indented code can be interpreted as a code block or as part of list indentation.
- “Lazy continuation” also exists in list items for paragraphs.

### A16.6 Examples

#### A16.6.1 Bullet list (canonical)

Markdown:

```markdown
- item 1
- item 2
```

Expected HTML (conceptual):

```html
<ul>
<li>item 1</li>
<li>item 2</li>
</ul>
```

#### A16.6.2 Ordered list start number semantics

Markdown:

```markdown
3. item
4. item
```

Explanation:

- CommonMark typically preserves the displayed order as an ordered list; the initial number may or may not be preserved in rendered HTML depending on renderer (HTML `<ol>` can have a `start` attribute; not all renderers emit it).

#### A16.6.3 Tight vs loose list (edge behavior)

Markdown (tight):

```markdown
- item 1
- item 2
```

Markdown (loose):

```markdown
- item 1

- item 2
```

Explanation:

- The blank line between items typically makes the list loose, changing paragraph wrapping in HTML.

#### A16.6.4 Common pitfall: list followed by indented code

Markdown:

```markdown
- item
    code?
```

Explanation:

- The interpretation depends on list indentation rules; in many CommonMark cases, the indented line becomes a code block *within the list item*.
- Many writers mistakenly expect it to be code outside the list.

Performance and complexity note:

- List parsing can be implementation-complex, but runtime is typically linear in input size for well-implemented algorithms.

---

## A17 — Code spans (inline code): backtick runs, trimming, and delimiter selection

### A17.1 Formal definition

A **code span** is an inline construct delimited by one or more backticks.

Let the opening delimiter be a run of $n \ge 1$ consecutive backticks. The closing delimiter must be a run of exactly $n$ consecutive backticks.

The content between the opening and closing delimiters becomes literal text (no emphasis parsing, no link parsing, no entity parsing as markup). It is rendered as inline code (typically `<code>…</code>` in HTML).

CommonMark specifies additional normalization:

- If the code span content begins and ends with a space, and contains at least one non-space character, then one leading and one trailing space are removed.
- Newlines within code spans are parsed as spaces.

### A17.2 Why the concept exists

- Writers need a way to include punctuation-heavy text without escaping.
- Inline code must be robust in prose and within list items/headings.

### A17.3 Historical/design motivation

- Backticks were used in original Markdown.
- CommonMark standardizes tricky cases: choosing delimiter length and handling backticks inside code.

### A17.4 Theoretical model

Code span parsing requires choosing delimiter runs before (or at least alongside) emphasis parsing because backticks are also punctuation used in many texts.

### A17.5 Internal mechanics

Key mechanics:

1. Scan for an opening backtick run; record its run length $n$.
2. Search forward for the next backtick run of length exactly $n$; that run closes.
3. The intervening content becomes code span content with normalization.

Practical consequence:

- If code contains a backtick, you can still represent it by choosing a longer delimiter.

### A17.6 Interactions with other constructs

- Code spans suppress inline parsing within their content (including emphasis, links, and raw HTML).
- Code spans can appear inside headings and link text, subject to nesting constraints.

### A17.7 Examples

#### A17.7.1 Minimal working example

Markdown:

```markdown
Use `git status` to inspect changes.
```

Expected HTML (conceptual):

```html
<p>Use <code>git status</code> to inspect changes.</p>
```

Line-by-line explanation:

- Backtick pairs delimit the code span.
- Inside the code span, spaces and punctuation are literal.

#### A17.7.2 Edge case: code containing backticks

Markdown:

```markdown
To show a backtick: `` ` ``.
```

Expected HTML (conceptual):

```html
<p>To show a backtick: <code>`</code>.</p>
```

Explanation:

- The outer delimiter uses two backticks, allowing a literal single backtick inside.

#### A17.7.3 Edge case: trimming a single leading/trailing space

Markdown:

```markdown
Here is code: ` a `.
```

Expected HTML (conceptual):

```html
<p>Here is code: <code>a</code>.</p>
```

Explanation:

- CommonMark removes one leading and one trailing space when both exist and the content is not all spaces.

Incorrect example (common misconception):

```markdown
`a
b`
```

Explanation:

- Newlines inside code spans are not preserved as literal newlines; they are typically turned into spaces.

Performance note:

- Implementations must avoid repeated rescans for closing delimiters in long documents; a linear scan with indexed delimiter runs is typical.

---

## A18 — Links and images: inline form, reference form, destinations, titles, and nesting constraints

### A18.1 Formal definition

CommonMark defines links and images as inline constructs.

- A **link** produces a node with link text and a destination URL (and optional title).
- An **image** is syntactically similar but begins with `!` and produces an image node (alt text + destination + optional title).

There are two broad forms:

1. **Inline links/images**: destination appears directly after link text.
2. **Reference links/images**: destination is looked up by label from a link reference definition.

The typical surface syntaxes include:

- Inline link: `[text](destination "title")`
- Reference link: `[text][label]` (and collapsed/shortcut forms)
- Inline image: `![alt](destination "title")`
- Reference image: `![alt][label]`

### A18.2 Why the concept exists

- Hyperlinks are central to documentation.
- Reference links improve readability and enable URL reuse.

### A18.3 Historical/design motivation

Reference links were core to original Markdown.
CommonMark standardizes:

- label normalization,
- allowed destination syntax (including angle-bracketed destinations),
- title parsing rules,
- and how nested brackets are interpreted.

### A18.4 Theoretical model

Link parsing is context-sensitive because it interacts with:

- bracket nesting,
- parentheses in destinations,
- backslash escaping,
- inline code,
- and emphasis parsing within link text.

### A18.5 Internal mechanics

Important mechanics to internalize:

1. **Link text** is parsed from `[` … `]` with bracket nesting rules.
2. After `]`, the parser decides among:
  - inline destination `( … )`,
  - reference label `[ … ]`,
  - shortcut/collapsed reference forms.
3. **Destination parsing** must handle:
  - angle-bracketed destinations: `(<https://example.com>)` style,
  - balanced parentheses (for non-angle destinations),
  - backslash escapes.
4. **Title parsing** is optional and may be delimited by `"…"`, `'…'`, or `(…)` in CommonMark rules.

Nesting constraint (CommonMark):

- Links cannot contain other links as descendants. This affects how nested `[` … `]` sequences are interpreted.

### A18.6 Failure modes

- Unbalanced brackets → no link; literal text.
- Destination contains unmatched parentheses → link may terminate early or be rejected.
- Reference label not found → reference link fails and becomes literal.
- Unsafe URL schemes (e.g., `javascript:`) are a security risk if not filtered during rendering/sanitization.

### A18.7 Examples

#### A18.7.1 Inline link (minimal)

Markdown:

```markdown
See [CommonMark](https://commonmark.org/).
```

Expected HTML (conceptual):

```html
<p>See <a href="https://commonmark.org/">CommonMark</a>.</p>
```

Line-by-line explanation:

- `[CommonMark]` is link text (inline parsing applies inside it).
- `(https://commonmark.org/)` is destination.

#### A18.7.2 Inline link with title

Markdown:

```markdown
See [Spec](https://commonmark.org "CommonMark spec").
```

Expected HTML (conceptual):

```html
<p>See <a href="https://commonmark.org" title="CommonMark spec">Spec</a>.</p>
```

#### A18.7.3 Angle-bracketed destination

Markdown:

```markdown
[Example](<https://example.com/a b>)
```

Explanation:

- Angle brackets allow spaces in destinations under the spec’s rules (the actual URL encoding behavior is renderer-dependent).

#### A18.7.4 Reference link (canonical)

Markdown:

```markdown
Use [the spec][cm].

[cm]: https://spec.commonmark.org/ "CommonMark"
```

Expected HTML (conceptual):

```html
<p>Use <a href="https://spec.commonmark.org/" title="CommonMark">the spec</a>.</p>
```

Failure mode example (unresolved reference):

```markdown
Use [the spec][missing].
```

Explanation:

- Without a matching definition, CommonMark does not fabricate a URL; it renders the brackets literally.

#### A18.7.5 Image (minimal)

Markdown:

```markdown
![Alt text](https://example.com/image.png "Title")
```

Expected HTML (conceptual):

```html
<p><img src="https://example.com/image.png" alt="Alt text" title="Title" /></p>
```

Security note:

- Image destinations can be used for tracking or to exfiltrate data via referrers; documentation systems may need CSP/referrer policy.

---

## A19 — Autolinks (angle form) and email autolinks

### A19.1 Formal definition

CommonMark recognizes **autolinks** in the form:

- URI autolink: `<https://example.com>`
- Email autolink: `<user@example.com>`

These are distinct from GFM “autolink literals” (bare URLs without angle brackets), which are an extension and are covered later.

### A19.2 Why the concept exists

- Provides a minimal, unambiguous way to write links without bracket/parenthesis syntax.

### A19.3 Internal mechanics

- The `<` … `>` sequence must match the URI/email patterns defined by the spec.
- If it does not match, it is treated as raw HTML (or literal text) depending on context.

### A19.4 Examples

#### A19.4.1 URI autolink

Markdown:

```markdown
<https://example.com>
```

Expected HTML (conceptual):

```html
<p><a href="https://example.com">https://example.com</a></p>
```

#### A19.4.2 Email autolink

Markdown:

```markdown
<me@example.com>
```

Expected HTML (conceptual):

```html
<p><a href="mailto:me@example.com">me@example.com</a></p>
```

Incorrect example:

```markdown
<not a link>
```

Explanation:

- If it does not match autolink or HTML tag rules, it will not become a link.

---

## A20 — Emphasis and strong emphasis: delimiter run classification and pairing algorithm

### A20.1 Formal definition

CommonMark defines emphasis constructs:

- *Emphasis* using `*` or `_` delimiters.
- **Strong emphasis** using `**` or `__` delimiters.

The semantics are defined by:

1. Classification of delimiter runs as potentially opening, potentially closing, or both.
2. A deterministic pairing algorithm that resolves nesting and adjacency.

### A20.2 Why the concept exists

- Emphasis is essential for prose.
- The pairing rules are the primary mechanism to prevent pathological or surprising parses.

### A20.3 Historical/design motivation

Emphasis parsing is the most notorious source of Markdown divergence.
CommonMark’s delimiter-run algorithm exists to replace inconsistent ad-hoc heuristics with a well-defined, testable procedure.

### A20.4 Theoretical model

The grammar is context-sensitive:

- Whether a delimiter can open/close depends on character categories around it.
- `_` has intraword restrictions that `*` does not, to avoid italicizing identifiers.

This makes emphasis parsing unsuitable for naive regular expressions.

### A20.5 Internal mechanics (conceptual but precise)

CommonMark defines the notions of:

- **left-flanking delimiter run** and **right-flanking delimiter run**
- “punctuation”, “whitespace”, and “alphanumeric” character classes

Determining if a delimiter run can open/close:

- A run is *left-flanking* if it is not followed by whitespace and is not followed by punctuation unless preceded by whitespace or punctuation.
- A run is *right-flanking* if it is not preceded by whitespace and is not preceded by punctuation unless followed by whitespace or punctuation.

For `*`:

- Can open if left-flanking.
- Can close if right-flanking.

For `_`:

- Additional rules restrict opening/closing inside words (intraword emphasis suppression).

Pairing:

- The parser uses a delimiter stack.
- When a closer is found, it searches backward for a compatible opener with rules about matching counts and avoidance of certain ambiguous pairings.

### A20.6 Examples

#### A20.6.1 Canonical nested emphasis

Markdown:

```markdown
***strong and em***
```

Expected HTML (one legal CommonMark parse, conceptual):

```html
<p><strong><em>strong and em</em></strong></p>
```

Explanation:

- The three asterisks are partitioned into `**` + `*` for opening and `*` + `**` for closing under the pairing rules.

#### A20.6.2 Underscore intraword suppression

Markdown:

```markdown
an_identifier_with_underscores
```

Expected behavior:

- Typically no emphasis is produced (underscores inside words are conservative).

#### A20.6.3 Incorrect example: assuming symmetric behavior for `*` and `_`

Markdown:

```markdown
foo_bar_ baz
```

Explanation:

- The space boundary changes flanking classification; `_` behavior can change dramatically with adjacent whitespace/punctuation.

Performance-sensitive example (pathological delimiters):

```markdown
*****************************************************************
```

Explanation:

- Long delimiter sequences can be adversarial to naive backtracking implementations.
- CommonMark’s algorithm is designed to avoid exponential behavior, but poor implementations still exist.

---

## A21 — Backslash escapes: escapable punctuation set and ambiguity control

### A21.1 Formal definition

In CommonMark, a backslash (`\`) can escape a defined set of punctuation characters, preventing them from being interpreted as Markdown syntax.

The escapable set is (ASCII punctuation):

```
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

Additionally, a backslash at end of line produces a hard line break.

### A21.2 Why the concept exists

- Writers must be able to write literal characters that otherwise introduce syntax.

### A21.3 Internal mechanics

- Escape applies at inline parsing time.
- Escapes are not universal; escaping a non-escapable character may leave the backslash literal.

### A21.4 Examples

#### A21.4.1 Escaping a literal asterisk

Markdown:

```markdown
\* literal asterisk, not emphasis
```

Expected HTML (conceptual):

```html
<p>* literal asterisk, not emphasis</p>
```

#### A21.4.2 Escaping backticks inside prose

Markdown:

```markdown
Use \`backticks\` literally.
```

Explanation:

- Escapes prevent backticks from starting code spans.

Incorrect example:

```markdown
\a
```

Explanation:

- `a` is not escapable punctuation; the backslash may remain literal.

---

## A22 — Inline HTML and entity/character references: parsing boundaries and safety

### A22.1 Formal definition

Markdown commonly supports:

- **Inline HTML**: HTML tags embedded within inline text (e.g., `<span>text</span>`).
- **Entity and character references**: sequences like `&amp;`, `&#35;`, `&#x1F600;`.

CommonMark specifies how these are recognized as inline constructs.

### A22.2 Why the concept exists

- Inline HTML is an escape hatch for formatting not represented in Markdown.
- Entities allow explicit characters and HTML compatibility.

### A22.3 Internal mechanics

- If a `<...>` sequence matches an HTML tag pattern, it may be treated as inline HTML.
- If `&...;` matches entity/character reference grammar, it may be treated as a single character in output.

### A22.4 Security model

Inline HTML is a primary XSS vector.

Key principle:

- **Parsing correctness is not output safety.** A spec-compliant Markdown parser can still produce dangerous HTML.

### A22.5 Examples

#### A22.5.1 Inline HTML preserved

Markdown:

```markdown
Hello <span>world</span>.
```

Expected HTML (conceptual):

```html
<p>Hello <span>world</span>.</p>
```

#### A22.5.2 Entity reference

Markdown:

```markdown
AT&amp;T
```

Expected HTML (conceptual):

```html
<p>AT&amp;T</p>
```

Explanation:

- Some renderers preserve the entity; some decode then re-encode. The visible result is typically `AT&T`.

Security-relevant example: attribute-based execution risk

```markdown
<img src=x onerror=alert(1)>
```

Explanation:

- If inline HTML is permitted and unsanitized, event handlers can execute.

---

## A23 — Link reference definitions: block-level syntax, normalization, and resolution semantics

### A23.1 Formal definition

A **link reference definition** is a block-level construct that defines a mapping from a label to a destination and optional title.

Syntactic form (conceptual):

```text
[label]: destination "optional title"
```

CommonMark specifies:

- how labels are normalized,
- which destinations/titles are valid,
- and that definitions do not produce visible output nodes (they are metadata for link resolution).

### A23.2 Why the concept exists

- Improves readability of prose.
- Enables reuse of URLs and centralizes changes.

### A23.3 Internal mechanics

- Definitions are collected during parsing (often during block parsing or in a combined block+inline phase).
- A later reference link lookup consults the definition map.
- Duplicate labels: CommonMark defines deterministic resolution behavior.

### A23.4 Examples

#### A23.4.1 Canonical definition + use

Markdown:

```markdown
See [CommonMark][cm].

[cm]: https://spec.commonmark.org/ "CommonMark Spec"
```

Expected HTML (conceptual):

```html
<p>See <a href="https://spec.commonmark.org/" title="CommonMark Spec">CommonMark</a>.</p>
```

#### A23.4.2 Edge case: definitions inside containers

Markdown:

```markdown
> [cm]: https://spec.commonmark.org/
>
> Use [cm][cm].
```

Explanation:

- Definitions can be placed inside block quotes and lists; whether they are visible depends on syntax validity.
- The key is that definitions are still document-scoped for reference resolution in CommonMark.

Pitfall:

- Some dialects treat definition scope differently; portability requires testing.

---

## A24 — HTML blocks (CommonMark): block types, termination rules, and interactions

### A24.1 Formal definition

CommonMark defines **HTML blocks** as leaf blocks recognized by specific line-start patterns.

Crucially, CommonMark distinguishes multiple HTML block *types* with different termination rules (some end at a blank line; others end at a matching closing tag or specific delimiter conditions).

Within an HTML block, Markdown parsing is typically suppressed (content treated as raw HTML/text according to the spec’s rules).

### A24.2 Why the concept exists

- Enables embedding arbitrary HTML structures that Markdown cannot represent.
- Preserves compatibility with historical Markdown behavior.

### A24.3 Internal mechanics (high-level)

The parser decides at line start whether an HTML block begins.

Important consequences:

- HTML block recognition can prevent Markdown lists/paragraphs from forming where writers expect them.
- HTML blocks can “eat” text until their termination condition, which is frequently a blank line for some types.

### A24.4 Examples

#### A24.4.1 HTML block that suppresses Markdown parsing

Markdown:

```markdown
<div>
*not emphasis*
</div>
```

Explanation:

- Depending on the HTML block type recognized, the `*not emphasis*` may remain literal and not be parsed as emphasis.
- This is one of the most common sources of “why didn’t my Markdown render?” confusion.

#### A24.4.2 Termination-by-blank-line pattern (edge behavior)

Markdown:

```markdown
<div>
inside

outside
```

Explanation:

- For HTML block types that terminate on a blank line, the blank line ends the HTML block, and `outside` begins normal Markdown again.

Security note:

- HTML blocks carry the same XSS risks as inline HTML and are frequently more dangerous because they allow complex tag structures.

---

# Part B — Complete Technical Reference

> This section is intentionally expanded construct-by-construct (CommonMark core first, then GFM extensions), with formal specification-style entries.

## B0 — Reference conventions (normative baseline, terminology, and outputs)

### B0.1 Baseline and conformance targets

This reference specifies behavior with a two-layer baseline:

1. **CommonMark**: normative core Markdown behavior.
2. **GFM**: normative extension layer that modifies/adds constructs.

Where behavior differs across dialects (including historical “Markdown”), it is explicitly called out as *non-portable*.

### B0.2 “Construct reference” template (how to read each entry)

For each construct, this reference provides:

- **Name**
- **Formal specification** (what the spec defines; where it is underspecified this is stated)
- **Purpose**
- **Syntax**
- **Semantics** (what AST nodes are produced; how rendering behaves)
- **Inputs** (line/character-level constraints)
- **Outputs** (node type + key fields)
- **Side effects** (global reference map updates, state changes)
- **Failure modes** (fallback behavior)
- **Invariants** (properties that must hold after parsing)
- **Version/dialect behavior** (CommonMark vs GFM vs others)
- **Performance implications**
- **Concurrency/threading behavior** (for renderers/libraries)

### B0.3 Abstract syntax tree (AST) model used in this manual

CommonMark does not mandate a public AST API; it mandates behavior through parsing rules and rendered output.
For pedagogical precision, this manual describes constructs as producing nodes in an abstract tree with these typical node families:

- **Block nodes**: `Document`, `Paragraph`, `Heading(level)`, `ThematicBreak`, `BlockQuote`, `List(type, tight, start)`, `ListItem`, `CodeBlock(kind, infoString, literal)`, `HTMLBlock(kind, literal)`.
- **Inline nodes**: `Text`, `SoftBreak`, `HardBreak`, `Emphasis`, `Strong`, `CodeSpan(literal)`, `Link(textChildren, destination, title)`, `Image(altChildren, destination, title)`, `Autolink(kind, destination)`, `HTMLInline(literal)`, `EntityOrCharRef(value)`.
- **Metadata**: `LinkReferenceDefinition(labelNorm, destination, title)` (not rendered as output).

This model is intentionally close to the node sets used by many real implementations, but the *normative truth* remains the CommonMark and GFM specs.

---

## B1 — CommonMark block constructs (complete reference)

### B1.1 Paragraph

#### B1.1.1 Name

Paragraph

#### B1.1.2 Formal specification

A paragraph is the default leaf block consisting of one or more consecutive non-blank lines of text that are not recognized as another block construct. Inline parsing is enabled within paragraph content.

#### B1.1.3 Purpose

Represent prose as the default block type.

#### B1.1.4 Syntax

- Starts at any line not matching a higher-precedence block-start pattern.
- Continues until a blank line or until interrupted by a block that can start at the next line (heading, list, thematic break, HTML block, etc.), subject to container context.

#### B1.1.5 Semantics

- Produces `Paragraph(children=inlineNodes)`.
- Newlines within the paragraph become `SoftBreak` inline nodes unless converted to `HardBreak` by explicit syntax.

#### B1.1.6 Inputs

- Lines of text in a context where a paragraph is permitted (not inside a code block).

#### B1.1.7 Outputs

- Node: `Paragraph`.
- Inline children: output of inline parsing phase.

#### B1.1.8 Side effects

- None directly; however, lines that match link reference definition syntax may be extracted as definitions rather than paragraph text.

#### B1.1.9 Failure modes

- If a line matches a different block-start rule, a paragraph does not form.
- If inline parsing fails to recognize a construct, it emits literal `Text` instead.

#### B1.1.10 Invariants

- A paragraph node contains only inline nodes.
- Inline parsing is not applied to code blocks; paragraphs never contain raw unparsed Markdown.

#### B1.1.11 Version/dialect behavior

- CommonMark specifies exact interruption precedence and link reference definition extraction.
- Many historical Markdown dialects treat single newlines as hard breaks or ignore them; CommonMark standardizes soft breaks.

#### B1.1.12 Performance implications

- Block detection is linear in number of lines.
- Inline parsing cost can dominate for large paragraphs with many delimiter characters.

#### B1.1.13 Concurrency/threading behavior

- Markdown parsing is typically pure and thread-safe when implemented without global mutable state.
- Renderers that maintain a shared reference-definition map across documents are not thread-safe unless the map is per-parse.

#### B1.1.14 Examples

Minimal:

```markdown
This is a paragraph.
```

Incorrect-intent (interrupted by heading):

```markdown
This is not a paragraph line
# because the next line starts a heading
```

---

### B1.2 Headings

#### B1.2.1 Name

Heading (ATX and Setext)

#### B1.2.2 Formal specification

CommonMark supports:

- **ATX headings**: `#` run of length 1–6 at line start (with up to 3 leading spaces), followed by content.
- **Setext headings**: a paragraph followed by a line of `=` (level 1) or `-` (level 2).

Heading content is inline-parsed.

#### B1.2.3 Purpose

Represent document outline structure.

#### B1.2.4 Syntax

ATX:

```text
### heading text ###
```

Setext:

```text
heading text
-----------
```

#### B1.2.5 Semantics

- Produces `Heading(level, children=inlineNodes)`.
- Trailing ATX closing `#` run may be stripped under CommonMark’s rules.

#### B1.2.6 Inputs

- ATX headings: require a space or end-of-line after the opening `#` run.
- Setext headings: require an underline line consisting only of `=` or `-` (plus spaces).

#### B1.2.7 Outputs

- Node: `Heading(level)`.

#### B1.2.8 Side effects

- None.

#### B1.2.9 Failure modes

- `##Title` is not an ATX heading in CommonMark; it becomes paragraph text.
- Setext underline lines may be interpreted as thematic breaks in other dialects; CommonMark specifies precedence rules.

#### B1.2.10 Invariants

- Heading levels are in 1–6 for ATX, 1–2 for Setext.

#### B1.2.11 Version/dialect behavior

- Some dialects accept ATX headings without a following space; CommonMark does not.

#### B1.2.12 Performance implications

- Heading recognition is constant-time per line; inline parsing cost dominates.

#### B1.2.13 Examples

Canonical ATX:

```markdown
## Title
```

Canonical Setext:

```markdown
Title
-----
```

---

### B1.3 Thematic break

#### B1.3.1 Name

Thematic break

#### B1.3.2 Formal specification

A thematic break is a line consisting of at least three `-` or `*` or `_` characters, possibly separated by spaces, with no other content (up to 3 leading spaces allowed).

#### B1.3.3 Purpose

Represent a topic/scene transition.

#### B1.3.4 Syntax

```markdown
---
* * *
___
```

#### B1.3.5 Semantics

- Produces a `ThematicBreak` block node.

#### B1.3.6 Failure modes

- Fewer than 3 markers → not a thematic break.
- Mixed markers (e.g., `-_*`) → not a thematic break.

#### B1.3.7 Performance

- Constant-time per candidate line.

---

### B1.4 Block quote

#### B1.4.1 Name

Block quote

#### B1.4.2 Formal specification

A block quote is a container block introduced by `>` at line start (with up to 3 leading spaces), optionally followed by a single space. It contains blocks.

Lazy continuation rules allow certain paragraph lines to continue the quote without repeating `>`.

#### B1.4.3 Purpose

Represent quoted content and nested quoted structures.

#### B1.4.4 Syntax

```markdown
> quoted
> content
```

#### B1.4.5 Semantics

- Produces `BlockQuote(children=blockNodes)`.

#### B1.4.6 Failure modes

- Missing `>` does not necessarily terminate a quote if lazy continuation applies; writers often mispredict scope.

#### B1.4.7 Version/dialect behavior

- Lazy continuation behavior differs across historical implementations; CommonMark defines it precisely.

---

### B1.5 Lists and list items

#### B1.5.1 Name

List, List item

#### B1.5.2 Formal specification

CommonMark defines:

- **Bullet lists** with markers `-`, `+`, `*`.
- **Ordered lists** with numeric markers of the forms specified by CommonMark.

Lists are container blocks composed of list item container blocks.

The spec defines indentation rules that determine:

- when a list begins,
- where list item content begins,
- when a sublist forms,
- when indented code is code vs list continuation,
- and whether the list is tight or loose.

#### B1.5.3 Purpose

Represent structured enumerations and outlines.

#### B1.5.4 Syntax

Bullet:

```markdown
- item
```

Ordered:

```markdown
1. item
```

#### B1.5.5 Semantics

- Produces `List(type, tight, start)` containing `ListItem` nodes.
- Tightness affects HTML rendering (whether item paragraphs are wrapped in `<p>`).

#### B1.5.6 Inputs

- Marker recognition depends on indentation and marker syntax.
- Item content indentation is computed relative to marker width and following spaces.

#### B1.5.7 Side effects

- None.

#### B1.5.8 Failure modes

- Writers frequently misindent, causing:
  - code blocks to appear inside list items unexpectedly,
  - sublists to fail to form,
  - or list termination to occur early.

#### B1.5.9 Performance implications

- Correct list parsing is algorithmically intricate but typically linear-time for well-designed implementations.

---

### B1.6 Code blocks (indented and fenced)

#### B1.6.1 Name

Code block

#### B1.6.2 Formal specification

CommonMark supports:

- **Indented code blocks**: begun by 4+ spaces indentation.
- **Fenced code blocks**: begun by a backtick or tilde fence (length ≥ 3), closed by a matching fence.

Code blocks do not undergo inline parsing.

#### B1.6.3 Purpose

Represent literal preformatted code/text.

#### B1.6.4 Syntax

Indented:

```markdown
    code
```

Fenced:

````text
```lang
code
```
````

#### B1.6.5 Semantics

- Produces `CodeBlock(kind=indented|fenced, infoString?, literal)`.
- For fenced blocks, the info string is captured (CommonMark defines its extraction constraints).

#### B1.6.6 Failure modes

- Mismatched fence length → unclosed block that runs to end-of-document.
- Backtick fences: info string cannot contain backticks.

#### B1.6.7 Performance

- Typically linear: scan line starts for closing fence.

---

### B1.7 HTML blocks

#### B1.7.1 Name

HTML block

#### B1.7.2 Formal specification

CommonMark defines multiple HTML block types with distinct start patterns and termination conditions.

Within an HTML block, Markdown parsing is suppressed per spec rules.

#### B1.7.3 Purpose

Allow embedding of raw HTML.

#### B1.7.4 Semantics

- Produces `HTMLBlock(kind, literal)`.

#### B1.7.5 Failure modes

- HTML block recognition can unexpectedly prevent list/paragraph formation.

#### B1.7.6 Security

- HTML blocks are high-risk in browser-rendered contexts; require sanitization or HTML disabling.

---

### B1.8 Link reference definitions (block-level metadata)

#### B1.8.1 Name

Link reference definition

#### B1.8.2 Formal specification

A link reference definition binds a normalized label to a destination and optional title.
Definitions are block-level constructs that do not produce visible output.

#### B1.8.3 Purpose

Enable reference links/images.

#### B1.8.4 Side effects

- Updates the document’s reference-definition map.

#### B1.8.5 Failure modes

- Malformed definitions are treated as paragraph text.

---

## B2 — CommonMark inline constructs (initial reference; expansion continues)

> Note: This section is written as a language reference. It intentionally repeats “basic” rules explicitly.

### B2.1 Code span

#### B2.1.1 Name

Code span

#### B2.1.2 Formal specification

A code span is delimited by a run of one or more backticks. The closing delimiter must be a run of the same length.

Within code spans:

- Markdown inline parsing is disabled.
- Newlines are normalized to spaces.
- A single leading and trailing space is trimmed if (and only if) both exist and the content is not all spaces.

#### B2.1.3 Purpose

Represent literal inline code or literal punctuation-rich text.

#### B2.1.4 Syntax

- `` `code` ``
- `` ``code with ` inside`` ``

#### B2.1.5 Semantics

- Produces `CodeSpan(literal)`.
- Rendering typically emits `<code>literal</code>` with HTML-escaping applied to the literal.

#### B2.1.6 Inputs

- Opening delimiter run length $n \ge 1$.
- Closing delimiter run length must be exactly $n$.

#### B2.1.7 Outputs

- Node: `CodeSpan(literal)`.

#### B2.1.8 Side effects

- None.

#### B2.1.9 Failure modes

- Missing closing delimiter: the opening backticks are treated as literal text; no code span node is produced.

#### B2.1.10 Invariants

- No inline nodes are parsed within a code span.

#### B2.1.11 Version/dialect behavior

- Most dialects support code spans, but trimming behavior and newline normalization have historically varied. CommonMark is normative here.

#### B2.1.12 Performance implications

- Efficient implementations index backtick runs; naive scanning on every backtick can degrade performance.

#### B2.1.13 Examples

Minimal:

```markdown
Use `x = 1`.
```

Edge case (delimiter choice):

```markdown
`` ` ``
```

---

### B2.2 Soft break and hard break

#### B2.2.1 Name

Soft break, Hard break

#### B2.2.2 Formal specification

Within paragraphs and other inline-capable blocks, a newline is normally a **soft break**.

A newline becomes a **hard break** if preceded by either:

- two or more spaces at end of line, or
- a backslash at end of line.

#### B2.2.3 Purpose

- Soft breaks allow source wrapping without changing semantics.
- Hard breaks allow explicit line breaks for addresses/poetry.

#### B2.2.4 Semantics

- Soft break emits `SoftBreak` inline node.
- Hard break emits `HardBreak` inline node.
- Rendering: hard break typically becomes `<br />`.

#### B2.2.5 Failure modes

- Trailing whitespace trimming by editors can unintentionally remove the hard-break trigger.

#### B2.2.6 Examples

Hard break (two spaces):

```markdown
line 1  
line 2
```

Hard break (backslash):

```markdown
line 1\\
line 2
```

---

### B2.3 Backslash escapes

#### B2.3.1 Name

Backslash escape

#### B2.3.2 Formal specification

Backslash escapes apply to a defined set of ASCII punctuation characters; escaping prevents those characters from being interpreted as Markdown syntax.

#### B2.3.3 Syntax

```markdown
\* \_ \[ \] \( \) \#
```

#### B2.3.4 Semantics

- Produces literal character output as `Text`.
- The backslash itself is not included.

#### B2.3.5 Failure modes

- Escaping a non-escapable character may leave the backslash literal.

---

### B2.4 Emphasis and strong emphasis

#### B2.4.1 Name

Emphasis, Strong

#### B2.4.2 Formal specification

Emphasis and strong are defined by delimiter-run classification and a deterministic pairing algorithm.

Key normative ideas:

- delimiter runs are classified by flanking rules (left/right-flanking),
- `_` has additional intraword restrictions,
- pairing is stack-based and deterministic.

#### B2.4.3 Purpose

Provide typographic emphasis in prose.

#### B2.4.4 Syntax

- `*em*`, `_em_`
- `**strong**`, `__strong__`
- combinations such as `***both***` (with deterministic parsing)

#### B2.4.5 Semantics

- Produces `Emphasis(children)` and `Strong(children)` nodes.
- Inline parsing applies recursively to children.

#### B2.4.6 Failure modes

- Many inputs that “look like emphasis” are not, due to flanking restrictions.
- Implementations that use regex heuristics often diverge from CommonMark.

#### B2.4.7 Performance implications

- Delimiter stack processing is designed to be efficient; naive backtracking can become quadratic.

---

### B2.5 Links

#### B2.5.1 Name

Link

#### B2.5.2 Formal specification

Links may be inline or reference forms.

- Inline: `[text](destination "title")`
- Reference: `[text][label]`, `[text][]`, `[text]` (shortcut)

The spec defines:

- bracket parsing for link text,
- destination parsing (including angle-bracketed destinations),
- title parsing (optional),
- reference label normalization and lookup,
- prohibition on nested links.

#### B2.5.3 Purpose

Represent hyperlinks.

#### B2.5.4 Semantics

- Produces `Link(textChildren, destination, title)`.
- Link text children are inline-parsed.

#### B2.5.5 Side effects

- Reference links consult the reference-definition map built from link reference definitions.

#### B2.5.6 Failure modes

- Unbalanced delimiters → literal text.
- Invalid destination/title syntax → link parse rejected.
- Unresolved reference → literal bracketed text.

#### B2.5.7 Security implications

- Renderers must enforce a URL policy. Without filtering/sanitization, `javascript:` (and other dangerous schemes) can produce XSS.

---

### B2.6 Images

#### B2.6.1 Name

Image

#### B2.6.2 Formal specification

Images share the same syntax forms as links but are prefixed with `!`.

#### B2.6.3 Semantics

- Produces `Image(altChildren, destination, title)`.

#### B2.6.4 Failure modes

- Same as links: delimiter/destination/title failures cause literal text.

#### B2.6.5 Security implications

- Images can be used for tracking; URL policy and CSP/referrer policy may be relevant.

---

### B2.7 Autolinks (angle form)

#### B2.7.1 Name

Autolink (URI), Autolink (email)

#### B2.7.2 Formal specification

Autolinks are recognized only in angle-bracket form under CommonMark:

- `<https://example.com>`
- `<user@example.com>`

#### B2.7.3 Semantics

- Produces an autolink node or a link node depending on implementation model; rendered as a link.

---

### B2.8 Entity and character references; inline HTML

#### B2.8.1 Name

Entity reference, Character reference, Inline HTML

#### B2.8.2 Formal specification

- Entity references: `&name;`
- Decimal numeric: `&#123;`
- Hex numeric: `&#x1F600;`
- Inline HTML tags are recognized by specific patterns.

#### B2.8.3 Semantics

- Entities/char refs produce literal character output.
- Inline HTML produces an inline HTML node that is emitted verbatim in HTML renderers.

#### B2.8.4 Security implications

- Inline HTML is a direct XSS vector in browser contexts; must be disabled or sanitized.


---

## B3 — GFM extensions (initial reference; expansion continues)

### B3.1 Strikethrough

#### B3.1.1 Name

Strikethrough

#### B3.1.2 Formal specification

GFM extends CommonMark with a strikethrough inline construct delimited by double tildes.

#### B3.1.3 Purpose

Represent deleted/obsolete text in prose and change logs.

#### B3.1.4 Syntax

```markdown
~~text~~
```

#### B3.1.5 Semantics

- Produces a strikethrough inline node (commonly rendered as `<del>text</del>`).
- Inline parsing applies within the delimited content (except where other constructs suppress it).

#### B3.1.6 Failure modes

- Unmatched `~~` delimiters → literal `~` characters.
- Ambiguity with sequences of `~` in code-like text; code spans should be used to force literalness.

#### B3.1.7 Invariants

- Strikethrough nodes do not overlap illegally with link nodes; implementations must preserve CommonMark’s nesting constraints.

#### B3.1.8 Version/dialect behavior

- Not present in CommonMark.
- Present in GFM; other dialects vary.

#### B3.1.9 Performance implications

- Similar to emphasis parsing; delimiter scanning and pairing must avoid pathological backtracking.

#### B3.1.10 Security implications

- Strikethrough itself is not a security risk; it becomes relevant only insofar as it can contain links/HTML in dialects that permit those.

### B3.2 Tables

#### B3.2.1 Name

Table

#### B3.2.2 Formal specification

GFM extends CommonMark with tables parsed from pipe-separated rows.

Tables are not a primitive CommonMark block. In practice, they are recognized in contexts where a paragraph would otherwise form.

The spec defines:

- header row parsing
- separator row parsing (the alignment row)
- body row parsing
- alignment markers with colons

#### B3.2.3 Purpose

Represent tabular data without HTML.

#### B3.2.4 Syntax

Canonical form:

```markdown
| col A | col B |
| ---   | ---:  |
| x     | y     |
```

Alignment markers (conceptual):

- `---` : default alignment
- `:---` : left
- `---:` : right
- `:---:` : center

#### B3.2.5 Semantics

- Produces a table block node with:
  - a header row,
  - optional body rows,
  - per-column alignment metadata.
- Inline parsing applies within cell content.

#### B3.2.6 Inputs

- Requires a header row and a valid separator row.
- Pipes at row edges are often optional; internal pipes delimit cells.
- Escaping rules and code spans influence whether a `|` is treated as a delimiter.

#### B3.2.7 Failure modes

- Invalid separator row → no table; the lines parse as normal paragraphs (and possibly as other constructs).
- Mismatched column counts → behavior can vary; GFM defines specific reconciliation rules.

#### B3.2.8 Invariants

- The separator row determines the number of columns in the table model.

#### B3.2.9 Version/dialect behavior

- Not present in CommonMark.
- Present in GFM.
- Many other dialects implement “tables” with incompatible rules.

#### B3.2.10 Performance implications

- Row splitting is typically linear in row length.
- Inline parsing inside many cells can dominate total runtime.

#### B3.2.11 Security implications

- Tables can contain links and (if permitted) inline HTML; enforce the same URL/HTML security policies as elsewhere.

### B3.3 Task list items

#### B3.3.1 Name

Task list item

#### B3.3.2 Formal specification

GFM extends list items with a task marker of the form:

- `[ ]` unchecked
- `[x]` or `[X]` checked (case handling is specified by GFM)

Task list items are not standalone blocks; they are a specialization of list items.

#### B3.3.3 Purpose

Represent checklists in issues, READMEs, and procedural docs.

#### B3.3.4 Syntax

```markdown
- [ ] todo
- [x] done
```

#### B3.3.5 Semantics

- Produces a list item node with an additional boolean state: `checked`.
- Renderers commonly emit an HTML checkbox input (often disabled) or a semantic marker.

#### B3.3.6 Inputs

- Marker must appear at the beginning of the list item’s content in the position defined by GFM.

#### B3.3.7 Failure modes

- If spacing is wrong or the bracket form is malformed, it remains literal text and no task state is set.

#### B3.3.8 Version/dialect behavior

- Not present in CommonMark.
- Present in GFM.
- Some platforms support task markers but with different requirements (non-portable).

#### B3.3.9 Security implications

- If rendered as `<input>`, ensure it is non-interactive unless intentional; otherwise it can create misleading UI.

### B3.4 Autolink literals

#### B3.4.1 Name

Autolink literal

#### B3.4.2 Formal specification

GFM extends CommonMark by recognizing certain URL/email patterns in plain text and converting them into links without requiring angle brackets.

This is distinct from CommonMark autolinks, which require `<...>`.

#### B3.4.3 Purpose

Increase authoring convenience by linkifying common URL patterns.

#### B3.4.4 Syntax

Examples (conceptual):

```markdown
https://example.com
www.example.com
user@example.com
```

#### B3.4.5 Semantics

- Produces link nodes with destinations derived from the recognized literal.

#### B3.4.6 Failure modes

- Ambiguous trailing punctuation (e.g., `).,]`) may or may not be included; GFM defines trimming rules, but many dialects diverge.

#### B3.4.7 Performance implications

- Implementations typically apply pattern recognition over text segments; naive regex can be expensive on very long lines.

#### B3.4.8 Security implications

- Autolink literals expand the set of strings that become clickable, increasing:
  - phishing/social-engineering risk,
  - accidental linkification,
  - and the need for strict destination URL policies.

- Scheme filtering remains required (`javascript:` must not become a clickable link in safe contexts).

---

# Part C — Structured Learning Path (Self-Study)

> This section is intentionally structured as a mastery curriculum with prerequisites, deep exercises, analytical questions, and mini research tasks.

## C0 — Global prerequisites (explicit; must not be assumed)

Markdown semantics depend on adjacent technical domains. You must learn these first because they directly affect correctness, portability, and safety.

### C0.1 Prerequisites

1. **Unicode and text processing**
  - Code points vs grapheme clusters
  - Normalization (NFC/NFD)
  - Why “character length” is not a stable metric across scripts
2. **Lines and whitespace**
  - LF vs CRLF
  - Trailing whitespace trimming and its semantic consequences
  - Tabs vs spaces and column-based indentation
3. **HTML model**
  - Escaping rules
  - Element/attribute semantics
4. **URL model**
  - Schemes and normalization
  - Percent-encoding
5. **Browser security baseline**
  - XSS
  - Sanitization vs escaping
  - URL scheme filtering

### C0.2 Readiness diagnostics

You should be able to answer precisely:

1. Why can removing trailing spaces change rendered HTML?
2. Why is CommonMark not just a regex grammar?
3. Why can a spec-compliant Markdown renderer still be unsafe?

---

## C1 — Foundations

### C1.1 Learning objectives

By the end of this level, you can:

1. Predict paragraph boundaries and interruptions.
2. Predict headings (ATX/Setext) and thematic breaks.
3. Predict soft vs hard line breaks.
4. Use code spans and code blocks without accidental parsing.

### C1.2 Concepts to master

1. Lines, blank lines, indentation thresholds
2. Paragraphs, headings, thematic breaks
3. Hard break triggers (two spaces, trailing backslash)
4. Code spans and fenced/indented code blocks
5. Backslash escapes (escapable punctuation set)

### C1.3 Prerequisites

- C0 prerequisites

### C1.4 Deep-dive exercises

#### C1.4.1 Block-tree reconstruction

Task:

1. Write a 10-line document containing:
  - one ATX heading,
  - one Setext heading,
  - one thematic break,
  - two paragraphs.
2. Draw the block tree (containers/leaf blocks).
3. Render using one CommonMark renderer and explain every block boundary.

#### C1.4.2 Hard-break whitespace lab

Task:

Create three variants of the same paragraph:

- variant A: no trailing spaces,
- variant B: two trailing spaces,
- variant C: trailing backslash.

For each variant:

1. Predict whether a hard break occurs.
2. Render and compare.
3. Explain why editor whitespace-trimming is a semantic hazard.

#### C1.4.3 Code-span delimiter selection

Task:

Write Markdown that renders the literal inline code content `` ` `` (a single backtick) as code.

Explain:

- why the delimiter must be longer than the content.

### C1.5 Thought experiments

1. If CommonMark allowed headings without a space after `##`, what ambiguous inputs become harder?
2. If code spans allowed “implicit close at end of line,” what new failure modes appear?

---

## C2 — Intermediate

### C2.1 Learning objectives

By the end of this level, you can:

1. Predict list structure including tight vs loose lists.
2. Predict block quote scope including lazy continuation.
3. Use reference links reliably and explain label normalization.
4. Distinguish CommonMark autolinks from GFM autolink literals.

### C2.2 Concepts to master

1. Lists: marker forms, indentation, continuation
2. Block quotes: explicit vs lazy continuation
3. Reference definitions: syntax, normalization, duplicates
4. Links/images: inline vs reference forms
5. Autolinks (angle form)

### C2.3 Prerequisites

- C1 mastery

### C2.4 Deep-dive exercises

#### C2.4.1 List indentation matrix

Task:

Construct a matrix of examples varying:

- marker width (`-` vs `10.`),
- continuation indentation (0, 2, 4+ spaces),
- blank lines (present/absent).

For each case:

1. Predict whether the continuation is paragraph text, code block, new item, or outside the list.
2. Render and reconcile using CommonMark rules.

#### C2.4.2 Reference label normalization traps

Task:

Create at least 6 reference labels that appear different but should normalize identically under CommonMark.

Then:

1. Confirm which actually resolve.
2. Document any renderer-specific differences.

---

## C3 — Advanced

### C3.1 Learning objectives

By the end of this level, you can:

1. Explain the delimiter-run algorithm for emphasis/strong.
2. Predict interactions among emphasis, links, code spans, and HTML.
3. Predict HTML block termination and how it suppresses Markdown.
4. Use and audit GFM extensions for portability.

### C3.2 Concepts to master

1. Emphasis/strong algorithm (flanking + pairing)
2. Links: “no nested links” and precedence
3. HTML blocks: start patterns and termination
4. GFM: strikethrough, tables, task lists, autolink literals

### C3.3 Prerequisites

- C2 mastery

### C3.4 Deep-dive exercises

#### C3.4.1 Emphasis algorithm replay

Task:

Pick 10 tricky emphasis examples from the CommonMark spec.

For each:

1. Identify delimiter runs.
2. Classify flanking.
3. Simulate stack pairing to the final parse.

#### C3.4.2 HTML block boundary experiments

Task:

Write 5 documents starting with `<div>` (and other tag forms) and observe when Markdown parsing resumes.
Explain the termination rule responsible.

---

## C4 — Expert / internals

### C4.1 Learning objectives

By the end of this level, you can:

1. Validate implementations against CommonMark and GFM test suites.
2. Use differential testing and fuzzing to find divergence and bugs.
3. Design a safe Markdown rendering pipeline.
4. Reason about adversarial performance inputs.

### C4.2 Deep-dive exercises

1. Design a differential test harness comparing 3 renderers on randomized inputs.
2. Create a threat model and mitigation plan for “user-supplied Markdown rendered to HTML”.
3. Identify at least 3 patterns that cause slow parsing in naive implementations and propose defenses.

---

# Appendix A — Dialect Compatibility Matrix and Known Divergences

## Appendix A.1 — Compatibility matrix (selected major features)

Legend: **Yes** supported and broadly consistent; **Varies** supported but semantics vary; **No** not supported.

| Feature | CommonMark | GFM | Gruber Markdown (historical) | Markdown Extra | Pandoc Markdown |
|---|---:|---:|---:|---:|---:|
| ATX headings | Yes | Yes | Yes | Yes | Yes |
| Setext headings | Yes | Yes | Yes | Yes | Yes |
| Fenced code blocks | Yes | Yes | Varies | Yes | Yes |
| Tables | No | Yes | No | Varies | Yes |
| Task lists | No | Yes | No | No | Varies |
| Strikethrough | No | Yes | No | Varies | Yes |
| Autolinks `<...>` | Yes | Yes | Varies | Varies | Yes |
| Autolink literals | No | Yes | No | Varies | Varies |
| Emphasis algorithm | Yes (precise) | Yes | Varies greatly | Varies | Varies |
| Raw HTML passthrough | Yes (specified) | Yes | Varies | Varies | Yes |

## Appendix A.2 — Divergence themes (what breaks portability)

1. **Emphasis**: underscore intraword rules differ widely.
2. **Lists**: indentation and continuation rules differ widely.
3. **HTML**: some systems strip HTML; others pass it through.
4. **Extensions**: tables/task lists/strikethrough are not portable to CommonMark-only environments.

---

# Appendix B — Security Model, Threats, and Sanitization Requirements

## Appendix B.1 — Core security principle

Markdown parsing correctness is not equivalent to safe output.

- A correct parser can still emit HTML that executes script.
- Safe rendering requires additional policy controls (disable HTML, sanitize output, restrict URL schemes).

## Appendix B.2 — Threats

1. XSS via inline HTML and HTML blocks
2. XSS via unsafe link destinations (e.g., `javascript:`)
3. Attribute injection (`onerror`, `onload`, etc.)
4. Resource-loading tracking (images)
5. Social engineering via deceptive links
6. DoS via pathological Markdown

## Appendix B.3 — Mitigation requirements (conceptual)

1. Prefer renderer modes that disable raw HTML.
2. If HTML is allowed, sanitize rendered HTML with an allowlist sanitizer.
3. Enforce URL scheme policy for links and images.
4. Use CSP and referrer policy in browsers.
5. Treat Markdown as untrusted input unless provenance is controlled.

---

# Appendix C — Testing, Verification, and Differential Fuzzing

## Appendix C.1 — Normative tests

1. Run the CommonMark test suite.
2. Run the GFM test suite for extension behavior.

## Appendix C.2 — Golden tests

Maintain a repository of inputs → expected outputs for:

- every construct,
- every edge case you rely on,
- every security-relevant case (HTML, links).

## Appendix C.3 — Differential testing

Compare multiple renderers on the same inputs to identify:

- dialect differences,
- spec misunderstandings,
- implementation bugs.

## Appendix C.4 — Fuzzing and reduction

Fuzz targeted patterns:

- delimiter runs,
- nested containers,
- bracket/parenthesis ambiguity.

Reduce failures by iterative deletion until a minimal counterexample remains.
