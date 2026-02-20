/* ==========================================================
   Global Search — indexes all markdown docs, shows results
   on the hub page with snippets and direct section links.
   ========================================================== */

(function () {
  'use strict';

  // ── Doc registry ──────────────────────────────────────────
  const DOCS = [
    {
      id: 'customtkinter',
      title: 'CustomTkinter',
      mdPath: 'content/customtkinter.md',
      htmlPage: 'pages/customtkinter.html',
      color: '#6366f1',
    },
    {
      id: 'reportlab',
      title: 'ReportLab',
      mdPath: 'content/reportlab.md',
      htmlPage: 'pages/reportlab.html',
      color: '#ef4444',
    },
    {
      id: 'python314',
      title: 'Python 3.14',
      mdPath: 'content/python-3.14.md',
      htmlPage: 'pages/python-3.14.html',
      color: '#306998',
    },
      {
  id: 'htmlcompletereferencepracticalguide',
  title: 'HTML Complete Reference & Practical Guide',
  mdPath: 'content/html-complete-reference-practical-guide.md',
  htmlPage: 'pages/html-complete-reference-practical-guide.html',
  color: '#6366f1',
},
      {
  id: 'csscompletereferencepracticalguide',
  title: 'CSS Complete Reference & Practical Guide',
  mdPath: 'content/css-complete-reference-practical-guide.md',
  htmlPage: 'pages/css-complete-reference-practical-guide.html',
  color: '#264de4',
},
      {
  id: 'markdownlanguage',
  title: 'Markdown Language',
  mdPath: 'content/markdown-language.md',
  htmlPage: 'pages/markdown-language.html',
  color: '#06b6d4',
},
  ];

  const assetVersion = (window.__ASSET_VERSION || '').toString().trim();
  function withVersion(url) {
    if (!assetVersion) return url;
    if (!url) return url;
    if (/\bv=/.test(url)) return url;
    const joiner = url.includes('?') ? '&' : '?';
    return `${url}${joiner}v=${encodeURIComponent(assetVersion)}`;
  }

  // ── State ─────────────────────────────────────────────────
  let index = [];        // {doc, heading, anchor, content, level}
  let loaded = false;
  let loadingPromise = null;

  // ── DOM refs ──────────────────────────────────────────────
  const searchWrap = document.getElementById('hub-search-wrap');
  const searchInput = document.getElementById('hub-search');
  const searchResults = document.getElementById('hub-search-results');
  const searchStatus = document.getElementById('hub-search-status');
  const searchClear = document.getElementById('hub-search-clear');
  const hubSections = document.getElementById('hub-sections');
  const hubShortcuts = document.querySelector('.hub-shortcuts');

  if (!searchInput || !searchResults) return;

  // ── Build index ───────────────────────────────────────────

  function slugify(text) {
    return text
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-|-$/g, '');
  }

  function parseMarkdown(mdText, doc) {
    const lines = mdText.split('\n');
    const sections = [];
    let currentHeading = null;
    let currentAnchor = '';
    let currentLevel = 0;
    let buffer = [];
    const idCount = {};
    let inCodeFence = false;
    let codeFenceMarker = '';

    for (const line of lines) {
      const trimmed = line.trim();

      // Skip fenced code blocks entirely so search results are about prose + headings,
      // not random identifiers from examples.
      const fenceMatch = trimmed.match(/^(```|~~~)/);
      if (fenceMatch) {
        const marker = fenceMatch[1];
        if (!inCodeFence) {
          inCodeFence = true;
          codeFenceMarker = marker;
        } else if (codeFenceMarker === marker) {
          inCodeFence = false;
          codeFenceMarker = '';
        }
        continue;
      }
      if (inCodeFence) continue;

      const headingMatch = line.match(/^(#{1,4})\s+(.+)/);
      if (headingMatch) {
        // Flush previous section
        if (currentHeading) {
          sections.push({
            doc: doc,
            heading: currentHeading,
            anchor: currentAnchor,
            level: currentLevel,
            content: buffer.join(' ').replace(/[#`*_\[\]()>|]/g, ' ').replace(/\s+/g, ' ').trim(),
          });
        }

        currentHeading = headingMatch[2].replace(/[`*_]/g, '').trim();
        currentLevel = headingMatch[1].length;

        // Generate anchor matching docs-renderer.js slug logic
        let base = slugify(currentHeading);
        if (idCount[base] == null) {
          idCount[base] = 0;
        } else {
          idCount[base]++;
          base += '-' + idCount[base];
        }
        currentAnchor = base;
        buffer = [];
      } else {
        // Collect content lines (strip markdown syntax)
        const cleaned = line
          .replace(/^>\s?/, '')          // blockquote
          .replace(/^\s*[-*+]\s/, '')    // list items
          .replace(/^\s*\d+\.\s/, '')    // numbered lists
          .replace(/```[\s\S]*?```/g, '') // inline code blocks (single-line)
          .replace(/`[^`]+`/g, '')       // inline code
          .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') // links
          .replace(/[*_~]/g, '')         // emphasis
          .trim();
        if (cleaned) buffer.push(cleaned);
      }
    }

    // Flush last section
    if (currentHeading) {
      sections.push({
        doc: doc,
        heading: currentHeading,
        anchor: currentAnchor,
        level: currentLevel,
        content: buffer.join(' ').replace(/[#`*_\[\]()>|]/g, ' ').replace(/\s+/g, ' ').trim(),
      });
    }

    return sections;
  }

  async function buildIndex() {
    if (loaded) return;
    if (loadingPromise) return loadingPromise;

    loadingPromise = Promise.all(
      DOCS.map(async (doc) => {
        try {
          const res = await fetch(withVersion(doc.mdPath), { cache: assetVersion ? 'force-cache' : 'no-store' });
          if (!res.ok) return [];
          const md = await res.text();
          return parseMarkdown(md, doc);
        } catch {
          return [];
        }
      })
    ).then((results) => {
      index = results.flat();
      loaded = true;
    });

    return loadingPromise;
  }

  // ── Search ────────────────────────────────────────────────

  function search(query) {
    if (!query || query.length < 2) return [];

    const terms = query.toLowerCase().split(/\s+/).filter(t => t.length >= 2);
    if (terms.length === 0) return [];

    const scored = [];

    for (const entry of index) {
      const headingLower = entry.heading.toLowerCase();
      const contentLower = entry.content.toLowerCase();

      let score = 0;
      let allTermsMatch = true;

      for (const term of terms) {
        const inHeading = headingLower.includes(term);
        const inContent = contentLower.includes(term);

        if (!inHeading && !inContent) {
          allTermsMatch = false;
          break;
        }

        // Heading matches score higher
        if (inHeading) {
          score += 100;
          // Exact heading match bonus
          if (headingLower === query.toLowerCase()) score += 500;
          // Starts-with bonus
          if (headingLower.startsWith(term)) score += 50;
        }
        if (inContent) {
          score += 10;
          // Count occurrences (cap at 5)
          const count = Math.min(5, (contentLower.split(term).length - 1));
          score += count * 2;
        }

        // Higher-level headings rank higher
        if (entry.level === 1) score += 30;
        else if (entry.level === 2) score += 20;
        else if (entry.level === 3) score += 10;
      }

      if (allTermsMatch && score > 0) {
        scored.push({ entry, score });
      }
    }

    // Sort by score descending, limit to 30
    scored.sort((a, b) => b.score - a.score);
    return scored.slice(0, 30);
  }

  // ── Snippet extraction ────────────────────────────────────

  function extractSnippet(content, query, maxLen = 140) {
    const lower = content.toLowerCase();
    const terms = query.toLowerCase().split(/\s+/).filter(t => t.length >= 2);
    const firstTerm = terms[0] || query.toLowerCase();

    const idx = lower.indexOf(firstTerm);
    if (idx === -1) return content.slice(0, maxLen) + (content.length > maxLen ? '…' : '');

    const start = Math.max(0, idx - 40);
    const end = Math.min(content.length, idx + maxLen - 40);
    let snippet = content.slice(start, end);

    if (start > 0) snippet = '…' + snippet;
    if (end < content.length) snippet += '…';

    // Bold matching terms
    for (const term of terms) {
      const regex = new RegExp(`(${term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
      snippet = snippet.replace(regex, '<mark>$1</mark>');
    }

    return snippet;
  }

  // ── Render results ────────────────────────────────────────

  function renderResults(results, query) {
    if (results.length === 0) {
      searchResults.innerHTML = `
        <div class="search-empty">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.3">
            <circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/>
          </svg>
          <p>No results for "<strong>${escapeHtml(query)}</strong>"</p>
          <span>Try different keywords or check spelling</span>
        </div>`;
      searchStatus.textContent = '0 results';
      return;
    }

    // Group by doc
    const groups = {};
    for (const r of results) {
      const docId = r.entry.doc.id;
      if (!groups[docId]) groups[docId] = { doc: r.entry.doc, items: [] };
      groups[docId].items.push(r);
    }

    let html = '';
    for (const group of Object.values(groups)) {
      html += `<div class="search-group">`;
      html += `<div class="search-group-header" style="border-left-color: ${group.doc.color}">
        <span class="search-group-dot" style="background: ${group.doc.color}"></span>
        ${escapeHtml(group.doc.title)}
        <span class="search-group-count">${group.items.length}</span>
      </div>`;

      for (const r of group.items) {
        const pageUrl = withVersion(r.entry.doc.htmlPage);
        const url = `${pageUrl}#${r.entry.anchor}`;
        const snippet = extractSnippet(r.entry.content, query);
        const levelTag = r.entry.level <= 2 ? '' : `<span class="search-level">h${r.entry.level}</span>`;

        html += `<a href="${url}" class="search-result-item">
          <div class="search-result-heading">${highlightTerms(r.entry.heading, query)} ${levelTag}</div>
          <div class="search-result-snippet">${snippet}</div>
        </a>`;
      }
      html += `</div>`;
    }

    searchResults.innerHTML = html;
    searchStatus.textContent = `${results.length} result${results.length !== 1 ? 's' : ''}`;
  }

  function highlightTerms(text, query) {
    const terms = query.toLowerCase().split(/\s+/).filter(t => t.length >= 2);
    let result = escapeHtml(text);
    for (const term of terms) {
      const regex = new RegExp(`(${term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
      result = result.replace(regex, '<mark>$1</mark>');
    }
    return result;
  }

  function escapeHtml(str) {
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  // ── UI behavior ───────────────────────────────────────────

  let debounceTimer = null;

  searchInput.addEventListener('input', () => {
    const query = searchInput.value.trim();

    // Show/hide clear button
    searchClear.style.display = query ? 'flex' : 'none';

    clearTimeout(debounceTimer);

    if (query.length < 2) {
      searchResults.classList.remove('visible');
      if (hubSections) hubSections.style.display = '';
      if (hubShortcuts) hubShortcuts.style.display = '';
      searchStatus.textContent = '';
      return;
    }

    debounceTimer = setTimeout(async () => {
      if (!loaded) {
        searchStatus.textContent = 'Loading docs…';
        searchResults.innerHTML = '<div class="search-loading"><div class="spinner"></div></div>';
        searchResults.classList.add('visible');
        if (hubSections) hubSections.style.display = 'none';
        if (hubShortcuts) hubShortcuts.style.display = 'none';
        await buildIndex();
      }

      const results = search(query);
      renderResults(results, query);
      searchResults.classList.add('visible');
      if (hubSections) hubSections.style.display = 'none';
      if (hubShortcuts) hubShortcuts.style.display = 'none';
    }, 200);
  });

  searchClear.addEventListener('click', () => {
    searchInput.value = '';
    searchClear.style.display = 'none';
    searchResults.classList.remove('visible');
    searchResults.innerHTML = '';
    searchStatus.textContent = '';
    if (hubSections) hubSections.style.display = '';
    if (hubShortcuts) hubShortcuts.style.display = '';
    searchInput.focus();
  });

  // Keyboard: / to focus, Esc to clear
  document.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT') {
      if (e.key === 'Escape') {
        searchInput.value = '';
        searchClear.style.display = 'none';
        searchResults.classList.remove('visible');
        searchResults.innerHTML = '';
        searchStatus.textContent = '';
        if (hubSections) hubSections.style.display = '';
        if (hubShortcuts) hubShortcuts.style.display = '';
        searchInput.blur();
      }
      return;
    }
    if (e.key === '/') {
      e.preventDefault();
      searchInput.focus();
    }
  });

  // Preload index on first focus (lazy)
  searchInput.addEventListener('focus', () => {
    if (!loaded && !loadingPromise) buildIndex();
  }, { once: true });

})();
