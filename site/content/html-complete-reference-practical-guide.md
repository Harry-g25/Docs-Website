# HTML Complete Reference & Practical Guide

A comprehensive, hands-on reference for writing modern HTML. This guide doesn't just show you the syntax — it explains **why** each element exists, **when** you should reach for it, **how** browsers actually interpret it, and **what goes wrong** when you get it wrong. It's designed to be kept open beside your editor while you work.

---

## Table of Contents

1. [Document Structure](#1-document-structure)
2. [The `<head>` Element — Metadata](#2-the-head-element--metadata)
3. [Text Content](#3-text-content)
4. [Links & Anchors](#4-links--anchors)
5. [Images & Media](#5-images--media)
6. [Lists](#6-lists)
7. [Tables](#7-tables)
8. [Forms & Inputs](#8-forms--inputs)
9. [Semantic & Structural Elements](#9-semantic--structural-elements)
10. [Interactive Elements](#10-interactive-elements)
11. [Embedding & Iframes](#11-embedding--iframes)
12. [Global Attributes](#12-global-attributes)
13. [ARIA & Accessibility](#13-aria--accessibility)
14. [Performance](#14-performance)
15. [SEO & Social Sharing](#15-seo--social-sharing)
16. [Security](#16-security)
17. [Responsive Design](#17-responsive-design)
18. [HTML Entities & Special Characters](#18-html-entities--special-characters)
19. [Common Patterns & Templates](#19-common-patterns--templates)
20. [Validation & Debugging](#20-validation--debugging)
21. [Quick-Reference Cheatsheet](#21-quick-reference-cheatsheet)
22. [Further Reading](#22-further-reading)

---

## 1. Document Structure

Every HTML5 document starts with the same skeleton. This isn't just boilerplate — each piece serves a specific purpose in telling the browser how to parse, render, and present your content. Getting the structure right means your page renders in **standards mode** across all browsers, your content is accessible to screen readers, and search engines can understand your page.

### 1.1 The DOCTYPE

```html
<!DOCTYPE html>
```

The DOCTYPE declaration is a historical artefact from the early web, but it still matters today. In the 1990s, browsers needed to know which version of HTML (or XHTML) a page was written in, so DOCTYPEs were long, complicated strings referencing DTD (Document Type Definition) files. HTML5 simplified this to just `<!DOCTYPE html>`.

**Why it matters:** Without a DOCTYPE (or with a malformed one), browsers fall into **quirks mode** — a backwards-compatibility rendering mode that mimics the buggy behaviour of 1990s browsers. In quirks mode, the box model works differently, margin collapsing changes, table sizing behaves unexpectedly, and many CSS features don't work as specified. Every modern page should start with `<!DOCTYPE html>` to trigger **standards mode**.

**Rules:**
- Must be the very **first thing** in the file — no whitespace, no comments, no blank lines before it.
- It is case-insensitive (`<!doctype html>` works), but uppercase `DOCTYPE` is the convention.
- It is not an HTML element — it's a processing instruction for the browser's parser.

### 1.2 The `<html>` Root

```html
<html lang="en" dir="ltr">
```

The `<html>` element is the root of the entire document. Everything else — `<head>` and `<body>` — lives inside it. It seems trivial, but the attributes you put here have far-reaching effects:

**The `lang` attribute** is one of the most important attributes on the entire page. It tells browsers, screen readers, search engines, spell-checkers, translation tools, and CSS `hyphens` what language the content is in. Screen readers like NVDA and VoiceOver use it to select the correct pronunciation engine — without it, a screen reader might try to pronounce French text with an English accent, making it unintelligible. Search engines use it for language indexing. The CSS `hyphens: auto` property relies on it to know how to break words.

Use BCP 47 language tags: `en` (English), `en-GB` (British English), `en-US` (American English), `fr` (French), `cy` (Welsh), `de` (German), etc. If a section of your page is in a different language, you can override it locally with `lang` on any element: `<p lang="fr">Bonjour le monde</p>`.

**The `dir` attribute** controls text direction. Most languages are left-to-right (`ltr`, the default), but Arabic, Hebrew, Farsi, and Urdu are right-to-left (`rtl`). Setting `dir="rtl"` flips the entire page layout — text alignment, punctuation positioning, and even CSS `margin-left`/`margin-right` behaviour with logical properties. If you're building a multilingual site, this is critical.

### 1.3 Minimal Valid Page

Here's the smallest complete page that follows all modern best practices:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page Title — Site Name</title>
  <link rel="icon" href="/favicon.ico">
  <link rel="stylesheet" href="/css/style.css">
</head>
<body>
  <header>
    <nav aria-label="Main">
      <a href="/">Home</a>
      <a href="/docs">Docs</a>
    </nav>
  </header>

  <main id="main">
    <h1>Welcome</h1>
    <p>Body content goes here.</p>
  </main>

  <footer>
    <p>&copy; 2026 My Project</p>
  </footer>

  <script src="/js/app.js" defer></script>
</body>
</html>
```

Let's break down **why each line is there:**

- `<meta charset="utf-8">` — tells the browser which character encoding to use when turning raw bytes into text. UTF-8 supports every character in Unicode (every language, emoji, mathematical symbol). Without this, special characters can render as garbled text (mojibake). It must appear within the first 1024 bytes of the document.
- `<meta name="viewport">` — tells mobile browsers not to pretend the screen is 980px wide. Without this, your mobile visitors see a tiny zoomed-out version of a desktop page. This single line is what makes CSS media queries and responsive design work on phones.
- `<title>` — appears in the browser tab, bookmarks list, search engine results, and screen reader announcements when the user switches tabs. It should be unique per page and descriptive.
- `<link rel="icon">` — the favicon shown in the browser tab next to the title.
- `<link rel="stylesheet">` — loads your CSS. Placed in `<head>` so the browser can start downloading it as early as possible.
- `<script defer>` — loads your JavaScript in parallel with HTML parsing, but waits to execute until the DOM is fully built. Placed at the end of `<body>` or in `<head>` with `defer` — both achieve the same result.

### 1.4 Comments

```html
<!-- This is a comment. It won't render in the browser. -->

<!--
  Multi-line comments work too.
  Use them for TODOs, section markers, or disabling code temporarily.
-->
```

HTML comments are useful for documentation inside your templates, leaving notes for other developers, or temporarily disabling a block of markup. However, they come with an important caveat: **comments are visible to anyone who views your page source**. Never put passwords, API keys, internal URLs, or sensitive business logic in HTML comments. Automated security scanners specifically look for sensitive data in HTML comments.

Comments also add to your page weight. In production, consider stripping them during your build process if performance is critical.

---

## 2. The `<head>` Element — Metadata

The `<head>` is the invisible brain of your page. Nothing inside `<head>` renders on screen, but it controls how the page behaves, how it appears in search results and social media shares, what resources it loads, and how browsers and assistive technologies interpret the content. Getting the `<head>` right is crucial for performance, SEO, accessibility, and social sharing.

### 2.1 Character Set

```html
<meta charset="utf-8">
```

Character encoding is how the browser converts the raw bytes of your HTML file into the characters you see on screen. UTF-8 is the universal standard that supports every character from every writing system in the world — Latin letters, Chinese characters, Arabic script, emoji, mathematical notation, and more.

**Why it must come first:** The browser needs to know the encoding before it can correctly parse anything else in the document. If this declaration is missing or comes too late (after the first 1024 bytes), the browser has to guess the encoding, which can lead to garbled text — a problem called "mojibake" where characters like "£" appear as "Â£" or "é" appears as "Ã©".

**Always use UTF-8.** There is no good reason to use any other encoding for new web pages. The alternative encodings (ISO-8859-1, Windows-1252, etc.) only support a subset of characters and cause problems with internationalisation.

### 2.2 Viewport

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

This single meta tag is the difference between a page that works on mobile and one that doesn't. Here's what's actually happening:

Before smartphones, all web pages were designed for desktop screens around 960-1024px wide. When the iPhone launched in 2007, Apple had a problem: existing websites would look terrible squished into a 320px screen. Their solution was to have the mobile browser pretend the screen was 980px wide, render the full desktop page, and then zoom out to fit. This is still the default behaviour today.

The viewport meta tag overrides this. `width=device-width` tells the browser "use the actual screen width, not a fake 980px width." `initial-scale=1` sets the initial zoom level to 100%. Together, they make your CSS media queries respond to the real screen dimensions, which is what makes responsive design possible.

**Without this tag:** Your carefully crafted `@media (max-width: 768px)` rules will never trigger on mobile, because the browser thinks the screen is 980px wide. Your font sizes won't adapt. Your layout won't reflow. The page will just be a tiny zoomed-out desktop version.

**Common mistakes to avoid:**
- Don't add `maximum-scale=1` or `user-scalable=no` — these prevent users from zooming in, which is a significant accessibility violation. Users with low vision need to be able to zoom.
- Don't set a fixed `width` like `width=1024` — this defeats the entire purpose.

### 2.3 Title

```html
<title>Article Name — Site Name</title>
```

The `<title>` element appears in more places than you might realise: the browser tab, the browser's title bar, bookmark names, browser history, search engine results pages (as the clickable blue link), screen reader announcements when switching between tabs or windows, and social media share previews as a fallback.

**Best practices:**
- Keep it **unique per page**. Every page on your site should have a distinct title that describes its specific content. "Home" or "Untitled" are unhelpful.
- Keep it **under ~60 characters**. Search engines truncate longer titles with an ellipsis, so put the most important words first.
- Use a consistent pattern like `Page Name — Site Name` or `Page Name | Site Name`. Putting the page-specific content first means users scanning browser tabs can distinguish between pages more easily.
- Make it **human-readable and descriptive**. "Python 3.14 New Features Guide — Documentation Hub" is better than "docs-python-314".

### 2.4 Meta Descriptions & Robots

```html
<meta name="description" content="A 150-160 character summary of this page for search results.">
<meta name="robots" content="index, follow">
<meta name="author" content="Harry Gomm">
```

**The description meta tag** doesn't directly affect your search ranking, but it has a huge impact on **click-through rate**. It's the grey text snippet shown below the title in Google/Bing search results. A well-written description acts like an advertisement for your page — it should summarise the content in a compelling way that makes people want to click. Keep it between 150-160 characters; longer descriptions get truncated.

**The robots meta tag** controls how search engine crawlers treat the page. `index, follow` is the default (you don't need to explicitly set it). The useful variations are:
- `noindex` — tells search engines not to include this page in search results. Useful for admin pages, login pages, or staging content.
- `nofollow` — tells search engines not to follow any links on the page.
- `nosnippet` — prevents search engines from showing a text snippet or video preview.

**The author meta tag** is informational and sometimes used by search engines to attribute content to a specific person.

### 2.5 Favicon & App Icons

```html
<!-- Basic favicon — what users see in the browser tab -->
<link rel="icon" href="/favicon.ico" sizes="32x32">

<!-- SVG favicon — scales perfectly to any size, supports dark mode -->
<link rel="icon" href="/icon.svg" type="image/svg+xml">

<!-- Apple touch icon — what iOS shows when users add your site to their home screen -->
<link rel="apple-touch-icon" href="/apple-touch-icon.png">

<!-- Web app manifest — defines your site as a Progressive Web App -->
<link rel="manifest" href="/manifest.json">
```

Favicons seem like a minor detail, but they're one of the most visible parts of your brand in a browser. Users see them in tabs, bookmarks, history, and (on mobile) the home screen. The modern approach is to provide multiple formats:

- **`.ico`** — the traditional format, still needed for older browsers and some bookmark managers. Best at 32x32 pixels.
- **SVG** — the modern choice. SVG favicons scale perfectly to any size, support CSS features like `prefers-color-scheme` (so your icon can adapt to dark mode), and have tiny file sizes. Not all browsers support them yet, so keep the `.ico` as a fallback.
- **Apple touch icon** — a 180x180 PNG that iOS uses when someone adds your site to their home screen as a bookmark. Without this, iOS takes a screenshot of your page instead, which usually looks terrible.
- **Web manifest** — a JSON file that defines your site's name, icons, theme colour, and display mode for Progressive Web Apps. Even if you're not building a PWA, it can improve how your site appears when saved to a mobile home screen.

### 2.6 Stylesheets

```html
<!-- External stylesheet (most common approach) -->
<link rel="stylesheet" href="/css/style.css">

<!-- Print-specific stylesheet — only applies when printing the page -->
<link rel="stylesheet" href="/css/print.css" media="print">

<!-- Inline critical CSS for above-the-fold speed -->
<style>
  body { margin: 0; font-family: system-ui, sans-serif; }
</style>
```

CSS loading has a direct impact on how fast your page appears to the user. Here's what happens behind the scenes:

When the browser encounters a `<link rel="stylesheet">` in the `<head>`, it **pauses rendering** and downloads that CSS file before painting anything on screen. This is called "render-blocking" and it happens because the browser can't know what the page looks like until it has all the CSS rules. If your CSS file is large or on a slow server, this means users stare at a white screen.

**Strategies to manage this:**
- **External stylesheets in `<head>`** — the standard approach. The browser discovers them early and starts downloading immediately. Good for CSS that applies to the whole page.
- **Print stylesheets with `media="print"`** — the browser downloads these but doesn't block rendering for them because they only apply when printing. This is a useful pattern for separating print-specific styles.
- **Inline critical CSS** — embedding the CSS needed for above-the-fold content directly in a `<style>` tag means no extra network request is needed. The page can render immediately. The rest of the CSS can be loaded asynchronously. This is an advanced performance optimisation.

### 2.7 Scripts

```html
<!-- Deferred: downloads in parallel, executes after HTML is fully parsed -->
<script src="/js/app.js" defer></script>

<!-- Async: downloads in parallel, executes as soon as the download finishes -->
<script src="/js/analytics.js" async></script>

<!-- Module: automatically deferred, supports import/export syntax -->
<script type="module" src="/js/main.mjs"></script>

<!-- Inline: executes immediately when the parser reaches it -->
<script>
  console.log('Hello from inline script');
</script>
```

How you load JavaScript has a massive impact on page performance and user experience. Here's what each loading strategy actually does:

**No attribute (default):** When the browser's HTML parser encounters a plain `<script>` tag, it **stops parsing the HTML**, downloads the script file, executes it, and only then continues parsing. If your script is 200KB and the server is slow, the user sees an incomplete page for seconds. This is why the old advice was "put scripts at the bottom of `<body>`" — by the time the parser reaches them, the page is already rendered. However, this delays script download because the browser doesn't discover the script until it's parsed the entire page.

**`defer`:** The browser starts downloading the script immediately (in parallel with HTML parsing) but waits to execute it until the HTML is fully parsed and the DOM is ready. Multiple `defer` scripts execute in the order they appear in the document. This is the best choice for most application scripts because they download early, don't block rendering, and the DOM is guaranteed to be ready when they run.

**`async`:** Like `defer`, the browser downloads the script in parallel. But unlike `defer`, it **executes immediately** when the download finishes — even if the HTML isn't fully parsed yet. Multiple `async` scripts execute in whatever order they finish downloading, not document order. This is ideal for independent scripts like analytics or ad trackers that don't interact with your DOM or with each other.

**`type="module"`:** Enables ES module syntax (`import`/`export`). Module scripts are automatically deferred (they wait for the DOM), support `import` statements, and run in strict mode. They also only execute once even if included multiple times. This is the modern approach for new projects.

| Strategy | Downloads | Executes | Order guaranteed | Best for |
|----------|-----------|----------|-----------------|----------|
| `<script>` (plain) | Blocks parsing | Immediately | Yes | Legacy; avoid |
| `defer` | Parallel | After DOM ready | Yes | Main app code |
| `async` | Parallel | When download finishes | No | Analytics, ads, independent tools |
| `type="module"` | Parallel | After DOM ready | Yes | Modern ES modules |

### 2.8 Preloading & Preconnecting

```html
<!-- Preload: "Download this specific file RIGHT NOW, I need it soon" -->
<link rel="preload" href="/fonts/Inter.woff2" as="font" type="font/woff2" crossorigin>

<!-- Preconnect: "I'm going to need something from this server, start connecting" -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://cdn.example.com" crossorigin>

<!-- DNS prefetch: lighter version of preconnect, just resolves the domain name -->
<link rel="dns-prefetch" href="https://api.example.com">
```

These resource hints let you tell the browser about resources it will need **before it naturally discovers them**. This is powerful because normally the browser can only download something after it finds a reference to it in the HTML or CSS:

**`preload`** is the strongest hint. It tells the browser "start downloading this exact file immediately at high priority." This is invaluable for fonts (which the browser normally doesn't discover until it's parsed both the HTML and the CSS that references the font), critical images, or JavaScript modules loaded by other scripts. The `as` attribute is required and tells the browser what type of resource it is (so it can set the right priority and apply the right security policies).

**`preconnect`** establishes an early connection to a server — performing DNS lookup, TCP handshake, and TLS negotiation all before anything is actually requested. Each of these steps takes time (especially on mobile networks), so doing them early can save 100-500ms. Use this for third-party origins you know you'll fetch from (CDNs, API servers, font providers).

**`dns-prefetch`** is a lighter version that only resolves the domain name to an IP address. It's lower cost than `preconnect` and good for origins where the connection might not actually be needed on every page load.

**Don't overuse these.** Every preload/preconnect consumes bandwidth and CPU. If you preload too many resources, you can actually slow down the page by competing with more critical downloads. Limit preloads to 2-4 truly critical resources.

### 2.9 Open Graph & Twitter Card

```html
<!-- Open Graph: controls how your page appears when shared on Facebook, 
     LinkedIn, Discord, Slack, iMessage, WhatsApp, and most other platforms -->
<meta property="og:type" content="website">
<meta property="og:title" content="My Page Title">
<meta property="og:description" content="Short summary of the page.">
<meta property="og:image" content="https://example.com/img/og-card.png">
<meta property="og:url" content="https://example.com/page">

<!-- Twitter Card: specifically for Twitter/X previews -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="My Page Title">
<meta name="twitter:description" content="Short summary.">
<meta name="twitter:image" content="https://example.com/img/tw-card.png">
```

When someone shares a link on social media or in a chat app, the platform fetches your page and looks for these meta tags to generate a **rich preview card** with a title, description, and image. Without them, shared links appear as plain URLs or the platform guesses (often poorly) from your page content.

**Open Graph (OG)** was created by Facebook but is now the universal standard. Almost every platform that generates link previews reads OG tags: Facebook, LinkedIn, Discord, Slack, Telegram, WhatsApp, iMessage, Reddit, and more. The most important tags are:
- `og:title` — the headline shown in the preview card (can differ from your `<title>`).
- `og:description` — the description text below the headline.
- `og:image` — the preview image. This is the single most impactful element — posts with images get dramatically more engagement. Use a 1200x630 pixel image for best results.
- `og:url` — the canonical URL for the page.

**Twitter Cards** are Twitter/X's own system. Twitter reads OG tags as a fallback, but `twitter:card` specifically controls the card format: `summary` (small square image) or `summary_large_image` (wide banner image). If you set both OG and Twitter tags, Twitter uses its own; other platforms use OG.

**Tip:** Use a tool like [opengraph.xyz](https://www.opengraph.xyz/) to preview how your link will appear before deploying.

### 2.10 Canonical & Alternate

```html
<!-- Canonical: "This is THE official URL for this content" -->
<link rel="canonical" href="https://example.com/page">

<!-- Alternate: "This same content exists in other languages at these URLs" -->
<link rel="alternate" hreflang="en" href="https://example.com/en/page">
<link rel="alternate" hreflang="fr" href="https://example.com/fr/page">
```

**Canonical URLs** solve a common SEO problem: the same content accessible at multiple URLs. For example, `https://example.com/page`, `https://example.com/page?lang=en`, `https://www.example.com/page`, and `http://example.com/page` might all show the same content. Without a canonical tag, search engines might index all four URLs separately, diluting your ranking. The canonical tag says "these are all the same page — treat this URL as the authoritative one."

**Alternate language links** tell search engines that the same content exists in different languages, so they can serve the right version based on the user's language preferences and location.

### 2.11 Full `<head>` Example

Putting it all together — here's a production-ready `<head>` with all the important elements:

```html
<head>
  <!-- Character encoding — must be first -->
  <meta charset="utf-8">
  <!-- Viewport for responsive design -->
  <meta name="viewport" content="width=device-width, initial-scale=1">
  
  <!-- Page title and description -->
  <title>HTML Guide — Documentation Hub</title>
  <meta name="description" content="Complete HTML reference with practical examples.">
  <meta name="author" content="Harry Gomm">

  <!-- Favicons -->
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="icon" href="/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">

  <!-- SEO -->
  <link rel="canonical" href="https://docs.example.com/html-guide">

  <!-- Social sharing -->
  <meta property="og:title" content="HTML Guide">
  <meta property="og:description" content="Complete HTML reference.">
  <meta property="og:image" content="https://docs.example.com/img/og.png">
  <meta property="og:url" content="https://docs.example.com/html-guide">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Performance hints -->
  <link rel="preconnect" href="https://fonts.googleapis.com">

  <!-- Styles and scripts -->
  <link rel="stylesheet" href="/css/style.css">
  <script src="/js/app.js" defer></script>
</head>
```

---

## 3. Text Content

Text is the foundation of the web. HTML provides a rich set of elements for structuring text content — each one carrying specific semantic meaning that goes beyond mere visual styling. Using the right elements means your content is understandable by screen readers, parseable by search engines, and styled consistently with CSS.

### 3.1 Headings

```html
<h1>Page Title (one per page)</h1>
<h2>Major Section</h2>
<h3>Subsection</h3>
<h4>Sub-subsection</h4>
<h5>Minor heading</h5>
<h6>Smallest heading</h6>
```

Headings are one of the most important structural elements in HTML. They do much more than make text bigger:

**For accessibility:** Screen reader users often navigate pages by jumping between headings — it's one of the most common navigation strategies. NVDA and VoiceOver let users press a key to jump to the next heading, or pull up a list of all headings on the page. If your heading hierarchy is broken (skipping from `h1` to `h4`, or using headings purely for visual size), screen reader users can't navigate your page effectively.

**For SEO:** Search engines use headings to understand the topic and structure of your page. The `<h1>` tells them what the page is about. `<h2>`s indicate major subtopics. This has a direct (though modest) impact on search ranking.

**For document outline:** Headings create a logical tree structure. Think of it like a table of contents — `h1` is the chapter title, `h2`s are sections, `h3`s are subsections. This outline should make sense if you extracted just the headings.

**Rules to follow:**
- Use **exactly one `<h1>` per page** — it should be the main topic/title.
- **Never skip heading levels.** Go `h1 → h2 → h3`, never `h1 → h3`. You can go back up (after an `h3` section, starting a new `h2` section is fine).
- Choose headings for **structure, not styling**. If you want small bold text, use CSS — don't use `<h5>` just because it looks the right size. If you want big text that isn't a heading, style a `<p>` or `<div>`.

### 3.2 Paragraphs

```html
<p>This is a paragraph. Keep sentences clear and focused on one idea.</p>

<p>
  Paragraphs can span multiple lines in source code.
  The browser collapses all whitespace (spaces, tabs, newlines)
  into single spaces. So this renders as one continuous line of text,
  regardless of how it looks in your HTML file.
</p>
```

The `<p>` element represents a paragraph of text — a self-contained unit of discourse dealing with a particular point or idea. Browsers add vertical margin above and below paragraphs by default (typically around 16px, or 1em).

**Whitespace collapsing** is an important concept to understand: the browser turns any sequence of whitespace characters (spaces, tabs, newlines) into a single space. This means your source code formatting doesn't affect the rendered output. If you need to preserve whitespace exactly as written, use `<pre>` instead.

**Don't use empty paragraphs (`<p></p>`) or `<br><br>` for spacing.** Use CSS `margin` or `padding` instead. Empty paragraphs create awkward pauses for screen readers.

### 3.3 Inline Text Formatting

HTML provides two categories of inline text formatting: **semantic** elements that convey meaning, and **presentational** elements that only affect appearance. Understanding the difference matters for accessibility and SEO.

**Semantic elements — these carry meaning:**

```html
<strong>Bold / important</strong>
```
`<strong>` indicates that the text is of **strong importance** — it's serious, urgent, or critical. Screen readers may announce it with a different tone. Search engines may give it extra weight. It happens to render as bold, but that's a side effect of its meaning.

```html
<em>Italic / emphasis</em>
```
`<em>` indicates **stress emphasis** — the kind you'd express by changing your voice pitch when speaking aloud. "I *didn't* say he stole it" has a different meaning from "I didn't say he *stole* it." `<em>` captures this distinction. It happens to render as italic.

```html
<mark>Highlighted text</mark>
```
`<mark>` indicates text that is **relevant or highlighted** in the current context — like search result highlighting, or marking a key phrase in a quotation. It renders with a yellow background by default.

```html
<del>Deleted text</del>
<ins>Inserted text</ins>
```
`<del>` and `<ins>` represent **editorial changes** — content that has been removed or added. Screen readers announce these as "deletion" and "insertion." They're useful for showing revisions, changelogs, or track-changes-style content. `<del>` renders with a strikethrough; `<ins>` with an underline.

```html
<abbr title="HyperText Markup Language">HTML</abbr>
```
`<abbr>` marks an abbreviation or acronym. The `title` attribute provides the full expansion as a tooltip. Screen readers can be configured to read the expansion. It's a small touch that significantly improves clarity.

```html
<time datetime="2026-02-17">February 17, 2026</time>
```
`<time>` makes dates and times machine-readable. The `datetime` attribute provides the value in ISO 8601 format, while the visible text can be in any human-friendly format. Search engines and browser extensions can parse `datetime` to display relative times ("2 hours ago") or add events to calendars.

```html
<code>inline code</code>
<kbd>Ctrl</kbd> + <kbd>S</kbd>
<samp>Output text</samp>
<var>x</var>
```
- `<code>` — a fragment of computer code. Renders in a monospace font.
- `<kbd>` — keyboard input the user should type. Often styled with a key-cap appearance.
- `<samp>` — sample output from a program.
- `<var>` — a variable in a mathematical expression or programming context.

**Presentational elements — visual only, no extra meaning:**

```html
<b>Bold text (no semantic importance)</b>
<i>Italic text (no semantic emphasis)</i>
<small>Fine print, legal text, side comments</small>
<sub>Subscript</sub>  H<sub>2</sub>O
<sup>Superscript</sup>  E=mc<sup>2</sup>
```

Use `<b>` and `<i>` when you want the visual style but don't mean "important" or "emphasized." For example, `<i>` is appropriate for a book title, a technical term being introduced, or a phrase in a foreign language — cases where italic is a typographic convention, not stress emphasis.

### 3.4 Block Quotes

```html
<blockquote cite="https://example.com/source">
  <p>The only way to do great work is to love what you do.</p>
  <footer>— <cite>Steve Jobs</cite></footer>
</blockquote>
```

`<blockquote>` represents an extended quotation from another source. The `cite` attribute (not visible to users) records the source URL. The `<cite>` element inside names the work being quoted. Screen readers announce blockquotes differently, and they're typically indented and styled distinctively with CSS.

**Don't use `<blockquote>` for indentation or visual styling.** It has semantic meaning — using it for non-quotes confuses screen readers and search engines. Use CSS margins for indentation.

### 3.5 Preformatted Text & Code Blocks

```html
<!-- Preformatted: whitespace is preserved exactly as written -->
<pre>
  Line 1
  Line 2
    Indented line
</pre>

<!-- Code block with syntax highlighting class -->
<pre><code class="language-python">
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
</code></pre>
```

`<pre>` (preformatted text) is the only block element where whitespace is preserved as-is — spaces, tabs, and newlines all render literally. The browser uses a monospace font by default. This makes it essential for code blocks, ASCII art, poetry with specific formatting, or any content where visual arrangement matters.

The convention for code blocks is to nest a `<code>` element inside `<pre>`. This gives you both the "preformatted" behaviour and the "this is code" semantics. Adding a `class="language-xxx"` (like `language-python`, `language-javascript`) allows syntax highlighting libraries like highlight.js or Prism to auto-detect and colourize the code.

### 3.6 Horizontal Rule

```html
<hr>
```

`<hr>` represents a **thematic break** — a shift in topic within a section. Visually it renders as a horizontal line, but semantically it's more like a scene break in a novel or a shift to a new topic in a conversation. Don't use it for pure decoration — use CSS `border-bottom` on a container instead.

### 3.7 Line Breaks & Word Breaks

```html
<p>Line one.<br>Line two on a new line.</p>

<!-- <wbr> suggests a possible word-break point for very long strings -->
<p>super<wbr>cali<wbr>fragilistic<wbr>expiali<wbr>docious</p>
```

**`<br>`** forces a line break within flowing text. Use it sparingly — it's appropriate for addresses, poetry, or anywhere line breaks are part of the content's meaning. Don't use chains of `<br><br>` for vertical spacing; use CSS margins on block elements instead.

**`<wbr>`** (word break opportunity) suggests a point where the browser **may** break a long string if it overflows its container. Unlike `<br>`, it doesn't force a break — it just gives permission. This is useful for very long URLs, file paths, or compound words that might overflow on narrow screens.

### 3.8 Address

```html
<address>
  Written by <a href="mailto:harry@example.com">Harry Gomm</a>.<br>
  Wall-Lag (Wales) Ltd<br>
  Cardiff, Wales
</address>
```

`<address>` provides contact information for the nearest `<article>` or `<body>` ancestor — typically the author of a document or the owner of a site. Browsers render it in italic by default. Despite the name, it's not just for postal addresses — it's for any contact information (email, phone, social media links).

---

## 4. Links & Anchors

Links are what make the web a web — they connect pages together. The `<a>` (anchor) element is one of the most important and most used HTML elements. Getting links right means good user experience, solid accessibility, and proper security.

### 4.1 Basic Link

```html
<a href="/about">About Us</a>
```

The `href` (hypertext reference) attribute specifies where the link goes. It can be:
- **Absolute URL:** `https://example.com/page` — a full URL including protocol and domain. Used for external sites.
- **Root-relative:** `/about` — starts from the root of your site. The browser builds the full URL using the current domain. Good for internal links because they work regardless of the current page's path.
- **Relative:** `../about` or `page.html` — relative to the current page's URL. Be careful with these as they break if you move the page.
- **Fragment:** `#section-id` — scrolls to an element on the current page.
- **Protocol-relative:** `//example.com/page` — inherits the current page's protocol. Rarely used today since everything should be HTTPS.

### 4.2 External Link (with security)

```html
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
  Visit Example
</a>
```

When you open a link in a new tab with `target="_blank"`, you create a potential security vulnerability: the new page gets access to `window.opener`, which is a reference back to your page. A malicious site could use this to redirect your page to a phishing page while the user's attention is on the new tab.

**`rel="noopener"`** prevents this by ensuring the new page's `window.opener` is `null`. Modern browsers do this automatically for `target="_blank"` links, but adding it explicitly ensures older browsers are covered.

**`rel="noreferrer"`** goes a step further — it also prevents the `Referer` header from being sent, so the destination site can't see where the user came from. This is useful for privacy.

**Best practice:** Always use `rel="noopener noreferrer"` on external links that open in new tabs.

### 4.3 Anchor Links (same-page navigation)

```html
<!-- Link that scrolls to a section -->
<a href="#installation">Jump to Installation</a>

<!-- The target section — the id must match the fragment -->
<h2 id="installation">Installation</h2>
```

Fragment links (starting with `#`) scroll the page to the element with the matching `id`. The scroll is instant by default, but you can add `scroll-behavior: smooth` in CSS for animated scrolling. The browser updates the URL to include the fragment, so users can bookmark specific sections.

**Tips for anchor IDs:**
- Use lowercase, hyphen-separated names: `getting-started`, not `GettingStarted` or `getting_started`.
- Keep them stable — if other sites or bookmarks link to `#installation` and you rename it, those links break.
- IDs must be unique within the page.

### 4.4 Download Links

```html
<a href="/files/report.pdf" download>Download Report (PDF)</a>
<a href="/files/data.csv" download="export-2026.csv">Download CSV</a>
```

The **`download` attribute** tells the browser to download the file instead of navigating to it. Without `download`, clicking a link to a PDF would open it in the browser's PDF viewer. With `download`, it triggers a download dialog.

You can optionally provide a filename: `download="export-2026.csv"` will suggest that name in the save dialog regardless of the file's actual name on the server.

**Security note:** The `download` attribute only works for same-origin URLs or `blob:` and `data:` URLs. For cross-origin files, the browser ignores `download` and navigates normally.

### 4.5 Email & Phone Links

```html
<a href="mailto:harry@example.com">Email us</a>
<a href="mailto:harry@example.com?subject=Hello&body=Hi%20there">Email with prefilled subject</a>
<a href="tel:+441234567890">Call us: +44 1234 567890</a>
```

**`mailto:` links** open the user's default email client with a new message pre-addressed to the specified address. You can prefill the subject and body using query parameters. These are excellent for contact pages because they respect the user's preferred email app.

**`tel:` links** initiate a phone call on mobile devices. On desktop, they may open Skype, FaceTime, or another calling app. Always use the international format with `+` country code for reliable dialling across countries.

**Important:** Be aware that `mailto:` links expose the email address in the page source, making it harvestable by spam bots. Consider using a contact form instead for public-facing pages.

### 4.6 Skip Links (accessibility)

```html
<!-- Place as the very first focusable element in <body> -->
<a href="#main" class="skip-link">Skip to main content</a>

<style>
.skip-link {
  position: absolute;
  left: -9999px;
  z-index: 999;
  padding: 8px 16px;
  background: #000;
  color: #fff;
  text-decoration: none;
}
.skip-link:focus {
  left: 10px;
  top: 10px;
}
</style>
```

Skip links are a critical accessibility feature that many developers overlook. When a keyboard user tabs into your page, they have to press Tab through every navigation link, logo, search bar, and toolbar button before reaching the main content. On a page with 30 nav items, that's 30 Tab presses just to start reading.

A skip link appears as the **first focusable element** when the user presses Tab. It's visually hidden until focused (using the CSS above), then it appears as a visible link saying "Skip to main content." Pressing Enter skips the user directly to the `<main>` element.

This is required by WCAG 2.4.1 (Bypass Blocks) and is one of the first things accessibility auditors check.

### 4.7 Link Accessibility Best Practices

**Write descriptive link text.** Screen readers can list all links on a page — if they all say "click here" or "read more," the list is useless. Compare:

```html
<!-- BAD — meaningless out of context -->
<p>To learn about accessibility, <a href="/a11y">click here</a>.</p>

<!-- GOOD — the link text describes the destination -->
<p>Read our <a href="/a11y">accessibility guidelines</a>.</p>
```

**Don't use URLs as link text:** "Visit https://example.com/very/long/path/to/page" is hard to read and screen readers spell it out character by character. Use descriptive text instead.

### 4.8 Link States (CSS reference)

```css
a:link    { color: #6366f1; }              /* unvisited link */
a:visited { color: #8b5cf6; }              /* user has been to this URL before */
a:hover   { color: #818cf8; }              /* mouse is hovering */
a:focus   { outline: 2px solid #6366f1; }  /* keyboard focus (Tab key) */
a:active  { color: #4f46e5; }             /* being clicked (mousedown) */
```

These must be declared in this specific order (LVHFA — "LoVe HAte" is the mnemonic) because of CSS specificity: if they're in the wrong order, later rules override earlier ones due to equal specificity.

**Never remove focus styles without providing a replacement.** `:focus { outline: none }` makes links invisible to keyboard users. If you don't like the default outline, replace it with a custom style — don't remove it.

---

## 5. Images & Media

Images, video, and audio make content engaging and informative. But they also introduce performance, accessibility, and layout challenges. Handling media properly means your pages load fast, look good on all devices, and remain accessible to users who can't see or hear the content.

### 5.1 Basic Image

```html
<img src="/img/photo.jpg" alt="A sunset over the mountains" width="800" height="600">
```

The `<img>` element is self-closing (no `</img>` needed) and has two required attributes:

**`src`** — the URL of the image file. Can be absolute, relative, or a data URI.

**`alt`** — alternative text that describes the image's content or function. This is one of the most important accessibility attributes in HTML:
- Screen readers read it aloud to blind users, so it should describe what the image **shows**, not just what it **is**. "A golden retriever catching a frisbee in a park" is better than "dog photo."
- It appears when the image fails to load (broken link, slow connection).
- Search engines use it to understand image content.
- For **decorative images** that add no informational value (background textures, decorative borders), use `alt=""` (empty string). This tells screen readers to skip the image entirely. Note: `alt=""` and **no `alt` attribute** are different — a missing `alt` is a validation error and screen readers may read the filename instead.

**`width` and `height`** — always set these, even if they're overridden by CSS. The browser uses them to calculate the image's aspect ratio **before the image loads**, reserving the correct amount of space in the layout. Without them, the page content jumps around as images load (cumulative layout shift — CLS), which is jarring for users and penalised by Google's Core Web Vitals.

### 5.2 Lazy Loading

```html
<!-- Lazy: only loads when the user scrolls near it -->
<img src="/img/photo.jpg" alt="Description" loading="lazy">

<!-- Eager: loads immediately (the default — use for above-the-fold images) -->
<img src="/img/hero.jpg" alt="Hero banner" loading="eager">
```

**`loading="lazy"`** tells the browser to defer loading the image until the user scrolls near it. This is a massive performance win for pages with many images — instead of downloading 50 images on page load, the browser only downloads the few that are currently visible.

**When to use it:**
- **Do** use `loading="lazy"` on any image that's below the fold (not visible on initial page load).
- **Don't** use it on the largest image visible when the page first loads (the "LCP element" — Largest Contentful Paint). Lazy-loading your hero image actually slows down the perceived load time.
- The browser is smart about the threshold — it starts loading a bit before the image is actually visible, so users rarely see a loading delay.

### 5.3 Responsive Images with `srcset`

```html
<img
  src="/img/photo-800.jpg"
  srcset="
    /img/photo-400.jpg   400w,
    /img/photo-800.jpg   800w,
    /img/photo-1200.jpg 1200w,
    /img/photo-1600.jpg 1600w
  "
  sizes="
    (max-width: 600px) 100vw,
    (max-width: 1200px) 50vw,
    800px
  "
  alt="Responsive photo"
>
```

This is one of the most powerful (and misunderstood) features in HTML. Here's what's actually happening:

**The problem:** A single image file can't be optimal for all devices. Serving a 2000px image to a phone on a 3G connection wastes bandwidth and slows the page. Serving a 400px image to a 4K monitor looks blurry. You need different sized images for different situations.

**`srcset`** tells the browser "here are multiple versions of this image and their intrinsic widths." The `400w`, `800w`, etc. are **width descriptors** — they tell the browser the actual pixel width of each file. The browser uses this information, combined with `sizes`, to pick the best file.

**`sizes`** tells the browser how wide the image will be rendered at different viewport sizes. `(max-width: 600px) 100vw` means "on screens 600px or narrower, this image takes up 100% of the viewport width." `800px` (with no condition) is the default.

**The browser does the maths automatically.** It knows the viewport width, the device pixel ratio (1x, 2x, 3x), and the available connection speed, then picks the best image from the `srcset` list. You don't need to write `@media` queries or JavaScript for this.

**`src`** is the fallback for browsers that don't support `srcset` (very old browsers).

### 5.4 The `<picture>` Element

```html
<picture>
  <!-- Modern format: AVIF (smallest file size, not all browsers support it) -->
  <source srcset="/img/hero.avif" type="image/avif">
  <!-- Modern format: WebP (good compression, widely supported) -->
  <source srcset="/img/hero.webp" type="image/webp">
  <!-- Different crop for mobile screens -->
  <source media="(max-width: 768px)" srcset="/img/hero-mobile.jpg">
  <!-- Fallback: JPEG (universally supported) -->
  <img src="/img/hero-desktop.jpg" alt="Hero banner" loading="lazy">
</picture>
```

While `srcset` lets the browser choose between different **sizes** of the same image, `<picture>` gives you control over different **formats** or completely different **images** based on conditions:

- **Format switching:** Serve AVIF to browsers that support it (30-50% smaller than JPEG), WebP to others (25-35% smaller), and JPEG as the universal fallback. The browser automatically picks the first `<source>` it supports.
- **Art direction:** Show a wide landscape photo on desktop and a tightly cropped portrait version on mobile, rather than just scaling the same image down.
- The `<img>` element inside `<picture>` is required — it's the fallback and also the element that CSS styles and JavaScript interact with.

### 5.5 Figure & Caption

```html
<figure>
  <img src="/img/diagram.svg" alt="Architecture diagram showing client-server flow">
  <figcaption>Figure 1 — Client-server architecture overview</figcaption>
</figure>
```

`<figure>` represents self-contained content that is referenced from the main text but could be moved elsewhere (to an appendix, sidebar, etc.) without affecting the main flow. `<figcaption>` provides a visible caption.

While most commonly used for images, `<figure>` is appropriate for any self-contained content block: code listings, charts, diagrams, poems, pull quotes, or tables. Screen readers announce the figure and associate the caption with it.

### 5.6 Video

```html
<video controls width="720" poster="/img/video-poster.jpg" preload="metadata">
  <source src="/video/demo.mp4" type="video/mp4">
  <source src="/video/demo.webm" type="video/webm">
  <track kind="captions" src="/video/demo-en.vtt" srclang="en" label="English" default>
  <p>Your browser doesn't support HTML video. <a href="/video/demo.mp4">Download</a>.</p>
</video>
```

HTML5's native video element eliminated the need for Flash. Here's what each part does:

**`controls`** — shows the browser's built-in play/pause, volume, progress bar, and fullscreen buttons. Without this, the video has no user interface (useful only for background videos).

**`poster`** — a thumbnail image shown before the video starts playing. Without it, the browser shows either nothing or the first frame (which might be black).

**`preload`** — controls how much the browser preloads:
- `"none"` — don't preload anything (saves bandwidth; good for pages with many videos).
- `"metadata"` — only load metadata like duration and dimensions (the best default).
- `"auto"` — the browser decides how much to preload (may download the whole video).

**Multiple `<source>` elements** — the browser picks the first format it supports. MP4 (H.264) is universally supported; WebM offers better compression.

**`<track>`** — adds captions, subtitles, or descriptions in WebVTT format. This is essential for accessibility — deaf and hard-of-hearing users, people in noisy environments, non-native speakers, and users who simply prefer reading along. `kind="captions"` includes both dialogue and sound effects; `kind="subtitles"` is dialogue only.

**Autoplay restrictions:** Most browsers now block autoplay videos with sound. If you need autoplay (for background videos), you must also include the `muted` attribute. `<video autoplay muted loop>` is the standard pattern for background videos.

### 5.7 Audio

```html
<audio controls preload="metadata">
  <source src="/audio/podcast.mp3" type="audio/mpeg">
  <source src="/audio/podcast.ogg" type="audio/ogg">
  <p>Your browser doesn't support HTML audio.</p>
</audio>
```

Works identically to `<video>` but for audio content. Always include `controls` so users can play, pause, and adjust volume. Provide a transcript for accessibility — there's no visual component for screen readers to describe, so a text transcript is the only way for deaf users to access audio content.

### 5.8 SVG Inline

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"
     fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
  <circle cx="12" cy="12" r="10"/>
  <path d="M12 6v6l4 2"/>
</svg>
```

SVG (Scalable Vector Graphics) can be embedded directly in HTML. Unlike raster images (JPEG, PNG), SVGs are resolution-independent — they look crisp at any size. When inlined, you can:
- Style them with CSS: `svg { fill: var(--accent); }` or use `currentColor` to match the surrounding text colour.
- Animate them with CSS transitions or JavaScript.
- Make individual parts interactive.

Add `aria-hidden="true"` for decorative SVGs, or provide `role="img"` and `aria-label="Description"` for meaningful ones.

---

## 6. Lists

Lists are one of the most commonly used HTML structures — for navigation menus, feature lists, step-by-step instructions, glossaries, and more. Using the correct list type gives your content proper semantic meaning.

### 6.1 Unordered List

```html
<ul>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ul>
```

**Use unordered lists when the order doesn't matter** — feature lists, navigation menus, ingredient lists, or any collection where rearranging the items wouldn't change the meaning. Screen readers announce "list, 3 items" and then each item, helping users understand the content structure.

### 6.2 Ordered List

```html
<ol>
  <li>Preheat the oven to 180C</li>
  <li>Mix the dry ingredients</li>
  <li>Add the wet ingredients</li>
</ol>
```

**Use ordered lists when sequence matters** — instructions, rankings, steps in a process, or any list where changing the order would change the meaning.

Ordered lists support several useful attributes:

```html
<!-- Start counting from a specific number -->
<ol start="5">
  <li>This renders as item 5</li>
  <li>This renders as item 6</li>
</ol>

<!-- Count backwards -->
<ol reversed>
  <li>Third place (renders as 3)</li>
  <li>Second place (renders as 2)</li>
  <li>First place (renders as 1)</li>
</ol>

<!-- Use letters or Roman numerals instead of numbers -->
<ol type="a">  <!-- a, b, c, d... -->
<ol type="A">  <!-- A, B, C, D... -->
<ol type="i">  <!-- i, ii, iii, iv... -->
<ol type="I">  <!-- I, II, III, IV... -->
```

### 6.3 Nested Lists

```html
<ul>
  <li>Frontend
    <ul>
      <li>HTML</li>
      <li>CSS</li>
      <li>JavaScript</li>
    </ul>
  </li>
  <li>Backend
    <ul>
      <li>Python</li>
      <li>Node.js</li>
    </ul>
  </li>
</ul>
```

Lists can be nested to create hierarchies. The inner `<ul>` or `<ol>` must be placed **inside a `<li>`**, not directly inside the parent list. Browsers typically change the bullet style for each nesting level (disc, circle, square). Screen readers announce the nesting depth so users understand the hierarchy.

### 6.4 Description List

```html
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language — the standard markup for web pages.</dd>

  <dt>CSS</dt>
  <dd>Cascading Style Sheets — describes the visual presentation of HTML.</dd>

  <dt>JavaScript</dt>
  <dd>A scripting language for dynamic, interactive web content.</dd>
</dl>
```

**Description lists** (`<dl>`) are for name/value pairs — glossaries, metadata, FAQ-style content, or any key/value data. Each term (`<dt>`) can have one or multiple descriptions (`<dd>`), and multiple terms can share a description. Screen readers announce "description list, 3 items" and associate terms with their descriptions.

They're surprisingly versatile — use them for settings panels, contact details (label: value), or product specifications.

---

## 7. Tables

Tables display data in rows and columns. They're the correct choice for **tabular data** — spreadsheets, schedules, comparison charts, financial reports, and similar data that has a natural two-dimensional structure. Never use tables for page layout (that's what CSS Grid and Flexbox are for).

### 7.1 Full Table with All Sections

```html
<table>
  <caption>Quarterly Sales (GBP) — 2026</caption>
  <thead>
    <tr>
      <th scope="col">Quarter</th>
      <th scope="col">Revenue</th>
      <th scope="col">Profit</th>
      <th scope="col">Margin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Q1</td>
      <td>12,400</td>
      <td>3,200</td>
      <td>25.8%</td>
    </tr>
    <tr>
      <td>Q2</td>
      <td>15,800</td>
      <td>4,600</td>
      <td>29.1%</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th scope="row">Total</th>
      <td>28,200</td>
      <td>7,800</td>
      <td>27.7%</td>
    </tr>
  </tfoot>
</table>
```

**Breaking down the elements:**

**`<caption>`** — a visible title/description for the table. This is the first thing screen readers announce, giving users context before they navigate the data. It's also useful for sighted users scanning the page. Always include one.

**`<thead>`** — the header row(s). Contains `<th>` (table header) cells rather than `<td>` (table data) cells. Header cells are bold and centred by default, but more importantly, they establish the meaning of each column. Screen readers use them to announce the column name when navigating cells.

**`<tbody>`** — the body of the table containing the actual data rows. You can have multiple `<tbody>` elements to group rows into logical sections.

**`<tfoot>`** — the footer, typically for totals, summaries, or aggregates. Despite appearing last in the HTML, the browser renders it at the bottom of the table.

**`scope="col"` and `scope="row"`** — these attributes on `<th>` elements tell screen readers whether a header applies to its **column** (downward) or its **row** (rightward). Without `scope`, screen readers have to guess, and they often get it wrong, especially with complex tables. This is one of the most impactful accessibility improvements you can make to a table.

### 7.2 Column & Row Spanning

```html
<table>
  <thead>
    <tr>
      <th rowspan="2">Student</th>
      <th colspan="2">Exam Scores</th>
    </tr>
    <tr>
      <th>Maths</th>
      <th>English</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alice</td>
      <td>92</td>
      <td>88</td>
    </tr>
  </tbody>
</table>
```

**`colspan="2"`** makes a cell span across multiple columns — like merging cells horizontally in Excel. **`rowspan="2"`** makes a cell span multiple rows vertically. These are essential for complex header structures (like grouped column headers) and for cells that logically span multiple entries.

**Accessibility warning:** Spanned cells make tables harder for screen readers to navigate. For complex tables with multiple levels of headers, use `id` on header cells and `headers` on data cells to explicitly associate them:

```html
<th id="q1">Q1</th>
<th id="rev">Revenue</th>
<td headers="q1 rev">12,400</td>
```

### 7.3 Responsive Tables

Tables are inherently wide, and they don't naturally adapt to narrow screens. The simplest responsive pattern is horizontal scrolling:

```html
<div style="overflow-x: auto;">
  <table>
    <!-- Your table content -->
  </table>
</div>
```

Wrapping the table in a scrollable container lets mobile users swipe left/right to see all columns while keeping the table structure intact. For more sophisticated approaches, consider CSS techniques that stack rows vertically or hide less important columns on mobile.

---

## 8. Forms & Inputs

Forms are how users interact with your site — logging in, searching, submitting data, configuring settings. HTML provides a comprehensive set of form controls with built-in validation, accessibility hooks, and browser autofill integration.

### 8.1 Basic Form Structure

```html
<form action="/api/submit" method="post">
  <fieldset>
    <legend>Contact Us</legend>

    <label for="name">Full Name</label>
    <input id="name" name="name" type="text" required autocomplete="name">

    <label for="email">Email</label>
    <input id="email" name="email" type="email" required autocomplete="email"
           placeholder="you@example.com">

    <label for="message">Message</label>
    <textarea id="message" name="message" rows="5" required></textarea>

    <button type="submit">Send Message</button>
  </fieldset>
</form>
```

**Every element serves a specific purpose:**

**`<form>`** — the container. `action` is the URL to send data to. `method` is `get` (data in URL query string — for searches and filters) or `post` (data in request body — for creating/modifying data). Without a `<form>` wrapper, submit buttons and Enter-key submission don't work.

**`<fieldset>` and `<legend>`** — group related fields together. `<legend>` labels the group. Screen readers announce the legend when a user focuses any field in the fieldset, providing crucial context. For example, if you have two address sections (billing and shipping), wrapping each in a fieldset with a legend clarifies which address the user is filling in.

**`<label>`** — associates a text label with a form control. The `for` attribute must match the `id` of the input. This linkage is critical:
- Clicking the label focuses/activates the input (larger click target).
- Screen readers read the label when the input is focused, so users know what information is being requested.
- Without labels, forms are essentially unusable for screen reader users.

**`autocomplete`** — tells the browser what type of data the field expects (`name`, `email`, `tel`, `address-level1`, `cc-number`, etc.). This enables browser autofill, which dramatically reduces friction for users. It also helps password managers fill in forms correctly.

**`placeholder`** — shows hint text inside the input when it's empty. **Never use placeholder as a replacement for labels** — placeholders disappear when the user starts typing, leaving them with no indication of what the field is for. Placeholders also typically fail contrast requirements.

### 8.2 Input Types

HTML5 introduced many specialised input types that provide built-in validation, appropriate on-screen keyboards on mobile, and browser-native UI:

```html
<input type="text">           <!-- generic single-line text -->
<input type="email">          <!-- validates email format; mobile shows @ key -->
<input type="password">       <!-- masks input with dots/asterisks -->
<input type="number" min="0" max="100" step="1">  <!-- number with spinner -->
<input type="tel">            <!-- phone keyboard on mobile (no validation) -->
<input type="url">            <!-- validates URL format -->
<input type="search">         <!-- may show a clear button; search keyboard -->
<input type="date">           <!-- native date picker -->
<input type="time">           <!-- native time picker -->
<input type="datetime-local"> <!-- combined date and time picker -->
<input type="month">          <!-- month and year picker -->
<input type="week">           <!-- week number picker -->
<input type="color">          <!-- colour picker swatch -->
<input type="range" min="0" max="100" step="5">  <!-- slider control -->
<input type="file" accept=".pdf,.docx">           <!-- file upload dialog -->
<input type="file" accept="image/*" multiple>     <!-- multiple image upload -->
<input type="hidden" name="csrf" value="abc123">  <!-- invisible, sent with form -->
```

**The key benefit of specific input types is mobile UX.** An `<input type="email">` shows a keyboard with `@` and `.` prominently displayed. `type="tel"` shows a numeric dialpad. `type="number"` shows a number pad. These small differences make a big impact on form completion rates.

**Dates and times:** The native date/time pickers vary in appearance between browsers and operating systems. They work well for simple cases but may need a JavaScript replacement for complex requirements (date ranges, custom formatting, etc.).

### 8.3 Checkboxes & Radio Buttons

```html
<!-- Checkboxes: users can select multiple options -->
<fieldset>
  <legend>Skills (select all that apply)</legend>
  <label><input type="checkbox" name="skills" value="html"> HTML</label>
  <label><input type="checkbox" name="skills" value="css"> CSS</label>
  <label><input type="checkbox" name="skills" value="js"> JavaScript</label>
  <label><input type="checkbox" name="skills" value="python"> Python</label>
</fieldset>

<!-- Radio buttons: users select exactly one option -->
<fieldset>
  <legend>Experience Level</legend>
  <label><input type="radio" name="level" value="beginner"> Beginner</label>
  <label><input type="radio" name="level" value="intermediate"> Intermediate</label>
  <label><input type="radio" name="level" value="advanced"> Advanced</label>
</fieldset>
```

**Checkboxes** allow multiple selections — they're independent boolean toggles. Each checked box sends its `value` as the form data.

**Radio buttons** allow exactly one selection from a group. Radio buttons with the **same `name`** attribute form a group — selecting one deselects the others. If no default is selected, the user can submit the form without making a choice, so consider adding `checked` to one option or making the field `required`.

**Always wrap checkbox/radio groups in `<fieldset>` with a `<legend>`.** Screen readers announce "Skills, select all that apply" before listing the options, which gives users essential context.

### 8.4 Select Dropdowns

```html
<label for="country">Country</label>
<select id="country" name="country">
  <option value="">-- Select a country --</option>
  <optgroup label="United Kingdom">
    <option value="eng">England</option>
    <option value="wal">Wales</option>
    <option value="sco">Scotland</option>
    <option value="ni">Northern Ireland</option>
  </optgroup>
  <optgroup label="Europe">
    <option value="fr">France</option>
    <option value="de">Germany</option>
  </optgroup>
</select>
```

`<select>` creates a dropdown menu. `<optgroup>` groups options under labelled headers — useful for long lists with natural categories. The first `<option>` with an empty value serves as a prompt; if you add `required` to the `<select>`, the user must choose something other than this placeholder.

**When to use `<select>` vs. radio buttons:** Use radio buttons for 2-5 options that you want visible at all times. Use `<select>` for 6+ options or when screen space is limited. Long `<select>` lists (50+ items) should use a searchable autocomplete instead (see datalist).

### 8.5 Datalist (autocomplete suggestions)

```html
<label for="framework">Framework</label>
<input id="framework" name="framework" list="frameworks" autocomplete="off">
<datalist id="frameworks">
  <option value="React">
  <option value="Vue">
  <option value="Angular">
  <option value="Svelte">
  <option value="HTMX">
</datalist>
```

`<datalist>` provides autocomplete suggestions for a text input. Unlike `<select>`, the user can type freely — the suggestions are just hints, not constraints. As the user types, matching options appear in a dropdown. This is perfect for fields where you want to suggest common values but allow arbitrary input.

### 8.6 Validation Attributes

HTML5 built-in validation lets you enforce rules without JavaScript:

| Attribute | What it does | Example |
|-----------|-------------|---------|
| `required` | Field cannot be submitted empty | `<input required>` |
| `minlength` / `maxlength` | Limits text length | `<input minlength="3" maxlength="50">` |
| `min` / `max` | Limits numeric range | `<input type="number" min="1" max="100">` |
| `pattern` | Must match a regex pattern | `<input pattern="[A-Z]{2}[0-9]{6}">` |
| `step` | Acceptable number increments | `<input type="number" step="0.01">` |

When validation fails, the browser shows a native error tooltip. You can customise the message with `title` (shown as part of the tooltip) or JavaScript's `setCustomValidity()`.

**Important:** Client-side validation is a **UX feature**, not a security feature. Always validate on the server too — client-side validation can be bypassed by anyone with browser developer tools.

### 8.7 Form Encoding

```html
<!-- Default: sends data as key=value&key=value -->
<form method="post" enctype="application/x-www-form-urlencoded">

<!-- Required for file uploads: sends data as multipart message -->
<form method="post" enctype="multipart/form-data">
```

If your form includes `<input type="file">`, you **must** set `enctype="multipart/form-data"`. Without it, the form only sends the filename, not the actual file content.

---

## 9. Semantic & Structural Elements

Semantic HTML is about choosing elements that describe the **meaning** of your content, not just its visual appearance. A `<nav>` isn't just a styled `<div>` — it tells browsers, screen readers, search engines, and other tools "this is navigation." This information is invisible to most sighted users but crucial for accessibility, SEO, and tooling.

### 9.1 Page Structure

```html
<body>
  <header>    <!-- Banner area: logo, site title, primary nav -->
    <nav>     <!-- Navigation links -->
    </nav>
  </header>

  <main>      <!-- The page's primary content (ONE per page) -->
    <article> <!-- Self-contained piece of content -->
      <section> <!-- Thematic grouping within the article -->
      </section>
    </article>
    <aside>   <!-- Related but tangential content (sidebar) -->
    </aside>
  </main>

  <footer>    <!-- Site footer: copyright, secondary links -->
  </footer>
</body>
```

### 9.2 Detailed Element Guide

**`<header>`** — introductory content for the page or a section. A page typically has one site-wide header (with logo and nav) and can have additional headers on individual `<article>` elements (with the article title and metadata). Screen readers identify this as the "banner" landmark.

**`<nav>`** — a section of navigation links. Use it for major navigation blocks (main menu, footer nav, breadcrumbs, pagination) but not for every random group of links. If you have multiple `<nav>` elements, distinguish them with `aria-label`: `<nav aria-label="Main">` and `<nav aria-label="Footer">`. Screen readers list all navigation landmarks, so labels help users pick the right one.

**`<main>`** — the dominant content of the page, unique to this page (not repeated across pages like headers and footers). There must be only **one** `<main>` per page (or only one visible at a time if you have multiple). Screen readers use it as the "main" landmark — this is what skip links jump to.

**`<article>`** — a self-contained composition that makes sense independently. Blog posts, news articles, forum posts, product cards, comments — anything that could be syndicated (shared via RSS, reposted) is an article. Each article should have its own heading.

**`<section>`** — a thematic grouping of content, typically with a heading. Sections are like chapters in a book — each covers a distinct subtopic. Use `<section>` when the content has a natural heading; if you'd just use it as a generic wrapper, a `<div>` is more appropriate.

**`<aside>`** — content that's tangentially related to the surrounding content. Sidebars, pull quotes, advertising, author bios, or "related articles" links. On a blog post, the post itself is in `<main>/<article>` and the sidebar with categories, archives, and ads is `<aside>`.

**`<footer>`** — footer information for the nearest `<article>` or `<body>`. Site footers typically contain copyright notices, secondary navigation, legal links, and contact information. Article footers might contain author info, publish date, or share buttons.

### 9.3 `<div>` and `<span>` — Generic Containers

```html
<div class="wrapper">Block-level generic container</div>
<span class="highlight">Inline generic container</span>
```

`<div>` and `<span>` are semantically meaningless — they're pure containers for styling and scripting purposes. Use them **only** when no semantic element fits. If you find yourself writing `<div class="nav">`, that should be `<nav>`. If you're writing `<div class="footer">`, that should be `<footer>`.

### 9.4 `<template>` — Hidden Reusable Markup

```html
<template id="notification-template">
  <div class="notification">
    <p class="notification-text"></p>
    <button class="dismiss">Dismiss</button>
  </div>
</template>

<script>
  function showNotification(message) {
    const template = document.getElementById('notification-template');
    const clone = template.content.cloneNode(true);
    clone.querySelector('.notification-text').textContent = message;
    document.body.appendChild(clone);
  }
</script>
```

Content inside `<template>` is completely **inert** — it's not rendered, scripts inside it don't execute, images don't load, and it's not part of the DOM. It's a fragment of HTML that you clone and insert with JavaScript. This is the foundation of many client-side templating patterns and Web Components.

---

## 10. Interactive Elements

HTML provides several built-in interactive elements that work without JavaScript. These native controls are accessible by default, keyboard-operable, and understood by all browsers.

### 10.1 `<details>` / `<summary>` — Collapsible Content

```html
<details>
  <summary>What is HTML?</summary>
  <p>HTML (HyperText Markup Language) is the standard language for 
     creating and structuring web pages and applications.</p>
</details>

<details open>
  <summary>This section starts expanded</summary>
  <p>The <code>open</code> attribute controls the initial state.</p>
</details>
```

This is a native, zero-JavaScript accordion/disclosure widget. Clicking the summary toggles visibility of the rest of the content. It's fully keyboard-accessible (Enter/Space to toggle) and screen readers announce the expanded/collapsed state.

**Use cases:** FAQs, advanced settings, spoiler text, collapsible code examples, "show more" sections. The `open` attribute can be toggled via JavaScript to programmatically open/close sections.

### 10.2 `<dialog>` — Native Modal

```html
<dialog id="confirm-dialog">
  <h2>Delete Document?</h2>
  <p>This action cannot be undone.</p>
  <form method="dialog">
    <button value="cancel">Cancel</button>
    <button value="delete">Delete</button>
  </form>
</dialog>

<button onclick="document.getElementById('confirm-dialog').showModal()">
  Delete
</button>
```

The `<dialog>` element provides a native modal dialog with built-in behaviours that would take hundreds of lines of JavaScript to replicate:
- **Focus trapping:** Tab key cycles only through elements inside the dialog.
- **Backdrop:** Shows a dimmed overlay behind the dialog (styleable with `::backdrop`).
- **Escape key:** Pressing Escape closes the dialog.
- **Focus restoration:** When the dialog closes, focus returns to the element that opened it.
- **Inert background:** Content behind the dialog is non-interactive.

`<form method="dialog">` is special — submitting the form closes the dialog and sets `dialog.returnValue` to the value of the button that was clicked. This makes it easy to handle "confirm/cancel" patterns.

```css
dialog::backdrop {
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
}
```

### 10.3 `<progress>` and `<meter>`

```html
<!-- Progress bar: shows completion of a task -->
<label for="upload">Upload progress:</label>
<progress id="upload" value="70" max="100">70%</progress>

<!-- Indeterminate progress (no value): shows an animation -->
<progress>Loading...</progress>

<!-- Meter: shows a scalar value within a known range -->
<label for="disk">Disk usage:</label>
<meter id="disk" value="0.7" min="0" max="1" low="0.3" high="0.8" optimum="0.5">70%</meter>
```

**`<progress>`** represents the completion of a task. With a `value`, it shows a determinate progress bar. Without a `value`, it shows an animated indeterminate indicator (pulsing or spinning, depending on the browser/OS).

**`<meter>`** represents a scalar measurement within a known range — disk usage, password strength, temperature. The `low`, `high`, and `optimum` attributes let the browser colour the gauge green/yellow/red automatically (e.g., a meter that turns red when disk usage exceeds 80%).

**Don't confuse them:** Progress is for **task completion** (0% to 100%). Meter is for **measurements** (a value within a range).

---

## 11. Embedding & Iframes

### 11.1 Iframes

```html
<iframe
  src="https://www.youtube.com/embed/dQw4w9WgXcQ"
  width="560" height="315"
  title="YouTube video player"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope"
  allowfullscreen
  loading="lazy"
></iframe>
```

An `<iframe>` embeds an entire separate HTML document inside your page. It's essentially a window into another webpage. Common uses include embedding YouTube videos, Google Maps, social media posts, payment forms, and third-party widgets.

**Always include a `title` attribute** — it's the only way screen readers can describe what the iframe contains. Without it, screen readers just say "frame" which is meaningless.

**`loading="lazy"`** defers loading iframes until they're near the viewport — especially valuable for video embeds which are often heavy (downloading megabytes of JavaScript).

### 11.2 Sandboxing

```html
<iframe src="/widget" sandbox="allow-scripts allow-same-origin" title="Widget"></iframe>
```

The `sandbox` attribute restricts what the embedded content can do. A plain `sandbox` (no value) blocks almost everything — scripts, forms, popups, top-level navigation, and plugins. You then selectively re-enable permissions:

| Permission | What it allows |
|------------|---------------|
| `allow-scripts` | JavaScript execution |
| `allow-same-origin` | Access to same-origin data (cookies, localStorage) |
| `allow-forms` | Form submission |
| `allow-popups` | Opening new windows/tabs |
| `allow-modals` | Using `alert()`, `confirm()`, `prompt()` |
| `allow-top-navigation` | Navigating the parent page |

Sandboxing is a crucial security feature when embedding third-party content. Even if a widget is compromised, the sandbox limits the damage it can do.

---

## 12. Global Attributes

Global attributes can be applied to **any** HTML element. Here are the most important ones with detailed explanations:

| Attribute | Purpose | When to use |
|-----------|---------|-------------|
| `id` | Unique identifier for the element | Fragment links, JavaScript targeting, label association, ARIA references |
| `class` | One or more CSS class names | Styling and JavaScript selection |
| `style` | Inline CSS styles | Quick overrides (avoid for production; prefer external CSS) |
| `title` | Tooltip text on hover | Abbreviation expansions, extra context |
| `lang` | Language of the element's content | Content in a different language than the page |
| `hidden` | Hides the element from rendering and accessibility tree | Content that should be invisible |
| `tabindex` | Controls keyboard tab order | Making non-interactive elements focusable (0) or removing focus (-1) |
| `data-*` | Custom data storage | Passing data between HTML and JavaScript |
| `inert` | Makes element and children non-interactive | Content behind modals, disabled sections |

### 12.1 Custom Data Attributes

```html
<article data-category="python" data-difficulty="intermediate" data-doc-id="42">
  <h2>Building REST APIs</h2>
</article>

<script>
  const article = document.querySelector('article');
  
  // Access via the dataset API (camelCase conversion)
  console.log(article.dataset.category);    // "python"
  console.log(article.dataset.difficulty);  // "intermediate"
  console.log(article.dataset.docId);       // "42" (note: data-doc-id → docId)
  
  // Set new data attributes
  article.dataset.lastModified = '2026-02-17';
  // This adds data-last-modified="2026-02-17" to the element
</script>
```

`data-*` attributes let you embed custom data in HTML elements that JavaScript can read. They're the official, spec-compliant way to pass information between your HTML and your scripts. The `dataset` property provides a convenient API for reading and writing them.

**Naming rules:** After `data-`, the attribute name must be lowercase, hyphen-separated. In JavaScript's `dataset`, hyphens are converted to camelCase: `data-doc-id` becomes `dataset.docId`.

---

## 13. ARIA & Accessibility

ARIA (Accessible Rich Internet Applications) is a set of attributes that enhance HTML's accessibility for users of screen readers and other assistive technologies. The golden rule: **use semantic HTML first.** Only reach for ARIA when native HTML can't express the semantics you need.

### 13.1 The Five Rules of ARIA

1. **Don't use ARIA if you can use native HTML.** A `<button>` is always better than `<div role="button">`.
2. **Don't change native semantics** unless you really have to. Don't put `role="heading"` on a `<div>` when you could use `<h2>`.
3. **All interactive ARIA controls must be keyboard operable.** If you add `role="button"`, you must also handle Enter and Space key presses.
4. **Don't use `role="presentation"` or `aria-hidden="true"` on focusable elements.** This makes them invisible to screen readers but still focusable — confusing and broken.
5. **All interactive elements must have an accessible name.** Every button, link, and input must have a label that screen readers can announce.

### 13.2 Landmark Roles

Semantic HTML elements automatically create ARIA landmarks:

```html
<header>  → role="banner"         (page header)
<nav>     → role="navigation"     (navigation)
<main>    → role="main"           (main content)
<aside>   → role="complementary"  (sidebar)
<footer>  → role="contentinfo"    (page footer)
```

Screen readers let users jump directly between landmarks. Use `aria-label` to distinguish multiple elements of the same type:

```html
<nav aria-label="Primary">...</nav>
<nav aria-label="Footer">...</nav>
```

### 13.3 Essential ARIA Attributes

**`aria-label`** — provides an invisible accessible name. Use when there's no visible text:
```html
<button aria-label="Close dialog">✕</button>
```

**`aria-labelledby`** — points to another element whose text content becomes the accessible name:
```html
<h2 id="settings-title">Account Settings</h2>
<section aria-labelledby="settings-title">...</section>
```

**`aria-describedby`** — provides additional descriptive text:
```html
<input type="password" aria-describedby="pw-help">
<p id="pw-help">Must be at least 8 characters with one uppercase letter.</p>
```

**`aria-expanded`** — indicates whether a collapsible element is open or closed:
```html
<button aria-expanded="false" aria-controls="menu">Menu</button>
<ul id="menu" hidden>...</ul>
```

**`aria-live`** — makes screen readers announce dynamic content changes:
```html
<div aria-live="polite">3 new messages</div>   <!-- announced after current speech -->
<div aria-live="assertive">Error occurred!</div> <!-- announced immediately -->
```

**`aria-current`** — indicates the current item in a set:
```html
<a href="/docs" aria-current="page">Docs</a>  <!-- current page in navigation -->
```

**`aria-hidden="true"`** — hides an element from screen readers. Use for decorative content:
```html
<span aria-hidden="true">🎨</span> Colour picker
```

### 13.4 Accessibility Checklist

Every web page should meet these fundamental requirements:

- [ ] `<html>` has a `lang` attribute
- [ ] Every page has a unique, descriptive `<title>`
- [ ] Heading hierarchy is correct (no skipped levels)
- [ ] All images have meaningful `alt` text (or `alt=""` for decorative)
- [ ] All form inputs have associated `<label>` elements
- [ ] Keyboard navigation works logically (tab order makes sense)
- [ ] Focus indicators are visible (never `outline: none` without a replacement)
- [ ] Colour contrast meets WCAG AA (4.5:1 for normal text, 3:1 for large text)
- [ ] All interactive elements work with keyboard alone (no mouse required)
- [ ] Dynamic content changes are announced via `aria-live`
- [ ] No information is conveyed by colour alone (use icons, text, patterns too)
- [ ] Videos have captions; audio has transcripts
- [ ] Skip link is present as the first focusable element

---

## 14. Performance

Performance isn't just about speed — it directly affects user engagement, conversion rates, and search ranking. Google uses Core Web Vitals (loading, interactivity, visual stability) as ranking factors.

### 14.1 Critical Rendering Path

Understanding how browsers render pages helps you optimise effectively:

1. **HTML parsing → DOM:** The browser reads your HTML and builds a tree of elements (the Document Object Model).
2. **CSS parsing → CSSOM:** CSS files are parsed into a tree of style rules.
3. **Render tree:** DOM + CSSOM are combined to determine what's visible and how it looks.
4. **Layout:** The browser calculates the exact position and size of every element.
5. **Paint:** Pixels are drawn to the screen.

**CSS blocks rendering** — the browser won't paint until it has all the CSS, because a late-arriving stylesheet could change everything. This is why CSS should be in `<head>` (discovered early) and as small as possible.

**JavaScript blocks parsing** (without `defer`/`async`) — if the parser hits a `<script>` tag, it stops building the DOM until the script is downloaded and executed. This is why `defer` is so important.

### 14.2 Image Optimisation Checklist

Images typically account for 50-80% of a page's total weight. Here's how to minimise their impact:

1. **Use modern formats** — AVIF and WebP are 30-50% smaller than JPEG at equivalent quality. Use `<picture>` to serve them with JPEG fallback.
2. **Set dimensions** — Always include `width` and `height` to prevent layout shift.
3. **Lazy-load below-the-fold images** — `loading="lazy"` defers downloading until they're needed.
4. **Prioritise the LCP image** — Use `fetchpriority="high"` on the largest above-the-fold image.
5. **Use responsive images** — Serve smaller files to small screens with `srcset` and `sizes`.
6. **Compress aggressively** — Most images can be compressed 60-80% with no visible quality loss.

### 14.3 Resource Hints

| Hint | What it does | When to use |
|------|-------------|-------------|
| `preload` | Downloads a specific resource immediately at high priority | Fonts, hero images, critical CSS |
| `preconnect` | Opens an early connection to a server (DNS + TCP + TLS) | CDNs, API servers, font providers |
| `dns-prefetch` | Only resolves the domain name (lighter than preconnect) | Third-party origins you might need |
| `prefetch` | Downloads a resource at low priority for future navigation | Assets needed on the likely next page |

**Don't overdo it** — each hint consumes browser resources. Limit to 2-4 truly critical resources.

---

## 15. SEO & Social Sharing

### 15.1 Structured Data (JSON-LD)

JSON-LD lets you tell search engines exactly what your content is — an article, a product, a recipe, an FAQ, an event. This enables **rich search results** (snippets with images, ratings, prices, FAQ expandable sections):

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "HTML Complete Guide",
  "datePublished": "2026-02-17",
  "author": { "@type": "Person", "name": "Harry Gomm" },
  "publisher": { "@type": "Organization", "name": "Documentation Hub" },
  "description": "A comprehensive HTML reference with practical examples."
}
</script>
```

Place JSON-LD in a `<script type="application/ld+json">` tag (usually in `<head>` or at the end of `<body>`). Google recommends JSON-LD over the older Microdata format.

### 15.2 Robots Control

```html
<meta name="robots" content="index, follow">       <!-- default: index this page, follow links -->
<meta name="robots" content="noindex, nofollow">   <!-- hide page from search, don't follow links -->
<meta name="robots" content="noindex, follow">     <!-- hide page, but follow links to discover other pages -->
```

Use `noindex` for pages you don't want in search results: admin panels, staging, login pages, thank-you pages, paginated duplicates. Use `nofollow` to prevent search engines from following outgoing links (rarely needed on your own site).

---

## 16. Security

Web security starts in your HTML. Several HTML-level features help protect your users from attacks.

### 16.1 Content Security Policy (CSP)

```html
<meta http-equiv="Content-Security-Policy"
      content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:;">
```

CSP is a **defence-in-depth** measure against Cross-Site Scripting (XSS). It tells the browser "only execute scripts from my own domain" — so even if an attacker manages to inject a `<script>` tag into your page, the browser refuses to run it because it doesn't come from an approved source.

CSP is better set as an HTTP header (more reliable, can't be bypassed if the meta tag is injected after a malicious script), but the meta tag works for static sites and development.

### 16.2 Preventing XSS

```javascript
// DANGEROUS — never insert untrusted content as HTML:
element.innerHTML = userInput;  // If userInput is "<script>steal()</script>", it executes!

// SAFE — textContent escapes HTML automatically:
element.textContent = userInput;  // "<script>" renders as literal text, not code
```

XSS (Cross-Site Scripting) is the most common web vulnerability. It occurs when user-provided content is inserted into the page as executable HTML or JavaScript. Always use `textContent` or proper escaping when displaying user input.

### 16.3 Subresource Integrity (SRI)

```html
<script src="https://cdn.example.com/lib.min.js"
        integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8w"
        crossorigin="anonymous"></script>
```

When loading scripts or styles from a CDN, SRI verifies that the file hasn't been tampered with. The `integrity` attribute contains a cryptographic hash of the expected file contents. If the CDN serves a different file (because it's compromised), the browser refuses to load it.

---

## 17. Responsive Design

Responsive design ensures your site looks and works well on all screen sizes — from 320px mobile phones to 2560px ultrawide monitors.

### 17.1 Mobile-First Approach

```css
/* Base styles: designed for the smallest screens */
.container { padding: 16px; }

/* Layer on complexity as screens get wider */
@media (min-width: 768px) {
  .container { padding: 24px; max-width: 720px; margin: 0 auto; }
}

@media (min-width: 1024px) {
  .container { max-width: 960px; }
}
```

Mobile-first means writing your base CSS for small screens, then using `min-width` media queries to add layout complexity for larger screens. This approach ensures mobile users (often on slower connections) download the simplest CSS, and bigger screens get progressive enhancement.

### 17.2 Common Breakpoints

| Name | Width | Typical devices |
|------|-------|-----------------|
| Small | < 768px | Phones |
| Medium | 768px+ | Tablets, large phones (landscape) |
| Large | 1024px+ | Laptops, small desktops |
| XL | 1280px+ | Desktops |
| 2XL | 1536px+ | Large monitors |

### 17.3 Fluid Typography

```css
/* Font size smoothly scales between 16px and 24px based on viewport width */
html {
  font-size: clamp(1rem, 0.5rem + 1.5vw, 1.5rem);
}
```

`clamp()` sets a minimum, a fluid value, and a maximum. This eliminates the need for font-size media queries in most cases and creates a smooth scaling experience across all viewport widths.

---

## 18. HTML Entities & Special Characters

HTML entities represent characters that are either reserved in HTML syntax or not available on a standard keyboard. In UTF-8 documents, you can type most characters directly, but entities are essential for `<`, `>`, and `&` which would otherwise be interpreted as HTML.

| Character | Entity | Description |
|-----------|--------|-------------|
| < | `&lt;` | Less than (required — otherwise parsed as a tag) |
| > | `&gt;` | Greater than (recommended in content) |
| & | `&amp;` | Ampersand (required — otherwise parsed as entity start) |
| " | `&quot;` | Double quote (required inside attribute values) |
| (non-breaking space) | `&nbsp;` | Prevents line break between words |
| -- | `&mdash;` | Em dash (—) |
| - | `&ndash;` | En dash (–) |
| ... | `&hellip;` | Ellipsis (...) |
| (c) | `&copy;` | Copyright symbol |
| GBP | `&pound;` | Pound sign |

**`&nbsp;` deserves special mention.** It's not just a space — it's a **non-breaking** space that prevents the browser from wrapping a line between two words. Use it between a number and its unit ("100&nbsp;km") or between a title and a name ("Mr&nbsp;Smith") to keep them on the same line.

---

## 19. Common Patterns & Templates

### 19.1 Card Component

```html
<article class="card">
  <img src="/img/thumbnail.webp" alt="Project screenshot" loading="lazy">
  <div class="card-body">
    <h3>Project Name</h3>
    <p>A short description of what this project does and why it matters.</p>
    <div class="card-tags">
      <span class="tag">Python</span>
      <span class="tag">API</span>
    </div>
    <a href="/projects/name" class="card-link">View Project</a>
  </div>
</article>
```

Cards are one of the most common UI patterns on the web. Using `<article>` makes each card a self-contained piece of content that is meaningful on its own.

### 19.2 Navigation with Mobile Menu

```html
<header class="site-header">
  <a href="/" class="logo">MyDocs</a>

  <button class="menu-toggle" aria-expanded="false" aria-controls="main-nav"
          aria-label="Toggle navigation menu">
    <span class="hamburger"></span>
  </button>

  <nav id="main-nav" aria-label="Main navigation">
    <ul>
      <li><a href="/" aria-current="page">Home</a></li>
      <li><a href="/docs">Docs</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
</header>
```

Note the ARIA attributes on the toggle button: `aria-expanded` tells screen readers whether the menu is open (must be updated with JavaScript), `aria-controls` associates the button with the nav it controls, and `aria-label` provides a name since the button only contains a visual hamburger icon.

### 19.3 Breadcrumbs

```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumbs">
    <li><a href="/">Home</a></li>
    <li><a href="/docs">Docs</a></li>
    <li aria-current="page">HTML Guide</li>
  </ol>
</nav>
```

Breadcrumbs use an **ordered list** (because the hierarchy order matters) inside a `<nav>` with an `aria-label` to distinguish it from the main navigation. The last item uses `aria-current="page"` rather than being a link, since users are already on that page.

### 19.4 Full Page Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page Title — Site Name</title>
  <meta name="description" content="Page description for search results.">
  <link rel="canonical" href="https://example.com/page">
  <meta property="og:title" content="Page Title">
  <meta property="og:description" content="Description for social sharing.">
  <meta property="og:image" content="https://example.com/img/og.png">
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="stylesheet" href="/css/style.css">
</head>
<body>
  <a href="#main" class="skip-link">Skip to main content</a>

  <header>
    <nav aria-label="Main">
      <a href="/" class="logo">Site</a>
      <ul>
        <li><a href="/docs">Docs</a></li>
        <li><a href="/about">About</a></li>
      </ul>
    </nav>
  </header>

  <main id="main">
    <article>
      <h1>Page Title</h1>
      <p>Content goes here...</p>
    </article>
  </main>

  <footer>
    <p>&copy; 2026 Site Name. All rights reserved.</p>
  </footer>

  <script src="/js/app.js" defer></script>
</body>
</html>
```

---

## 20. Validation & Debugging

### 20.1 Tools

- **W3C Validator** (https://validator.w3.org/) — the official HTML validator. Paste a URL or upload code to check for errors.
- **Lighthouse** (Chrome DevTools) — audits performance, accessibility, best practices, and SEO with scores and specific recommendations.
- **axe DevTools** — a browser extension that catches accessibility violations with clear explanations and fix suggestions.
- **Chrome DevTools Accessibility Tree** — shows how screen readers interpret your page structure.

### 20.2 Common HTML Errors

| Error | What causes it | How to fix it |
|-------|----------------|---------------|
| "Element X not allowed as child of Y" | Nesting violation (e.g. `<div>` inside `<p>`) | Check which elements can contain which |
| "Duplicate ID" | Two elements with the same `id` | IDs must be unique per page |
| "Missing alt attribute" | `<img>` without `alt` | Add `alt="description"` or `alt=""` for decorative |
| "Unclosed element" | Missing closing tag | Add `</div>`, `</p>`, etc. |
| "Stray end tag" | Closing tag without matching opening tag | Remove it |
| "Empty heading" | `<h2></h2>` with no content | Add heading text or remove the element |

### 20.3 Nesting Rules to Remember

The HTML parser has strict rules about which elements can contain which. The most common mistakes:

- **`<p>` cannot contain block elements.** `<p><div>text</div></p>` is invalid — the browser auto-closes the `<p>` before the `<div>`, creating two separate elements and an orphan `</p>`.
- **`<a>` cannot contain `<a>`.** Nested links are invalid and produce unpredictable behaviour.
- **Interactive elements cannot contain other interactive elements.** `<button>` inside `<a>`, or `<a>` inside `<button>`, are both invalid.
- **`<ul>` and `<ol>` can only contain `<li>` as direct children.** Don't put `<div>` directly inside a list.

---

## 21. Quick-Reference Cheatsheet

### Document Skeleton
```
<!DOCTYPE html>              Standards mode
<html lang="en">             Root + language
<head>                       Metadata
<body>                       Visible content
```

### Head Essentials
```
<meta charset="utf-8">       Encoding (first in head)
<meta name="viewport" ...>   Mobile responsive
<title>                       Tab/search title
<link rel="stylesheet" ...>  CSS
<script defer>               JS (non-blocking)
```

### Semantic Layout
```
<header>     Page header / banner
<nav>        Navigation links
<main>       Primary content (one per page)
<article>    Self-contained content
<section>    Thematic group with heading
<aside>      Sidebar / related content
<footer>     Page footer
```

### Text
```
<h1>-<h6>    Heading hierarchy
<p>          Paragraph
<strong>     Strong importance (bold)
<em>         Stress emphasis (italic)
<code>       Inline code
<pre>        Preformatted block
<blockquote> Extended quotation
```

### Media
```
<img>        Image (always set alt)
<picture>    Format/art-direction switching
<video>      Video (use controls + track)
<audio>      Audio (use controls)
<figure>     Media + caption wrapper
<svg>        Inline vector graphic
```

### Forms
```
<form>       Container (action + method)
<label>      Input label (always use for=)
<input>      Field (many types available)
<textarea>   Multi-line text
<select>     Dropdown
<button>     Action trigger
<fieldset>   Group with <legend>
```

---

## 22. Further Reading

### Official Specifications
- **MDN Web Docs — HTML:** https://developer.mozilla.org/en-US/docs/Web/HTML
- **HTML Living Standard (WHATWG):** https://html.spec.whatwg.org/

### Accessibility
- **WebAIM:** https://webaim.org/
- **WCAG 2.2 Guidelines:** https://www.w3.org/TR/WCAG22/
- **ARIA Authoring Practices Guide:** https://www.w3.org/WAI/ARIA/apg/

### Performance
- **web.dev:** https://web.dev/
- **Core Web Vitals:** https://web.dev/vitals/

### Tools
- **W3C Validator:** https://validator.w3.org/
- **Can I Use:** https://caniuse.com/
- **Lighthouse:** Built into Chrome DevTools
- **axe DevTools:** Browser extension for accessibility testing

---

*This guide is designed as a practical coding-time reference. Keep it open alongside your editor for quick lookups, deep explanations, and copy-pasteable patterns.*
