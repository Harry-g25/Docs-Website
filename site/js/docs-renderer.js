/* ==========================================================
   Docs Renderer — shared script for all doc pages
   Theme · Markdown · TOC · Search · Copy · Shortcuts · Progress
   ========================================================== */

(async function () {
  'use strict';

  // ---- Config (set by each page before loading this script) ----
  const config = window.__DOC_CONFIG || {};
  const mdPath = config.mdPath || '../CUSTOMTKINTER_DOCUMENTATION.md';
  const docTitle = config.title || 'Documentation';

  const assetVersion = (window.__ASSET_VERSION || '').toString().trim();
  function withVersion(url) {
    if (!assetVersion) return url;
    if (!url) return url;
    if (/\bv=/.test(url)) return url;
    const joiner = url.includes('?') ? '&' : '?';
    return `${url}${joiner}v=${encodeURIComponent(assetVersion)}`;
  }

  // ---- Helpers ----
  const $ = (s, p) => (p || document).querySelector(s);
  const $$ = (s, p) => [...(p || document).querySelectorAll(s)];
  const content    = $('#content');
  const toc        = $('#toc');
  const main       = $('#main');
  const sidebar    = $('#sidebar');
  const overlay    = $('#overlay');
  const backTop    = $('#back-to-top');
  const progressBar = $('#progress-bar');

  // ===== 1. Theme Toggle =====
  function currentTheme() {
    return document.documentElement.getAttribute('data-theme') || 'dark';
  }

  function setTheme(t) {
    document.documentElement.classList.add('theme-transition');
    document.documentElement.setAttribute('data-theme', t);
    localStorage.setItem('ctk-theme', t);

    const hljsLink = $('#hljs-theme');
    if (hljsLink) {
      hljsLink.href = t === 'dark'
        ? withVersion('../css/highlight-github-dark.min.css')
        : withVersion('../css/highlight-github.min.css');
    }

    setTimeout(() => document.documentElement.classList.remove('theme-transition'), 350);
  }

  function toggleTheme() {
    setTheme(currentTheme() === 'dark' ? 'light' : 'dark');
  }

  const themeBtn = $('#theme-btn');
  if (themeBtn) themeBtn.addEventListener('click', toggleTheme);
  const mobileThemeBtn = $('#theme-btn-mobile');
  if (mobileThemeBtn) mobileThemeBtn.addEventListener('click', toggleTheme);
  setTheme(currentTheme());

  // ===== 2. Mobile sidebar toggle =====
  const menuBtn = $('#menu-btn');
  if (menuBtn) {
    menuBtn.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      overlay.classList.toggle('visible');
    });
  }
  if (overlay) {
    overlay.addEventListener('click', () => {
      sidebar.classList.remove('open');
      overlay.classList.remove('visible');
    });
  }

  // ===== 3. Fetch & render Markdown =====
  let md = '';
  try {
    const res = await fetch(withVersion(mdPath), { cache: 'no-store' });
    if (!res.ok) throw new Error(res.statusText);
    md = await res.text();
  } catch (err) {
    content.innerHTML = `
      <div style="text-align:center;padding:60px 20px">
        <h2 style="margin-bottom:12px">Could not load documentation</h2>
        <p style="color:var(--content-muted)">Make sure you're running a local server from the project root:</p>
        <pre style="display:inline-block;text-align:left;margin-top:12px"><code>python serve.py</code></pre>
        <p style="color:var(--content-muted);margin-top:16px;font-size:13px">Error: ${err}</p>
      </div>`;
    return;
  }

  // Configure marked with a custom renderer
  const renderer = new marked.Renderer();
  renderer.code = function (code, lang) {
    let text = typeof code === 'object' ? code.text : code;
    let language = typeof code === 'object' ? code.lang : lang;

    // CTk widget preview — render raw HTML inside a styled wrapper
    if (language === 'ctk-preview') {
      return `<div class="ctk-preview-wrap">${text}</div>\n`;
    }

    const langClass = language ? `language-${language}` : '';
    const escaped = text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
    return `<pre><code class="hljs ${langClass}">${escaped}</code></pre>\n`;
  };

  content.innerHTML = marked.parse(md, { gfm: true, breaks: true, renderer: renderer });

  // Run highlight.js on all code blocks
  $$('pre code', content).forEach(block => {
    hljs.highlightElement(block);
  });

  // ===== 3b. PDF embeds: bigger preview + full-page link =====
  // Many guides embed PDFs via <object type="application/pdf">.
  // QtWebEngine and some browsers can preview them inline, but users may want a
  // full-page PDF view (like a normal PDF viewer). We provide both.
  $$('object[type="application/pdf"]', content).forEach(obj => {
    const src = (obj.getAttribute('data') || '').trim();
    if (!src) return;
    if (obj.dataset.pdfEnhanced === '1') return;
    obj.dataset.pdfEnhanced = '1';

    // Make the inline preview feel like a full-page viewer.
    // Keep border styling from the HTML, but increase height.
    obj.style.height = '85vh';

    // Add an "Open PDF (full page)" link above the object.
    const row = document.createElement('p');
    row.style.margin = '0 0 10px 0';

    const a = document.createElement('a');
    a.href = withVersion(src);
    a.textContent = 'Open PDF (full page)';
    a.title = 'Open the PDF without the doc page UI';

    row.appendChild(a);
    obj.parentNode.insertBefore(row, obj);
  });

  // ===== 4. Estimated reading time =====
  const wordCount = content.innerText.split(/\s+/).length;
  const readMin = Math.max(1, Math.ceil(wordCount / 220));
  const firstH1 = $('h1', content);
  if (firstH1) {
    const badge = document.createElement('div');
    badge.className = 'reading-time';
    badge.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg> ${readMin} min read &middot; ${wordCount.toLocaleString()} words`;
    firstH1.insertAdjacentElement('afterend', badge);
  }

  // ===== 5. Add copy buttons + language labels to <pre> =====
  $$('pre', content).forEach(pre => {
    pre.style.position = 'relative';
    const codeEl = pre.querySelector('code');

    // Language label
    if (codeEl) {
      const cls = [...codeEl.classList].find(c => c.startsWith('language-'));
      if (cls) {
        const lang = cls.replace('language-', '');
        const label = document.createElement('span');
        label.className = 'code-lang-label';
        label.textContent = lang;
        pre.appendChild(label);
      }
    }

    // Copy button
    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg> Copy';
    btn.addEventListener('click', () => {
      navigator.clipboard.writeText(codeEl ? codeEl.innerText : pre.innerText).then(() => {
        btn.innerHTML = '✓ Copied';
        btn.classList.add('copied');
        setTimeout(() => {
          btn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg> Copy';
          btn.classList.remove('copied');
        }, 1800);
      });
    });
    pre.appendChild(btn);
  });

  // ===== 6. Heading anchor links =====
  $$('h1,h2,h3,h4', content).forEach(h => {
    if (!h.id) return;
    const anchor = document.createElement('a');
    anchor.className = 'heading-anchor';
    anchor.href = '#' + h.id;
    anchor.textContent = '#';
    anchor.title = 'Copy link to section';
    anchor.addEventListener('click', (e) => {
      e.preventDefault();
      history.replaceState(null, '', '#' + h.id);
      h.scrollIntoView({ behavior: 'smooth', block: 'start' });
      navigator.clipboard.writeText(window.location.href).catch(() => {});
    });
    h.prepend(anchor);
  });

  // ===== 7. Build TOC (with collapsible sub-headings) =====
  const headings = $$('h1,h2,h3,h4', content);
  const idCount = {};
  let groupId = 0;

  headings.forEach(h => {
    let base = h.textContent.replace('#', '').trim().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    if (idCount[base] == null) { idCount[base] = 0; } else { idCount[base]++; base += '-' + idCount[base]; }
    h.id = base;

    const tag = h.tagName.toLowerCase();
    const a = document.createElement('a');
    a.href = '#' + base;
    a.className = 'toc-' + tag;
    a.dataset.search = h.textContent.trim().toLowerCase();

    if (tag === 'h3') {
      groupId++;
      const gid = groupId;
      a.dataset.group = gid;

      // Chevron toggle
      const chevron = document.createElement('span');
      chevron.className = 'toc-chevron';
      chevron.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        a.classList.toggle('expanded');
        $$(`#toc a.toc-h4[data-parent-group="${gid}"]`).forEach(sub => {
          sub.classList.toggle('toc-sub-hidden');
        });
      });
      a.appendChild(chevron);

      // Section text
      const span = document.createElement('span');
      span.textContent = h.textContent.replace('#', '').trim();
      a.appendChild(span);
    } else {
      a.textContent = h.textContent.replace('#', '').trim();
    }

    if (tag === 'h4') {
      a.dataset.parentGroup = groupId;
      a.classList.add('toc-sub-hidden');
    }

    a.addEventListener('click', (e) => {
      e.preventDefault();
      h.scrollIntoView({ behavior: 'smooth', block: 'start' });
      $$('#toc a').forEach(x => x.classList.remove('active'));
      a.classList.add('active');
      sidebar.classList.remove('open');
      overlay.classList.remove('visible');
    });

    toc.appendChild(a);
  });

  // ===== 8. TOC search / filter =====
  const searchInput = $('#toc-search');
  if (searchInput) {
    searchInput.addEventListener('input', () => {
      const q = searchInput.value.toLowerCase().trim();
      if (q.length === 0) {
        // Restore: hide all h4 sub-items, show everything else
        $$('#toc a').forEach(a => {
          a.classList.remove('hidden');
          if (a.classList.contains('toc-h4')) {
            const parent = $(`#toc a.toc-h3[data-group="${a.dataset.parentGroup}"]`);
            if (!parent || !parent.classList.contains('expanded')) {
              a.classList.add('toc-sub-hidden');
            }
          }
        });
      } else {
        // While searching, show all matching items regardless of collapse state
        $$('#toc a').forEach(a => {
          const matches = a.dataset.search.includes(q);
          a.classList.toggle('hidden', !matches);
          if (matches) a.classList.remove('toc-sub-hidden');
        });
      }
    });
  }

  // ===== 9. Scroll spy + progress bar =====
  let ticking = false;

  function updateScrollSpy() {
    const scrollTop = main.scrollTop;
    const scrollHeight = main.scrollHeight - main.clientHeight;
    const pct = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;

    // Update progress bar
    if (progressBar) progressBar.style.width = pct + '%';

    // Find current heading
    let current = null;
    headings.forEach(h => {
      if (h.offsetTop <= scrollTop + 120) current = h;
    });
    if (current) {
      const id = current.id;
      $$('#toc a').forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + id));

      const activeLink = toc.querySelector('a.active');
      if (activeLink) {
        // Auto-expand parent group when an h4 becomes active
        if (activeLink.classList.contains('toc-h4') && activeLink.classList.contains('toc-sub-hidden')) {
          const gid = activeLink.dataset.parentGroup;
          const parentH3 = $(`#toc a.toc-h3[data-group="${gid}"]`);
          if (parentH3 && !parentH3.classList.contains('expanded')) {
            parentH3.classList.add('expanded');
            $$(`#toc a.toc-h4[data-parent-group="${gid}"]`).forEach(sub => {
              sub.classList.remove('toc-sub-hidden');
            });
          }
        }

        const tocRect = toc.getBoundingClientRect();
        const linkRect = activeLink.getBoundingClientRect();
        if (linkRect.top < tocRect.top || linkRect.bottom > tocRect.bottom) {
          activeLink.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        }
      }
    }
  }

  main.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => { updateScrollSpy(); ticking = false; });
      ticking = true;
    }
    backTop.classList.toggle('visible', main.scrollTop > 400);
  });

  // ===== 10. Back to top =====
  backTop.addEventListener('click', () => {
    main.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // ===== 11. Keyboard shortcuts =====
  document.addEventListener('keydown', (e) => {
    // Skip if typing in an input
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
      if (e.key === 'Escape') {
        e.target.blur();
        e.target.value = '';
        $$('#toc a').forEach(a => a.classList.remove('hidden'));
      }
      return;
    }

    switch (e.key) {
      case '/':
        e.preventDefault();
        searchInput && searchInput.focus();
        break;
      case 't':
      case 'T':
        toggleTheme();
        break;
      case 'Escape':
        sidebar.classList.remove('open');
        overlay.classList.remove('visible');
        break;
    }
  });

  // ===== 12. Handle hash on load =====
  if (window.location.hash) {
    const target = document.getElementById(window.location.hash.slice(1));
    if (target) {
      setTimeout(() => target.scrollIntoView({ behavior: 'smooth', block: 'start' }), 300);
    }
  }

  // Initial scroll spy
  updateScrollSpy();

})();
