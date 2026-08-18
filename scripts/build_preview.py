preview_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Rivlet — Elite Email Template Suite & Gmail Helper</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,400&family=Inter:wght@400;500;600;700;800&family=DM+Mono:wght@500&display=swap" rel="stylesheet" />
  <style>
    :root {
      --bg-dark: #081422;
      --navy: #0C1E34;
      --navy-light: #173252;
      --gold: #C4963A;
      --gold-light: #E5BE6B;
      --sand: #F6F4F0;
      --card-bg: #FFFFFF;
      --text: #1F2937;
      --text-muted: #64748B;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-dark);
      color: #FAF8F5;
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    header {
      background: rgba(12, 30, 52, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(196, 150, 58, 0.3);
      padding: 16px 32px;
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .brand-title {
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 22px;
      font-weight: 600;
      letter-spacing: 2px;
      color: #FAF8F5;
      text-transform: uppercase;
    }

    .brand-tag {
      font-family: 'DM Mono', monospace;
      font-size: 11px;
      color: var(--gold-light);
      background: rgba(196, 150, 58, 0.15);
      border: 1px solid rgba(196, 150, 58, 0.35);
      padding: 4px 10px;
      border-radius: 20px;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .action-buttons {
      display: flex;
      gap: 10px;
      align-items: center;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 20px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s ease;
      font-family: 'Inter', sans-serif;
    }

    .btn-gold {
      background: var(--gold);
      color: #0C1E34;
      border: 1px solid var(--gold-light);
    }

    .btn-gold:hover {
      background: var(--gold-light);
      box-shadow: 0 0 15px rgba(196, 150, 58, 0.4);
    }

    .btn-outline {
      background: transparent;
      color: #FAF8F5;
      border: 1px solid #334155;
    }

    .btn-outline:hover {
      background: #1E293B;
      border-color: #475569;
    }

    /* Template Category Navigation */
    .template-selector-bar {
      background: #0B192C;
      border-bottom: 1px solid #1E2E44;
      padding: 10px 32px;
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      white-space: nowrap;
    }

    .selector-label {
      font-family: 'DM Mono', monospace;
      font-size: 11px;
      color: #718096;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-right: 8px;
    }

    .tab-btn {
      background: #081422;
      border: 1px solid #1E2E44;
      color: #94A3B8;
      padding: 8px 14px;
      font-size: 12px;
      font-weight: 600;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: 'Inter', sans-serif;
      white-space: nowrap;
    }

    .tab-btn:hover {
      color: #FAF8F5;
      border-color: #475569;
    }

    .tab-btn.active {
      background: var(--navy-light);
      color: var(--gold-light);
      border-color: rgba(196, 150, 58, 0.6);
      font-weight: 700;
    }

    .main-container {
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 28px;
      padding: 28px 32px 40px 32px;
      max-width: 1340px;
      margin: 0 auto;
      width: 100%;
      flex: 1;
    }

    @media (max-width: 992px) {
      .main-container {
        grid-template-columns: 1fr;
        padding: 20px 16px;
      }
      .template-selector-bar {
        padding: 10px 16px;
      }
    }

    .preview-card {
      background: #0E1F36;
      border: 1px solid #1E2E44;
      border-radius: 12px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    .preview-header {
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid #1E2E44;
      flex-wrap: wrap;
      gap: 10px;
    }

    .preview-title {
      font-size: 15px;
      font-weight: 700;
      color: #E2E8F0;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .iframe-wrapper {
      width: 100%;
      background: var(--sand);
      border-radius: 8px;
      padding: 20px 0;
      display: flex;
      justify-content: center;
      border: 1px solid #334155;
    }

    iframe {
      width: 100%;
      height: 800px;
      border: none;
      background: transparent;
    }

    .sidebar {
      display: flex;
      flex-direction: column;
      gap: 18px;
    }

    .side-card {
      background: #0E1F36;
      border: 1px solid #1E2E44;
      border-radius: 12px;
      padding: 18px;
    }

    .side-title {
      font-size: 13px;
      font-weight: 700;
      color: var(--gold-light);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .steps-list {
      list-style: none;
      counter-reset: step-counter;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .steps-list li {
      counter-increment: step-counter;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 13px;
      color: #CBD5E1;
      line-height: 1.5;
    }

    .steps-list li::before {
      content: counter(step-counter);
      background: var(--gold);
      color: #0C1E34;
      font-weight: 700;
      font-size: 11px;
      min-width: 18px;
      height: 18px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-top: 2px;
      flex-shrink: 0;
    }

    .asset-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 10px;
      background: #081422;
      border: 1px solid #1E2E44;
      border-radius: 6px;
      margin-bottom: 6px;
    }

    .asset-name {
      font-family: 'DM Mono', monospace;
      font-size: 11px;
      color: #94A3B8;
    }

    .asset-link {
      font-size: 11px;
      color: var(--gold-light);
      text-decoration: none;
      font-weight: 600;
    }

    .asset-link:hover {
      text-decoration: underline;
    }

    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--gold);
      color: #0C1E34;
      padding: 12px 24px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 14px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.4);
      display: none;
      animation: slideUp 0.3s ease;
      z-index: 1000;
    }

    @keyframes slideUp {
      from { transform: translateY(20px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
  </style>
</head>
<body>

  <header>
    <div class="brand">
      <div class="brand-title">RIVLET</div>
      <div class="brand-tag">Elite Template Suite</div>
    </div>

    <div class="action-buttons">
      <button class="btn btn-gold" onclick="copyRenderedTemplate()">
        📋 Copy for Gmail Compose
      </button>
      <button class="btn btn-outline" onclick="openRaw()">
        ↗ Open File
      </button>
    </div>
  </header>

  <!-- OCCASION SELECTOR BAR -->
  <div class="template-selector-bar">
    <span class="selector-label">Templates:</span>
    <button class="tab-btn active" onclick="switchTemplate('general-template-light.html', this)">🌟 General (Master)</button>
    <button class="tab-btn" onclick="switchTemplate('occasion-manufacturer-outreach.html', this)">🏭 Manufacturer Outreach & Tech Specs</button>
    <button class="tab-btn" onclick="switchTemplate('occasion-reply-thread.html', this)">💬 Fast Reply (Ongoing Thread)</button>
    <button class="tab-btn" onclick="switchTemplate('occasion-vip-launch.html', this)">🚀 VIP Early Access / Drop</button>
    <button class="tab-btn" onclick="switchTemplate('occasion-founder-letter.html', this)">✍️ Founder’s Vision Letter</button>
    <button class="tab-btn" onclick="switchTemplate('occasion-b2b-partnership.html', this)">🤝 B2B & Partnership</button>
    <button class="tab-btn" onclick="switchTemplate('occasion-order-concierge.html', this)">📦 Order Concierge</button>
    <button class="tab-btn" onclick="switchTemplate('occasion-event-invite.html', this)">🏃 Run Club & Event Invite</button>
    <button class="tab-btn" onclick="switchTemplate('general-template-navy.html', this)">🌌 Iconic Navy</button>
    <button class="tab-btn" onclick="switchTemplate('general-template-minimal.html', this)">📄 Minimal Signature</button>
  </div>

  <div class="main-container">
    <div class="preview-card">
      <div class="preview-header">
        <div class="preview-title" id="currentTitle">
          ✦ General Master Template (Centered · Graphic Wordmark & Logo)
        </div>
        <div style="font-size: 12px; color: #94A3B8;">
          Graphic Wordmark · Centered in Gmail · Mobile Optimized
        </div>
      </div>
      <div class="iframe-wrapper">
        <iframe id="previewFrame" src="general-template-light.html"></iframe>
      </div>
    </div>

    <div class="sidebar">
      <div class="side-card">
        <div class="side-title">⚡ Gmail Quick Start</div>
        <ol class="steps-list">
          <li>Select your desired occasion template from the top bar.</li>
          <li>Click the golden <strong>“Copy for Gmail Compose”</strong> button.</li>
          <li>Open Gmail and click <strong>Compose</strong>.</li>
          <li>Click into the email body and press <strong>Ctrl + V</strong> (Cmd + V on Mac).</li>
          <li>Edit your message, technical specs, or payment terms directly in Gmail!</li>
        </ol>
      </div>

      <div class="side-card">
        <div class="side-title">✨ Template Occasions</div>
        <div style="font-size: 12px; color: #CBD5E1; line-height: 1.6;">
          • <strong>Manufacturer Outreach</strong>: Technical discussion, fabric specs, payment & attachments.<br />
          • <strong>Fast Reply Thread</strong>: Ultra-clean minimal ongoing thread response.<br />
          • <strong>VIP Launch</strong>: Exclusive early access & drop codes.<br />
          • <strong>Founder's Letter</strong>: High-touch personal vision & milestones.<br />
          • <strong>B2B & Collab</strong>: Retailer, studio & athlete outreach.<br />
          • <strong>Order Concierge</strong>: Luxe transactional care.<br />
          • <strong>Run Club / Event</strong>: Community motion sessions.
        </div>
      </div>

      <div class="side-card">
        <div class="side-title">📁 Brand Assets Hub</div>
        <div class="asset-item">
          <span class="asset-name">rivlet-logo-lockup.svg</span>
          <a class="asset-link" href="assets/rivlet-logo-lockup.svg" download>Download</a>
        </div>
        <div class="asset-item">
          <span class="asset-name">rivlet-wave-logo.svg</span>
          <a class="asset-link" href="assets/rivlet-wave-logo.svg" download>Download</a>
        </div>
        <div class="asset-item">
          <span class="asset-name">rivlet-wordmark.svg</span>
          <a class="asset-link" href="assets/rivlet-wordmark.svg" download>Download</a>
        </div>
        <div class="asset-item">
          <span class="asset-name">rivlet-logo-navy.png (3x)</span>
          <a class="asset-link" href="assets/rivlet-logo-navy.png" download>Download</a>
        </div>
        <div class="asset-item">
          <span class="asset-name">rivlet-logo-gold.png (3x)</span>
          <a class="asset-link" href="assets/rivlet-logo-gold.png" download>Download</a>
        </div>
      </div>
    </div>
  </div>

  <div class="toast" id="toast">
    ✓ Template copied! Switch to Gmail & paste (Ctrl+V)
  </div>

  <script>
    let currentSrc = 'general-template-light.html';

    const titles = {
      'general-template-light.html': '✦ General Master Template (Modern Luxury Light)',
      'occasion-manufacturer-outreach.html': '✦ Manufacturer Outreach, Technical Specs & Commercial Payment Terms',
      'occasion-reply-thread.html': '✦ Minimal Quick Reply & Continuous Ongoing Thread Template',
      'occasion-vip-launch.html': '✦ VIP Early Access & Product Drop Invitation',
      'occasion-founder-letter.html': '✦ Founder’s Personal Vision & Milestone Dispatch',
      'occasion-b2b-partnership.html': '✦ B2B Partnership, Stockist & Creator Collaboration',
      'occasion-order-concierge.html': '✦ Order Confirmation & Luxe Customer Concierge',
      'occasion-event-invite.html': '✦ Motion Circle & Community Run Club Invitation',
      'general-template-navy.html': '✦ Variant B: Iconic Deep Midnight Navy Header',
      'general-template-minimal.html': '✦ Variant C: Minimalist Clean Signature'
    };

    function switchTemplate(file, btn) {
      currentSrc = file;
      const iframe = document.getElementById('previewFrame');
      iframe.src = file;
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById('currentTitle').innerText = titles[file] || file;
    }

    function openRaw() {
      window.open(currentSrc, '_blank');
    }

    async function copyRenderedTemplate() {
      const iframe = document.getElementById('previewFrame');
      try {
        const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
        const html = iframeDoc.documentElement.outerHTML;
        
        const blobHtml = new Blob([html], { type: 'text/html' });
        const blobText = new Blob([iframeDoc.body.innerText], { type: 'text/plain' });
        
        const data = [new ClipboardItem({
          'text/html': blobHtml,
          'text/plain': blobText
        })];
        
        await navigator.clipboard.write(data);
        showToast('✓ Template copied! Switch to Gmail & paste (Ctrl+V)');
      } catch (e) {
        try {
          const iframeWindow = iframe.contentWindow;
          const iframeDoc = iframe.contentDocument;
          iframeWindow.focus();
          const range = iframeDoc.createRange();
          range.selectNodeContents(iframeDoc.body);
          const sel = iframeWindow.getSelection();
          sel.removeAllRanges();
          sel.addRange(range);
          iframeDoc.execCommand('copy');
          sel.removeAllRanges();
          showToast('✓ Copied template to clipboard!');
        } catch (err) {
          window.open(currentSrc, '_blank');
          showToast('Opened in new tab: Press Ctrl+A then Ctrl+C to copy!');
        }
      }
    }

    function showToast(msg) {
      const toast = document.getElementById('toast');
      toast.innerText = msg;
      toast.style.display = 'block';
      setTimeout(() => { toast.style.display = 'none'; }, 4000);
    }
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(preview_html)

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(preview_html)

print('Updated preview dashboard (index.html & preview.html) with all 10 templates!')
