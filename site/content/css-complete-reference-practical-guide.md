# CSS Complete Reference & Practical Guide

A comprehensive, hands-on reference for writing modern CSS. This guide explains not just *how* to use CSS, but *why* the language works the way it does — covering the cascade, the box model, layout systems, and everything in between. It's designed to be kept open beside your editor, whether you are writing your first stylesheet or debugging a flexbox edge case.

---

## Table of Contents

1. [What Is CSS & How It Works](#1-what-is-css--how-it-works)
2. [Adding CSS to a Page](#2-adding-css-to-a-page)
3. [Selectors](#3-selectors)
4. [The Cascade, Specificity & Inheritance](#4-the-cascade-specificity--inheritance)
5. [The Box Model](#5-the-box-model)
6. [Display & Layout Fundamentals](#6-display--layout-fundamentals)
7. [Flexbox](#7-flexbox)
8. [CSS Grid](#8-css-grid)
9. [Positioning & Stacking Contexts](#9-positioning--stacking-contexts)
10. [Typography & Fonts](#10-typography--fonts)
11. [Colors, Gradients & Backgrounds](#11-colors-gradients--backgrounds)
12. [Pseudo-classes & Pseudo-elements](#12-pseudo-classes--pseudo-elements)
13. [Custom Properties (CSS Variables)](#13-custom-properties-css-variables)
14. [Responsive Design & Media Queries](#14-responsive-design--media-queries)
15. [Transitions & Animations](#15-transitions--animations)
16. [Transforms (2D & 3D)](#16-transforms-2d--3d)
17. [CSS Functions](#17-css-functions)
18. [Shadows, Filters & Visual Effects](#18-shadows-filters--visual-effects)
19. [CSS Reset & Normalisation](#19-css-reset--normalisation)
20. [CSS Architecture](#20-css-architecture)
21. [Quick-Reference Cheatsheet](#21-quick-reference-cheatsheet)
22. [Further Reading](#22-further-reading)

---

## 1. What Is CSS & How It Works

CSS (Cascading Style Sheets) is the language that controls the visual presentation of HTML documents. While HTML defines *what* content is, CSS defines *how* it looks — its colour, size, spacing, position, animation, and more.

### 1.1 The Rendering Pipeline

When a browser loads a page, it follows a precise sequence:

1. **Parse HTML** → build the DOM (Document Object Model)
2. **Parse CSS** → build the CSSOM (CSS Object Model)
3. **Combine DOM + CSSOM** → build the Render Tree (only visible nodes)
4. **Layout** → calculate the size and position of every box
5. **Paint** → fill in pixels (colours, text, images, borders)
6. **Composite** → layer the painted tiles onto the screen

Understanding this pipeline explains why certain CSS properties are expensive. Changing `color` only triggers a repaint. Changing `width` or `height` triggers a layout *and* repaint. Using `transform` or `opacity` for animations is cheap because they operate at the compositing stage without triggering layout or paint — which is why they are the backbone of performant animation.

### 1.2 The Syntax

Every CSS rule has the same structure:

```css
selector {
  property: value;
  property: value;
}
```

A **selector** targets one or more HTML elements. A **declaration block** (inside `{ }`) contains one or more **declarations**. Each declaration is a `property: value` pair ended with a semicolon.

```css
/* This is a CSS comment */

h1 {
  color: #1a1a2e;
  font-size: 2rem;
  margin-bottom: 1rem;
}
```

```html
<!-- HTML -->
<h1>Getting Started</h1>
<p>Body text follows below.</p>
```

**🖥 Rendered output:**

<div style="border:1px solid #e0e0e0;border-radius:8px;padding:24px 28px;background:#fff;font-family:'Segoe UI',system-ui,sans-serif;">
  <h1 style="font-size:2rem;color:#1a1a2e;font-weight:700;margin:0 0 1rem 0;">Getting Started</h1>
  <p style="font-size:1rem;color:#444;margin:0;">Body text follows below.</p>
</div>

### 1.3 At-rules

CSS also has **at-rules**, which are instructions starting with `@` that control the meta-level behaviour of CSS:

```css
@import url("reset.css");          /* Import another stylesheet */
@media (max-width: 768px) { ... }  /* Apply rules conditionally */
@keyframes slide-in { ... }        /* Define an animation */
@font-face { ... }                 /* Load a custom font */
@layer base, components, utilities;/* Control cascade layering */
```

---

## 2. Adding CSS to a Page

There are three ways to apply CSS. Only one of them belongs in production code.

### 2.1 External Stylesheet (Recommended)

```html
<head>
  <link rel="stylesheet" href="/css/style.css">
</head>
```

External stylesheets are the correct approach for any real project. The browser caches the file, so it only downloads it once per deployment. The CSS is separate from your HTML, making both easier to read, maintain, and test.

**Use this method for everything except trivial static pages.**

### 2.2 The `<style>` Element

```html
<head>
  <style>
    body {
      font-family: sans-serif;
    }
  </style>
</head>
```

Embedding a `<style>` block in HTML is sometimes used for **Critical CSS** — the minimum CSS to render above-the-fold content without a network round-trip. Frameworks and build tools generate this automatically. For hand-written CSS, avoid it.

### 2.3 Inline Styles

```html
<p style="color: red; font-size: 14px;">Hello</p>
```

Inline styles have the highest specificity of any author styles (short of `!important`) and cannot be overridden from a stylesheet without fighting specificity. They cannot use media queries, pseudo-classes, or animations. They are a maintenance nightmare. **Do not use inline styles in production** — their only legitimate uses are JavaScript-driven dynamic values and HTML emails.

### 2.4 The `@import` Rule

```css
/* style.css */
@import url("typography.css");
@import url("layout.css");
```

`@import` must appear before all other rules in a stylesheet. It forces the browser to download each file sequentially, creating a chain of blocking requests. **Prefer multiple `<link>` elements or a build tool bundler over `@import`.**

> **Note:** CSS is render-blocking. The browser will not display anything until all linked stylesheets have been downloaded and parsed. If a stylesheet is large or on a slow network, this delays the first paint. This is why critical CSS inlining exists — but optimising for it is a build-step concern, not something you solve in authoring.

---

## 3. Selectors

Selectors are the means by which you target elements. Mastering them is the difference between writing CSS that fights the cascade and CSS that flows with it.

### 3.1 Basic Selectors

| Selector | Example | What it targets |
|---|---|---|
| Type | `p` | All `<p>` elements |
| Class | `.btn` | Elements with `class="btn"` |
| ID | `#header` | The element with `id="header"` |
| Universal | `*` | Every element |
| Attribute | `[type="text"]` | `<input type="text">` |

```css
/* Type */
h2 { font-size: 1.5rem; }

/* Class — reusable, preferred for styling */
.card { border-radius: 8px; }

/* ID — high specificity, hard to override, best avoided for styling */
#sidebar { width: 300px; }

/* Universal — use with care, targets everything */
* { box-sizing: border-box; }
```

> **Why prefer classes over IDs?** IDs are unique per page and have much higher specificity than classes. This makes them difficult to override without using `!important` or another ID. Reserve IDs for JavaScript hooks and anchor links. Use classes for all styling.

### 3.2 Combinators

Combinators describe relationships between elements.

```css
/* Descendant — any .note inside article, no matter how deep */
article .note { font-style: italic; }

/* Child — only direct children of nav */
nav > a { padding: 0.5rem; }

/* Adjacent sibling — the first p directly after h2 */
h2 + p { font-weight: bold; }

/* General sibling — all p elements that share a parent with h2 */
h2 ~ p { margin-top: 0.5rem; }
```

### 3.3 Attribute Selectors

```css
/* Has the attribute */
[disabled] { opacity: 0.5; cursor: not-allowed; }

/* Exact value */
[type="submit"] { background: #0056b3; }

/* Value starts with */
a[href^="https"] { color: green; }

/* Value ends with */
a[href$=".pdf"]::after { content: " (PDF)"; }

/* Value contains substring */
a[href*="example.com"] { color: orange; }

/* Space-separated list contains word */
[class~="active"] { font-weight: bold; }

/* Hyphen-separated prefix */
[lang|="en"] { font-family: serif; }
```

### 3.4 Selector Lists

Comma-separate selectors to apply the same rules to multiple targets:

```css
h1, h2, h3 {
  font-family: "Georgia", serif;
  line-height: 1.2;
}
```

> **Warning:** If *any* selector in a comma-separated list is invalid, the **entire rule is thrown out** in older browsers. When using experimental selectors alongside standard ones, write them as separate rules.

### 3.5 Specificity at a Glance

Every selector has a specificity weight, calculated as three buckets — `(A, B, C)`:

- **A** — ID selectors (`#id`)
- **B** — class selectors (`.class`), attribute selectors, pseudo-classes
- **C** — type selectors (`p`, `div`), pseudo-elements

```
p                    → (0, 0, 1)
.card                → (0, 1, 0)
#header              → (1, 0, 0)
p.card               → (0, 1, 1)
#header .nav > a     → (1, 1, 1)
```

The full specificity rules are covered in the next chapter.

---

## 4. The Cascade, Specificity & Inheritance

The cascade is CSS's most fundamental and most misunderstood concept. It determines which declaration wins when multiple rules target the same element and property.

### 4.1 What is the Cascade?

The cascade is an algorithm. When two or more declarations conflict on the same property for the same element, the browser resolves the conflict by applying rules in this order:

1. **Origin & importance** — who wrote it, and did they use `!important`?
2. **Specificity** — how precise is the selector?
3. **Source order** — which rule came last in the stylesheet?

Understanding this order prevents 90% of "why isn't this working?" frustrations.

### 4.2 Origin & Importance

Declarations come from three origins:

- **User-agent styles** — the browser's built-in defaults (`<a>` is blue and underlined, `<h1>` is larger than body text)
- **Author styles** — CSS you write for your site
- **User styles** — CSS the end user may have added (rare today, used for accessibility tools)

The normal cascade order (weakest to strongest):

1. User-agent normal
2. User normal
3. Author normal
4. Author `!important`
5. User `!important`
6. User-agent `!important`

`!important` flips the origin order. User `!important` is stronger than author `!important` — this exists so users can enforce accessibility overrides (like large text) that cannot be suppressed by site stylesheets.

```css
/* Avoid this — it is a cascade nuclear option that creates maintenance debt */
.button { color: red !important; }
```

> **When is `!important` ever okay?** Two legitimate cases: utility classes that must always win (e.g., `.hidden { display: none !important; }`), and accessibility overrides. Everywhere else, restructure your selectors.

### 4.3 Specificity in Detail

Specificity is a weight calculated per selector:

```
(A, B, C)
 │  │  │
 │  │  └─ Type selectors, pseudo-elements
 │  └──── Class selectors, attribute selectors, pseudo-classes
 └─────── ID selectors
```

Specificity is compared left-to-right. A rule with (1, 0, 0) beats (0, 10, 0). Inline styles are equivalent to (1, 0, 0, 0) — a fourth column above IDs. `!important` overrides all specificity.

```css
/* (0, 0, 1) — type */
p { color: black; }

/* (0, 1, 0) — class */
.intro { color: navy; }

/* (0, 1, 1) — class + type */
p.intro { color: teal; }

/* (1, 0, 0) — ID */
#about p { color: darkgreen; }
```

A `p` element with `class="intro"` inside `<section id="about">` will be **dark green** — the ID selector wins.

> **Practical tip:** Write your CSS in order of increasing specificity: base element styles first, then classes, then state modifiers. This keeps the cascade predictable and easy to override.

### 4.4 Inheritance

Some CSS properties **inherit** their value from their parent element by default. Others do not.

**Properties that inherit by default:**
- `color`
- `font-family`, `font-size`, `font-weight`, `font-style`, `font-variant`
- `letter-spacing`, `word-spacing`, `line-height`
- `text-align`, `text-indent`, `text-transform`
- `white-space`
- `list-style-*`
- `visibility`
- `cursor`

**Properties that do NOT inherit by default:**
- `background-*`
- `border-*`
- `margin`, `padding`
- `width`, `height`
- `display`, `position`
- `overflow`
- `box-shadow`, `text-shadow` do NOT inherit — but `color` does, and `currentColor` propagates it

```css
/* Set font for the whole page — all text elements inherit it */
body {
  font-family: "Inter", sans-serif;
  font-size: 16px;
  color: #222;
}
```

### 4.5 The `inherit`, `initial`, `unset`, and `revert` Keywords

Every CSS property accepts these universal values:

| Keyword | Meaning |
|---|---|
| `inherit` | Force this property to inherit from the parent |
| `initial` | Reset to the CSS specification's initial value |
| `unset` | `inherit` if the property normally inherits, otherwise `initial` |
| `revert` | Roll back to the browser's default stylesheet value |

```css
/* Reset all properties on an element to their initial values */
.reset-box {
  all: revert;
}

/* Force a non-inheriting property to inherit */
.child-border {
  border-color: inherit;
}
```

---

## 5. The Box Model

Every element in CSS is a rectangular box. The box model defines how that box's total size is calculated.

### 5.1 The Four Layers

From inside to outside, a box has four layers:

```
┌─────────────────────────────────────┐
│              MARGIN                 │  ← Transparent space outside
│  ┌───────────────────────────────┐  │
│  │            BORDER             │  │  ← The visible border
│  │  ┌─────────────────────────┐  │  │
│  │  │         PADDING         │  │  │  ← Space between border and content
│  │  │  ┌───────────────────┐  │  │  │
│  │  │  │     CONTENT       │  │  │  │  ← Text, images, etc.
│  │  │  └───────────────────┘  │  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

- **Content** — the actual content area
- **Padding** — transparent space between content and border; inherits background colour
- **Border** — a visible (or invisible) line around the padding
- **Margin** — transparent space outside the border, between this element and neighbours

### 5.2 `box-sizing`

The `box-sizing` property controls whether `width` and `height` refer to just the content area or the full box.

**`content-box` (default):**
```css
.box {
  box-sizing: content-box;
  width: 200px;
  padding: 20px;
  border: 2px solid;
  /* Total rendered width = 200 + 40 + 4 = 244px */
}
```

**`border-box` (recommended):**
```css
.box {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
  border: 2px solid;
  /* Total rendered width = 200px (padding and border included) */
}
```

**🖥 Rendered output — comparing both models side by side:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;border:1px solid #e0e0e0;border-radius:8px;padding:20px;background:#fff;">
  <p style="margin:0 0 8px 0;font-size:0.75rem;font-weight:600;color:#666;text-transform:uppercase;letter-spacing:0.05em;">content-box — declared width: 200px</p>
  <div style="width:244px;background:#dbeafe;border:2px solid #3b82f6;padding:0;box-sizing:content-box;">
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <div style="width:20px;background:#93c5fd;text-align:center;font-size:11px;color:#1e40af;padding:12px 0;">p</div>
      <div style="flex:1;background:#dbeafe;text-align:center;font-size:12px;color:#1e40af;padding:12px 4px;">content 200px</div>
      <div style="width:20px;background:#93c5fd;text-align:center;font-size:11px;color:#1e40af;padding:12px 0;">p</div>
    </div>
  </div>
  <p style="font-size:12px;color:#dc2626;margin:4px 0 20px 0;">⚠ Actual rendered width = 244px (200 content + 40 padding + 4 border)</p>

  <p style="margin:0 0 8px 0;font-size:0.75rem;font-weight:600;color:#666;text-transform:uppercase;letter-spacing:0.05em;">border-box — declared width: 200px</p>
  <div style="width:200px;background:#dcfce7;border:2px solid #16a34a;padding:0;box-sizing:border-box;">
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <div style="width:20px;background:#86efac;text-align:center;font-size:11px;color:#14532d;padding:12px 0;">p</div>
      <div style="flex:1;background:#dcfce7;text-align:center;font-size:12px;color:#14532d;padding:12px 4px;">content 156px</div>
      <div style="width:20px;background:#86efac;text-align:center;font-size:11px;color:#14532d;padding:12px 0;">p</div>
    </div>
  </div>
  <p style="font-size:12px;color:#16a34a;margin:4px 0 0 0;">✓ Actual rendered width = 200px exactly</p>
</div>

`border-box` is far more intuitive — when you say an element is 200px wide, it *is* 200px wide, regardless of padding or border. Apply it universally:

```css
*, *::before, *::after {
  box-sizing: border-box;
}
```

This is included in virtually every modern CSS reset and should be on every project.

### 5.3 Margin, Padding & Border Shorthand

```css
/* All four sides */
margin: 16px;

/* Vertical | Horizontal */
margin: 16px 24px;

/* Top | Horizontal | Bottom */
margin: 8px 16px 24px;

/* Top | Right | Bottom | Left (clockwise from top) */
margin: 8px 16px 24px 32px;

/* Individual sides */
margin-top: 8px;
margin-right: 16px;
margin-bottom: 24px;
margin-left: 32px;
```

The same shorthand rules apply to `padding` and `border-width`.

```css
/* Border shorthand: width style colour */
border: 2px solid #ccc;

/* Individual border sides */
border-top: 1px dashed #999;
border-bottom: none;
```

### 5.4 Margin Collapsing

Vertical margins between block elements **collapse** — they merge into a single margin equal to the largest of the two. This is intentional and goes back to the typographic principle that headings and paragraphs should not double-space from each other.

```css
p { margin-bottom: 16px; }
h2 { margin-top: 24px; }

/* The space between h2 and p is 24px, not 40px */
```

```html
<!-- HTML -->
<p>A paragraph of text.</p>
<h2>The Next Section</h2>
<p>Another paragraph.</p>
```

**🖥 Rendered output:**

<div style="display:flex;gap:16px;flex-wrap:wrap;">
  <div style="flex:1;min-width:220px;">
    <p style="font-size:11px;font-weight:700;color:#16a34a;margin:0 0 4px 0;font-family:monospace;">✓ WITH collapsing (real browser behaviour)</p>
    <div style="border:1px solid #e0e0e0;border-radius:8px;padding:16px;background:#fff;font-family:'Segoe UI',system-ui,sans-serif;">
      <p style="margin:0 0 16px 0;font-size:14px;color:#333;">A paragraph of text.</p>
      <div style="height:1px;background:#e5e7eb;margin:0;"></div>
      <p style="font-size:10px;color:#6b7280;text-align:center;margin:2px 0;">24px gap (collapsed — max of 16px + 24px, not the sum)</p>
      <div style="height:1px;background:#e5e7eb;margin:0;"></div>
      <h2 style="font-size:1.1rem;font-weight:700;color:#1a1a2e;margin:16px 0 8px 0;">The Next Section</h2>
      <p style="margin:0;font-size:14px;color:#333;">Another paragraph.</p>
    </div>
  </div>
  <div style="flex:1;min-width:220px;">
    <p style="font-size:11px;font-weight:700;color:#dc2626;margin:0 0 4px 0;font-family:monospace;">✗ WITHOUT collapsing (hypothetical)</p>
    <div style="border:1px solid #e0e0e0;border-radius:8px;padding:16px;background:#fff;font-family:'Segoe UI',system-ui,sans-serif;">
      <p style="margin:0 0 40px 0;font-size:14px;color:#333;">A paragraph of text.</p>
      <div style="height:1px;background:#e5e7eb;margin:0;"></div>
      <p style="font-size:10px;color:#dc2626;text-align:center;margin:2px 0;">40px gap — would feel too spacious</p>
      <div style="height:1px;background:#e5e7eb;margin:0;"></div>
      <h2 style="font-size:1.1rem;font-weight:700;color:#1a1a2e;margin:16px 0 8px 0;">The Next Section</h2>
      <p style="margin:0;font-size:14px;color:#333;">Another paragraph.</p>
    </div>
  </div>
</div>

Margin collapsing occurs:
- Between adjacent block siblings
- Between a parent and its first/last child (when there is no border, padding, or clearance separating them)
- On empty blocks (top and bottom margins collapse with themselves)

**Margins do NOT collapse when:**
- Elements are positioned (`absolute` or `fixed`)
- Elements are flex or grid items
- There is a border, padding, or inline content between parent and child

> **Gotcha:** If a container has no padding or border on top, its first child's `margin-top` bleeds through to the container and collapses with whatever is above the container. Fix this by adding `padding-top: 1px` or `overflow: hidden` to the container, or by using padding on the child instead of margin.

### 5.5 Width, Height & Overflow

```css
.box {
  width: 400px;          /* Fixed width */
  max-width: 100%;       /* Never wider than the parent */
  min-width: 200px;      /* Never narrower than 200px */

  height: auto;          /* Default: shrinks to fit content */
  min-height: 100vh;     /* At least the full viewport height */

  overflow: hidden;      /* Clip content that exceeds the box */
  overflow-y: auto;      /* Scroll vertically if needed */
  overflow: visible;     /* Default: content sticks out */
}
```

---

## 6. Display & Layout Fundamentals

The `display` property is the most important layout property in CSS. It changes how an element participates in flow layout and how its children are arranged.

### 6.1 Block vs Inline

In normal flow, elements are either **block-level** or **inline-level**:

| Type | Examples | Behaviour |
|---|---|---|
| Block | `div`, `p`, `h1`–`h6`, `section`, `article` | Takes full width of parent, starts on new line, respects width/height |
| Inline | `span`, `a`, `strong`, `em`, `img` | Flows with text, does not start on new line, ignores top/bottom margin and width/height |
| Inline-block | `display: inline-block` | Flows inline but respects width, height, and all margin/padding |

```css
/* Make links look like buttons inline */
a.badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  background: #e9f1ff;
}
```

```html
<!-- HTML — badges flow inline with surrounding text -->
<p>
  Available in
  <a class="badge" href="/python">Python</a>
  <a class="badge" href="/js">JavaScript</a>
  and <a class="badge" href="/rust">Rust</a>.
</p>
```

**🖥 Rendered output:**

<div style="border:1px solid #e0e0e0;border-radius:8px;padding:20px 24px;background:#fff;font-family:'Segoe UI',system-ui,sans-serif;font-size:1rem;color:#333;line-height:2;">
  Available in
  <a href="#" style="display:inline-block;padding:0.25rem 0.75rem;border-radius:12px;background:#e9f1ff;color:#0056b3;text-decoration:none;font-size:0.875rem;font-weight:500;">Python</a>
  <a href="#" style="display:inline-block;padding:0.25rem 0.75rem;border-radius:12px;background:#e9f1ff;color:#0056b3;text-decoration:none;font-size:0.875rem;font-weight:500;">JavaScript</a>
  and <a href="#" style="display:inline-block;padding:0.25rem 0.75rem;border-radius:12px;background:#e9f1ff;color:#0056b3;text-decoration:none;font-size:0.875rem;font-weight:500;">Rust</a>.
</div>

### 6.2 Common `display` Values

| Value | Description |
|---|---|
| `block` | Block-level box |
| `inline` | Inline box |
| `inline-block` | Inline but accepts box model properties |
| `flex` | Block-level flex container |
| `inline-flex` | Inline flex container |
| `grid` | Block-level grid container |
| `inline-grid` | Inline grid container |
| `none` | Removes element from layout entirely (not just visible) |
| `contents` | Element itself generates no box; children participate in parent layout |
| `table`, `table-row`, `table-cell` | Table-like layout (rarely used directly) |

### 6.3 Normal Flow

In normal flow (no flexbox or grid), block elements stack vertically and inline elements flow horizontally. This is the default and you should work *with* it before reaching for flexbox or grid.

```css
/* A centred content column — purely with block layout */
.container {
  max-width: 800px;
  margin: 0 auto;       /* auto horizontal margins with a max-width = centred */
  padding: 0 1rem;
}
```

```html
<!-- HTML -->
<div class="container">
  <p>This text is constrained to 800px and centred in the viewport.</p>
</div>
```

**🖥 Rendered output (at 1200px viewport):**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;gap:12px;">
  <div>
    <p style="margin:0 0 6px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">At 1200px viewport — container is 800px wide, centred with auto margins:</p>
    <div style="background:#e0f2fe;border-radius:8px;padding:16px;position:relative;">
      <div style="font-size:10px;color:#0369a1;margin-bottom:6px;text-align:center;">viewport (1200px)</div>
      <div style="max-width:480px;margin:0 auto;background:#fff;border:2px solid #7dd3fc;border-radius:6px;padding:12px 16px;position:relative;">
        <div style="font-size:10px;color:#0284c7;font-weight:700;margin-bottom:4px;font-family:monospace;">container (800px — max-width)</div>
        <p style="margin:0;font-size:13px;color:#334155;">This text is constrained to 800px and centred in the viewport.</p>
        <div style="position:absolute;left:-60px;top:50%;transform:translateY(-50%);font-size:10px;color:#94a3b8;text-align:center;width:55px;">auto<br>margin</div>
        <div style="position:absolute;right:-60px;top:50%;transform:translateY(-50%);font-size:10px;color:#94a3b8;text-align:center;width:55px;">auto<br>margin</div>
      </div>
    </div>
    <p style="margin:4px 0 0 0;font-size:11px;color:#64748b;"><code>margin: 0 auto</code> distributes remaining space equally on both sides, horizontally centring the box.</p>
  </div>
  <div>
    <p style="margin:0 0 6px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">At 600px viewport — narrower than max-width, container fills 100%:</p>
    <div style="background:#e0f2fe;border-radius:8px;padding:16px;max-width:320px;">
      <div style="background:#fff;border:2px solid #7dd3fc;border-radius:6px;padding:12px 16px;">
        <p style="margin:0;font-size:12px;color:#334155;">Container fills the full viewport width — <code>max-width</code> is not reached, no auto margins needed.</p>
      </div>
    </div>
  </div>
</div>

### 6.4 Hiding Elements

```css
/* Removed from layout entirely */
.hidden { display: none; }

/* Invisible but still occupies space */
.invisible { visibility: hidden; }

/* Invisible but still accessible to screen readers */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

---

## 7. Flexbox

Flexbox (Flexible Box Layout) is a one-dimensional layout system — it handles either a row or a column at a time. It is ideal for nav bars, card rows, form controls, button groups, and centring.

### 7.1 Activating Flexbox

```css
.container {
  display: flex; /* or inline-flex */
}
```

The element becomes a **flex container**, and its direct children become **flex items**. All normal flow is abandoned for these children; they are now subject to flexbox rules.

### 7.2 Flex Direction & Wrapping

```css
.container {
  flex-direction: row;          /* Default: items in a horizontal row */
  flex-direction: row-reverse;  /* Right to left */
  flex-direction: column;       /* Items in a vertical column */
  flex-direction: column-reverse;

  flex-wrap: nowrap;   /* Default: items never wrap, may overflow */
  flex-wrap: wrap;     /* Items wrap to the next line */

  /* Shorthand: direction + wrap */
  flex-flow: row wrap;
}
```

### 7.3 Alignment

Flexbox provides two axes: the **main axis** (direction of flex-direction) and the **cross axis** (perpendicular to it).

```css
.container {
  /* Main axis alignment */
  justify-content: flex-start;    /* Default: pack items at the start */
  justify-content: flex-end;
  justify-content: center;
  justify-content: space-between; /* Even gaps, no outer gaps */
  justify-content: space-around;  /* Even gaps including outer */
  justify-content: space-evenly;  /* Perfectly equal gaps everywhere */

  /* Cross axis alignment (single line) */
  align-items: stretch;    /* Default: items stretch to fill container height */
  align-items: flex-start;
  align-items: flex-end;
  align-items: center;
  align-items: baseline;

  /* Cross axis alignment for wrapped rows */
  align-content: flex-start;
  align-content: space-between;
  align-content: center;
}
```

```html
<!-- HTML used in all diagrams below -->
<div class="container">
  <div class="item">A</div>
  <div class="item">B</div>
  <div class="item">C</div>
</div>
```

**🖥 Rendered output — `justify-content` (main axis / horizontal):**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;gap:12px;">
  <div><p style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#555;font-family:monospace;">flex-start</p><div style="display:flex;justify-content:flex-start;gap:8px;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:6px;padding:10px;"><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">A</div><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">B</div><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">C</div></div></div>
  <div><p style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#555;font-family:monospace;">center</p><div style="display:flex;justify-content:center;gap:8px;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:6px;padding:10px;"><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">A</div><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">B</div><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">C</div></div></div>
  <div><p style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#555;font-family:monospace;">flex-end</p><div style="display:flex;justify-content:flex-end;gap:8px;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:6px;padding:10px;"><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">A</div><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">B</div><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">C</div></div></div>
  <div><p style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#555;font-family:monospace;">space-between</p><div style="display:flex;justify-content:space-between;gap:8px;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:6px;padding:10px;"><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">A</div><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">B</div><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">C</div></div></div>
  <div><p style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#555;font-family:monospace;">space-around</p><div style="display:flex;justify-content:space-around;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:6px;padding:10px;"><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">A</div><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">B</div><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">C</div></div></div>
  <div><p style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#555;font-family:monospace;">space-evenly</p><div style="display:flex;justify-content:space-evenly;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:6px;padding:10px;"><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">A</div><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">B</div><div style="background:#3b82f6;color:#fff;padding:8px 16px;border-radius:4px;font-size:14px;font-weight:600;">C</div></div></div>
</div>

**🖥 Rendered output — `align-items` (cross axis / vertical, items have varying heights):**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;gap:12px;">
  <div><p style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#555;font-family:monospace;">stretch (default — items fill container height)</p>
    <div style="display:flex;align-items:stretch;gap:8px;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:6px;padding:10px;height:80px;">
      <div style="background:#3b82f6;color:#fff;padding:8px 20px;border-radius:4px;font-size:14px;font-weight:600;display:flex;align-items:center;">A</div>
      <div style="background:#6366f1;color:#fff;padding:8px 20px;border-radius:4px;font-size:14px;font-weight:600;display:flex;align-items:center;">B</div>
      <div style="background:#8b5cf6;color:#fff;padding:8px 20px;border-radius:4px;font-size:14px;font-weight:600;display:flex;align-items:center;">C</div>
    </div>
  </div>
  <div><p style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#555;font-family:monospace;">flex-start</p>
    <div style="display:flex;align-items:flex-start;gap:8px;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:6px;padding:10px;height:80px;">
      <div style="background:#3b82f6;color:#fff;padding:8px 20px;border-radius:4px;font-size:14px;font-weight:600;">A</div>
      <div style="background:#6366f1;color:#fff;padding:16px 20px;border-radius:4px;font-size:14px;font-weight:600;">B</div>
      <div style="background:#8b5cf6;color:#fff;padding:8px 20px;border-radius:4px;font-size:14px;font-weight:600;">C</div>
    </div>
  </div>
  <div><p style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#555;font-family:monospace;">center</p>
    <div style="display:flex;align-items:center;gap:8px;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:6px;padding:10px;height:80px;">
      <div style="background:#3b82f6;color:#fff;padding:8px 20px;border-radius:4px;font-size:14px;font-weight:600;">A</div>
      <div style="background:#6366f1;color:#fff;padding:16px 20px;border-radius:4px;font-size:14px;font-weight:600;">B</div>
      <div style="background:#8b5cf6;color:#fff;padding:8px 20px;border-radius:4px;font-size:14px;font-weight:600;">C</div>
    </div>
  </div>
  <div><p style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#555;font-family:monospace;">flex-end</p>
    <div style="display:flex;align-items:flex-end;gap:8px;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:6px;padding:10px;height:80px;">
      <div style="background:#3b82f6;color:#fff;padding:8px 20px;border-radius:4px;font-size:14px;font-weight:600;">A</div>
      <div style="background:#6366f1;color:#fff;padding:16px 20px;border-radius:4px;font-size:14px;font-weight:600;">B</div>
      <div style="background:#8b5cf6;color:#fff;padding:8px 20px;border-radius:4px;font-size:14px;font-weight:600;">C</div>
    </div>
  </div>
</div>

### 7.4 Flex Items

```css
.item {
  /* How much an item grows to fill available space (ratio) */
  flex-grow: 0;    /* Default: don't grow */
  flex-grow: 1;    /* Take all available space */

  /* How much an item shrinks when space is tight */
  flex-shrink: 1;  /* Default: shrink equally */
  flex-shrink: 0;  /* Never shrink below flex-basis */

  /* The starting size before growing/shrinking */
  flex-basis: auto;   /* Default: use the item's natural size */
  flex-basis: 200px;  /* Start at 200px */
  flex-basis: 0;      /* Size is entirely determined by flex-grow ratio */

  /* Shorthand: flex-grow flex-shrink flex-basis */
  flex: 1;           /* Equivalent to: flex: 1 1 0 (grow, shrink, basis 0) */
  flex: 1 0 200px;   /* Grow, don't shrink, start at 200px */
  flex: none;        /* Equivalent to: flex: 0 0 auto (rigid) */

  /* Override container's align-items for this item only */
  align-self: center;
}
```

> **`flex: 1` vs `flex-grow: 1`:** `flex: 1` sets `flex-basis: 0`, so items share available space equally regardless of content size. `flex-grow: 1` alone keeps the natural size difference between items and just distributes leftover space. Use `flex: 1` when you want equal-width items.

### 7.5 The `gap` Property

```css
.container {
  display: flex;
  gap: 1rem;           /* Both row and column gaps */
  gap: 1rem 2rem;      /* Row gap | Column gap */
  row-gap: 1rem;
  column-gap: 2rem;
}
```

`gap` is far cleaner than using `margin` on items, as it only applies between items — no "last child no margin" tricks needed.

### 7.6 Common Flexbox Patterns

**Centring anything:**
```css
.centred {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

```html
<!-- HTML -->
<div class="centred" style="width: 400px; height: 200px; border: 1px solid;">
  <p>I am centred!</p>
</div>
```

**🖥 Rendered output:**

<div style="display:flex;justify-content:center;align-items:center;width:400px;height:160px;background:#f1f5f9;border:2px dashed #94a3b8;border-radius:8px;font-family:'Segoe UI',system-ui,sans-serif;">
  <p style="margin:0;font-weight:600;color:#334155;font-size:1rem;">I am centred!</p>
</div>

**Sticky footer:**
```css
body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
main { flex: 1; }   /* Pushes footer to the bottom */
```

**Equal-width nav items:**
```css
nav { display: flex; }
nav a { flex: 1; text-align: center; }
```

**Sidebar layout (two columns):**
```css
.layout {
  display: flex;
  align-items: flex-start;
  gap: 2rem;
}
.sidebar { flex: 0 0 280px; } /* Fixed width sidebar never shrinks */
.content  { flex: 1; }        /* Content takes remaining space */
```

```html
<!-- HTML -->
<div class="layout">
  <aside class="sidebar">Menu &amp; filters</aside>
  <main class="content">Page content goes here</main>
</div>
```

**🖥 Rendered output (1100px viewport):**

<div style="font-family:'Segoe UI',system-ui,sans-serif;">
  <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">flex layout at 1100px — sidebar fixed, content fills remaining space:</p>
  <div style="display:flex;gap:16px;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:8px;padding:12px;min-height:120px;">
    <div style="flex:0 0 140px;background:#1e293b;border-radius:6px;padding:12px;display:flex;flex-direction:column;gap:6px;">
      <div style="font-size:10px;font-weight:700;color:#64748b;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:4px;">sidebar</div>
      <div style="font-size:10px;color:#94a3b8;font-family:monospace;">flex: 0 0 280px<br>(fixed, won't shrink)</div>
      <div style="background:#334155;border-radius:3px;padding:4px 8px;font-size:11px;color:#cbd5e1;">Nav item</div>
      <div style="background:#0284c7;border-radius:3px;padding:4px 8px;font-size:11px;color:#fff;">Active</div>
    </div>
    <div style="flex:1;background:#fff;border-radius:6px;padding:12px;">
      <div style="font-size:10px;font-weight:700;color:#94a3b8;text-transform:uppercase;letter-spacing:0.08em;font-family:monospace;margin-bottom:6px;">content area — flex: 1</div>
      <p style="margin:0;font-size:12px;color:#475569;">Takes all remaining horizontal space. At 1100px viewport: 1100px − 280px sidebar − 2rem gap ≈ <strong>786px</strong>.</p>
    </div>
  </div>
  <p style="margin:8px 0 0 0;font-size:11px;color:#64748b;"><code>flex: 0 0 280px</code> on the sidebar = won't grow, won't shrink, always 280px. <code>flex: 1</code> on content = grows to fill all remaining space.</p>
</div>

---

## 8. CSS Grid

CSS Grid is a two-dimensional layout system for rows *and* columns simultaneously. It is the right tool for page-level layouts, complex card grids, and any layout where you need control over both axes.

### 8.1 Activating Grid

```css
.container { display: grid; }
```

### 8.2 Defining Columns & Rows

```css
.container {
  /* Three equal columns */
  grid-template-columns: 1fr 1fr 1fr;

  /* Shorthand using repeat() */
  grid-template-columns: repeat(3, 1fr);

  /* Mixed units */
  grid-template-columns: 280px 1fr;

  /* Three rows, middle one grows */
  grid-template-rows: auto 1fr auto;

  /* Gap between all tracks */
  gap: 1.5rem;
  column-gap: 2rem;
  row-gap: 1rem;
}
```

```html
<!-- HTML: six items in the example grids -->
<div class="container">
  <div>1</div><div>2</div><div>3</div>
  <div>4</div><div>5</div><div>6</div>
</div>
```

**🖥 Rendered output — `repeat(3, 1fr)` (three equal columns, 6 items):**

<div style="font-family:'Segoe UI',system-ui,sans-serif;">
  <p style="margin:0 0 6px 0;font-size:12px;font-weight:700;color:#555;font-family:monospace;">grid-template-columns: repeat(3, 1fr)</p>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;">
    <div style="background:#3b82f6;color:#fff;padding:16px;border-radius:6px;text-align:center;font-weight:700;font-size:14px;">1</div>
    <div style="background:#3b82f6;color:#fff;padding:16px;border-radius:6px;text-align:center;font-weight:700;font-size:14px;">2</div>
    <div style="background:#3b82f6;color:#fff;padding:16px;border-radius:6px;text-align:center;font-weight:700;font-size:14px;">3</div>
    <div style="background:#3b82f6;color:#fff;padding:16px;border-radius:6px;text-align:center;font-weight:700;font-size:14px;">4</div>
    <div style="background:#3b82f6;color:#fff;padding:16px;border-radius:6px;text-align:center;font-weight:700;font-size:14px;">5</div>
    <div style="background:#3b82f6;color:#fff;padding:16px;border-radius:6px;text-align:center;font-weight:700;font-size:14px;">6</div>
  </div>
  <p style="margin:12px 0 6px 0;font-size:12px;font-weight:700;color:#555;font-family:monospace;">grid-template-columns: 180px 1fr (sidebar + content)</p>
  <div style="display:grid;grid-template-columns:180px 1fr;gap:8px;">
    <div style="background:#6366f1;color:#fff;padding:16px;border-radius:6px;text-align:center;font-weight:700;font-size:14px;">Sidebar<br><span style="font-size:10px;font-weight:400;">180px fixed</span></div>
    <div style="background:#8b5cf6;color:#fff;padding:16px;border-radius:6px;text-align:center;font-weight:700;font-size:14px;">Content<br><span style="font-size:10px;font-weight:400;">1fr (remaining space)</span></div>
    <div style="background:#6366f1;color:#fff;padding:16px;border-radius:6px;text-align:center;font-weight:700;font-size:14px;">3</div>
    <div style="background:#8b5cf6;color:#fff;padding:16px;border-radius:6px;text-align:center;font-weight:700;font-size:14px;">4</div>
  </div>
</div>

**The `fr` unit** means "fraction of available space". After fixed sizes are allocated, remaining space is divided among `fr` units. `1fr 1fr` = two equal columns. `1fr 2fr` = the second column is twice as wide.

### 8.3 The `minmax()` Function

`minmax(min, max)` lets a track be flexible while staying within limits:

```css
.container {
  /* Columns that are at least 200px, but grow to fill space equally */
  grid-template-columns: repeat(3, minmax(200px, 1fr));
}
```

### 8.4 `auto-fill` and `auto-fit`

These keywords let the grid decide how many columns to create:

```css
.cards {
  display: grid;
  /* As many columns as fit, each at least 250px, up to 1fr */
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}
```

- **`auto-fill`** — creates as many tracks as will fit, even if some are empty
- **`auto-fit`** — same but collapses empty tracks, letting existing items grow to fill space

For card grids where you always have items, `auto-fit` is usually what you want.

### 8.5 Placing Items

By default, grid items are placed automatically left-to-right, top-to-bottom. You can override this:

```css
.item {
  /* Grid lines are numbered from 1 */
  grid-column: 1 / 3;     /* Start at line 1, end at line 3 (spans 2 columns) */
  grid-row: 2 / 4;         /* Span 2 rows */

  /* Span shorthand */
  grid-column: span 2;    /* Span 2 columns from current position */
  grid-column: 1 / -1;    /* From first line to last (full width) */
}
```

**🖥 Rendered output — 3-column grid, `.item` placed at `grid-column: 1/3, grid-row: 1/2`:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;">
  <p style="margin:0 0 6px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">grid-column: 1 / 3 (spans 2 of 3 columns)</p>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;">
    <div style="grid-column:1/3;background:#0ea5e9;color:#fff;padding:14px;border-radius:6px;text-align:center;font-weight:700;font-size:13px;">item — grid-column: 1/3 (spans cols 1–2)</div>
    <div style="background:#94a3b8;color:#fff;padding:14px;border-radius:6px;text-align:center;font-weight:700;font-size:13px;">auto</div>
    <div style="background:#94a3b8;color:#fff;padding:14px;border-radius:6px;text-align:center;font-weight:700;font-size:13px;">auto</div>
    <div style="background:#94a3b8;color:#fff;padding:14px;border-radius:6px;text-align:center;font-weight:700;font-size:13px;">auto</div>
    <div style="background:#94a3b8;color:#fff;padding:14px;border-radius:6px;text-align:center;font-weight:700;font-size:13px;">auto</div>
  </div>
  <p style="margin:12px 0 6px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">grid-column: 1 / -1 (full width — spans all columns)</p>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;">
    <div style="grid-column:1/-1;background:#f59e0b;color:#fff;padding:14px;border-radius:6px;text-align:center;font-weight:700;font-size:13px;">full-width item — grid-column: 1 / -1</div>
    <div style="background:#94a3b8;color:#fff;padding:14px;border-radius:6px;text-align:center;font-weight:700;font-size:13px;">auto</div>
    <div style="background:#94a3b8;color:#fff;padding:14px;border-radius:6px;text-align:center;font-weight:700;font-size:13px;">auto</div>
    <div style="background:#94a3b8;color:#fff;padding:14px;border-radius:6px;text-align:center;font-weight:700;font-size:13px;">auto</div>
  </div>
</div>

### 8.6 Named Areas

Named areas make complex layouts readable:

```css
.page {
  display: grid;
  grid-template-columns: 280px 1fr;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header  header"
    "sidebar content"
    "footer  footer";
  min-height: 100vh;
  gap: 0;
}

header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
main    { grid-area: content; }
footer  { grid-area: footer; }
```

Each quoted string in `grid-template-areas` is a row. Names in the same row/column form a rectangular area. A dot (`.`) represents an empty cell.

**🖥 Rendered output — the full page layout from `grid-template-areas`:**

<div style="display:grid;grid-template-columns:140px 1fr;grid-template-rows:auto 1fr auto;grid-template-areas:'header header' 'sidebar content' 'footer footer';gap:4px;min-height:260px;font-family:'Segoe UI',system-ui,sans-serif;font-size:12px;">
  <header style="grid-area:header;background:#1e293b;color:#f1f5f9;padding:10px 16px;border-radius:6px 6px 0 0;font-weight:700;">HEADER — spans full width (grid-area: header)</header>
  <aside style="grid-area:sidebar;background:#334155;color:#cbd5e1;padding:12px;">
    <div style="font-size:10px;font-weight:700;color:#64748b;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:8px;">sidebar</div>
    <div style="font-size:10px;color:#94a3b8;margin-bottom:8px;">140px fixed</div>
    <div style="background:#1e293b;border-radius:3px;padding:4px 8px;margin-bottom:4px;font-size:11px;">Nav item</div>
    <div style="background:#0284c7;border-radius:3px;padding:4px 8px;margin-bottom:4px;font-size:11px;">Active</div>
    <div style="background:#1e293b;border-radius:3px;padding:4px 8px;font-size:11px;">Nav item</div>
  </aside>
  <main style="grid-area:content;background:#f8fafc;padding:12px;">
    <div style="font-size:10px;font-weight:700;color:#94a3b8;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:6px;">content (1fr)</div>
    <p style="margin:0;font-size:11px;color:#475569;">Page content area. Grows to fill all remaining horizontal space after the 140px sidebar. Header and footer above and below span both columns.</p>
  </main>
  <footer style="grid-area:footer;background:#1e293b;color:#94a3b8;padding:8px 16px;border-radius:0 0 6px 6px;font-size:11px;">FOOTER — spans full width (grid-area: footer)</footer>
</div>

### 8.7 Alignment in Grid

```css
.container {
  /* Align items within their cell */
  justify-items: stretch;   /* Default: fill cell width */
  justify-items: start;
  justify-items: center;
  justify-items: end;

  align-items: stretch;     /* Default: fill cell height */
  align-items: start;
  align-items: center;

  /* Align the entire grid within the container */
  justify-content: start;
  justify-content: center;
  justify-content: space-between;

  align-content: start;
}

.item {
  /* Override for a single item */
  justify-self: center;
  align-self: end;

  /* Shorthand: justify-self + align-self */
  place-self: center;
}
```

These work identically to their Flexbox counterparts. `justify-` works along the **inline axis** (horizontal), `align-` works along the **block axis** (vertical).

---

## 9. CSS Positioning

Normal flow stacks elements top-to-bottom and left-to-right. The `position` property lets you **remove an element from the flow**, place it precisely, or make it stick to the viewport.

### 9.1 Position Property

```css
.element {
  position: static;    /* Default — participates in normal flow, top/left/etc. ignored */
  position: relative;  /* Offset from its normal position; original space reserved */
  position: absolute;  /* Removed from flow, positioned relative to nearest positioned ancestor */
  position: fixed;     /* Removed from flow, positioned relative to the viewport */
  position: sticky;    /* Behaves like relative until scroll threshold, then becomes fixed */
}

/* Offset properties (only apply when position != static) */
.box {
  top:    20px;   /* Distance from top edge of containing block */
  right:  20px;
  bottom: 20px;
  left:   20px;
}
```

`static` is the default. All other values create a **positioned element** — a prerequisite for `z-index` to work and for absolute children to anchor to.

**🖥 Rendered output — how each position value behaves:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;gap:12px;">
  <div>
    <p style="margin:0 0 6px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">static / relative — space is always reserved in flow</p>
    <div style="background:#f1f5f9;border:1px solid #e2e8f0;border-radius:6px;padding:12px;position:relative;">
      <div style="background:#3b82f6;color:#fff;padding:8px 14px;border-radius:4px;display:inline-block;font-size:13px;font-weight:600;">A (static)</div>
      <div style="background:#6366f1;color:#fff;padding:8px 14px;border-radius:4px;display:inline-block;font-size:13px;font-weight:600;position:relative;top:10px;left:20px;margin-left:8px;">B (relative: top 10px, left 20px)</div>
      <p style="margin:8px 0 0 0;font-size:11px;color:#64748b;">B is shifted from its original position but its original space is still reserved in the flow.</p>
    </div>
  </div>
  <div>
    <p style="margin:0 0 6px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">absolute — removed from flow, anchored to positioned ancestor</p>
    <div style="background:#f1f5f9;border:2px dashed #94a3b8;border-radius:6px;padding:12px;position:relative;min-height:80px;">
      <p style="margin:0 0 8px 0;font-size:12px;color:#475569;">Positioned ancestor (position: relative)</p>
      <p style="margin:0;font-size:12px;color:#94a3b8;">Normal flow content here...</p>
      <div style="position:absolute;top:8px;right:8px;background:#0ea5e9;color:#fff;padding:4px 10px;border-radius:4px;font-size:12px;font-weight:700;">abs</div>
    </div>
    <p style="margin:4px 0 0 0;font-size:11px;color:#64748b;">The "abs" badge is at top: 8px, right: 8px relative to the dashed container. No layout space is reserved for it.</p>
  </div>
  <div>
    <p style="margin:0 0 6px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">fixed — removed from flow, anchored to the viewport</p>
    <div style="background:#fef3c7;border:1px solid #f59e0b;border-radius:6px;padding:12px;font-size:12px;color:#92400e;">
      📌 A <code>position: fixed</code> element stays in the same viewport corner regardless of scrolling. Example: a sticky chat button at <code>bottom: 2rem; right: 2rem</code> always visible on screen.
    </div>
  </div>
  <div>
    <p style="margin:0 0 6px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">sticky — relative until scroll threshold, then fixed within parent</p>
    <div style="background:#f0fdf4;border:1px solid #86efac;border-radius:6px;padding:12px;font-size:12px;color:#166534;">
      📌 A <code>position: sticky; top: 80px</code> header flows normally in the page. Once scrolled to within 80px of the viewport top, it locks there until its parent element scrolls off screen.
    </div>
  </div>
</div>

### 9.2 The Positioned Ancestor Trick

`position: absolute` positions an element relative to the nearest ancestor with `position` set to anything other than `static`. This is how tooltips, dropdowns, and overlays are built:

```css
.card {
  position: relative; /* Establishes a positioning context */
}

.card .badge {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  /* Positioned relative to .card, not the page */
}
```

```html
<!-- HTML -->
<div class="card">
  <img src="photo.jpg" alt="">
  <h2>Card Title</h2>
  <span class="badge">NEW</span>
</div>
```

**🖥 Rendered output:**

<div style="position:relative;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden;font-family:'Segoe UI',system-ui,sans-serif;width:260px;">
  <div style="background:#1e293b;height:140px;display:flex;align-items:center;justify-content:center;">
    <span style="color:#475569;font-size:13px;">[photo.jpg]</span>
  </div>
  <div style="padding:12px 14px;">
    <h2 style="margin:0;font-size:16px;color:#1e293b;">Card Title</h2>
  </div>
  <span style="position:absolute;top:8px;right:8px;background:#0ea5e9;color:#fff;font-size:11px;font-weight:700;padding:3px 8px;border-radius:4px;letter-spacing:0.04em;">NEW</span>
</div>
<p style="font-size:12px;color:#64748b;margin:6px 0 0 0;font-family:'Segoe UI',system-ui,sans-serif;">💡 The NEW badge is at <code>position: absolute; top: 8px; right: 8px</code> relative to the card&rsquo;s <code>position: relative</code> context. Remove <code>position: relative</code> from <code>.card</code> and the badge escapes to the top-right corner of the entire page.</p>

### 9.3 `z-index` & Stacking Contexts

`z-index` controls the vertical stacking order of positioned elements. Higher values appear in front.

```css
.modal-overlay { z-index: 1000; }
.modal-dialog  { z-index: 1001; }
.tooltip       { z-index: 1100; }
```

**🖥 Rendered output — how z-index layers stack (viewed from the side):**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;gap:8px;">
  <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">z-index stacking order (higher = closer to viewer)</p>
  <div style="position:relative;height:120px;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:6px;overflow:hidden;">
    <div style="position:absolute;bottom:8px;left:8px;right:8px;background:#cbd5e1;border-radius:4px;padding:8px 12px;font-size:12px;color:#475569;">z-index: auto — page content (background)</div>
    <div style="position:absolute;bottom:24px;left:20px;right:20px;background:#93c5fd;border-radius:4px;padding:8px 12px;font-size:12px;color:#1e3a8a;">z-index: 1000 — modal overlay</div>
    <div style="position:absolute;bottom:40px;left:32px;right:32px;background:#3b82f6;border-radius:4px;padding:8px 12px;font-size:12px;color:#fff;">z-index: 1001 — modal dialog</div>
    <div style="position:absolute;bottom:56px;left:44px;right:44px;background:#1d4ed8;border-radius:4px;padding:8px 12px;font-size:12px;color:#fff;font-weight:700;">z-index: 1100 — tooltip (frontmost)</div>
  </div>
  <div style="background:#fef3c7;border:1px solid #f59e0b;border-radius:6px;padding:10px 12px;font-size:12px;color:#92400e;">
    <strong>Stacking context trap:</strong> A child with <code>z-index: 9999</code> inside a parent with <code>z-index: 10</code> can <em>never</em> appear above a sibling element with <code>z-index: 20</code>. The entire parent group moves as a unit. Fix by using <code>isolation: isolate</code> or restructuring the DOM.
  </div>
</div>

`z-index` only works on elements where `position` is not `static`, or on flex/grid items.

**Stacking contexts** are isolated stacking scopes. An element with a stacking context and its descendants are all painted together. Within the context, children can have any `z-index`; outside the context, the group moves together as a unit.

A stacking context is created by:
- `position: relative/absolute/fixed/sticky` with a `z-index` other than `auto`
- `opacity` less than `1`
- `transform`, `filter`, `perspective`, `clip-path` (any value)
- `isolation: isolate`
- Flex/grid items with a `z-index` other than `auto`

> **Why won't my z-index work?** The most common cause is that the element is inside a stacking context with a lower z-index than a sibling context. No matter how large the child's z-index is, it cannot escape its parent's stacking context. Use `isolation: isolate` to deliberately create a stacking context without a z-index, or restructure the DOM.

---

## 10. Typography

Typography in CSS encompasses webfonts, sizing, weight, spacing, and fluid type that adapts gracefully across viewport sizes.

### 10.1 Web Fonts (`@font-face`)

`@font-face` lets you serve custom fonts from your own server:

```css
@font-face {
  font-family: "Inter";
  src: url("/fonts/Inter-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;  /* Show fallback immediately, swap when loaded */
}

@font-face {
  font-family: "Inter";
  src: url("/fonts/Inter-Bold.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

body {
  font-family: "Inter", system-ui, sans-serif;
}
```

Always serve `.woff2` — it has the best compression and is supported by all modern browsers. Include a system font stack as a fallback.

**`font-display: swap`** is critical for performance — without it, the browser holds an invisible text slot (FOIT: Flash of Invisible Text) until the font loads. `swap` shows a fallback font immediately, then swaps it (FOUT: Flash of Unstyled Text). For most sites, FOUT is far better than FOIT.

### 10.2 Google Fonts & Variable Fonts

**Google Fonts (quick setup):**

```html
<!-- In <head> — preconnect first to speed up DNS + TLS -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
```

**Variable fonts** — a single font file that contains an entire type family, controlled with CSS:

```css
/* A variable font responds to custom axes */
body {
  font-family: "Inter Variable", sans-serif;
  font-weight: 450;            /* Any value from 100–900 */
  font-variation-settings: "wght" 450, "slnt" -5;
}
```

### 10.3 Font Properties

```css
p {
  font-size: 1rem;         /* 1rem = root element's font-size (usually 16px) */
  font-weight: 400;        /* 100–900 in increments of 100 */
  font-style: italic;      /* normal | italic | oblique */
  font-variant: small-caps;/* normal | small-caps */
  line-height: 1.6;        /* Unitless: ratio of font-size; avoid units here */
  letter-spacing: 0.02em;  /* Tracking — em units are best */
  word-spacing: 0.05em;
  text-transform: uppercase; /* lowercase | capitalize */
}
```

**🖥 Rendered output — visual effect of each property on body text:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:20px;display:flex;flex-direction:column;gap:10px;">
  <div style="display:grid;grid-template-columns:180px 1fr;gap:6px 16px;align-items:baseline;">
    <code style="font-size:11px;color:#6366f1;">font-size: 0.875rem</code><span style="font-size:0.875rem;color:#334155;">The quick brown fox</span>
    <code style="font-size:11px;color:#6366f1;">font-size: 1rem</code><span style="font-size:1rem;color:#334155;">The quick brown fox</span>
    <code style="font-size:11px;color:#6366f1;">font-size: 1.5rem</code><span style="font-size:1.5rem;color:#334155;">The quick brown fox</span>
    <code style="font-size:11px;color:#6366f1;">font-weight: 100</code><span style="font-weight:100;color:#334155;">The quick brown fox</span>
    <code style="font-size:11px;color:#6366f1;">font-weight: 400</code><span style="font-weight:400;color:#334155;">The quick brown fox</span>
    <code style="font-size:11px;color:#6366f1;">font-weight: 700</code><span style="font-weight:700;color:#334155;">The quick brown fox</span>
    <code style="font-size:11px;color:#6366f1;">font-weight: 900</code><span style="font-weight:900;color:#334155;">The quick brown fox</span>
    <code style="font-size:11px;color:#6366f1;">font-style: normal</code><span style="font-style:normal;color:#334155;">The quick brown fox</span>
    <code style="font-size:11px;color:#6366f1;">font-style: italic</code><span style="font-style:italic;color:#334155;">The quick brown fox</span>
    <code style="font-size:11px;color:#6366f1;">font-variant: small-caps</code><span style="font-variant:small-caps;color:#334155;">The quick brown fox</span>
    <code style="font-size:11px;color:#6366f1;">letter-spacing: -0.05em</code><span style="letter-spacing:-0.05em;color:#334155;">Tight condensed text</span>
    <code style="font-size:11px;color:#6366f1;">letter-spacing: 0.1em</code><span style="letter-spacing:0.1em;color:#334155;">Spaced out look</span>
    <code style="font-size:11px;color:#6366f1;">text-transform: uppercase</code><span style="text-transform:uppercase;color:#334155;">The quick brown fox</span>
    <code style="font-size:11px;color:#6366f1;">text-transform: capitalize</code><span style="text-transform:capitalize;color:#334155;">The quick brown fox</span>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:8px;">
    <div style="background:#fef3c7;border-radius:4px;padding:10px;">
      <p style="margin:0 0 4px 0;font-size:11px;font-weight:700;color:#92400e;font-family:monospace;">line-height: 1 (tight)</p>
      <p style="margin:0;line-height:1;font-size:13px;color:#334155;">This line of text sits very close to the line below making it hard to read.</p>
    </div>
    <div style="background:#f0fdf4;border-radius:4px;padding:10px;">
      <p style="margin:0 0 4px 0;font-size:11px;font-weight:700;color:#166534;font-family:monospace;">line-height: 1.6 (comfortable)</p>
      <p style="margin:0;line-height:1.6;font-size:13px;color:#334155;">This line of text sits with comfortable space below, easier for reading longer paragraphs.</p>
    </div>
  </div>
</div>

### 10.4 Text Decorations & Overflow

```css
p {
  text-decoration: underline;
  text-decoration: none;                      /* Remove underline from links */
  text-decoration: underline dotted #ff5733;  /* Colour + style */
  text-underline-offset: 3px;                 /* Gap between text and underline */

  text-overflow: ellipsis;  /* Requires overflow: hidden; white-space: nowrap */
  overflow: hidden;
  white-space: nowrap;      /* Prevent wrapping — needed for ellipsis */
}
```

### 10.5 Fluid Typography

Fluid type scales smoothly between a minimum and maximum size without media queries:

```css
/* clamp(min, preferred, max) */
h1 { font-size: clamp(1.75rem, 5vw, 3rem); }
h2 { font-size: clamp(1.5rem,  4vw, 2.25rem); }
p  { font-size: clamp(1rem,    2.5vw, 1.125rem); }

/* Full fluid type scale (based on viewport width) */
:root {
  --text-sm:   clamp(0.8rem,   1.5vw, 0.875rem);
  --text-base: clamp(1rem,     2vw,   1.125rem);
  --text-lg:   clamp(1.125rem, 2.5vw, 1.25rem);
  --text-xl:   clamp(1.25rem,  3vw,   1.5rem);
  --text-2xl:  clamp(1.5rem,   4vw,   2rem);
  --text-3xl:  clamp(1.75rem,  5vw,   3rem);
}
```

**🖥 Rendered output — font-size at different viewport widths:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:20px;">
  <p style="margin:0 0 12px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">font-size: clamp(1.5rem, 5vw, 3rem)</p>
  <div style="display:flex;flex-direction:column;gap:8px;">
    <div style="display:flex;align-items:baseline;gap:12px;"><span style="font-size:11px;color:#94a3b8;width:60px;flex-shrink:0;">320px</span><span style="font-size:1.5rem;color:#1e293b;font-weight:700;">Heading</span><span style="font-size:11px;color:#64748b;">(24px — clamped to min)</span></div>
    <div style="display:flex;align-items:baseline;gap:12px;"><span style="font-size:11px;color:#94a3b8;width:60px;flex-shrink:0;">600px</span><span style="font-size:1.875rem;color:#1e293b;font-weight:700;">Heading</span><span style="font-size:11px;color:#64748b;">(30px — fluid zone)</span></div>
    <div style="display:flex;align-items:baseline;gap:12px;"><span style="font-size:11px;color:#94a3b8;width:60px;flex-shrink:0;">800px</span><span style="font-size:2.25rem;color:#1e293b;font-weight:700;">Heading</span><span style="font-size:11px;color:#64748b;">(40px — fluid zone)</span></div>
    <div style="display:flex;align-items:baseline;gap:12px;"><span style="font-size:11px;color:#94a3b8;width:60px;flex-shrink:0;">1000px+</span><span style="font-size:3rem;color:#1e293b;font-weight:700;">Heading</span><span style="font-size:11px;color:#64748b;">(48px — clamped to max)</span></div>
  </div>
  <p style="margin:12px 0 0 0;font-size:11px;color:#64748b;">No media queries needed — scales smoothly between 24px and 48px based on viewport width.</p>
</div>

---

## 11. Colors & Backgrounds

### 11.1 Color Formats

CSS accepts colour in many formats. All four below produce the same orange-red:

```css
.box { color: #ff5733; }            /* Hex */
.box { color: #f53; }               /* Shorthand hex (expands to #ff5533) */
.box { color: rgb(255, 87, 51); }   /* RGB */
.box { color: rgba(255, 87, 51, 0.5); }  /* RGBA — 50% transparent */
.box { color: hsl(14, 100%, 60%); } /* HSL — hue 14°, 100% sat, 60% lightness */
.box { color: oklch(0.65 0.22 28); }/* OKLCH — perceptually uniform, best for design systems */
```

**🖥 Rendered output — color format equivalents (all the same orange-red):**

<div style="font-family:'Segoe UI',system-ui,sans-serif;background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:20px;display:flex;flex-direction:column;gap:8px;">
  <div style="display:flex;align-items:center;gap:12px;"><div style="width:40px;height:24px;border-radius:4px;background:#ff5733;flex-shrink:0;"></div><code style="font-size:12px;color:#6366f1;">#ff5733</code><span style="font-size:12px;color:#475569;">vivid orange-red, 100% opacity</span></div>
  <div style="display:flex;align-items:center;gap:12px;"><div style="width:40px;height:24px;border-radius:4px;background:#ff5533;flex-shrink:0;"></div><code style="font-size:12px;color:#6366f1;">#f53</code><span style="font-size:12px;color:#475569;">shorthand (expands to #ff5533 — very close)</span></div>
  <div style="display:flex;align-items:center;gap:12px;"><div style="width:40px;height:24px;border-radius:4px;background:rgb(255,87,51);flex-shrink:0;"></div><code style="font-size:12px;color:#6366f1;">rgb(255, 87, 51)</code><span style="font-size:12px;color:#475569;">same orange-red, explicit channels</span></div>
  <div style="display:flex;align-items:center;gap:12px;"><div style="width:40px;height:24px;border-radius:4px;background:rgba(255,87,51,0.5);flex-shrink:0;border:1px solid #e2e8f0;"></div><code style="font-size:12px;color:#6366f1;">rgba(255, 87, 51, 0.5)</code><span style="font-size:12px;color:#475569;">50% transparent — shows background through</span></div>
  <div style="display:flex;align-items:center;gap:12px;"><div style="width:40px;height:24px;border-radius:4px;background:hsl(14,100%,60%);flex-shrink:0;"></div><code style="font-size:12px;color:#6366f1;">hsl(14, 100%, 60%)</code><span style="font-size:12px;color:#475569;">hue 14° · saturation 100% · lightness 60%</span></div>
  <hr style="border:none;border-top:1px solid #f1f5f9;margin:4px 0;">
  <p style="margin:0 0 6px 0;font-size:11px;font-weight:700;color:#555;">HSL tonal scale (same hue &amp; saturation, varying lightness):</p>
  <div style="display:flex;gap:4px;flex-wrap:wrap;">
    <div style="display:flex;flex-direction:column;align-items:center;gap:3px;"><div style="width:36px;height:36px;border-radius:4px;background:hsl(14,100%,10%);"></div><span style="font-size:9px;color:#64748b;">10%</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:3px;"><div style="width:36px;height:36px;border-radius:4px;background:hsl(14,100%,25%);"></div><span style="font-size:9px;color:#64748b;">25%</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:3px;"><div style="width:36px;height:36px;border-radius:4px;background:hsl(14,100%,40%);"></div><span style="font-size:9px;color:#64748b;">40%</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:3px;"><div style="width:36px;height:36px;border-radius:4px;background:hsl(14,100%,55%);"></div><span style="font-size:9px;color:#64748b;">55%</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:3px;"><div style="width:36px;height:36px;border-radius:4px;background:hsl(14,100%,70%);"></div><span style="font-size:9px;color:#64748b;">70%</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:3px;"><div style="width:36px;height:36px;border-radius:4px;background:hsl(14,100%,85%);border:1px solid #e2e8f0;"></div><span style="font-size:9px;color:#64748b;">85%</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:3px;"><div style="width:36px;height:36px;border-radius:4px;background:hsl(14,100%,95%);border:1px solid #e2e8f0;"></div><span style="font-size:9px;color:#64748b;">95%</span></div>
  </div>
  <p style="margin:4px 0 0 0;font-size:11px;color:#64748b;">Change only the lightness to generate a full tonal palette — no hex math needed.</p>
</div>

### 11.2 `currentColor` & `transparent`

```css
.icon {
  color: currentColor;  /* Inherits the element's own text colour */
  fill: currentColor;   /* SVG icons can inherit text colour */
}

.overlay {
  background: transparent;  /* Fully transparent; also the default */
}
```

### 11.3 Backgrounds

```css
.hero {
  background-color: #1e293b;
  background-image: url("/img/hero.jpg");
  background-size: cover;         /* cover | contain | 100% auto | 400px 300px */
  background-position: center;    /* center | top right | 50% 30% */
  background-repeat: no-repeat;   /* repeat | repeat-x | repeat-y */
  background-attachment: fixed;   /* Parallax effect */
  background-origin: border-box;  /* Where the image starts */
  background-clip: text;          /* Clip to text shape */

  /* Shorthand: colour image position/size repeat origin clip attachment */
  background: #1e293b url("/img/hero.jpg") center/cover no-repeat;
}

.card {
  /* Multiple backgrounds (first is on top) */
  background:
    linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
    url("/img/card.jpg") center/cover;
}
```

### 11.4 Gradients

```css
/* Linear — straight line from one colour to another */
.hero { background: linear-gradient(to right, #6a11cb, #2575fc); }
.diagonal { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }

/* Radial — circular or elliptical */
.glow { background: radial-gradient(circle at center, #fff 0%, #e0e0e0 100%); }

/* Conic — sweeps around a centre point (good for pie charts) */
.wheel { background: conic-gradient(from 0deg, red, yellow, green, blue, red); }

/* Repeating variants */
.stripes {
  background: repeating-linear-gradient(
    45deg,
    white 0px, white 10px,
    #f0f0f0 10px, #f0f0f0 20px
  );
}
```

**🖥 Rendered output — how each gradient direction/type looks:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;gap:12px;">
  <div>
    <p style="margin:0 0 4px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">linear-gradient(to right, #6a11cb, #2575fc)</p>
    <div style="height:50px;border-radius:6px;background:linear-gradient(to right,#6a11cb,#2575fc);"></div>
  </div>
  <div>
    <p style="margin:0 0 4px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">linear-gradient(135deg, #667eea 0%, #764ba2 100%)</p>
    <div style="height:50px;border-radius:6px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);"></div>
  </div>
  <div>
    <p style="margin:0 0 4px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">radial-gradient(circle at center, #fff 0%, #e0e0e0 100%)</p>
    <div style="height:50px;border-radius:6px;background:radial-gradient(circle at center,#fff 0%,#e0e0e0 100%);border:1px solid #e2e8f0;"></div>
  </div>
  <div>
    <p style="margin:0 0 4px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">conic-gradient(from 0deg, red, yellow, green, blue, red)</p>
    <div style="width:80px;height:80px;border-radius:50%;background:conic-gradient(from 0deg,red,yellow,green,blue,red);"></div>
  </div>
  <div>
    <p style="margin:0 0 4px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">repeating-linear-gradient(45deg, white 0-10px, #f0f0f0 10-20px)</p>
    <div style="height:50px;border-radius:6px;background:repeating-linear-gradient(45deg,#fff 0px,#fff 10px,#f0f0f0 10px,#f0f0f0 20px);border:1px solid #e2e8f0;"></div>
  </div>
</div>

Gradients are treated as images in CSS. You can use them anywhere a `background-image` or `border-image` is accepted.

---

## 12. Pseudo-classes & Pseudo-elements

### 12.1 Pseudo-classes

Pseudo-classes select elements based on their state or position in the DOM tree, without requiring extra class names.

**User action states:**

```css
a:link    { color: blue; }     /* Unvisited link */
a:visited { color: purple; }   /* Visited link */
a:hover   { color: red; }      /* Mouse over */
a:focus   { outline: 2px solid blue; } /* Keyboard focus */
a:active  { color: orange; }   /* Actively being clicked */

/* LVHFA ordering rule: Link, Visited, Hover, Focus, Active */
```

> **`focus` vs `focus-visible`:** `:focus` shows outlines on *all* focus events, including mouse clicks. `:focus-visible` only shows the outline when the browser deems it necessary — i.e., for keyboard navigation — not for mouse clicks. Use `:focus-visible` to satisfy both "don't show outlines on click" design preferences *and* keyboard accessibility requirements. Never remove outlines entirely without a `:focus-visible` replacement.

**Structural pseudo-classes:**

```css
/* First and last children */
li:first-child  { font-weight: bold; }
li:last-child   { border-bottom: none; }

/* Nth patterns — accepts formulas like 2n, 2n+1, 3n+2 */
li:nth-child(even)  { background: #f5f5f5; }
li:nth-child(3)     { color: red; }
li:nth-child(3n+1)  { margin-left: 0; }

/* Type-scoped variants */
p:first-of-type { font-size: 1.1em; }
img:last-of-type { margin-bottom: 0; }

/* Only child */
p:only-child { margin: 0; }

/* Negation */
li:not(:last-child) { border-bottom: 1px solid #eee; }
input:not([type="submit"]):not([type="reset"]) { border: 1px solid #ccc; }

/* :is() — matches any in a list (forgiving, takes highest specificity in list) */
:is(h1, h2, h3) { line-height: 1.3; }

/* :where() — same as :is() but always zero specificity */
:where(h1, h2, h3) { color: inherit; }

/* :has() — parent selector: select X if it contains Y */
.card:has(img) { padding: 0; }               /* Cards with images */
label:has(+ input:required)::after { content: " *"; } /* Label for required field */
```

### 12.2 Pseudo-elements

Pseudo-elements create virtual elements in the DOM, or target specific sub-parts of real elements. They use `::` (two colons to distinguish from pseudo-classes).

```css
/* ::first-letter — styles the first letter of a block */
p.article-body::first-letter {
  font-size: 3em;
  font-weight: bold;
  float: left;
  line-height: 0.85;
  margin-right: 0.1em;
}

/* ::first-line — styles the first rendered line */
p::first-line { font-variant: small-caps; }

/* ::before and ::after — inject generated content */
.quote::before { content: "\201C"; font-size: 3em; color: #ccc; }
.quote::after  { content: "\201D"; }

/* No content, but useful for decorative shapes */
.badge::after {
  content: "";
  display: block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: green;
}

/* The highlighted text selection */
::selection {
  background: #ffeb3b;
  color: #000;
}

/* Placeholder text */
input::placeholder { color: #aaa; font-style: italic; }

/* Scroll marker (new, limited support) */
.track::before { content: ""; }
```

```html
<!-- HTML for the examples above -->
<p class="article-body">Lorem ipsum dolor sit amet, consectetur
adipiscing elit. Sed do eiusmod tempor.</p>

<blockquote class="quote">The best code is no code at all.</blockquote>

<span class="badge">Active</span>

<input type="text" placeholder="Enter your name">
```


## 13. Custom Properties (CSS Variables)

Custom properties (often called CSS variables) store reusable values in CSS itself. Unlike Sass variables which are resolved at compile time, CSS custom properties are live — they can be changed with JavaScript and respond to media queries.

### 13.1 Defining & Using Custom Properties

```css
:root {
  /* Convention: define on :root for global scope */
  --color-primary:   #0056b3;
  --color-text:      #1a1a2e;
  --color-bg:        #ffffff;
  --spacing-sm:      0.5rem;
  --spacing-md:      1rem;
  --spacing-lg:      2rem;
  --radius:          8px;
  --font-body:       "Inter", sans-serif;
  --transition-fast: 150ms ease;
}

.button {
  background: var(--color-primary);
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--radius);
  font-family: var(--font-body);
}
```

```html
<!-- HTML -->
<button class="button">Save changes</button>
```

**🖥 Rendered output — custom properties resolved to their computed values:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:20px;display:flex;flex-direction:column;gap:12px;">
  <p style="margin:0 0 4px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">.button — custom properties resolved to computed values:</p>
  <div style="display:grid;grid-template-columns:180px 1fr;gap:5px 16px;align-items:center;">
    <code style="font-size:11px;color:#6366f1;">background</code>
    <span style="font-size:12px;color:#334155;display:flex;align-items:center;gap:6px;">#0056b3 <span style="display:inline-block;width:14px;height:14px;background:#0056b3;border-radius:3px;vertical-align:middle;flex-shrink:0;"></span> <span style="color:#94a3b8;">(from --color-primary)</span></span>
    <code style="font-size:11px;color:#6366f1;">padding</code>
    <span style="font-size:12px;color:#334155;">8px 16px <span style="color:#94a3b8;">(--spacing-sm --spacing-md)</span></span>
    <code style="font-size:11px;color:#6366f1;">border-radius</code>
    <span style="font-size:12px;color:#334155;">8px <span style="color:#94a3b8;">(--radius)</span></span>
    <code style="font-size:11px;color:#6366f1;">font-family</code>
    <span style="font-size:12px;color:#334155;">"Inter", sans-serif <span style="color:#94a3b8;">(--font-body)</span></span>
  </div>
  <div>
    <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;">Visual result:</p>
    <button style="background:#0056b3;color:#fff;padding:8px 16px;border-radius:8px;border:none;font-family:'Segoe UI',system-ui,sans-serif;font-size:14px;font-weight:600;cursor:default;box-shadow:0 1px 3px rgba(0,0,0,0.15);">Save changes</button>
  </div>
  <div style="background:#fef3c7;border:1px solid #f59e0b;border-radius:6px;padding:10px 12px;font-size:12px;color:#92400e;">
    💡 Change <code>--color-primary</code> to <code>#dc3545</code> at <code>:root</code> and <em>every</em> button on the page updates automatically — no find &amp; replace needed.
  </div>
</div>

### 13.2 Fallback Values

```css
color: var(--color-accent, #ff5733);
/* Uses --color-accent if defined, #ff5733 if not */

/* Chained fallback */
color: var(--color-accent, var(--color-primary, #0056b3));
```

### 13.3 Scoped Custom Properties

Custom properties cascade and can be overridden locally:

```css
:root { --accent: blue; }

.dark-theme {
  --color-text: #f0f0f0;
  --color-bg:   #1a1a2e;
  --accent:     #7eb8f7;
}

/* Inside .dark-theme, elements pick up the overridden values */
```


### 13.4 Dynamic Themes with Custom Properties

```css
:root {
  --hue: 220;
  --color-primary: hsl(var(--hue), 80%, 45%);
  --color-primary-light: hsl(var(--hue), 80%, 80%);
  --color-primary-dark: hsl(var(--hue), 80%, 25%);
}

/* Changing --hue once updates the entire palette */
.theme-red    { --hue: 5; }
.theme-green  { --hue: 140; }
.theme-purple { --hue: 270; }
```

### 13.5 JavaScript & Custom Properties

```javascript
// Read a custom property
const style = getComputedStyle(document.documentElement);
const primary = style.getPropertyValue("--color-primary");

// Set a custom property
document.documentElement.style.setProperty("--color-primary", "#ff5733");

// This triggers a rerender — the variable change propagates to all usages
```

---

## 14. Responsive Design & Media Queries

Responsive design means your layout adapts to the device's screen size. The cornerstone is the viewport meta tag (in HTML) and media queries (in CSS).

### 14.1 The Viewport Meta Tag

This goes in your HTML `<head>` and is not a CSS property, but nothing else works without it:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Without it, mobile browsers render the page at desktop width and scale it down — your media queries will not fire correctly.

### 14.2 Media Query Syntax

```css
/* Apply rules when viewport is 768px or wider */
@media (min-width: 768px) {
  .container { max-width: 960px; }
}

/* Combine conditions */
@media (min-width: 600px) and (max-width: 1199px) {
  .sidebar { display: none; }
}

/* Target by media type */
@media print {
  nav, footer { display: none; }
}

/* Orientation */
@media (orientation: landscape) {
  .gallery { columns: 3; }
}

/* User preferences */
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #1a1a2e;
    --color-text: #e0e0e0;
  }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}

@media (prefers-contrast: more) {
  :root { --color-text: #000; --color-bg: #fff; }
}
```

### 14.3 Mobile-First vs Desktop-First

**Mobile-first:** Write base styles for small screens, then use `min-width` queries to add styles for larger screens.

```css
/* Base: mobile */
.nav { flex-direction: column; }

/* Tablet and above */
@media (min-width: 768px) {
  .nav { flex-direction: row; }
}

/* Desktop and above */
@media (min-width: 1200px) {
  .nav { gap: 2rem; }
}
```

```html
<!-- HTML -->
<nav class="nav">
  <a href="/">Home</a>
  <a href="/about">About</a>
  <a href="/docs">Docs</a>
  <a href="/contact">Contact</a>
</nav>
```

**🖥 Rendered output at each breakpoint:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;gap:14px;">
  <div>
    <p style="margin:0 0 6px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">Mobile (&lt; 768px) — flex-direction: column</p>
    <nav style="background:#1e293b;border-radius:6px;padding:8px;display:inline-flex;flex-direction:column;gap:4px;min-width:160px;">
      <a style="color:#f1f5f9;padding:6px 12px;border-radius:4px;font-size:13px;text-decoration:none;background:#0f172a;display:block;">Home</a>
      <a style="color:#94a3b8;padding:6px 12px;border-radius:4px;font-size:13px;text-decoration:none;display:block;">About</a>
      <a style="color:#94a3b8;padding:6px 12px;border-radius:4px;font-size:13px;text-decoration:none;display:block;">Docs</a>
      <a style="color:#94a3b8;padding:6px 12px;border-radius:4px;font-size:13px;text-decoration:none;display:block;">Contact</a>
    </nav>
    <p style="margin:4px 0 0 0;font-size:11px;color:#64748b;">Base styles (no media query). Links stack vertically, each taking full width.</p>
  </div>
  <div>
    <p style="margin:0 0 6px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">Tablet+ (≥ 768px) — flex-direction: row</p>
    <nav style="background:#1e293b;border-radius:6px;padding:8px 12px;display:inline-flex;flex-direction:row;gap:4px;">
      <a style="color:#f1f5f9;padding:6px 12px;border-radius:4px;font-size:13px;text-decoration:none;background:#0f172a;">Home</a>
      <a style="color:#94a3b8;padding:6px 12px;border-radius:4px;font-size:13px;text-decoration:none;">About</a>
      <a style="color:#94a3b8;padding:6px 12px;border-radius:4px;font-size:13px;text-decoration:none;">Docs</a>
      <a style="color:#94a3b8;padding:6px 12px;border-radius:4px;font-size:13px;text-decoration:none;">Contact</a>
    </nav>
    <p style="margin:4px 0 0 0;font-size:11px;color:#64748b;"><code>@media (min-width: 768px)</code> — <code>flex-direction: row</code> kicks in; links sit side by side.</p>
  </div>
  <div>
    <p style="margin:0 0 6px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">Desktop (≥ 1200px) — row + gap: 2rem</p>
    <nav style="background:#1e293b;border-radius:6px;padding:8px 24px;display:inline-flex;flex-direction:row;gap:32px;">
      <a style="color:#f1f5f9;padding:6px 12px;border-radius:4px;font-size:13px;text-decoration:none;background:#0f172a;">Home</a>
      <a style="color:#94a3b8;padding:6px 12px;border-radius:4px;font-size:13px;text-decoration:none;">About</a>
      <a style="color:#94a3b8;padding:6px 12px;border-radius:4px;font-size:13px;text-decoration:none;">Docs</a>
      <a style="color:#94a3b8;padding:6px 12px;border-radius:4px;font-size:13px;text-decoration:none;">Contact</a>
    </nav>
    <p style="margin:4px 0 0 0;font-size:11px;color:#64748b;"><code>@media (min-width: 1200px)</code> — <code>gap: 2rem</code> adds wider spacing between items.</p>
  </div>
</div>

**Desktop-first:** Write styles for desktop, then use `max-width` queries to adjust for smaller screens.

Mobile-first is considered best practice. Progressive enhancement works better with the cascade: start with a simple, functional layout and add complexity. It also tends to result in leaner CSS for mobile users.

### 14.4 Common Breakpoints

There are no universally correct breakpoints. Base them on your content, not device names. Common starting points:

```css
:root {
  /* These are guidelines, not rules */
}
/* Small phones: < 480px  */
/* Landscape phones / large phones: 480px+ */
/* Tablets: 768px+ */
/* Small desktops: 1024px+ */
/* Large desktops: 1280px+ */
/* Wide desktops: 1536px+ */
```

### 14.5 Responsive Units

| Unit | Relative to | Use case |
|---|---|---|
| `px` | Absolute (physical pixels) | Borders, fine details |
| `%` | Parent element's size | Fluid widths, relative padding |
| `em` | Current element's font-size | Component-scoped spacing |
| `rem` | Root (`html`) font-size | Site-wide type scale, spacing |
| `vw` | 1% of viewport width | Full-bleed elements, fluid type |
| `vh` | 1% of viewport height | Full-height layouts |
| `dvh` | 1% of dynamic viewport height | Mobile, where browser chrome appears/disappears |
| `svh` | 1% of smallest viewport height | Safe full-height on mobile |
| `ch` | Width of the "0" glyph | Limiting text column width |

```css
/* Limit readable line length */
p { max-width: 70ch; }

/* Full-height mobile-safe */
.hero { min-height: 100dvh; }
```

> **`vh` on mobile:** The browser chrome (address bar, toolbar) causes `100vh` to overflow on mobile browsers — the viewport height is calculated as if the chrome is hidden, but at page load it is visible. Use `100dvh` (dynamic viewport height) to get the actual visible height. Browser support is now excellent.

---


> **`vh` on mobile:** The browser chrome (address bar, toolbar) causes `100vh` to overflow on mobile browsers — the viewport height is calculated as if the chrome is hidden, but at page load it is visible. Use `100dvh` (dynamic viewport height) to get the actual visible height. Browser support is now excellent.

---

## 15. Transitions & Animations

### 15.1 Transitions

Transitions smoothly interpolate between two CSS states. They are triggered by state changes (hover, focus, class toggles).

```css
.button {
  background: #0056b3;
  transform: translateY(0);
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);

  /* Syntax: property duration timing-function delay */
  transition: background 200ms ease,
              transform  200ms ease,
              box-shadow 200ms ease;
}

.button:hover {
  background: #003d82;
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.15);
}
```

```html
<!-- HTML -->
<button class="button">Save changes</button>
```

**🖥 Rendered output — default state vs hover state:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;gap:40px;align-items:flex-start;flex-wrap:wrap;">
  <div>
    <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">Default state:</p>
    <button style="background:#0056b3;color:#fff;padding:10px 20px;border-radius:6px;border:none;font-family:'Segoe UI',system-ui,sans-serif;font-size:14px;font-weight:600;box-shadow:0 2px 4px rgba(0,0,0,0.12);cursor:default;display:block;">Save changes</button>
    <ul style="margin:8px 0 0 0;padding-left:16px;font-size:11px;color:#64748b;line-height:1.8;">
      <li>background: <code>#0056b3</code></li>
      <li>transform: <code>translateY(0)</code></li>
      <li>box-shadow: <code>0 2px 4px</code> (subtle)</li>
    </ul>
  </div>
  <div>
    <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">Hover state (200ms ease transition complete):</p>
    <button style="background:#003d82;color:#fff;padding:10px 20px;border-radius:6px;border:none;font-family:'Segoe UI',system-ui,sans-serif;font-size:14px;font-weight:600;box-shadow:0 8px 16px rgba(0,0,0,0.18);cursor:default;display:block;transform:translateY(-2px);position:relative;top:-2px;">Save changes</button>
    <ul style="margin:8px 0 0 0;padding-left:16px;font-size:11px;color:#64748b;line-height:1.8;">
      <li>background: <code>#003d82</code> (darker)</li>
      <li>transform: <code>translateY(-2px)</code> (lifts)</li>
      <li>box-shadow: <code>0 8px 16px</code> (larger)</li>
    </ul>
  </div>
</div>
<p style="margin:12px 0 0 0;font-size:11px;color:#64748b;font-family:'Segoe UI',system-ui,sans-serif;background:#f0fdf4;border:1px solid #86efac;border-radius:6px;padding:10px 12px;">
  <strong style="color:#166534;">Performance tip:</strong> Only <code>transform</code> and <code>opacity</code> are GPU-composited — animating them never triggers layout. Avoid animating <code>width</code>, <code>height</code>, <code>top</code>, <code>left</code>, <code>margin</code> or <code>padding</code> which cause expensive layout reflows every frame.
</p>

**Transition properties:**
```css
transition-property: background, transform;  /* Which properties to animate */
transition-duration: 200ms;                  /* How long */
transition-timing-function: ease;            /* Easing curve */
transition-delay: 50ms;                      /* Wait before starting */
transition: all 300ms ease;                  /* All properties (avoid in production) */
```

**Timing functions:**

| Value | Description |
|---|---|
| `ease` | Slow start, fast middle, slow end (default) |
| `linear` | Constant speed |
| `ease-in` | Slow start, fast end |
| `ease-out` | Fast start, slow end |
| `ease-in-out` | Slow start and end |
| `cubic-bezier(x1,y1,x2,y2)` | Custom curve |
| `steps(4, end)` | Discrete steps (good for sprite animations) |

> **Do not transition `all`.** It causes the browser to check every single property on every frame, which is expensive. Always list only the properties you intend to animate.

> **Only animate `transform` and `opacity` for smooth 60fps animations.** These are handled by the GPU compositor and do not trigger layout or paint. Animating `width`, `height`, `margin`, `padding`, `top`, `left` causes a layout reflow on every frame, leading to janky animations.

### 15.2 Keyframe Animations

`@keyframes` define animations that play automatically, loop, or play on load.

```css
@keyframes fade-in {
  from { opacity: 0; transform: translateY(10px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50%       { transform: scale(1.05); }
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

Apply with `animation`:

```css
.hero-title {
  animation: fade-in 400ms ease-out both;
  /* Name | Duration | Easing | Fill-mode */
}

.loader {
  animation: spin 1s linear infinite;
}

.notification {
  animation: pulse 2s ease-in-out infinite;
}
```

**🖥 Rendered output — animation states at key moments:**

<style>
@keyframes css-guide-fade-in { from { opacity:0; transform:translateY(12px); } to { opacity:1; transform:translateY(0); } }
@keyframes css-guide-spin { to { transform:rotate(360deg); } }
@keyframes css-guide-pulse { 0%,100% { transform:scale(1); box-shadow:0 0 0 0 rgba(239,68,68,0.4); } 50% { transform:scale(1.06); box-shadow:0 0 0 8px rgba(239,68,68,0); } }
</style>
<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;gap:18px;">
  <div>
    <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">fade-in — animation: fade-in 400ms ease-out both</p>
    <div style="background:#f1f5f9;border:1px solid #e2e8f0;border-radius:6px;padding:14px 18px;animation:css-guide-fade-in 2s ease-out both infinite alternate;font-size:15px;font-weight:600;color:#1e293b;">Hero Title</div>
    <p style="margin:6px 0 0 0;font-size:11px;color:#64748b;"><strong>0ms</strong>: opacity 0, translateY +12px → <strong>400ms</strong>: opacity 1, translateY 0 → holds final state (<code>fill-mode: both</code>).</p>
  </div>
  <div style="display:flex;gap:32px;align-items:flex-start;flex-wrap:wrap;">
    <div>
      <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">spin — animation: spin 1s linear infinite</p>
      <div style="width:44px;height:44px;border:5px solid #e2e8f0;border-top-color:#6366f1;border-radius:50%;animation:css-guide-spin 1s linear infinite;"></div>
      <p style="margin:6px 0 0 0;font-size:11px;color:#64748b;">Loader spinner — rotates 360° every second, forever.</p>
    </div>
    <div>
      <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">pulse — animation: pulse 2s ease-in-out infinite</p>
      <div style="display:flex;align-items:center;gap:10px;margin-top:6px;">
        <span style="display:inline-block;background:#ef4444;width:14px;height:14px;border-radius:50%;animation:css-guide-pulse 2s ease-in-out infinite;flex-shrink:0;"></span>
        <span style="font-size:13px;color:#334155;font-weight:600;">3 new notifications</span>
      </div>
      <p style="margin:6px 0 0 0;font-size:11px;color:#64748b;">Scales between 1.0 and 1.06 — subtle "breathing" badge. 0% &amp; 100% = scale(1), 50% = scale(1.06).</p>
    </div>
  </div>
  <div style="background:#fef3c7;border:1px solid #f59e0b;border-radius:6px;padding:10px 12px;font-size:12px;color:#92400e;">
    <strong>Reduced motion:</strong> Always wrap intensive animations in <code>@media (prefers-reduced-motion: reduce)</code> so users who have enabled OS-level "Reduce Motion" get a static version.
  </div>
</div>

**Animation properties:**

```css
animation-name:            fade-in;
animation-duration:        400ms;
animation-timing-function: ease-out;
animation-delay:           100ms;
animation-iteration-count: 1;         /* infinite | any number */
animation-direction:       normal;    /* reverse | alternate | alternate-reverse */
animation-fill-mode:       both;      /* none | forwards | backwards | both */
animation-play-state:      running;   /* paused — for JS control */
```


## 16. Transforms (2D & 3D)

The `transform` property applies visual transformations without affecting layout — the element still occupies its original space in the flow.

### 16.1 2D Transforms

```css
.box {
  transform: translateX(50px);         /* Move right 50px */
  transform: translateY(-20px);        /* Move up 20px */
  transform: translate(50px, -20px);   /* Move right and up */
  transform: translate(50%);           /* Move right by 50% of element's own width */

  transform: rotate(45deg);            /* Rotate clockwise 45° */
  transform: rotate(-0.25turn);        /* Quarter turn anticlockwise */

  transform: scale(1.5);              /* Scale to 150% */
  transform: scale(2, 0.5);           /* Width ×2, height ×0.5 */
  transform: scaleX(0);               /* Collapse width (good for reveal animations) */

  transform: skew(10deg, 5deg);       /* Skew on X and Y axes */

  /* Multiple transforms — applied right to left */
  transform: rotate(45deg) scale(1.2) translateX(20px);
}
```

**🖥 Rendered output — visual effect of each transform on a square element:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-wrap:wrap;gap:20px;align-items:flex-end;">
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <div style="width:60px;height:60px;background:#6366f1;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;">■</div>
    <p style="margin:0;font-size:10px;color:#555;font-family:monospace;text-align:center;">Original</p>
  </div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <div style="width:60px;height:60px;background:#6366f1;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;transform:translateX(20px);"></div>
    <p style="margin:0;font-size:10px;color:#555;font-family:monospace;text-align:center;">translateX<br>(20px)</p>
  </div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <div style="width:60px;height:60px;background:#6366f1;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;transform:translateY(-14px);"></div>
    <p style="margin:0;font-size:10px;color:#555;font-family:monospace;text-align:center;">translateY<br>(-14px)</p>
  </div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <div style="width:60px;height:60px;background:#6366f1;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;transform:rotate(35deg);"></div>
    <p style="margin:0;font-size:10px;color:#555;font-family:monospace;text-align:center;">rotate<br>(35deg)</p>
  </div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <div style="width:60px;height:60px;background:#6366f1;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;transform:scale(1.5);"></div>
    <p style="margin:0;font-size:10px;color:#555;font-family:monospace;text-align:center;">scale<br>(1.5)</p>
  </div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <div style="width:60px;height:60px;background:#6366f1;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;transform:scale(2, 0.5);"></div>
    <p style="margin:0;font-size:10px;color:#555;font-family:monospace;text-align:center;">scale<br>(2, 0.5)</p>
  </div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <div style="width:60px;height:60px;background:#6366f1;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;transform:skew(15deg, 5deg);"></div>
    <p style="margin:0;font-size:10px;color:#555;font-family:monospace;text-align:center;">skew<br>(15deg,5deg)</p>
  </div>
</div>
<p style="margin:12px 0 0 0;font-size:11px;color:#64748b;font-family:'Segoe UI',system-ui,sans-serif;background:#f0f9ff;border:1px solid #7dd3fc;border-radius:6px;padding:10px 12px;">
  <strong style="color:#0369a1;">Key point:</strong> <code>transform</code> does <em>not</em> affect layout. Each box above still occupies its original document-flow space — neighbouring elements are never pushed or pulled.
</p>

### 16.2 Transform Origin

`transform-origin` sets the pivot point of the transform. Default is `50% 50%` (the centre).

```css
.pin {
  transform-origin: bottom center; /* Rotate from the bottom */
  transform: rotate(15deg);
}

.tooltip {
  transform-origin: top left;
  transform: scale(0);   /* Expands from top-left corner */
}

.tooltip.visible {
  transform: scale(1);
}
\
### 16.3 3D Transforms

For 3D effects, the parent needs a \perspective\ value to establish the 3D space:

\\css
.scene {
  perspective: 800px;   /* Distance from viewer to z=0 plane */
}

.card {
  transform: rotateY(30deg);
  transform-style: preserve-3d;  /* Children participate in 3D space */
}
\

**Card flip animation:**
```css
.card-inner {
  transform-style: preserve-3d;
  transition: transform 600ms ease;
}

.card:hover .card-inner {
  transform: rotateY(180deg);
}

.card-front, .card-back {
  backface-visibility: hidden; /* Hide the back of the face when flipped away */
}

.card-back {
  transform: rotateY(180deg);
}
```

```html
<!-- HTML -->
<div class="card">
  <div class="card-inner">
    <div class="card-front">Front content</div>
    <div class="card-back">Back content</div>
  </div>
</div>
```

**🖥 Rendered output — card flip state sequence (viewed from above):**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;gap:20px;align-items:flex-start;flex-wrap:wrap;">
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <p style="margin:0;font-size:10px;font-weight:700;color:#555;font-family:monospace;">0deg — front visible</p>
    <div style="width:120px;height:80px;background:#6366f1;border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:13px;font-weight:600;box-shadow:0 4px 12px rgba(99,102,241,0.35);">Front content</div>
  </div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <p style="margin:0;font-size:10px;font-weight:700;color:#555;font-family:monospace;">90deg — edge-on (card invisible)</p>
    <div style="width:4px;height:80px;background:#94a3b8;border-radius:2px;"></div>
    <p style="margin:0;font-size:10px;color:#94a3b8;text-align:center;">neither face<br>visible</p>
  </div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <p style="margin:0;font-size:10px;font-weight:700;color:#555;font-family:monospace;">180deg — back face visible</p>
    <div style="width:120px;height:80px;background:#0f172a;border-radius:8px;display:flex;align-items:center;justify-content:center;color:#e2e8f0;font-size:13px;font-weight:600;box-shadow:0 4px 12px rgba(0,0,0,0.3);">Back content</div>
  </div>
</div>
<div style="margin-top:14px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:12px 14px;font-size:12px;color:#475569;font-family:'Segoe UI',system-ui,sans-serif;">
  <p style="margin:0 0 6px 0;"><strong style="color:#1e293b;">How <code>backface-visibility: hidden</code> works:</strong></p>
  <ul style="margin:0;padding-left:18px;line-height:1.8;">
    <li><strong>.card-front</strong> at 0deg faces viewer — visible. At 180deg it faces away → hidden.</li>
    <li><strong>.card-back</strong> pre-rotated 180deg (faces away at rest). At hover (180deg flip) it faces viewer — visible.</li>
    <li>The 600ms <code>ease</code> transition starts and ends slowly with a fast middle, giving a natural physical flip feel.</li>
  </ul>
</div>

---

## 17. CSS Functions

CSS has a growing library of built-in functions that dramatically reduce the need for JavaScript or preprocessors.

### 17.1 `calc()`

Perform arithmetic with mixed units:

```css
.sidebar {
  width: calc(300px - 2rem);
}

.full-bleed {
  /* Negative calc to break out of a container */
  margin-left: calc(-1 * var(--page-padding));
  width: calc(100% + 2 * var(--page-padding));
}

.striped-bg {
  background-size: calc(var(--stripe-width) * 2) 100%;
}
```


**🖥 Rendered output — calculated values at runtime:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;gap:14px;">
  <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;">
    <p style="margin:0 0 10px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">Computed values (assuming 1rem = 16px, --page-padding = 24px, container = 800px):</p>
    <div style="display:grid;grid-template-columns:240px 1fr;gap:6px 16px;align-items:baseline;">
      <code style="font-size:12px;color:#6366f1;">calc(300px - 2rem)</code><span style="font-size:13px;color:#1e293b;font-weight:600;">= 268px</span>
      <code style="font-size:12px;color:#6366f1;">calc(-1 * 24px)</code><span style="font-size:13px;color:#1e293b;font-weight:600;">= -24px <span style="font-weight:400;color:#64748b;">(margin-left: shifts left by 24px)</span></span>
      <code style="font-size:12px;color:#6366f1;">calc(100% + 48px)</code><span style="font-size:13px;color:#1e293b;font-weight:600;">= 848px <span style="font-weight:400;color:#64748b;">(of 800px container)</span></span>
    </div>
  </div>
  <div>
    <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">Full-bleed layout diagram:</p>
    <div style="background:#e0f2fe;border-radius:6px;padding:8px;position:relative;">
      <div style="background:#7dd3fc;border-radius:4px;padding:6px 10px;font-size:11px;color:#075985;text-align:center;">parent container (800px)</div>
      <div style="background:#0284c7;border-radius:4px;padding:6px 10px;font-size:11px;color:#fff;text-align:center;margin:4px -8px;position:relative;">
        .full-bleed (848px = 800px + 48px)
        <span style="position:absolute;left:0;top:50%;transform:translateY(-50%);font-size:10px;background:#075985;color:#fff;padding:2px 5px;border-radius:2px;">←24px</span>
        <span style="position:absolute;right:0;top:50%;transform:translateY(-50%);font-size:10px;background:#075985;color:#fff;padding:2px 5px;border-radius:2px;">24px→</span>
      </div>
    </div>
    <p style="margin:6px 0 0 0;font-size:11px;color:#64748b;">The element bleeds 24px beyond both edges of its parent — without any JavaScript. <code>+</code> and <code>-</code> operators require whitespace: <code>calc(50% - 2rem)</code> ✓ &nbsp; <code>calc(50%-2rem)</code> ✗</p>
  </div>
</div>

`calc()` supports `+`, `-`, `*`, `/`. Whitespace around `+` and `-` is **required** — `calc(50% -2rem)` is invalid; `calc(50% - 2rem)` is correct.

### 17.2 `clamp()`

Constrains a value between a minimum and maximum:

```css
/* clamp(minimum, preferred, maximum) */

font-size: clamp(1rem, 4vw, 2rem);
/* At narrow viewports: 1rem; at wide viewports: 2rem; fluid in between */

padding: clamp(1rem, 5%, 3rem);
/* Fluid padding that never gets too small or too large */

.container {
  width: clamp(320px, 90%, 1200px);
  /* Never narrower than 320px, never wider than 1200px, 90% of viewport in between */
}
```

**🖥 Rendered output — computed values at various viewport widths (1rem = 16px):**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;gap:14px;">
  <div>
    <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">font-size: clamp(1rem, 4vw, 2rem)</p>
    <div style="overflow-x:auto;">
      <table style="border-collapse:collapse;width:100%;font-size:12px;">
        <thead>
          <tr style="background:#f1f5f9;">
            <th style="padding:6px 12px;text-align:left;border:1px solid #e2e8f0;color:#475569;">Viewport</th>
            <th style="padding:6px 12px;text-align:left;border:1px solid #e2e8f0;color:#475569;">4vw preferred</th>
            <th style="padding:6px 12px;text-align:left;border:1px solid #e2e8f0;color:#475569;">Clamped result</th>
            <th style="padding:6px 12px;text-align:left;border:1px solid #e2e8f0;color:#475569;">Zone</th>
          </tr>
        </thead>
        <tbody>
          <tr><td style="padding:5px 12px;border:1px solid #e2e8f0;">320px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;">12.8px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;font-weight:600;">16px (1rem)</td><td style="padding:5px 12px;border:1px solid #e2e8f0;color:#0369a1;font-size:11px;">min clamp</td></tr>
          <tr style="background:#f8fafc;"><td style="padding:5px 12px;border:1px solid #e2e8f0;">500px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;">20px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;font-weight:600;">20px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;color:#166534;font-size:11px;">fluid zone</td></tr>
          <tr><td style="padding:5px 12px;border:1px solid #e2e8f0;">700px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;">28px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;font-weight:600;">28px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;color:#166534;font-size:11px;">fluid zone</td></tr>
          <tr style="background:#f8fafc;"><td style="padding:5px 12px;border:1px solid #e2e8f0;">800px+</td><td style="padding:5px 12px;border:1px solid #e2e8f0;">32px+</td><td style="padding:5px 12px;border:1px solid #e2e8f0;font-weight:600;">32px (2rem)</td><td style="padding:5px 12px;border:1px solid #e2e8f0;color:#9f1239;font-size:11px;">max clamp</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <p style="margin:0;font-size:11px;color:#64748b;"><code>clamp()</code> is shorthand for <code>max(MIN, min(PREFERRED, MAX))</code>. No media queries needed.</p>
</div>


<div style="margin-top:14px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:12px 14px;font-size:12px;color:#475569;font-family:'Segoe UI',system-ui,sans-serif;">
  <p style="margin:0 0 6px 0;"><strong style="color:#1e293b;">How <code>backface-visibility: hidden</code> works:</strong></p>
  <ul style="margin:0;padding-left:18px;line-height:1.8;">
    <li><strong>.card-front</strong> at 0deg faces viewer — visible. At 180deg it faces away → hidden.</li>
    <li><strong>.card-back</strong> pre-rotated 180deg (faces away at rest). At hover (180deg flip) it faces viewer — visible.</li>
    <li>The 600ms <code>ease</code> transition starts and ends slowly with a fast middle, giving a natural physical flip feel.</li>
  </ul>
</div>

**🖥 Rendered output — computed values at various viewport widths (1rem = 16px):**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;gap:14px;">
  <div>
    <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">font-size: clamp(1rem, 4vw, 2rem)</p>
    <div style="overflow-x:auto;">
      <table style="border-collapse:collapse;width:100%;font-size:12px;">
        <thead>
          <tr style="background:#f1f5f9;">
            <th style="padding:6px 12px;text-align:left;border:1px solid #e2e8f0;color:#475569;">Viewport</th>
            <th style="padding:6px 12px;text-align:left;border:1px solid #e2e8f0;color:#475569;">4vw preferred</th>
            <th style="padding:6px 12px;text-align:left;border:1px solid #e2e8f0;color:#475569;">Clamped result</th>
            <th style="padding:6px 12px;text-align:left;border:1px solid #e2e8f0;color:#475569;">Zone</th>
          </tr>
        </thead>
        <tbody>
          <tr><td style="padding:5px 12px;border:1px solid #e2e8f0;">320px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;">12.8px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;font-weight:600;">16px (1rem)</td><td style="padding:5px 12px;border:1px solid #e2e8f0;color:#0369a1;font-size:11px;">min clamp</td></tr>
          <tr style="background:#f8fafc;"><td style="padding:5px 12px;border:1px solid #e2e8f0;">500px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;">20px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;font-weight:600;">20px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;color:#166534;font-size:11px;">fluid zone</td></tr>
          <tr><td style="padding:5px 12px;border:1px solid #e2e8f0;">700px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;">28px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;font-weight:600;">28px</td><td style="padding:5px 12px;border:1px solid #e2e8f0;color:#166534;font-size:11px;">fluid zone</td></tr>
          <tr style="background:#f8fafc;"><td style="padding:5px 12px;border:1px solid #e2e8f0;">800px+</td><td style="padding:5px 12px;border:1px solid #e2e8f0;">32px+</td><td style="padding:5px 12px;border:1px solid #e2e8f0;font-weight:600;">32px (2rem)</td><td style="padding:5px 12px;border:1px solid #e2e8f0;color:#9f1239;font-size:11px;">max clamp</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div>
    <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">width: clamp(320px, 90%, 1200px)</p>
    <div style="display:flex;gap:3px;align-items:flex-end;height:60px;">
      <div style="flex:0 0 40px;display:flex;flex-direction:column;align-items:center;gap:2px;"><div style="width:100%;height:40px;background:#0284c7;border-radius:4px 4px 0 0;"></div><span style="font-size:9px;color:#64748b;">320px<br>min</span></div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:2px;"><div style="width:100%;height:30px;background:#86efac;border-radius:4px 4px 0 0;"></div><span style="font-size:9px;color:#64748b;">fluid (90%)</span></div>
      <div style="flex:0 0 52px;display:flex;flex-direction:column;align-items:center;gap:2px;"><div style="width:100%;height:40px;background:#f97316;border-radius:4px 4px 0 0;"></div><span style="font-size:9px;color:#64748b;">1200px<br>max</span></div>
    </div>
    <p style="margin:8px 0 0 0;font-size:11px;color:#64748b;"><code>clamp()</code> is shorthand for <code>max(MIN, min(PREFERRED, MAX))</code>. No media queries needed.</p>
  </div>
</div>

### 17.3 `min()` and `max()`

```css
/* min() — uses the smallest value */
width: min(100%, 600px);          /* As wide as parent but never exceeds 600px */
font-size: min(2rem, 5vw);        /* Smaller of the two */

/* max() — uses the largest value */
height: max(200px, 50vh);         /* Taller of the two */
padding: max(1rem, env(safe-area-inset-bottom)); /* Handles iPhone notch */
```


### 17.4 `env()`

Safe area insets for devices with notches and rounded corners (primarily iOS):

```css
.fixed-bar {
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}
```

Always combine with a fallback or `max()`:

```css
padding-bottom: max(1rem, env(safe-area-inset-bottom));
```


Always combine with a fallback or `max()`:

```css
padding-bottom: max(1rem, env(safe-area-inset-bottom));
```

### 17.5 `var()`

Covered in [Section 13](#13-custom-properties-css-variables). Quick reference:

```css
color: var(--color-primary);
color: var(--color-primary, #0056b3);   /* With fallback */
```

### 17.6 Color Functions

```css
/* Mix two colours */
color: color-mix(in oklch, var(--color-primary) 50%, white);

/* Relative colour syntax (powerful — modify a colour channel) */
--color-primary-light: oklch(from var(--color-primary) calc(l + 0.2) c h);
```

### 17.7 `counter()`

CSS counters allow auto-numbering without JavaScript:

```css
ol {
  counter-reset: item;
  list-style: none;
}

li {
  counter-increment: item;
}

li::before {
  content: counter(item, decimal-leading-zero) ".";
  margin-right: 0.5rem;
}
```

---

## 18. Shadows, Filters & Visual Effects

### 18.1 Box Shadow

```css
.card {
  /* Offset-X | Offset-Y | Blur | Spread | Colour */
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);

  /* Inset shadow (inside the box) */
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);

  /* Multiple shadows (layered, first is on top) */
  box-shadow:
    0 1px 3px rgba(0,0,0,0.12),
    0 8px 24px rgba(0,0,0,0.08);
}
```

**🖥 Rendered output — shadow anatomy and elevation levels:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;gap:16px;">
  <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;">
    <p style="margin:0 0 10px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">Shadow anatomy: box-shadow: X-offset Y-offset Blur Spread Colour</p>
    <div style="display:grid;grid-template-columns:auto 1fr;gap:4px 12px;align-items:center;font-size:12px;">
      <code style="color:#6366f1;">0px</code><span style="color:#334155;">X-offset — no horizontal shift</span>
      <code style="color:#6366f1;">2px</code><span style="color:#334155;">Y-offset — shadow falls 2px downward</span>
      <code style="color:#6366f1;">8px</code><span style="color:#334155;">Blur radius — how diffuse/soft</span>
      <code style="color:#6366f1;">0px</code><span style="color:#334155;">Spread — no extra size expansion</span>
      <code style="color:#6366f1;">rgba(0,0,0,0.12)</code><span style="color:#334155;">Colour — 12% opaque black</span>
    </div>
  </div>
  <div>
    <p style="margin:0 0 10px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">Elevation levels (material-style):</p>
    <div style="display:flex;gap:20px;flex-wrap:wrap;align-items:flex-end;padding:16px 0 20px 0;">
      <div style="display:flex;flex-direction:column;align-items:center;gap:10px;">
        <div style="width:100px;height:64px;background:#fff;border-radius:8px;box-shadow:0 1px 3px rgba(0,0,0,0.12),0 1px 2px rgba(0,0,0,0.24);display:flex;align-items:center;justify-content:center;font-size:11px;color:#475569;font-weight:600;">Level 1</div>
        <p style="margin:0;font-size:10px;color:#64748b;text-align:center;">default card<br>subtle shadow</p>
      </div>
      <div style="display:flex;flex-direction:column;align-items:center;gap:10px;">
        <div style="width:100px;height:64px;background:#fff;border-radius:8px;box-shadow:0 10px 20px rgba(0,0,0,0.15),0 3px 6px rgba(0,0,0,0.10);display:flex;align-items:center;justify-content:center;font-size:11px;color:#475569;font-weight:600;">Level 3</div>
        <p style="margin:0;font-size:10px;color:#64748b;text-align:center;">hover state<br>visually lifts</p>
      </div>
      <div style="display:flex;flex-direction:column;align-items:center;gap:10px;">
        <div style="width:100px;height:64px;background:#fff;border-radius:8px;box-shadow:0 15px 25px rgba(0,0,0,0.15),0 5px 10px rgba(0,0,0,0.05);display:flex;align-items:center;justify-content:center;font-size:11px;color:#475569;font-weight:600;">Level 4</div>
        <p style="margin:0;font-size:10px;color:#64748b;text-align:center;">modal dialog<br>highest elev.</p>
      </div>
    </div>
    <p style="margin:0;font-size:11px;color:#64748b;">Higher elevation = larger, softer, more diffuse shadow — communicates depth and importance.</p>
  </div>
</div>

**Cheat sheet for material-style shadows:**
```css
/* Level 1 — subtle elevation */
box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);

/* Level 2 */
box-shadow: 0 3px 6px rgba(0,0,0,0.15), 0 2px 4px rgba(0,0,0,0.12);

/* Level 3 — card hover */
box-shadow: 0 10px 20px rgba(0,0,0,0.15), 0 3px 6px rgba(0,0,0,0.10);

/* Level 4 — modals */
box-shadow: 0 15px 25px rgba(0,0,0,0.15), 0 5px 10px rgba(0,0,0,0.05);
```

### 18.2 Text Shadow

```css
h1 {
  /* Offset-X | Offset-Y | Blur | Colour */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);

  /* Multiple layered shadows */
  text-shadow:
    0 1px 0 #ccc,
    0 2px 0 #c9c9c9,
    0 3px 0 #bbb;
}
```

### 18.3 CSS Filters

`filter` applies graphical effects to an element and its children:

```css
img {
  filter: grayscale(100%);      /* Black and white */
  filter: blur(4px);            /* Blur */
  filter: brightness(1.2);      /* 20% brighter */
  filter: contrast(2);          /* Double contrast */
  filter: sepia(100%);          /* Sepia tone */
  filter: saturate(150%);       /* More vivid */
  filter: hue-rotate(90deg);    /* Shift hue */
  filter: invert(100%);         /* Invert colours */
  filter: opacity(50%);         /* Semi-transparent (same as opacity but compositable) */

  /* Multiple filters */
  filter: brightness(1.1) contrast(1.05) saturate(1.2);
}
```

`backdrop-filter` applies filters to what is *behind* an element — perfect for frosted glass:

```css
.frosted-panel {
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(12px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
```

```html
<!-- HTML: panel floats over a colourful background -->
<div class="colourful-bg">
  <div class="frosted-panel">
    <h2>Frosted Glass Panel</h2>
    <p>Content here appears to float over a blurred background.</p>
  </div>
</div>
```

**🖥 Rendered output — filters and frosted glass effect:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;gap:14px;">
  <div>
    <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">filter: applied to the same image swatch:</p>
    <div style="display:flex;gap:8px;flex-wrap:wrap;">
      <div style="display:flex;flex-direction:column;align-items:center;gap:4px;"><div style="width:70px;height:50px;border-radius:4px;background:linear-gradient(135deg,#f97316,#fb923c);"></div><span style="font-size:10px;color:#64748b;text-align:center;">original</span></div>
      <div style="display:flex;flex-direction:column;align-items:center;gap:4px;"><div style="width:70px;height:50px;border-radius:4px;background:linear-gradient(135deg,#f97316,#fb923c);filter:grayscale(100%);"></div><span style="font-size:10px;color:#64748b;text-align:center;">grayscale<br>(100%)</span></div>
      <div style="display:flex;flex-direction:column;align-items:center;gap:4px;"><div style="width:70px;height:50px;border-radius:4px;background:linear-gradient(135deg,#f97316,#fb923c);filter:blur(4px);"></div><span style="font-size:10px;color:#64748b;text-align:center;">blur<br>(4px)</span></div>
      <div style="display:flex;flex-direction:column;align-items:center;gap:4px;"><div style="width:70px;height:50px;border-radius:4px;background:linear-gradient(135deg,#f97316,#fb923c);filter:brightness(1.5);"></div><span style="font-size:10px;color:#64748b;text-align:center;">brightness<br>(1.5)</span></div>
      <div style="display:flex;flex-direction:column;align-items:center;gap:4px;"><div style="width:70px;height:50px;border-radius:4px;background:linear-gradient(135deg,#f97316,#fb923c);filter:sepia(100%);"></div><span style="font-size:10px;color:#64748b;text-align:center;">sepia<br>(100%)</span></div>
      <div style="display:flex;flex-direction:column;align-items:center;gap:4px;"><div style="width:70px;height:50px;border-radius:4px;background:linear-gradient(135deg,#f97316,#fb923c);filter:hue-rotate(120deg);"></div><span style="font-size:10px;color:#64748b;text-align:center;">hue-rotate<br>(120deg)</span></div>
      <div style="display:flex;flex-direction:column;align-items:center;gap:4px;"><div style="width:70px;height:50px;border-radius:4px;background:linear-gradient(135deg,#f97316,#fb923c);filter:invert(100%);"></div><span style="font-size:10px;color:#64748b;text-align:center;">invert<br>(100%)</span></div>
    </div>
  </div>
  <div>
    <p style="margin:0 0 8px 0;font-size:11px;font-weight:700;color:#555;font-family:monospace;">backdrop-filter: blur(12px) — frosted glass panel:</p>
    <div style="position:relative;border-radius:10px;overflow:hidden;height:130px;background:linear-gradient(135deg,#6366f1 0%,#f97316 50%,#22c55e 100%);">
      <div style="position:absolute;inset:0;display:flex;align-items:center;gap:8px;padding:8px;opacity:0.4;">
        <div style="width:40px;height:40px;background:#fff;border-radius:50%;"></div>
        <div style="flex:1;height:10px;background:#fff;border-radius:4px;"></div>
        <div style="width:40px;height:40px;background:#fff;border-radius:50%;"></div>
      </div>
      <div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:rgba(255,255,255,0.18);backdrop-filter:blur(12px) saturate(180%);-webkit-backdrop-filter:blur(12px) saturate(180%);border:1px solid rgba(255,255,255,0.3);border-radius:10px;padding:14px 20px;min-width:200px;text-align:center;">
        <p style="margin:0 0 4px 0;font-size:13px;font-weight:700;color:#fff;text-shadow:0 1px 3px rgba(0,0,0,0.5);">Frosted Glass Panel</p>
        <p style="margin:0;font-size:11px;color:rgba(255,255,255,0.85);">backdrop-filter blurs what is<br>behind this element</p>
      </div>
    </div>
    <p style="margin:6px 0 0 0;font-size:11px;color:#64748b;"><code>filter</code> affects the element &amp; its children. <code>backdrop-filter</code> affects what is <em>behind</em> the element — perfect for glass/acrylic UI effects.</p>
  </div>
</div>

### 18.4 Clip Path

`clip-path` masks an element to a custom shape:

```css
.circle    { clip-path: circle(50%); }
.ellipse   { clip-path: ellipse(60% 40% at 50% 50%); }
.triangle  { clip-path: polygon(50% 0%, 0% 100%, 100% 100%); }
.diagonal  { clip-path: polygon(0 0, 100% 0, 100% 80%, 0 100%); }
```

**🖥️ Rendered output — visible region for each clip-path shape:**

<div style="font-family:'Segoe UI',system-ui,sans-serif;display:flex;gap:16px;flex-wrap:wrap;align-items:flex-start;">
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <div style="width:90px;height:90px;background:linear-gradient(135deg,#6366f1,#8b5cf6);clip-path:circle(50%);display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;">Circle</div>
    <p style="margin:0;font-size:10px;color:#555;font-family:monospace;text-align:center;">circle(50%)</p>
  </div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <div style="width:90px;height:90px;background:linear-gradient(135deg,#0ea5e9,#38bdf8);clip-path:ellipse(50% 35% at 50% 50%);display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;">Ellipse</div>
    <p style="margin:0;font-size:10px;color:#555;font-family:monospace;text-align:center;">ellipse(50% 35%<br>at 50% 50%)</p>
  </div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <div style="width:90px;height:90px;background:linear-gradient(135deg,#f97316,#fb923c);clip-path:polygon(50% 0%,0% 100%,100% 100%);display:flex;align-items:flex-end;justify-content:center;color:#fff;font-size:11px;font-weight:700;padding-bottom:10px;">Tri</div>
    <p style="margin:0;font-size:10px;color:#555;font-family:monospace;text-align:center;">polygon<br>triangle</p>
  </div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <div style="width:90px;height:90px;background:linear-gradient(135deg,#22c55e,#4ade80);clip-path:polygon(0 0,100% 0,100% 75%,0 100%);display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;">Diag</div>
    <p style="margin:0;font-size:10px;color:#555;font-family:monospace;text-align:center;">polygon<br>diagonal cut</p>
  </div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
    <div style="width:90px;height:90px;background:linear-gradient(135deg,#f43f5e,#fb7185);clip-path:polygon(25% 0%,75% 0%,100% 50%,75% 100%,25% 100%,0% 50%);display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;">Hex</div>
    <p style="margin:0;font-size:10px;color:#555;font-family:monospace;text-align:center;">polygon<br>hexagon</p>
  </div>
</div>
<p style="margin:12px 0 0 0;font-size:11px;color:#64748b;font-family:'Segoe UI',system-ui,sans-serif;">Everything outside the clip path — background, borders, text — is completely hidden. Useful for hero diagonals, avatar circles, and decorative section dividers.</p>

### 18.5 Mix Blend Mode

```css
.overlay {
  mix-blend-mode: multiply;    /* Darkens */
  mix-blend-mode: screen;      /* Lightens */
  mix-blend-mode: overlay;     /* Contrast boost */
  mix-blend-mode: color-burn;
  mix-blend-mode: hard-light;
  mix-blend-mode: difference;  /* Inverts where colours overlap */
}
```


> A few highlights: `font: inherit` on form elements is essential — browsers render `<input>` and `<button>` with their own font stack instead of inheriting from the page. `max-width: 100%` on images prevents them from overflowing containers. `display: block` on images removes the inline baseline gap that causes gaps below images.

---

## 19. CSS Reset & Normalisation

Browsers have default stylesheets with inconsistent values. A CSS reset or normalisation stylesheet ensures a consistent, predictable base.

### 19.1 Full Reset vs Normalise

| | Full Reset | Normalise |
|---|---|---|
| Example | Eric Meyer Reset | `normalize.css` |
| Approach | Zero out nearly everything | Fix inconsistencies, preserve useful defaults |
| Result | You style everything from scratch | Consistent base that you build from |

### 19.2 A Modern Minimal Reset

This is a practical reset suitable for most projects in 2024+:

```css
/* Modern CSS Reset — a practical starting point */

*, *::before, *::after {
  box-sizing: border-box;
}

* {
  margin: 0;
}

body {
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
}

input, button, textarea, select {
  font: inherit; /* Browsers don't inherit font by default */
}

p, h1, h2, h3, h4, h5, h6 {
  overflow-wrap: break-word;
}

#root, #__next {
  isolation: isolate; /* Prevent z-index leaking from React root */
}
```

### 19.3 `all: revert`

The `all` shorthand with `revert` removes all styles and falls back to the browser's user-agent stylesheet:

```css
.isolated-component {
  all: revert;  /* Undo ALL CSS (including inherited styles) */
}
```

Useful for embedding third-party widgets or isolated components that must not be affected by your global stylesheet.

---



> A few highlights: `font: inherit` on form elements is essential — browsers render `<input>` and `<button>` with their own font stack instead of inheriting from the page. `max-width: 100%` on images prevents them from overflowing containers. `display: block` on images removes the inline baseline gap that causes gaps below images.

---

## 20. CSS Architecture

As projects grow, CSS becomes hard to maintain without a strategy for naming, organising, and structuring it.

### 20.1 The Problem

Without architecture:
- Names clash (`button`, `.header`, `.text` — used by multiple components)
- Specificity wars — every fix needs a more specific selector
- Dead CSS — nobody knows what is safe to delete
- No predictability — a change in one place breaks another

### 20.2 BEM (Block Element Modifier)

BEM is a naming convention, not a framework. It makes relationships between CSS classes explicit in the class name.

```
.block {}              — A standalone component (e.g., .card)
.block__element {}     — Part of the block (e.g., .card__title)
.block--modifier {}    — A variant of the block (e.g., .card--featured)
.block__element--modifier {} — A variant of a part (e.g., .card__title--large)
```

```html
<article class="card card--featured">
  <img class="card__image" src="..." alt="">
  <div class="card__body">
    <h2 class="card__title card__title--large">Title</h2>
    <p class="card__excerpt">...</p>
  </div>
  <a class="card__cta" href="...">Read more</a>
</article>
```

```css
.card             { border-radius: 8px; overflow: hidden; }
.card--featured   { border: 2px solid gold; }
.card__image      { width: 100%; aspect-ratio: 16/9; object-fit: cover; }
.card__title      { font-size: 1.25rem; }
.card__title--large { font-size: 1.75rem; }
.card__cta        { display: inline-block; padding: 0.5rem 1rem; }
```

**Benefits:** Every class is flat (specificity `(0,1,0)`), meaning no selector wars. Class names are self-documenting. Easy to know where a style belongs.

### 20.3 Utility-First CSS

Utility-first CSS (popularised by Tailwind CSS) uses single-purpose classes:

```html
<button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg
               font-medium transition-colors duration-200">
  Click me
</button>
```

Applied in your own stylesheet:

```css
/* Small utility helpers */
.text-center   { text-align: center; }
.text-muted    { color: #666; }
.mt-auto       { margin-top: auto; }
.d-flex        { display: flex; }
.gap-1         { gap: 0.25rem; }
.gap-2         { gap: 0.5rem; }
.sr-only       { /* ... */ }
.hidden        { display: none !important; }
.truncate      { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
```

**Benefits:** No need to invent class names, no CSS bloat from one-off styles, rapid iteration.  
**Downsides:** HTML becomes noisy, harder to extract reusable components, requires discipline.

### 20.4 OOCSS (Object-Oriented CSS)

OOCSS separates **structure** (sizing, layout, positioning) from **skin** (colours, fonts, borders):

```css
/* Structure — reused by many objects */
.btn           { display: inline-flex; align-items: center; padding: 0.5rem 1rem; border-radius: 6px; border: none; cursor: pointer; }

/* Skin — applied alongside structure */
.btn-primary   { background: #0056b3; color: white; }
.btn-secondary { background: #f0f0f0; color: #333; border: 1px solid #ccc; }
.btn-danger    { background: #dc3545; color: white; }

/* Size modifiers */
.btn-sm        { padding: 0.25rem 0.75rem; font-size: 0.875rem; }
.btn-lg        { padding: 0.75rem 1.5rem; font-size: 1.125rem; }
```

```html
<button class="btn btn-primary btn-lg">Save</button>
<button class="btn btn-secondary">Cancel</button>
```

### 20.5 Practical Recommendations

For most projects, a practical mix works best:

1. **A reset** at the start
2. **Custom properties** on `:root` for all design tokens (colours, spacing, typography)
3. **BEM or component-scoped classes** for components
4. **A small set of utilities** for layout helpers and spacing
5. **A logical file organisation** — split into base, components, pages, and utilities

```
css/
  base/
    reset.css
    typography.css
    tokens.css     ← custom properties
  components/
    button.css
    card.css
    nav.css
  pages/
    home.css
  utilities/
    spacing.css
    text.css
  style.css        ← imports everything in order
```

---

## 21. Quick-Reference Cheatsheet

### Selectors

```css
*           All elements         li:first-child    First list item
div         Type                 li:last-child     Last list item
.class      Class                li:nth-child(2n)  Even items
#id         ID                   :not(.foo)        Not .foo
[attr]      Has attribute        :is(h1,h2)        Matches any
a:hover     State                p::before         Before pseudo-element
```

### Box Model

```css
box-sizing: border-box        /* Width includes padding + border */
margin: 0 auto                /* Centre a block */
padding: 1rem 2rem            /* Vertical | Horizontal */
overflow: hidden | scroll | auto
```

### Flexbox Container

```css
display: flex
flex-direction: row | column
flex-wrap: wrap
justify-content: center | space-between | space-evenly
align-items: center | stretch | flex-start
gap: 1rem
```

### Flexbox Item

```css
flex: 1                       /* Grow and shrink, basis 0 */
flex: 0 0 200px               /* Fixed 200px, no grow/shrink */
align-self: center
```

### Grid Container

```css
display: grid
grid-template-columns: repeat(3, 1fr)
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))
gap: 1rem
place-items: center           /* align-items + justify-items shorthand */
```

### Grid Item

```css
grid-column: 1 / -1           /* Full width */
grid-column: span 2
grid-area: header
```

### Common Patterns

```css
/* Centre absolutely anything */
display: flex; justify-content: center; align-items: center;

/* Responsive grid with no media queries */
grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));

/* Truncate to one line */
overflow: hidden; text-overflow: ellipsis; white-space: nowrap;

/* Visually hidden but accessible */
position: absolute; width: 1px; height: 1px; overflow: hidden;
clip: rect(0,0,0,0); white-space: nowrap;

/* Aspect ratio */
aspect-ratio: 16 / 9;

/* Full-height page with sticky footer */
body { display: flex; flex-direction: column; min-height: 100vh; }
main  { flex: 1; }

/* Object-fit for images */
img { width: 100%; height: 200px; object-fit: cover; object-position: center; }
```

### CSS Functions

```css
clamp(1rem, 4vw, 2rem)         /* Fluid value between min and max */
calc(100% - 2rem)              /* Mixed-unit arithmetic */
min(100%, 600px)               /* Use the smaller */
max(200px, 50vh)               /* Use the larger */
var(--token, fallback)         /* Custom property */
color-mix(in oklch, red 50%, blue)
```

---

## 22. Further Reading

- **MDN Web Docs** — [developer.mozilla.org/en-US/docs/Web/CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) — the definitive reference
- **CSS-Tricks Almanac** — [css-tricks.com/almanac](https://css-tricks.com/almanac) — property-by-property explanations with browser support notes
- **Every Layout** — [every-layout.dev](https://every-layout.dev) — algorithmic layout patterns using intrinsic CSS
- **web.dev / Learn CSS** — [web.dev/learn/css](https://web.dev/learn/css) — structured course from the Chrome team
- **Can I Use** — [caniuse.com](https://caniuse.com) — browser support tables for every CSS feature
- **Lea Verou's blog** — deep dives on advanced CSS features by a CSS working group member
- **Josh W. Comeau's blog** — [joshwcomeau.com](https://joshwcomeau.com) — excellent visual explanations of CSS fundamentals
- **The CSS Cascade** — [2019.wattenberger.com/blog/css-cascade](https://2019.wattenberger.com/blog/css-cascade) — interactive cascade visualiser

---

*This guide covers CSS as of 2025/2026. Features such as `@layer`, container queries, `:has()`, `color-mix()`, and `oklch()` have excellent cross-browser support in modern browsers but should be verified on [caniuse.com](https://caniuse.com) for your specific target audience.*

---

## 23. Practical UI Components

Real-world components built with pure CSS. Every example below is live — the HTML block renders directly in the browser.

---

### 23.1 Navigation — Basic Horizontal Nav

A simple horizontal nav bar using Flexbox with hover underline effect.

```css
.nav-basic {
  display: flex;
  gap: 0;
  list-style: none;
  margin: 0;
  padding: 0;
  background: #1e293b;
  border-radius: 8px;
  overflow: hidden;
}

.nav-basic a {
  display: block;
  padding: 0.75rem 1.25rem;
  color: #cbd5e1;
  text-decoration: none;
  font-size: 0.9rem;
  position: relative;
  transition: color 0.2s, background 0.2s;
}

.nav-basic a::after {
  content: '';
  position: absolute;
  bottom: 0; left: 50%; right: 50%;
  height: 2px;
  background: #38bdf8;
  transition: left 0.2s, right 0.2s;
}

.nav-basic a:hover { color: #f1f5f9; background: #334155; }
.nav-basic a:hover::after { left: 0; right: 0; }
.nav-basic a.active { color: #38bdf8; }
.nav-basic a.active::after { left: 0; right: 0; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .nav-basic{display:flex;gap:0;list-style:none;margin:0;padding:0;background:#1e293b;border-radius:8px;overflow:hidden}
    .nav-basic a{display:block;padding:.75rem 1.25rem;color:#cbd5e1;text-decoration:none;font-size:.9rem;position:relative;transition:color .2s,background .2s}
    .nav-basic a::after{content:'';position:absolute;bottom:0;left:50%;right:50%;height:2px;background:#38bdf8;transition:left .2s,right .2s}
    .nav-basic a:hover{color:#f1f5f9;background:#334155}
    .nav-basic a:hover::after{left:0;right:0}
    .nav-basic .active{color:#38bdf8}
    .nav-basic .active::after{left:0;right:0}
  </style>
  <ul class="nav-basic">
    <li><a href="#" class="active">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Services</a></li>
    <li><a href="#">Portfolio</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</div>

---

### 23.2 Navigation — Dropdown Menu

A multi-level dropdown using `:hover` and `position: absolute`. No JavaScript required.

```css
.nav-dropdown { display:flex; list-style:none; margin:0; padding:0;
                background:#1e293b; border-radius:8px; overflow:visible;
                position:relative; }
.nav-dropdown > li { position: relative; }
.nav-dropdown > li > a { display:block; padding:.75rem 1.25rem; color:#cbd5e1;
                          text-decoration:none; font-size:.9rem;
                          transition:background .2s; white-space:nowrap; }
.nav-dropdown > li:hover > a { background:#334155; color:#f1f5f9; }

/* Submenu */
.nav-dropdown .submenu { display:none; position:absolute; top:100%; left:0;
                          background:#1e293b; border:1px solid #334155;
                          border-radius:0 0 8px 8px; list-style:none;
                          margin:0; padding:.25rem 0; min-width:180px;
                          box-shadow:0 8px 24px rgba(0,0,0,.4); z-index:100; }
.nav-dropdown .submenu li a { display:block; padding:.6rem 1.25rem;
                               color:#cbd5e1; text-decoration:none;
                               font-size:.85rem; transition:background .2s; }
.nav-dropdown .submenu li a:hover { background:#334155; color:#38bdf8; }
.nav-dropdown > li:hover .submenu { display:block; }
```

<div style="background:#f8fafc;padding:1.5rem 1.5rem 3rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .nav-dd{display:flex;list-style:none;margin:0;padding:0;background:#1e293b;border-radius:8px;position:relative}
    .nav-dd>li{position:relative}
    .nav-dd>li>a{display:block;padding:.75rem 1.25rem;color:#cbd5e1;text-decoration:none;font-size:.9rem;transition:background .2s;white-space:nowrap}
    .nav-dd>li:hover>a{background:#334155;color:#f1f5f9}
    .nav-dd .submenu{display:none;position:absolute;top:100%;left:0;background:#1e293b;border:1px solid #334155;border-radius:0 0 8px 8px;list-style:none;margin:0;padding:.25rem 0;min-width:180px;box-shadow:0 8px 24px rgba(0,0,0,.4);z-index:100}
    .nav-dd .submenu li a{display:block;padding:.6rem 1.25rem;color:#cbd5e1;text-decoration:none;font-size:.85rem;transition:background .2s}
    .nav-dd .submenu li a:hover{background:#334155;color:#38bdf8}
    .nav-dd>li:hover .submenu{display:block}
  </style>
  <ul class="nav-dd">
    <li><a href="#">Home</a></li>
    <li>
      <a href="#">Services ▾</a>
      <ul class="submenu">
        <li><a href="#">Web Design</a></li>
        <li><a href="#">Development</a></li>
        <li><a href="#">SEO</a></li>
      </ul>
    </li>
    <li>
      <a href="#">Products ▾</a>
      <ul class="submenu">
        <li><a href="#">Starter</a></li>
        <li><a href="#">Pro</a></li>
        <li><a href="#">Enterprise</a></li>
      </ul>
    </li>
    <li><a href="#">Contact</a></li>
  </ul>
</div>

---

### 23.3 Navigation — Breadcrumb Trail

Breadcrumbs with `::before` generated separators — no extra markup needed.

```css
.breadcrumb { display:flex; flex-wrap:wrap; gap:0; list-style:none;
              margin:0; padding:0; font-size:.875rem; }
.breadcrumb li + li::before { content:'/'; padding:0 .5rem; color:#94a3b8; }
.breadcrumb a { color:#3b82f6; text-decoration:none; }
.breadcrumb a:hover { text-decoration:underline; }
.breadcrumb li:last-child { color:#64748b; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .breadcrumb{display:flex;flex-wrap:wrap;gap:0;list-style:none;margin:0;padding:0;font-size:.875rem}
    .breadcrumb li+li::before{content:'/';padding:0 .5rem;color:#94a3b8}
    .breadcrumb a{color:#3b82f6;text-decoration:none}
    .breadcrumb a:hover{text-decoration:underline}
    .breadcrumb li:last-child{color:#64748b}
  </style>
  <ul class="breadcrumb">
    <li><a href="#">Home</a></li>
    <li><a href="#">Products</a></li>
    <li><a href="#">Electronics</a></li>
    <li>Wireless Headphones</li>
  </ul>
</div>

---

### 23.4 Navigation — Tab Bar / Pill Switcher

A stateless visual tab bar. Swap to `:checked` trick for a CSS-only active state.

```css
.tab-bar { display:flex; gap:.375rem; padding:.375rem;
           background:#f1f5f9; border-radius:10px; width:fit-content; }
.tab-bar a { padding:.45rem 1rem; border-radius:7px; font-size:.875rem;
             text-decoration:none; color:#64748b; transition:all .2s; }
.tab-bar a:hover { background:#e2e8f0; color:#1e293b; }
.tab-bar a.active { background:#ffffff; color:#1e293b;
                    box-shadow:0 1px 4px rgba(0,0,0,.12); font-weight:500; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .tab-bar{display:flex;gap:.375rem;padding:.375rem;background:#f1f5f9;border-radius:10px;width:fit-content}
    .tab-bar a{padding:.45rem 1rem;border-radius:7px;font-size:.875rem;text-decoration:none;color:#64748b;transition:all .2s}
    .tab-bar a:hover{background:#e2e8f0;color:#1e293b}
    .tab-bar a.tab-active{background:#ffffff;color:#1e293b;box-shadow:0 1px 4px rgba(0,0,0,.12);font-weight:500}
  </style>
  <div class="tab-bar">
    <a href="#" class="tab-active">Overview</a>
    <a href="#">Analytics</a>
    <a href="#">Reports</a>
    <a href="#">Settings</a>
  </div>
</div>

---

### 23.5 Navigation — Pagination

Accessible pagination controls with active and disabled states.

```css
.pagination { display:flex; gap:.375rem; align-items:center;
              list-style:none; margin:0; padding:0; }
.pagination a, .pagination span {
  display:grid; place-items:center;
  width:2.25rem; height:2.25rem; border-radius:6px;
  font-size:.875rem; text-decoration:none; color:#374151;
  border:1px solid #e5e7eb; background:#fff; transition:all .15s;
}
.pagination a:hover { background:#f3f4f6; border-color:#d1d5db; }
.pagination .pag-active { background:#3b82f6; color:#fff;
                           border-color:#3b82f6; font-weight:600; }
.pagination .pag-disabled { color:#d1d5db; pointer-events:none; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .pagination{display:flex;gap:.375rem;align-items:center;list-style:none;margin:0;padding:0}
    .pagination a,.pagination span{display:grid;place-items:center;width:2.25rem;height:2.25rem;border-radius:6px;font-size:.875rem;text-decoration:none;color:#374151;border:1px solid #e5e7eb;background:#fff;transition:all .15s}
    .pagination a:hover{background:#f3f4f6;border-color:#d1d5db}
    .pagination .pag-active{background:#3b82f6;color:#fff;border-color:#3b82f6;font-weight:600}
    .pagination .pag-disabled{color:#d1d5db;pointer-events:none}
  </style>
  <ul class="pagination">
    <li><span class="pag-disabled">«</span></li>
    <li><a href="#">1</a></li>
    <li><a href="#" class="pag-active">2</a></li>
    <li><a href="#">3</a></li>
    <li><a href="#">4</a></li>
    <li><a href="#">5</a></li>
    <li><a href="#">»</a></li>
  </ul>
</div>

---

### 23.6 Button Variants

Filled, outlined, ghost, and danger buttons — all from one base class.

```css
.btn { display:inline-flex; align-items:center; gap:.4rem;
       padding:.55rem 1.2rem; border-radius:7px; font-size:.875rem;
       font-weight:500; cursor:pointer; border:2px solid transparent;
       text-decoration:none; transition:all .15s; }

.btn-primary  { background:#3b82f6; color:#fff; }
.btn-primary:hover  { background:#2563eb; }

.btn-outline  { background:transparent; color:#3b82f6; border-color:#3b82f6; }
.btn-outline:hover  { background:#eff6ff; }

.btn-ghost    { background:transparent; color:#374151; }
.btn-ghost:hover    { background:#f3f4f6; }

.btn-danger   { background:#ef4444; color:#fff; }
.btn-danger:hover   { background:#dc2626; }

.btn-sm { padding:.35rem .8rem; font-size:.8rem; }
.btn-lg { padding:.75rem 1.6rem; font-size:1rem; }

.btn:disabled { opacity:.45; pointer-events:none; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;display:flex;flex-wrap:wrap;gap:.75rem;align-items:center">
  <style>
    .btn{display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;border-radius:7px;font-size:.875rem;font-weight:500;cursor:pointer;border:2px solid transparent;text-decoration:none;transition:all .15s;font-family:inherit}
    .btn-primary{background:#3b82f6;color:#fff}.btn-primary:hover{background:#2563eb}
    .btn-outline{background:transparent;color:#3b82f6;border-color:#3b82f6}.btn-outline:hover{background:#eff6ff}
    .btn-ghost{background:transparent;color:#374151}.btn-ghost:hover{background:#f3f4f6}
    .btn-danger{background:#ef4444;color:#fff}.btn-danger:hover{background:#dc2626}
    .btn-sm{padding:.35rem .8rem;font-size:.8rem}
    .btn-lg{padding:.75rem 1.6rem;font-size:1rem}
    .btn:disabled{opacity:.45;pointer-events:none}
  </style>
  <button class="btn btn-primary">Primary</button>
  <button class="btn btn-outline">Outlined</button>
  <button class="btn btn-ghost">Ghost</button>
  <button class="btn btn-danger">Danger</button>
  <button class="btn btn-primary btn-sm">Small</button>
  <button class="btn btn-primary btn-lg">Large</button>
  <button class="btn btn-primary" disabled>Disabled</button>
</div>

---

### 23.7 Form Styling

Clean, accessible form inputs with focus rings, validation states, and error messages.

```css
.form-group { display:flex; flex-direction:column; gap:.375rem;
              margin-bottom:1.25rem; }
.form-label  { font-size:.875rem; font-weight:500; color:#374151; }
.form-input  { padding:.55rem .85rem; border:1.5px solid #d1d5db;
               border-radius:7px; font-size:.9rem; color:#111827;
               outline:none; transition:border-color .15s, box-shadow .15s; }
.form-input:focus { border-color:#3b82f6;
                    box-shadow:0 0 0 3px rgba(59,130,246,.18); }
.form-input.is-error { border-color:#ef4444; }
.form-input.is-error:focus { box-shadow:0 0 0 3px rgba(239,68,68,.18); }
.form-input.is-success { border-color:#22c55e; }
.form-error { font-size:.8rem; color:#ef4444; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;max-width:360px">
  <style>
    .fg{display:flex;flex-direction:column;gap:.375rem;margin-bottom:1.25rem}
    .fl{font-size:.875rem;font-weight:500;color:#374151}
    .fi{padding:.55rem .85rem;border:1.5px solid #d1d5db;border-radius:7px;font-size:.9rem;color:#111827;outline:none;transition:border-color .15s,box-shadow .15s;font-family:inherit;width:100%;box-sizing:border-box}
    .fi:focus{border-color:#3b82f6;box-shadow:0 0 0 3px rgba(59,130,246,.18)}
    .fi.is-error{border-color:#ef4444}
    .fi.is-success{border-color:#22c55e}
    .fe{font-size:.8rem;color:#ef4444}
  </style>
  <div class="fg">
    <label class="fl">Name</label>
    <input class="fi" type="text" placeholder="John Doe">
  </div>
  <div class="fg">
    <label class="fl">Email</label>
    <input class="fi is-error" type="email" value="not-an-email">
    <span class="fe">Please enter a valid email address.</span>
  </div>
  <div class="fg">
    <label class="fl">Website</label>
    <input class="fi is-success" type="url" value="https://example.com">
  </div>
</div>

---

### 23.8 Custom Checkbox & Radio

Fully styled checkboxes and radios using `appearance: none` — keyboard accessible.

```css
.custom-check { display:flex; align-items:center; gap:.6rem;
                cursor:pointer; font-size:.9rem; color:#374151; }
.custom-check input[type="checkbox"],
.custom-check input[type="radio"] {
  appearance: none; -webkit-appearance: none;
  width:1.125rem; height:1.125rem; border:2px solid #d1d5db;
  border-radius:4px; background:#fff; cursor:pointer;
  display:grid; place-items:center; transition:all .15s;
  flex-shrink:0;
}
.custom-check input[type="radio"] { border-radius:50%; }
.custom-check input:checked { background:#3b82f6; border-color:#3b82f6; }
.custom-check input[type="checkbox"]:checked::before {
  content:''; width:.4rem; height:.65rem;
  border:2px solid #fff; border-top:0; border-left:0;
  transform:rotate(45deg) translate(-1px, -1px);
}
.custom-check input[type="radio"]:checked::before {
  content:''; width:.45rem; height:.45rem;
  border-radius:50%; background:#fff;
}
.custom-check input:focus-visible { outline:2px solid #3b82f6; outline-offset:2px; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;display:flex;flex-direction:column;gap:.75rem">
  <style>
    .cc{display:flex;align-items:center;gap:.6rem;cursor:pointer;font-size:.9rem;color:#374151}
    .cc input[type=checkbox],.cc input[type=radio]{appearance:none;-webkit-appearance:none;width:1.125rem;height:1.125rem;border:2px solid #d1d5db;border-radius:4px;background:#fff;cursor:pointer;display:grid;place-items:center;transition:all .15s;flex-shrink:0}
    .cc input[type=radio]{border-radius:50%}
    .cc input:checked{background:#3b82f6;border-color:#3b82f6}
    .cc input[type=checkbox]:checked::before{content:'';width:.4rem;height:.65rem;border:2px solid #fff;border-top:0;border-left:0;transform:rotate(45deg) translate(-1px,-1px)}
    .cc input[type=radio]:checked::before{content:'';width:.45rem;height:.45rem;border-radius:50%;background:#fff}
    .cc input:focus-visible{outline:2px solid #3b82f6;outline-offset:2px}
  </style>
  <label class="cc"><input type="checkbox" checked> Accept terms and conditions</label>
  <label class="cc"><input type="checkbox"> Subscribe to newsletter</label>
  <label class="cc"><input type="radio" name="plan"> Starter plan</label>
  <label class="cc"><input type="radio" name="plan" checked> Pro plan</label>
  <label class="cc"><input type="radio" name="plan"> Enterprise plan</label>
</div>

---

### 23.9 Toggle Switch

A CSS-only toggle switch built on a hidden `<input type="checkbox">`.

```css
.toggle-wrap { display:flex; align-items:center; gap:.75rem;
               font-size:.9rem; color:#374151; cursor:pointer; }
.toggle-wrap input { display:none; }
.toggle-slider {
  width:2.75rem; height:1.5rem; background:#d1d5db; border-radius:999px;
  position:relative; transition:background .2s; flex-shrink:0;
}
.toggle-slider::before {
  content:''; position:absolute; width:1.125rem; height:1.125rem;
  background:#fff; border-radius:50%; top:.1875rem; left:.1875rem;
  transition:transform .2s; box-shadow:0 1px 3px rgba(0,0,0,.2);
}
.toggle-wrap input:checked + .toggle-slider { background:#3b82f6; }
.toggle-wrap input:checked + .toggle-slider::before {
  transform:translateX(1.25rem);
}
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;display:flex;flex-direction:column;gap:1rem">
  <style>
    .tw{display:flex;align-items:center;gap:.75rem;font-size:.9rem;color:#374151;cursor:pointer}
    .tw input{display:none}
    .ts{width:2.75rem;height:1.5rem;background:#d1d5db;border-radius:999px;position:relative;transition:background .2s;flex-shrink:0}
    .ts::before{content:'';position:absolute;width:1.125rem;height:1.125rem;background:#fff;border-radius:50%;top:.1875rem;left:.1875rem;transition:transform .2s;box-shadow:0 1px 3px rgba(0,0,0,.2)}
    .tw input:checked+.ts{background:#3b82f6}
    .tw input:checked+.ts::before{transform:translateX(1.25rem)}
  </style>
  <label class="tw"><input type="checkbox" checked><span class="ts"></span> Enable notifications</label>
  <label class="tw"><input type="checkbox"><span class="ts"></span> Dark mode</label>
  <label class="tw"><input type="checkbox" checked><span class="ts"></span> Auto-save drafts</label>
</div>

---

### 23.10 Floating Label Input

The label floats above the input when focused or filled, using the `:placeholder-shown` trick.

```css
.float-group { position:relative; margin-bottom:1.5rem; }
.float-group input {
  width:100%; padding:1.25rem .85rem .45rem;
  border:1.5px solid #d1d5db; border-radius:7px;
  font-size:.95rem; outline:none; background:#fff;
  transition:border-color .2s; box-sizing:border-box;
}
.float-group input:focus { border-color:#3b82f6; }
.float-group label {
  position:absolute; left:.85rem; top:50%;
  transform:translateY(-50%); color:#94a3b8;
  font-size:.95rem; pointer-events:none;
  transition:all .15s;
}
/* Float up when focused OR when placeholder is hidden (i.e. has value) */
.float-group input:focus + label,
.float-group input:not(:placeholder-shown) + label {
  top:.45rem; transform:none; font-size:.72rem; color:#3b82f6;
}
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;max-width:320px">
  <style>
    .floatg{position:relative;margin-bottom:1.5rem}
    .floatg input{width:100%;padding:1.25rem .85rem .45rem;border:1.5px solid #d1d5db;border-radius:7px;font-size:.95rem;outline:none;background:#fff;transition:border-color .2s;box-sizing:border-box;font-family:inherit}
    .floatg input:focus{border-color:#3b82f6}
    .floatg label{position:absolute;left:.85rem;top:50%;transform:translateY(-50%);color:#94a3b8;font-size:.95rem;pointer-events:none;transition:all .15s}
    .floatg input:focus+label,.floatg input:not(:placeholder-shown)+label{top:.45rem;transform:none;font-size:.72rem;color:#3b82f6}
  </style>
  <div class="floatg">
    <input type="text" id="fl1" placeholder=" ">
    <label for="fl1">Full Name</label>
  </div>
  <div class="floatg">
    <input type="email" id="fl2" placeholder=" " value="hello@example.com">
    <label for="fl2">Email Address</label>
  </div>
  <div class="floatg">
    <input type="password" id="fl3" placeholder=" ">
    <label for="fl3">Password</label>
  </div>
</div>

---

### 23.11 Custom Select

A styled `<select>` using `appearance: none` with a custom dropdown arrow via `background-image`.

```css
.custom-select-wrap { position:relative; display:inline-block; }
.custom-select {
  appearance:none; -webkit-appearance:none;
  padding:.55rem 2.5rem .55rem .85rem;
  border:1.5px solid #d1d5db; border-radius:7px;
  font-size:.9rem; color:#374151; background:#fff;
  cursor:pointer; outline:none; transition:border-color .2s;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%2364748b' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat:no-repeat;
  background-position:right .75rem center;
}
.custom-select:focus { border-color:#3b82f6;
                        box-shadow:0 0 0 3px rgba(59,130,246,.18); }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .csel{appearance:none;-webkit-appearance:none;padding:.55rem 2.5rem .55rem .85rem;border:1.5px solid #d1d5db;border-radius:7px;font-size:.9rem;color:#374151;background:#fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%2364748b' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E") no-repeat right .75rem center;cursor:pointer;outline:none;transition:border-color .2s;font-family:inherit}
    .csel:focus{border-color:#3b82f6;box-shadow:0 0 0 3px rgba(59,130,246,.18)}
  </style>
  <select class="csel">
    <option>Select a country…</option>
    <option>United Kingdom</option>
    <option>United States</option>
    <option>Germany</option>
    <option>France</option>
  </select>
</div>

---

### 23.12 Tooltip (Four Directions)

Pure-CSS tooltips using `::before` / `::after` on a `[data-tooltip]` attribute.

```css
[data-tip] { position:relative; cursor:default; }
[data-tip]::before {
  content: attr(data-tip);
  position:absolute; left:50%; transform:translateX(-50%);
  bottom:calc(100% + 6px);
  background:#1e293b; color:#f1f5f9; white-space:nowrap;
  padding:.3rem .65rem; border-radius:5px; font-size:.78rem;
  opacity:0; pointer-events:none; transition:opacity .15s;
}
[data-tip]::after {
  content:''; position:absolute;
  left:50%; transform:translateX(-50%);
  bottom:calc(100% + 1px);
  border:5px solid transparent; border-top-color:#1e293b;
  opacity:0; pointer-events:none; transition:opacity .15s;
}
[data-tip]:hover::before, [data-tip]:hover::after { opacity:1; }
```

<div style="background:#f8fafc;padding:2.5rem 1.5rem 1.5rem;border-radius:8px;border:1px solid #e2e8f0;display:flex;gap:1.5rem;flex-wrap:wrap;justify-content:center">
  <style>
    [data-tip]{position:relative;cursor:default;display:inline-block;padding:.5rem 1rem;background:#e2e8f0;border-radius:6px;font-size:.875rem;color:#374151}
    [data-tip]::before{content:attr(data-tip);position:absolute;left:50%;transform:translateX(-50%);bottom:calc(100% + 6px);background:#1e293b;color:#f1f5f9;white-space:nowrap;padding:.3rem .65rem;border-radius:5px;font-size:.78rem;opacity:0;pointer-events:none;transition:opacity .15s;z-index:10}
    [data-tip]::after{content:'';position:absolute;left:50%;transform:translateX(-50%);bottom:calc(100% + 1px);border:5px solid transparent;border-top-color:#1e293b;opacity:0;pointer-events:none;transition:opacity .15s;z-index:10}
    [data-tip]:hover::before,[data-tip]:hover::after{opacity:1}
  </style>
  <span data-tip="This is a tooltip!">Hover me</span>
  <span data-tip="Save your work often">Auto-save</span>
  <span data-tip="Opens in new tab">External link</span>
</div>

---

### 23.13 Badge / Pill / Notification Dot

Status badges, pill labels, and a notification counter dot.

```css
.badge { display:inline-flex; align-items:center; gap:.3rem;
         padding:.2rem .6rem; border-radius:999px;
         font-size:.75rem; font-weight:600; line-height:1.4; }
.badge-blue    { background:#dbeafe; color:#1d4ed8; }
.badge-green   { background:#dcfce7; color:#15803d; }
.badge-yellow  { background:#fef9c3; color:#a16207; }
.badge-red     { background:#fee2e2; color:#b91c1c; }
.badge-gray    { background:#f1f5f9; color:#475569; }

/* Notification dot */
.notif-wrap { position:relative; display:inline-block; }
.notif-dot  { position:absolute; top:-4px; right:-4px;
              width:10px; height:10px; background:#ef4444;
              border-radius:50%; border:2px solid #fff; }
.notif-count { position:absolute; top:-6px; right:-10px;
               background:#ef4444; color:#fff;
               border-radius:999px; font-size:.65rem; font-weight:700;
               padding:.05rem .3rem; border:2px solid #fff; min-width:18px;
               text-align:center; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;display:flex;flex-wrap:wrap;gap:1rem;align-items:center">
  <style>
    .badge{display:inline-flex;align-items:center;gap:.3rem;padding:.2rem .6rem;border-radius:999px;font-size:.75rem;font-weight:600;line-height:1.4}
    .badge-blue{background:#dbeafe;color:#1d4ed8}
    .badge-green{background:#dcfce7;color:#15803d}
    .badge-yellow{background:#fef9c3;color:#a16207}
    .badge-red{background:#fee2e2;color:#b91c1c}
    .badge-gray{background:#f1f5f9;color:#475569}
    .nw{position:relative;display:inline-block}
    .ndot{position:absolute;top:-4px;right:-4px;width:10px;height:10px;background:#ef4444;border-radius:50%;border:2px solid #fff}
    .ncount{position:absolute;top:-6px;right:-10px;background:#ef4444;color:#fff;border-radius:999px;font-size:.65rem;font-weight:700;padding:.05rem .3rem;border:2px solid #fff;min-width:18px;text-align:center}
  </style>
  <span class="badge badge-green">Active</span>
  <span class="badge badge-yellow">Pending</span>
  <span class="badge badge-red">Failed</span>
  <span class="badge badge-blue">New</span>
  <span class="badge badge-gray">Draft</span>
  <span class="nw" style="margin-left:.5rem">
    <button style="padding:.5rem 1rem;border-radius:7px;background:#e2e8f0;border:none;cursor:pointer;font-size:.875rem">Inbox</button>
    <span class="ncount">4</span>
  </span>
  <span class="nw" style="margin-left:.5rem">
    <button style="padding:.5rem;border-radius:50%;background:#e2e8f0;border:none;cursor:pointer;width:2.25rem;height:2.25rem">🔔</button>
    <span class="ndot"></span>
  </span>
</div>

---

### 23.14 Progress Bar

An animated progress bar with labelled value, using CSS custom properties for flexibility.

```css
.progress-wrap { background:#e2e8f0; border-radius:999px;
                  height:.75rem; overflow:hidden; }
.progress-bar  { height:100%; border-radius:999px;
                  background:linear-gradient(90deg,#3b82f6,#6366f1);
                  width: var(--pct, 0%);
                  transition:width .6s ease; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;display:flex;flex-direction:column;gap:1rem">
  <style>
    .pw{background:#e2e8f0;border-radius:999px;height:.75rem;overflow:hidden}
    .pb{height:100%;border-radius:999px;background:linear-gradient(90deg,#3b82f6,#6366f1);transition:width .6s ease}
    .plabel{display:flex;justify-content:space-between;font-size:.8rem;color:#64748b;margin-bottom:.3rem}
  </style>
  <div>
    <div class="plabel"><span>Storage</span><span>72%</span></div>
    <div class="pw"><div class="pb" style="width:72%"></div></div>
  </div>
  <div>
    <div class="plabel"><span>Bandwidth</span><span>45%</span></div>
    <div class="pw"><div class="pb" style="width:45%;background:linear-gradient(90deg,#22c55e,#10b981)"></div></div>
  </div>
  <div>
    <div class="plabel"><span>CPU usage</span><span>91%</span></div>
    <div class="pw"><div class="pb" style="width:91%;background:linear-gradient(90deg,#f59e0b,#ef4444)"></div></div>
  </div>
</div>

---

### 23.15 Accordion (CSS-only)

A CSS-only accordion using the `<details>` / `<summary>` elements with custom styling and animated open/close.

```css
.accordion details { border:1.5px solid #e2e8f0; border-radius:8px;
                     margin-bottom:.5rem; overflow:hidden; }
.accordion summary  { padding:.85rem 1.1rem; font-weight:500; font-size:.9rem;
                       cursor:pointer; list-style:none; display:flex;
                       justify-content:space-between; align-items:center;
                       background:#f8fafc; color:#1e293b;
                       transition:background .15s; }
.accordion summary:hover { background:#f1f5f9; }
.accordion summary::after { content:'+'; font-size:1.2rem; color:#64748b;
                              transition:transform .2s; }
.accordion details[open] summary::after { transform:rotate(45deg); }
.accordion details[open] summary { background:#eff6ff; color:#1d4ed8; }
.accordion .acc-content { padding:.9rem 1.1rem; font-size:.875rem;
                           color:#475569; line-height:1.6; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;max-width:480px">
  <style>
    .accordion details{border:1.5px solid #e2e8f0;border-radius:8px;margin-bottom:.5rem;overflow:hidden}
    .accordion summary{padding:.85rem 1.1rem;font-weight:500;font-size:.9rem;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;background:#f8fafc;color:#1e293b;transition:background .15s}
    .accordion summary:hover{background:#f1f5f9}
    .accordion summary::after{content:'+';font-size:1.2rem;color:#64748b;transition:transform .2s}
    .accordion details[open] summary::after{transform:rotate(45deg)}
    .accordion details[open] summary{background:#eff6ff;color:#1d4ed8}
    .acc-content{padding:.9rem 1.1rem;font-size:.875rem;color:#475569;line-height:1.6}
  </style>
  <div class="accordion">
    <details open>
      <summary>What is CSS?</summary>
      <div class="acc-content">CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation of HTML documents — controlling layout, colours, fonts, and visual effects.</div>
    </details>
    <details>
      <summary>What is the box model?</summary>
      <div class="acc-content">Every element is a rectangular box composed of content, padding, border, and margin. The <code>box-sizing: border-box</code> rule makes sizing intuitive by including padding and border in the stated width/height.</div>
    </details>
    <details>
      <summary>What is specificity?</summary>
      <div class="acc-content">Specificity is the algorithm browsers use to determine which CSS rule wins when multiple rules target the same element. IDs beat classes, classes beat elements, and <code>!important</code> overrides all.</div>
    </details>
  </div>
</div>

---

### 23.16 Alert / Callout Boxes

Info, success, warning, and error callouts with a left border accent.

```css
.alert { display:flex; gap:.75rem; align-items:flex-start;
         padding:.9rem 1.1rem; border-radius:8px;
         border-left:4px solid; font-size:.875rem; line-height:1.5;
         margin-bottom:.75rem; }
.alert-info    { background:#eff6ff; border-color:#3b82f6; color:#1e40af; }
.alert-success { background:#f0fdf4; border-color:#22c55e; color:#15803d; }
.alert-warning { background:#fffbeb; border-color:#f59e0b; color:#92400e; }
.alert-error   { background:#fef2f2; border-color:#ef4444; color:#991b1b; }
.alert-icon    { font-size:1.1rem; flex-shrink:0; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .alert{display:flex;gap:.75rem;align-items:flex-start;padding:.9rem 1.1rem;border-radius:8px;border-left:4px solid;font-size:.875rem;line-height:1.5;margin-bottom:.75rem}
    .alert-info{background:#eff6ff;border-color:#3b82f6;color:#1e40af}
    .alert-success{background:#f0fdf4;border-color:#22c55e;color:#15803d}
    .alert-warning{background:#fffbeb;border-color:#f59e0b;color:#92400e}
    .alert-error{background:#fef2f2;border-color:#ef4444;color:#991b1b}
    .alert-icon{font-size:1.1rem;flex-shrink:0}
  </style>
  <div class="alert alert-info"><span class="alert-icon">ℹ️</span><div><strong>Information.</strong> This action will affect all users in your workspace.</div></div>
  <div class="alert alert-success"><span class="alert-icon">✅</span><div><strong>Success!</strong> Your changes have been saved successfully.</div></div>
  <div class="alert alert-warning"><span class="alert-icon">⚠️</span><div><strong>Warning.</strong> Your subscription expires in 3 days. Please renew soon.</div></div>
  <div class="alert alert-error"><span class="alert-icon">❌</span><div><strong>Error.</strong> We couldn't process your payment. Please check your card details.</div></div>
</div>

---

### 23.17 Toast / Snackbar Notification

An animated slide-in toast notification using `@keyframes`.

```css
@keyframes toast-in {
  from { transform:translateY(2rem); opacity:0; }
  to   { transform:translateY(0);    opacity:1; }
}
.toast-stack { display:flex; flex-direction:column; gap:.5rem; }
.toast { display:flex; align-items:center; gap:.75rem;
         padding:.75rem 1.1rem; border-radius:8px;
         background:#1e293b; color:#f1f5f9; font-size:.875rem;
         box-shadow:0 8px 24px rgba(0,0,0,.25);
         animation:toast-in .3s ease forwards;
         max-width:320px; }
.toast-success { border-left:3px solid #22c55e; }
.toast-error   { border-left:3px solid #ef4444; }
.toast-close   { margin-left:auto; cursor:pointer; opacity:.6;
                  background:none; border:none; color:#f1f5f9;
                  font-size:1rem; padding:0; }
.toast-close:hover { opacity:1; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    @keyframes toast-in{from{transform:translateY(2rem);opacity:0}to{transform:translateY(0);opacity:1}}
    .toast-stack{display:flex;flex-direction:column;gap:.5rem}
    .toast{display:flex;align-items:center;gap:.75rem;padding:.75rem 1.1rem;border-radius:8px;background:#1e293b;color:#f1f5f9;font-size:.875rem;box-shadow:0 8px 24px rgba(0,0,0,.25);animation:toast-in .3s ease forwards;max-width:320px}
    .toast-success{border-left:3px solid #22c55e}
    .toast-error{border-left:3px solid #ef4444}
    .toast-close{margin-left:auto;cursor:pointer;opacity:.6;background:none;border:none;color:#f1f5f9;font-size:1rem;padding:0}
    .toast-close:hover{opacity:1}
  </style>
  <div class="toast-stack">
    <div class="toast toast-success">✅ Profile updated successfully. <button class="toast-close">✕</button></div>
    <div class="toast toast-error">❌ Upload failed — file too large. <button class="toast-close">✕</button></div>
    <div class="toast">📋 Link copied to clipboard. <button class="toast-close">✕</button></div>
  </div>
</div>

---

### 23.18 Skeleton Loading Screen

Animated skeleton placeholders using a CSS shimmer `@keyframes` — shown while content loads.

```css
@keyframes shimmer {
  from { background-position:-200% 0; }
  to   { background-position: 200% 0; }
}
.skeleton { background:linear-gradient(90deg,
              #e2e8f0 25%, #f1f5f9 50%, #e2e8f0 75%);
            background-size:200% 100%;
            animation:shimmer 1.4s infinite linear;
            border-radius:4px; }
.sk-avatar { width:2.75rem; height:2.75rem; border-radius:50%; }
.sk-line    { height:.75rem; margin-bottom:.5rem; }
.sk-card    { padding:1.25rem; border:1px solid #e2e8f0;
              border-radius:8px; background:#fff; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;max-width:360px">
  <style>
    @keyframes shimmer{from{background-position:-200% 0}to{background-position:200% 0}}
    .skeleton{background:linear-gradient(90deg,#e2e8f0 25%,#f1f5f9 50%,#e2e8f0 75%);background-size:200% 100%;animation:shimmer 1.4s infinite linear;border-radius:4px}
    .sk-avatar{width:2.75rem;height:2.75rem;border-radius:50%}
    .sk-line{height:.75rem;margin-bottom:.5rem}
    .sk-card{padding:1.25rem;border:1px solid #e2e8f0;border-radius:8px;background:#fff}
  </style>
  <div class="sk-card">
    <div style="display:flex;align-items:center;gap:.75rem;margin-bottom:1rem">
      <div class="skeleton sk-avatar"></div>
      <div style="flex:1">
        <div class="skeleton sk-line" style="width:60%"></div>
        <div class="skeleton sk-line" style="width:40%"></div>
      </div>
    </div>
    <div class="skeleton sk-line" style="width:100%"></div>
    <div class="skeleton sk-line" style="width:95%"></div>
    <div class="skeleton sk-line" style="width:80%"></div>
    <div class="skeleton sk-line" style="width:55%;margin-bottom:0"></div>
  </div>
</div>

---

### 23.19 Card Grid with Hover Lift

A responsive auto-filling card grid where cards lift on hover.

```css
.card-grid { display:grid;
             grid-template-columns:repeat(auto-fill, minmax(200px, 1fr));
             gap:1.25rem; }
.card-item { background:#fff; border:1px solid #e2e8f0; border-radius:10px;
             padding:1.25rem; cursor:pointer;
             transition:transform .2s, box-shadow .2s; }
.card-item:hover { transform:translateY(-4px);
                   box-shadow:0 12px 32px rgba(0,0,0,.1); }
.card-item h3 { font-size:.95rem; color:#1e293b; margin:0 0 .4rem; }
.card-item p  { font-size:.82rem; color:#64748b; margin:0; line-height:1.5; }
.card-tag { display:inline-block; margin-top:.75rem;
            padding:.15rem .55rem; border-radius:999px;
            background:#eff6ff; color:#1d4ed8; font-size:.72rem;
            font-weight:600; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:1.25rem}
    .card-item{background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:1.25rem;cursor:pointer;transition:transform .2s,box-shadow .2s}
    .card-item:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(0,0,0,.1)}
    .card-item h3{font-size:.95rem;color:#1e293b;margin:0 0 .4rem}
    .card-item p{font-size:.82rem;color:#64748b;margin:0;line-height:1.5}
    .card-tag{display:inline-block;margin-top:.75rem;padding:.15rem .55rem;border-radius:999px;background:#eff6ff;color:#1d4ed8;font-size:.72rem;font-weight:600}
  </style>
  <div class="card-grid">
    <div class="card-item"><h3>Flexbox</h3><p>One-dimensional layout for rows and columns.</p><span class="card-tag">Layout</span></div>
    <div class="card-item"><h3>CSS Grid</h3><p>Two-dimensional layout with explicit tracks.</p><span class="card-tag">Layout</span></div>
    <div class="card-item"><h3>Animations</h3><p>Keyframe-driven motion with full control.</p><span class="card-tag">Motion</span></div>
    <div class="card-item"><h3>Custom Props</h3><p>CSS variables for maintainable, themeable code.</p><span class="card-tag">Variables</span></div>
  </div>
</div>

---

### 23.20 Responsive Data Table

A scrollable data table with zebra striping, sticky header row, and hover highlight.

```css
.table-wrap { overflow-x:auto; border-radius:8px;
              border:1px solid #e2e8f0; }
.data-table  { width:100%; border-collapse:collapse; font-size:.875rem; }
.data-table thead th { background:#1e293b; color:#f1f5f9; padding:.75rem 1rem;
                        text-align:left; font-weight:600; white-space:nowrap;
                        position:sticky; top:0; }
.data-table tbody tr:nth-child(even) { background:#f8fafc; }
.data-table tbody tr:hover           { background:#eff6ff; }
.data-table tbody td { padding:.65rem 1rem; border-bottom:1px solid #f1f5f9;
                        color:#374151; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .table-wrap{overflow-x:auto;border-radius:8px;border:1px solid #e2e8f0}
    .data-table{width:100%;border-collapse:collapse;font-size:.875rem}
    .data-table thead th{background:#1e293b;color:#f1f5f9;padding:.75rem 1rem;text-align:left;font-weight:600;white-space:nowrap;position:sticky;top:0}
    .data-table tbody tr:nth-child(even){background:#f8fafc}
    .data-table tbody tr:hover{background:#eff6ff}
    .data-table tbody td{padding:.65rem 1rem;border-bottom:1px solid #f1f5f9;color:#374151}
  </style>
  <div class="table-wrap">
    <table class="data-table">
      <thead>
        <tr><th>Name</th><th>Role</th><th>Status</th><th>Joined</th></tr>
      </thead>
      <tbody>
        <tr><td>Alice Chen</td><td>Frontend Dev</td><td>Active</td><td>Jan 2024</td></tr>
        <tr><td>Bob Patel</td><td>Designer</td><td>Active</td><td>Mar 2024</td></tr>
        <tr><td>Carol Smith</td><td>Backend Dev</td><td>On leave</td><td>Nov 2023</td></tr>
        <tr><td>David Jones</td><td>DevOps</td><td>Active</td><td>Feb 2025</td></tr>
        <tr><td>Eva Liu</td><td>Product Manager</td><td>Active</td><td>Jun 2023</td></tr>
      </tbody>
    </table>
  </div>
</div>

---

### 23.21 Vertical Timeline

A vertical timeline using the `::before` pseudo-element for the connecting line and a dot for each event.

```css
.timeline { list-style:none; margin:0; padding:0;
            position:relative; padding-left:2rem; }
.timeline::before { content:''; position:absolute; left:.5625rem; top:.5rem;
                    bottom:.5rem; width:2px; background:#e2e8f0; }
.timeline li { position:relative; padding-bottom:1.5rem; }
.timeline li::before { content:''; position:absolute;
                        left:-1.4375rem; top:.35rem;
                        width:.875rem; height:.875rem;
                        border-radius:50%; background:#3b82f6;
                        border:2px solid #fff;
                        box-shadow:0 0 0 2px #3b82f6; }
.tl-date { font-size:.75rem; color:#94a3b8; margin-bottom:.2rem; }
.tl-title { font-weight:600; font-size:.9rem; color:#1e293b;
             margin-bottom:.25rem; }
.tl-body  { font-size:.82rem; color:#64748b; line-height:1.5; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;max-width:400px">
  <style>
    .timeline{list-style:none;margin:0;padding:0 0 0 2rem;position:relative}
    .timeline::before{content:'';position:absolute;left:.5625rem;top:.5rem;bottom:.5rem;width:2px;background:#e2e8f0}
    .timeline li{position:relative;padding-bottom:1.5rem}
    .timeline li::before{content:'';position:absolute;left:-1.4375rem;top:.35rem;width:.875rem;height:.875rem;border-radius:50%;background:#3b82f6;border:2px solid #fff;box-shadow:0 0 0 2px #3b82f6}
    .timeline li:last-child::before{background:#22c55e;box-shadow:0 0 0 2px #22c55e}
    .tl-date{font-size:.75rem;color:#94a3b8;margin-bottom:.2rem}
    .tl-title{font-weight:600;font-size:.9rem;color:#1e293b;margin-bottom:.25rem}
    .tl-body{font-size:.82rem;color:#64748b;line-height:1.5}
  </style>
  <ul class="timeline">
    <li>
      <div class="tl-date">January 2024</div>
      <div class="tl-title">Project Kicked Off</div>
      <div class="tl-body">Initial scoping, stakeholder alignment, and team formation complete.</div>
    </li>
    <li>
      <div class="tl-date">March 2024</div>
      <div class="tl-title">Design Phase Complete</div>
      <div class="tl-body">All wireframes and high-fidelity mockups signed off by the client.</div>
    </li>
    <li>
      <div class="tl-date">July 2024</div>
      <div class="tl-title">Beta Launch</div>
      <div class="tl-body">Soft launch to 500 beta users for usability testing and feedback.</div>
    </li>
    <li>
      <div class="tl-date">October 2024</div>
      <div class="tl-title">Public Launch ✓</div>
      <div class="tl-body">Full production release with all features, marketing campaign live.</div>
    </li>
  </ul>
</div>

---

### 23.22 Pricing Table

A three-column pricing table with a highlighted "most popular" centre column.

```css
.pricing-grid { display:grid;
                grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));
                gap:1.25rem; align-items:start; }
.pricing-card { border:1.5px solid #e2e8f0; border-radius:12px;
                padding:1.75rem 1.5rem; background:#fff; }
.pricing-card.featured { border-color:#3b82f6; background:#eff6ff;
                          transform:scale(1.04);
                          box-shadow:0 8px 32px rgba(59,130,246,.18); }
.pricing-tier  { font-size:.8rem; font-weight:600; text-transform:uppercase;
                  letter-spacing:.06em; color:#64748b; margin-bottom:.5rem; }
.pricing-price { font-size:2.25rem; font-weight:800; color:#0f172a; }
.pricing-price sup { font-size:1rem; font-weight:600; vertical-align:super; }
.pricing-price sub { font-size:.9rem; font-weight:400; color:#64748b; }
.pricing-features { list-style:none; margin:.75rem 0 1.5rem; padding:0;
                     font-size:.85rem; color:#475569; }
.pricing-features li { padding:.3rem 0; border-bottom:1px solid #f1f5f9; }
.pricing-features li::before { content:'✓ '; color:#22c55e; font-weight:700; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .pricing-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1.25rem;align-items:start}
    .pricing-card{border:1.5px solid #e2e8f0;border-radius:12px;padding:1.75rem 1.5rem;background:#fff}
    .pricing-card.featured{border-color:#3b82f6;background:#eff6ff;transform:scale(1.04);box-shadow:0 8px 32px rgba(59,130,246,.18)}
    .pricing-tier{font-size:.8rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:#64748b;margin-bottom:.5rem}
    .pricing-price{font-size:2.25rem;font-weight:800;color:#0f172a}
    .pricing-price sup{font-size:1rem;font-weight:600;vertical-align:super}
    .pricing-price sub{font-size:.9rem;font-weight:400;color:#64748b}
    .pricing-features{list-style:none;margin:.75rem 0 1.5rem;padding:0;font-size:.85rem;color:#475569}
    .pricing-features li{padding:.3rem 0;border-bottom:1px solid #f1f5f9}
    .pricing-features li::before{content:'✓ ';color:#22c55e;font-weight:700}
    .pricing-btn{display:block;width:100%;padding:.65rem;border-radius:7px;border:none;cursor:pointer;font-size:.875rem;font-weight:600;text-align:center;background:#e2e8f0;color:#374151;transition:background .15s}
    .pricing-btn.featured-btn{background:#3b82f6;color:#fff}
    .pricing-btn:hover{filter:brightness(.93)}
  </style>
  <div class="pricing-grid">
    <div class="pricing-card">
      <div class="pricing-tier">Starter</div>
      <div class="pricing-price"><sup>£</sup>9<sub>/mo</sub></div>
      <ul class="pricing-features">
        <li>5 projects</li>
        <li>10 GB storage</li>
        <li>Email support</li>
      </ul>
      <button class="pricing-btn">Get started</button>
    </div>
    <div class="pricing-card featured">
      <div class="pricing-tier" style="color:#1d4ed8">Pro ⭐</div>
      <div class="pricing-price"><sup>£</sup>29<sub>/mo</sub></div>
      <ul class="pricing-features">
        <li>Unlimited projects</li>
        <li>100 GB storage</li>
        <li>Priority support</li>
        <li>Analytics dashboard</li>
      </ul>
      <button class="pricing-btn featured-btn">Get started</button>
    </div>
    <div class="pricing-card">
      <div class="pricing-tier">Enterprise</div>
      <div class="pricing-price"><sup>£</sup>99<sub>/mo</sub></div>
      <ul class="pricing-features">
        <li>Unlimited everything</li>
        <li>1 TB storage</li>
        <li>Dedicated support</li>
        <li>SSO / SAML</li>
      </ul>
      <button class="pricing-btn">Contact sales</button>
    </div>
  </div>
</div>

---

### 23.23 Multi-Column Text Layout

The CSS `columns` property creates newspaper-style flowing multi-column text with no JavaScript.

```css
.multicol {
  columns: 3 220px;          /* Max 3 cols, min 220px each */
  column-gap: 2rem;
  column-rule: 1px solid #e2e8f0;
}
.multicol h3 {
  column-span: all;          /* Heading spans across all columns */
  margin-bottom: .75rem;
}
.multicol p { break-inside: avoid; margin: 0 0 .75rem; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .multicol{columns:3 200px;column-gap:2rem;column-rule:1px solid #e2e8f0;font-size:.875rem;color:#374151;line-height:1.6}
    .multicol h3{column-span:all;margin-bottom:.75rem;color:#1e293b}
    .multicol p{break-inside:avoid;margin:0 0 .75rem}
  </style>
  <div class="multicol">
    <h3>The History of CSS</h3>
    <p>CSS was first proposed by Håkon Wium Lie in 1994 while working with Tim Berners-Lee at CERN. The goal was to separate document structure from presentation.</p>
    <p>CSS Level 1 became a W3C recommendation in 1996, covering fonts, colors, and basic positioning. Browsers were slow to implement it correctly, leading to years of inconsistency.</p>
    <p>CSS2 arrived in 1998, adding media types, positioning, and z-index. Flexbox and Grid arrived much later — in 2012 and 2017 respectively — and truly transformed layout on the web.</p>
    <p>Today CSS is a living standard, with features like custom properties, container queries, and scroll-driven animations shipping regularly across browsers.</p>
  </div>
</div>

---

### 23.24 Pull Quote / Blockquote Styling

A visually impactful pull quote using `::before` for the large opening quotation mark.

```css
.pullquote {
  position:relative; border-left:none;
  margin:2rem 0; padding:1.5rem 1.5rem 1.5rem 3rem;
  background:#f8fafc; border-radius:8px;
}
.pullquote::before {
  content:'"'; position:absolute; left:.25rem; top:-.25rem;
  font-size:5rem; line-height:1; color:#cbd5e1;
  font-family:Georgia, serif;
}
.pullquote p { font-size:1.15rem; font-style:italic;
               color:#334155; line-height:1.6; margin:0 0 .75rem; }
.pullquote cite { font-size:.8rem; color:#94a3b8; font-style:normal; }
.pullquote cite::before { content:'— '; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;max-width:480px">
  <style>
    .pullquote{position:relative;margin:0;padding:1.5rem 1.5rem 1.5rem 3rem;background:#eff6ff;border-radius:8px}
    .pullquote::before{content:'"';position:absolute;left:.25rem;top:-.25rem;font-size:5rem;line-height:1;color:#bfdbfe;font-family:Georgia,serif}
    .pullquote p{font-size:1.1rem;font-style:italic;color:#334155;line-height:1.6;margin:0 0 .75rem}
    .pullquote cite{font-size:.8rem;color:#64748b;font-style:normal}
    .pullquote cite::before{content:'— '}
  </style>
  <blockquote class="pullquote">
    <p>The best CSS is the CSS you don't have to write. Lean on the browser's defaults, and add only what you genuinely need.</p>
    <cite>Principle of minimal intervention</cite>
  </blockquote>
</div>

---

### 23.25 Aspect-Ratio Image Containers

Use the native `aspect-ratio` property (modern CSS) instead of the old padding-top hack.

```css
/* Modern approach */
.img-box {
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  border-radius: 8px;
}
.img-box img {
  width: 100%; height: 100%;
  object-fit: cover;
  display: block;
}

/* Old padding-top hack (legacy reference) */
.img-box-legacy {
  position: relative;
  padding-top: 56.25%;   /* 9/16 = 56.25% */
  overflow: hidden;
}
.img-box-legacy > * {
  position: absolute;
  inset: 0;
}
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;display:grid;grid-template-columns:1fr 1fr;gap:1rem">
  <style>
    .abox{width:100%;aspect-ratio:16/9;overflow:hidden;border-radius:8px;background:linear-gradient(135deg,#6366f1,#8b5cf6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:.8rem;font-weight:600}
    .abox-1{aspect-ratio:16/9}
    .abox-2{aspect-ratio:4/3}
    .abox-3{aspect-ratio:1/1}
    .abox-4{aspect-ratio:9/16;max-height:200px}
  </style>
  <div class="abox abox-1">16 / 9</div>
  <div class="abox abox-2" style="background:linear-gradient(135deg,#0ea5e9,#06b6d4)">4 / 3</div>
  <div class="abox abox-3" style="background:linear-gradient(135deg,#f43f5e,#ec4899)">1 / 1</div>
  <div class="abox abox-4" style="background:linear-gradient(135deg,#f59e0b,#ea580c)">9 / 16</div>
</div>

---

## 24. Visual Effects & Modern CSS Techniques

---

### 24.1 Glassmorphism Card

Frosted-glass effect using `backdrop-filter: blur()` layered over a gradient background.

```css
.glass-scene { background:linear-gradient(135deg,#6366f1 0%,#8b5cf6 50%,#ec4899 100%);
               padding:3rem 2rem; border-radius:12px; }
.glass-card  { background:rgba(255,255,255,.15);
               backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px);
               border:1px solid rgba(255,255,255,.3);
               border-radius:12px; padding:1.75rem;
               color:#fff; box-shadow:0 8px 32px rgba(0,0,0,.18); }
.glass-card h3 { margin:0 0 .5rem; font-size:1.1rem; }
.glass-card p  { margin:0; font-size:.875rem; opacity:.85; line-height:1.5; }
```

<div style="background:linear-gradient(135deg,#6366f1 0%,#8b5cf6 50%,#ec4899 100%);padding:3rem 2rem;border-radius:12px">
  <style>
    .glass-card{background:rgba(255,255,255,.15);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.3);border-radius:12px;padding:1.75rem;color:#fff;box-shadow:0 8px 32px rgba(0,0,0,.18);max-width:320px}
    .glass-card h3{margin:0 0 .5rem;font-size:1.1rem}
    .glass-card p{margin:0;font-size:.875rem;opacity:.85;line-height:1.5}
  </style>
  <div class="glass-card">
    <h3>Glassmorphism</h3>
    <p>Built with <code style="background:rgba(255,255,255,.2);padding:.1rem .3rem;border-radius:4px">backdrop-filter: blur()</code> and a semi-transparent background. Works best layered over colourful content.</p>
  </div>
</div>

---

### 24.2 Gradient Text

Clip a background gradient to the text itself using `background-clip: text`.

```css
.grad-text {
  background: linear-gradient(135deg, #6366f1, #ec4899, #f59e0b);
  -webkit-background-clip: text;
          background-clip: text;
  color: transparent;
  font-size: 2.5rem;
  font-weight: 800;
  display: inline-block;
}
```

<div style="background:#f8fafc;padding:2rem;border-radius:8px;border:1px solid #e2e8f0;text-align:center">
  <style>
    .grad-text{background:linear-gradient(135deg,#6366f1,#ec4899,#f59e0b);-webkit-background-clip:text;background-clip:text;color:transparent;font-size:2.5rem;font-weight:800;display:inline-block;line-height:1.2}
    .grad-text2{background:linear-gradient(90deg,#0ea5e9,#22c55e);-webkit-background-clip:text;background-clip:text;color:transparent;font-size:1.5rem;font-weight:700;display:inline-block}
  </style>
  <div class="grad-text">Gradient Text</div><br>
  <div class="grad-text2">Another gradient style</div>
</div>

---

### 24.3 Gradient Border

A gradient border using a `background` gradient on the element with `background-clip: padding-box` on the inner surface — or the modern `border-image` approach.

```css
/* Approach 1: pseudo-element wrapper */
.grad-border {
  position: relative;
  border-radius: 10px;
  padding: 1.5rem;
  background: #fff;
}
.grad-border::before {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: 12px;
  background: linear-gradient(135deg, #6366f1, #ec4899);
  z-index: -1;
}

/* Approach 2: border-image (no border-radius support) */
.grad-border-2 {
  border: 2px solid;
  border-image: linear-gradient(135deg, #6366f1, #ec4899) 1;
  padding: 1rem;
}
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;display:flex;flex-wrap:wrap;gap:1.5rem;align-items:flex-start">
  <style>
    .gb{position:relative;border-radius:10px;padding:1.25rem 1.5rem;background:#fff;display:inline-block}
    .gb::before{content:'';position:absolute;inset:-2px;border-radius:12px;background:linear-gradient(135deg,#6366f1,#ec4899);z-index:-1}
    .gb p{margin:0;font-size:.875rem;color:#374151}
    .gb2{border:2px solid;border-image:linear-gradient(135deg,#0ea5e9,#22c55e) 1;padding:1rem 1.5rem;font-size:.875rem;color:#374151}
  </style>
  <div class="gb"><p>Pseudo-element gradient border<br><small style="color:#94a3b8">works with border-radius</small></p></div>
  <div class="gb2">border-image gradient<br><small style="color:#94a3b8">no border-radius support</small></div>
</div>

---

### 24.4 Neumorphism

Soft UI / neumorphism using two `box-shadow` values (light and dark) to create an extruded look.

```css
.neuo-scene  { background:#e0e5ec; padding:2.5rem; border-radius:12px; }
.neuo-card   { background:#e0e5ec; border-radius:12px; padding:1.5rem;
               box-shadow:6px 6px 14px #b8bec7, -6px -6px 14px #ffffff; }
.neuo-btn    { background:#e0e5ec; border:none; border-radius:8px;
               padding:.65rem 1.5rem; font-size:.9rem; cursor:pointer;
               box-shadow:4px 4px 10px #b8bec7, -4px -4px 10px #ffffff;
               color:#5c6e8a; font-weight:600; transition:box-shadow .15s; }
.neuo-btn:active { box-shadow:inset 4px 4px 10px #b8bec7,
                               inset -4px -4px 10px #ffffff; }
```

<div style="background:#e0e5ec;padding:2.5rem;border-radius:12px">
  <style>
    .neuo-card{background:#e0e5ec;border-radius:12px;padding:1.5rem;box-shadow:6px 6px 14px #b8bec7,-6px -6px 14px #ffffff;max-width:280px}
    .neuo-card h3{margin:0 0 .5rem;color:#5c6e8a;font-size:1rem}
    .neuo-card p{margin:0 0 1rem;font-size:.82rem;color:#7a8a9e;line-height:1.5}
    .neuo-btn{background:#e0e5ec;border:none;border-radius:8px;padding:.65rem 1.5rem;font-size:.875rem;cursor:pointer;box-shadow:4px 4px 10px #b8bec7,-4px -4px 10px #ffffff;color:#5c6e8a;font-weight:600;transition:box-shadow .15s;font-family:inherit}
    .neuo-btn:active{box-shadow:inset 4px 4px 10px #b8bec7,inset -4px -4px 10px #ffffff}
  </style>
  <div class="neuo-card">
    <h3>Neumorphism</h3>
    <p>Two offset shadows — one dark, one light — on a matching background create a soft extruded effect.</p>
    <button class="neuo-btn">Click me</button>
  </div>
</div>

---

### 24.5 CSS-Only Dark Mode

Use `prefers-color-scheme` with CSS custom properties to implement a system-following dark mode.

```css
:root {
  --bg:       #ffffff;
  --surface:  #f8fafc;
  --border:   #e2e8f0;
  --text:     #0f172a;
  --muted:    #64748b;
  --accent:   #3b82f6;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg:      #0f172a;
    --surface: #1e293b;
    --border:  #334155;
    --text:    #f1f5f9;
    --muted:   #94a3b8;
    --accent:  #60a5fa;
  }
}

body { background:var(--bg); color:var(--text); }
.card { background:var(--surface); border:1px solid var(--border); }
a    { color:var(--accent); }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .dm-demo{--dm-bg:#f8fafc;--dm-surface:#fff;--dm-border:#e2e8f0;--dm-text:#0f172a;--dm-muted:#64748b;--dm-accent:#3b82f6}
    .dm-demo.dark{--dm-bg:#0f172a;--dm-surface:#1e293b;--dm-border:#334155;--dm-text:#f1f5f9;--dm-muted:#94a3b8;--dm-accent:#60a5fa}
    .dm-wrap{background:var(--dm-bg);border-radius:8px;padding:1.25rem;transition:all .3s}
    .dm-card{background:var(--dm-surface);border:1px solid var(--dm-border);border-radius:8px;padding:1rem;color:var(--dm-text)}
    .dm-card h4{margin:0 0 .4rem;font-size:.9rem;color:var(--dm-text)}
    .dm-card p{margin:0;font-size:.8rem;color:var(--dm-muted);line-height:1.5}
    .dm-toggle{margin-top:.75rem;padding:.4rem .9rem;border-radius:6px;border:1px solid var(--dm-border);background:var(--dm-surface);color:var(--dm-text);cursor:pointer;font-size:.8rem;font-family:inherit}
  </style>
  <div class="dm-demo" id="dmDemo">
    <div class="dm-wrap">
      <div class="dm-card">
        <h4>Dark Mode Card</h4>
        <p>Toggle the button to see the theme switch using CSS custom properties. In production, <code>prefers-color-scheme</code> detects the OS setting automatically.</p>
        <button class="dm-toggle" onclick="document.getElementById('dmDemo').classList.toggle('dark')">Toggle Dark / Light</button>
      </div>
    </div>
  </div>
</div>

---

### 24.6 Container Queries

Size a component based on its *own* container width, not the viewport — the game-changer for truly reusable components.

```css
/* 1. Establish a containment context */
.cq-wrapper {
  container-type: inline-size;
  container-name: card;
}

/* 2. Query the container */
@container card (min-width: 400px) {
  .cq-card { flex-direction: row; }
  .cq-card img { width: 120px; }
}

/* Default (narrow): stacked */
.cq-card { display:flex; flex-direction:column; gap:.75rem; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .cq-wrapper{container-type:inline-size;container-name:cqcard;border:1px dashed #cbd5e1;border-radius:8px;padding:.5rem;resize:horizontal;overflow:auto;min-width:180px;max-width:100%}
    .cq-card{display:flex;flex-direction:column;gap:.75rem;background:#fff;border-radius:8px;padding:1rem}
    .cq-img{width:100%;aspect-ratio:16/9;background:linear-gradient(135deg,#6366f1,#8b5cf6);border-radius:6px;flex-shrink:0}
    .cq-card h4{margin:0 0 .3rem;font-size:.9rem;color:#1e293b}
    .cq-card p{margin:0;font-size:.8rem;color:#64748b;line-height:1.5}
    @container cqcard (min-width:380px){
      .cq-card{flex-direction:row;align-items:flex-start}
      .cq-img{width:110px;aspect-ratio:1/1}
    }
  </style>
  <p style="font-size:.8rem;color:#94a3b8;margin:0 0 .75rem">↔ Drag the right edge to resize the container</p>
  <div class="cq-wrapper">
    <div class="cq-card">
      <div class="cq-img"></div>
      <div>
        <h4>Container Query Card</h4>
        <p>This card stacks vertically when its container is narrow, and switches to a horizontal layout when it has enough room — regardless of the viewport width.</p>
      </div>
    </div>
  </div>
</div>

---

### 24.7 CSS `@layer` — Cascade Management

`@layer` lets you define explicit cascade layers so third-party CSS, utility overrides, and component styles never fight each other.

```css
/* Declare layer order — lower layers lose to higher layers */
@layer base, components, utilities;

@layer base {
  a { color: blue; text-decoration: underline; }
  h1 { font-size: 2rem; }
}

@layer components {
  .btn { padding:.5rem 1rem; border-radius:6px; color:#fff; background:#3b82f6; }
  .btn a { color: inherit; text-decoration: none; } /* overrides base */
}

@layer utilities {
  .text-red { color:#ef4444 !important; }
}

/* Outside any layer — always wins (useful for emergency overrides) */
.must-win { color: green; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <div style="font-family:monospace;font-size:.82rem;background:#1e293b;color:#e2e8f0;padding:1rem;border-radius:8px;line-height:1.6">
    <span style="color:#94a3b8">/* Layer priority (highest wins) */</span><br>
    outside any layer &gt; utilities &gt; components &gt; base<br><br>
    <span style="color:#94a3b8">/* Key benefit */</span><br>
    <span style="color:#38bdf8">@layer</span> base { <span style="color:#fbbf24">a</span> { color: blue } }<br>
    <span style="color:#94a3b8">/* A 0-specificity rule in "utilities" beats a 1-0-0 rule in "base" */</span><br>
    <span style="color:#38bdf8">@layer</span> utilities { <span style="color:#fbbf24">.text-red</span> { color: red } } <span style="color:#94a3b8">/* wins */</span>
  </div>
</div>

---

### 24.8 Logical Properties (RTL/LTR-Aware)

Logical properties use writing-mode-relative directions instead of physical ones, making RTL layouts automatic.

```css
/* Physical (breaks in RTL) */
.card-old { margin-left: 1rem; padding-left: 1.5rem; border-left: 3px solid blue; }

/* Logical (works in any writing mode / direction) */
.card-new {
  margin-inline-start: 1rem;    /* = margin-left in LTR, margin-right in RTL */
  padding-inline-start: 1.5rem;
  border-inline-start: 3px solid blue;
  /* Block axis */
  margin-block: 1.5rem;         /* = margin-top + margin-bottom */
  padding-block-start: 1rem;    /* = padding-top */
}
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0;display:grid;grid-template-columns:1fr 1fr;gap:1rem">
  <style>
    .ltr-card{padding:1rem;background:#fff;border-radius:8px;border:1px solid #e2e8f0;border-inline-start:4px solid #3b82f6;font-size:.82rem;color:#374151}
    .rtl-card{padding:1rem;background:#fff;border-radius:8px;border:1px solid #e2e8f0;border-inline-start:4px solid #ec4899;font-size:.82rem;color:#374151;direction:rtl}
  </style>
  <div>
    <p style="font-size:.75rem;color:#94a3b8;margin:0 0 .5rem">LTR (English)</p>
    <div class="ltr-card">border-inline-start appears on the left</div>
  </div>
  <div>
    <p style="font-size:.75rem;color:#94a3b8;margin:0 0 .5rem">RTL (Arabic / Hebrew)</p>
    <div class="rtl-card">border-inline-start appears on the right</div>
  </div>
</div>

---

### 24.9 Print Stylesheet

Use `@media print` to create a clean, ink-friendly version of a page — hiding navigation, adjusting typography, and forcing page breaks.

```css
@media print {
  /* Hide non-essential chrome */
  nav, footer, .sidebar, .btn, .ad { display:none !important; }

  /* Reset to print-friendly colours */
  body { color:#000; background:#fff; font-size:12pt; }
  a    { color:#000; text-decoration:none; }
  a[href]::after { content:' (' attr(href) ')'; font-size:10pt; color:#555; }

  /* Let images breathe */
  img  { max-width:100%; page-break-inside:avoid; }

  /* Keep headings with their following paragraph */
  h1, h2, h3 { page-break-after:avoid; }
  p, li       { orphans:3; widows:3; }

  /* Force a new page before major sections */
  .page-break-before { page-break-before:always; }
}
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <div style="font-size:.875rem;color:#374151;line-height:1.7;display:grid;grid-template-columns:1fr 1fr;gap:1.5rem">
    <div>
      <strong style="display:block;margin-bottom:.5rem;color:#1e293b">Hide from print:</strong>
      <code style="display:block;background:#f1f5f9;padding:.5rem;border-radius:5px;font-size:.8rem">nav, .sidebar, .btn,<br>.ad, video { display:none }</code>
    </div>
    <div>
      <strong style="display:block;margin-bottom:.5rem;color:#1e293b">Show URLs inline:</strong>
      <code style="display:block;background:#f1f5f9;padding:.5rem;border-radius:5px;font-size:.8rem">a[href]::after {<br>  content: ' (' attr(href) ')'<br>}</code>
    </div>
  </div>
</div>

---

### 24.10 Reduced Motion

Respect the `prefers-reduced-motion` media query — wrap all transitions and animations in an opt-in, not hard-coding them in.

```css
/* Default: animations enabled */
.animated-element { transition:transform .3s ease, opacity .3s ease; }
@keyframes spin { to { transform:rotate(360deg); } }
.loader { animation:spin 1s linear infinite; }

/* Respect user preference */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration:0.01ms !important;
    animation-iteration-count:1 !important;
    transition-duration:0.01ms !important;
    scroll-behavior:auto !important;
  }
}
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    @keyframes spin2{to{transform:rotate(360deg)}}
    .spin-demo{width:2.5rem;height:2.5rem;border:3px solid #e2e8f0;border-top-color:#3b82f6;border-radius:50%;animation:spin2 1s linear infinite;display:inline-block}
    @media(prefers-reduced-motion:reduce){.spin-demo{animation:none;border-color:#3b82f6;opacity:.5}}
  </style>
  <div style="display:flex;align-items:center;gap:1rem">
    <div class="spin-demo"></div>
    <p style="font-size:.875rem;color:#374151;margin:0">This spinner stops if <em>Reduce Motion</em> is enabled in your OS accessibility settings.</p>
  </div>
</div>

---

## 25. Page-Level Layout Patterns

Full-page layout shells built with CSS Grid and Flexbox.

---

### 25.1 Holy Grail Layout

The classic header / left-sidebar / main / right-sidebar / footer layout — trivially solved with Grid.

```css
.holy-grail {
  display: grid;
  grid-template:
    "header  header  header " auto
    "sidebar main    aside  " 1fr
    "footer  footer  footer " auto
    / 200px  1fr     180px;
  min-height: 100vh;
  gap: 0;
}
.hg-header  { grid-area:header;  background:#1e293b; color:#f1f5f9; }
.hg-sidebar { grid-area:sidebar; background:#f8fafc; border-right:1px solid #e2e8f0; }
.hg-main    { grid-area:main;    background:#fff; }
.hg-aside   { grid-area:aside;   background:#f8fafc; border-left:1px solid #e2e8f0; }
.hg-footer  { grid-area:footer;  background:#1e293b; color:#f1f5f9; }

@media (max-width:768px) {
  .holy-grail { grid-template:
    "header"  auto
    "main"    1fr
    "sidebar" auto
    "aside"   auto
    "footer"  auto / 1fr; }
}
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .hg{display:grid;grid-template:"hd hd hd" auto "sb mn as" minmax(80px,1fr) "ft ft ft" auto / 100px 1fr 80px;gap:3px;background:#e2e8f0;border-radius:6px;overflow:hidden;font-size:.75rem;font-weight:600;text-align:center}
    .hg-hd{grid-area:hd;background:#1e293b;color:#f1f5f9;padding:.6rem}
    .hg-sb{grid-area:sb;background:#f8fafc;color:#64748b;padding:.6rem;border-right:none}
    .hg-mn{grid-area:mn;background:#fff;color:#474747;padding:.75rem;font-size:.85rem;font-weight:400;text-align:left}
    .hg-as{grid-area:as;background:#f8fafc;color:#64748b;padding:.6rem}
    .hg-ft{grid-area:ft;background:#334155;color:#94a3b8;padding:.6rem}
  </style>
  <div class="hg">
    <div class="hg-hd">Header</div>
    <div class="hg-sb">Sidebar</div>
    <div class="hg-mn">Main content area — this grows to fill available space. On mobile the sidebar and aside stack below.</div>
    <div class="hg-as">Aside</div>
    <div class="hg-ft">Footer</div>
  </div>
</div>

---

### 25.2 Dashboard Shell

A real-world dashboard layout: fixed sidebar nav, sticky topbar, scrollable main content.

```css
.dashboard {
  display: grid;
  grid-template-columns: 220px 1fr;
  grid-template-rows: auto 1fr;
  min-height: 100vh;
}
.db-topbar  { grid-column:1 / -1; position:sticky; top:0; z-index:10;
              background:#fff; border-bottom:1px solid #e2e8f0;
              padding:.75rem 1.5rem; display:flex; align-items:center;
              justify-content:space-between; }
.db-sidebar { background:#1e293b; padding:1rem 0; overflow-y:auto; }
.db-main    { background:#f8fafc; padding:1.5rem; overflow-y:auto; }

/* Sidebar nav items */
.db-nav-item { display:flex; align-items:center; gap:.75rem;
               padding:.65rem 1.25rem; color:#94a3b8; text-decoration:none;
               font-size:.875rem; transition:all .15s; }
.db-nav-item:hover { background:#334155; color:#f1f5f9; }
.db-nav-item.db-active { background:#3b82f6; color:#fff; border-radius 0; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .db-shell{display:grid;grid-template-columns:150px 1fr;grid-template-rows:auto 1fr;height:260px;border-radius:8px;overflow:hidden;border:1px solid #e2e8f0;font-size:.8rem}
    .db-topbar{grid-column:1/-1;background:#fff;border-bottom:1px solid #e2e8f0;padding:.6rem 1rem;display:flex;align-items:center;justify-content:space-between;font-weight:600;color:#1e293b}
    .db-sidebar2{background:#1e293b;padding:.5rem 0;overflow-y:auto}
    .db-navitem{display:block;padding:.5rem 1rem;color:#94a3b8;font-size:.78rem;cursor:pointer;transition:background .15s}
    .db-navitem:hover{background:#334155;color:#f1f5f9}
    .db-navitem.db-act{background:#3b82f6;color:#fff}
    .db-main2{background:#f8fafc;padding:1rem;overflow-y:auto;display:grid;grid-template-columns:1fr 1fr;gap:.75rem;align-content:start}
    .db-widget{background:#fff;border:1px solid #e2e8f0;border-radius:6px;padding:.75rem}
    .db-widget .label{font-size:.7rem;color:#94a3b8;margin-bottom:.2rem}
    .db-widget .value{font-size:1.3rem;font-weight:700;color:#1e293b}
  </style>
  <div class="db-shell">
    <div class="db-topbar"><span>MyDashboard</span><span style="font-size:.75rem;color:#64748b;font-weight:400">Harry Gomm</span></div>
    <div class="db-sidebar2">
      <div class="db-navitem db-act">📊 Overview</div>
      <div class="db-navitem">📈 Analytics</div>
      <div class="db-navitem">👤 Users</div>
      <div class="db-navitem">⚙️ Settings</div>
      <div class="db-navitem">💬 Support</div>
    </div>
    <div class="db-main2">
      <div class="db-widget"><div class="label">Revenue</div><div class="value">£24,892</div></div>
      <div class="db-widget"><div class="label">Users</div><div class="value">1,204</div></div>
      <div class="db-widget"><div class="label">Orders</div><div class="value">342</div></div>
      <div class="db-widget"><div class="label">Uptime</div><div class="value">99.9%</div></div>
    </div>
  </div>
</div>

---

### 25.3 Hero Section with Text Overlay

A full-width hero with a background image, darkening scrim, and centred text — a foundational pattern for landing pages.

```css
.hero {
  position: relative;
  min-height: 420px;
  display: flex; align-items: center; justify-content: center;
  text-align: center;
  background: url('hero.jpg') center/cover no-repeat;
  color: #fff;
}
/* Dark scrim overlay */
.hero::before {
  content: '';
  position: absolute; inset: 0;
  background: linear-gradient(to bottom,
    rgba(0,0,0,.3) 0%, rgba(0,0,0,.65) 100%);
}
.hero-content { position: relative; z-index: 1; max-width: 600px; padding: 2rem; }
.hero-content h1 { font-size: clamp(2rem, 5vw, 3.5rem); font-weight: 800; margin:0 0 1rem; }
.hero-content p  { font-size: clamp(1rem, 2vw, 1.2rem); opacity:.9; margin:0 0 1.5rem; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .hero-demo{position:relative;min-height:220px;display:flex;align-items:center;justify-content:center;text-align:center;background:linear-gradient(135deg,#0f172a 0%,#1e3a5f 60%,#0f4c81 100%);color:#fff;border-radius:8px;overflow:hidden}
    .hero-demo::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 120%,rgba(59,130,246,.3),transparent 70%)}
    .hero-content-d{position:relative;z-index:1;max-width:500px;padding:2rem}
    .hero-content-d h2{font-size:clamp(1.5rem,4vw,2.5rem);font-weight:800;margin:0 0 .75rem;line-height:1.2}
    .hero-content-d p{font-size:clamp(.875rem,2vw,1.05rem);opacity:.85;margin:0 0 1.25rem;line-height:1.6}
    .hero-cta{display:inline-block;padding:.65rem 1.75rem;background:#3b82f6;color:#fff;border-radius:7px;text-decoration:none;font-weight:600;font-size:.9rem;transition:background .15s}
    .hero-cta:hover{background:#2563eb}
  </style>
  <div class="hero-demo">
    <div class="hero-content-d">
      <h2>Build Better Interfaces</h2>
      <p>A complete CSS reference with live examples, practical patterns, and everything you need to master modern CSS.</p>
      <a class="hero-cta" href="#">Get Started →</a>
    </div>
  </div>
</div>

---

### 25.4 Blog Post Layout

A readable article layout: constrained prose width, large drop-caps, generous line-height, and responsive figure captions.

```css
.prose {
  max-width: 68ch;
  margin-inline: auto;
  font-size: clamp(1rem, 1.5vw, 1.125rem);
  line-height: 1.75;
  color: #374151;
}
.prose h1 { font-size:2.5rem; line-height:1.2; color:#0f172a; }
.prose h2 { font-size:1.5rem; margin-top:2.5rem; color:#1e293b; }
.prose p  { margin:1.25rem 0; }

/* Drop cap on first paragraph */
.prose > p:first-of-type::first-letter {
  font-size:3.5rem; font-weight:800; float:left;
  line-height:.85; margin:.05em .08em 0 0;
  color:#3b82f6;
}
.prose figure { margin:2rem 0; }
.prose figcaption { font-size:.82rem; color:#94a3b8; text-align:center;
                     margin-top:.5rem; }
.prose blockquote { border-left:3px solid #3b82f6; margin:1.5rem 0;
                     padding:.5rem 1.25rem; color:#475569;
                     font-style:italic; background:#f8fafc; border-radius:0 6px 6px 0; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .prose-demo{max-width:60ch;margin-inline:auto;font-size:.9rem;line-height:1.75;color:#374151}
    .prose-demo h2{font-size:1.3rem;margin:1.5rem 0 .5rem;color:#1e293b;line-height:1.3}
    .prose-demo p{margin:.9rem 0}
    .prose-demo>p:first-of-type::first-letter{font-size:3rem;font-weight:800;float:left;line-height:.85;margin:.05em .08em 0 0;color:#3b82f6}
    .prose-demo blockquote{border-left:3px solid #3b82f6;margin:1rem 0;padding:.4rem 1rem;color:#475569;font-style:italic;background:#fff;border-radius:0 6px 6px 0}
  </style>
  <div class="prose-demo">
    <h2>Why CSS Still Matters</h2>
    <p>CSS has evolved far beyond its roots as a simple styling language. Today it handles animation, layout, logic-like functions, and even scroll-driven interactions — all without JavaScript.</p>
    <blockquote>First, solve the problem. Then, write the code.</blockquote>
    <p>The shift to custom properties, container queries, and cascade layers means CSS can now scale to the demands of large design systems whilst remaining maintainable.</p>
  </div>
</div>

---

### 25.5 Login / Register Card

A centred auth card — a common pattern that exercises flexbox centering, form styling, and focus management.

```css
.auth-scene { min-height:100vh; display:flex; align-items:center;
              justify-content:center; background:#f1f5f9; padding:2rem; }
.auth-card  { width:100%; max-width:400px; background:#fff; border-radius:12px;
              padding:2.5rem; box-shadow:0 4px 24px rgba(0,0,0,.08); }
.auth-card h2 { margin:0 0 .4rem; font-size:1.5rem; color:#0f172a; }
.auth-card .sub { margin:0 0 1.75rem; font-size:.875rem; color:#64748b; }
.auth-divider { display:flex; align-items:center; gap:.75rem;
                margin:1.25rem 0; color:#94a3b8; font-size:.8rem; }
.auth-divider::before, .auth-divider::after {
  content:''; flex:1; height:1px; background:#e2e8f0;
}
```

<div style="background:#f1f5f9;padding:2rem;border-radius:8px">
  <style>
    .auth-card-d{width:100%;max-width:380px;background:#fff;border-radius:12px;padding:2rem;box-shadow:0 4px 24px rgba(0,0,0,.08);margin:0 auto}
    .auth-card-d h3{margin:0 0 .3rem;font-size:1.3rem;color:#0f172a}
    .auth-card-d .sub2{margin:0 0 1.5rem;font-size:.82rem;color:#64748b}
    .auth-fg{display:flex;flex-direction:column;gap:.3rem;margin-bottom:1rem}
    .auth-fl{font-size:.8rem;font-weight:500;color:#374151}
    .auth-fi{padding:.55rem .85rem;border:1.5px solid #d1d5db;border-radius:7px;font-size:.875rem;outline:none;width:100%;box-sizing:border-box;font-family:inherit;transition:border-color .15s}
    .auth-fi:focus{border-color:#3b82f6}
    .auth-btn-f{width:100%;padding:.65rem;background:#3b82f6;color:#fff;border:none;border-radius:7px;font-size:.9rem;font-weight:600;cursor:pointer;font-family:inherit;transition:background .15s}
    .auth-btn-f:hover{background:#2563eb}
    .auth-div{display:flex;align-items:center;gap:.75rem;margin:.9rem 0;color:#94a3b8;font-size:.78rem}
    .auth-div::before,.auth-div::after{content:'';flex:1;height:1px;background:#e2e8f0}
    .auth-foot{text-align:center;font-size:.8rem;color:#64748b;margin-top:1rem}
    .auth-foot a{color:#3b82f6;text-decoration:none}
  </style>
  <div class="auth-card-d">
    <h3>Welcome back</h3>
    <p class="sub2">Sign in to your account to continue.</p>
    <div class="auth-fg">
      <label class="auth-fl">Email</label>
      <input class="auth-fi" type="email" placeholder="you@example.com">
    </div>
    <div class="auth-fg">
      <label class="auth-fl">Password</label>
      <input class="auth-fi" type="password" placeholder="••••••••">
    </div>
    <button class="auth-btn-f">Sign in</button>
    <div class="auth-div">or</div>
    <button style="width:100%;padding:.6rem;border:1.5px solid #e2e8f0;border-radius:7px;background:#fff;font-size:.875rem;cursor:pointer;font-family:inherit;color:#374151;font-weight:500">Continue with Google</button>
    <p class="auth-foot">Don't have an account? <a href="#">Sign up free</a></p>
  </div>
</div>

---

### 25.6 Masonry-Style Gallery

CSS `columns` creates a flowing masonry layout without JavaScript, where items naturally fill vertical space.

```css
.masonry {
  columns: 3 200px;     /* up to 3 cols, min 200px each */
  column-gap: 1rem;
}
.masonry-item {
  break-inside: avoid;  /* prevent items splitting across columns */
  margin-bottom: 1rem;
  border-radius: 8px;
  overflow: hidden;
}
.masonry-item img { display:block; width:100%; height:auto; }
```

<div style="background:#f8fafc;padding:1.5rem;border-radius:8px;border:1px solid #e2e8f0">
  <style>
    .masonry-d{columns:3 150px;column-gap:.75rem}
    .masonry-item-d{break-inside:avoid;margin-bottom:.75rem;border-radius:6px;overflow:hidden}
    .masonry-tile{width:100%;border-radius:6px;display:block}
  </style>
  <div class="masonry-d">
    <div class="masonry-item-d"><div class="masonry-tile" style="height:120px;background:linear-gradient(135deg,#6366f1,#8b5cf6)"></div></div>
    <div class="masonry-item-d"><div class="masonry-tile" style="height:80px;background:linear-gradient(135deg,#0ea5e9,#22c55e)"></div></div>
    <div class="masonry-item-d"><div class="masonry-tile" style="height:160px;background:linear-gradient(135deg,#f43f5e,#f59e0b)"></div></div>
    <div class="masonry-item-d"><div class="masonry-tile" style="height:100px;background:linear-gradient(135deg,#ec4899,#6366f1)"></div></div>
    <div class="masonry-item-d"><div class="masonry-tile" style="height:140px;background:linear-gradient(135deg,#14b8a6,#0ea5e9)"></div></div>
    <div class="masonry-item-d"><div class="masonry-tile" style="height:90px;background:linear-gradient(135deg,#f59e0b,#ef4444)"></div></div>
    <div class="masonry-item-d"><div class="masonry-tile" style="height:110px;background:linear-gradient(135deg,#22c55e,#14b8a6)"></div></div>
    <div class="masonry-item-d"><div class="masonry-tile" style="height:130px;background:linear-gradient(135deg,#8b5cf6,#ec4899)"></div></div>
  </div>
</div>
