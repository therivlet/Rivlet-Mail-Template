# Rivlet — General Email Templates & Brand Assets

> **“Move like water. Feel like air.”**  
> Premium Indian-crafted activewear, sportswear, athleisure, and easy wear engineered for heat, humidity, and daily motion. Tamil Nadu, India. Launching 2026.

This repository contains official, responsive, table-based HTML email templates for **Rivlet**, specifically structured for **Gmail Compose** workflow with a branded **Header**, **In-between editable content area**, and comprehensive **Footer**.

---

## 📁 Repository Structure

```text
Rivlet-Mail-Template/
├── index.html                    # Master General Template (Modern Luxury Light)
├── general-template-light.html    # Variant A: Modern Luxury Light (White Header + Navy Footer)
├── general-template-navy.html     # Variant B: Iconic Midnight Navy Header
├── general-template-minimal.html  # Variant C: Minimalist Clean Signature
├── preview.html                  # Interactive Browser Preview & 1-Click Copy Tool
├── assets/                       # Official Vector SVGs & High-Res PNG Assets
│   ├── rivlet-wave-logo.svg      # Vector Wave Icon
│   ├── rivlet-wordmark.svg       # Vector Rivlet Wordmark
│   ├── rivlet-logo-lockup.svg    # Vector Combined Lockup (Wave + Wordmark)
│   ├── rivlet-logo-navy.png      # High-res Navy Lockup (3x)
│   ├── rivlet-logo-gold.png      # High-res Cardamom Gold Lockup (3x)
│   ├── rivlet-logo-white.png     # High-res White Lockup (3x)
│   ├── rivlet-wave-navy.png      # Navy Wave Icon
│   ├── rivlet-wave-gold.png      # Gold Wave Icon
│   ├── rivlet-wave-white.png     # White Wave Icon
│   ├── rivlet-wordmark-navy.png  # Navy Wordmark
│   ├── rivlet-wordmark-gold.png  # Gold Wordmark
│   └── rivlet-wordmark-white.png # White Wordmark
└── scripts/                      # Asset & Template Generation Build Utilities
```

---

## 🚀 How to Use in Gmail (Fastest Method)

### Method 1: Using the 1-Click Preview Helper (`preview.html`)
1. Open [`preview.html`](file:///c:/Users/thari/.gemini/antigravity-ide/scratch/Rivlet-Mail-Template/preview.html) in your web browser (Chrome, Edge, Safari, Brave).
2. Choose your preferred style (**Modern Light**, **Iconic Navy**, or **Minimal**).
3. Click the golden **“📋 Copy for Gmail Compose”** button at the top right.
4. Open [Gmail](https://mail.google.com) and click **Compose**.
5. Click inside the email body and press **Ctrl + V** (`Cmd + V` on Mac).
6. Click into the body text to type or edit your custom message directly in Gmail!

### Method 2: Standard Browser Copy
1. Double-click [`index.html`](file:///c:/Users/thari/.gemini/antigravity-ide/scratch/Rivlet-Mail-Template/index.html) to open in your browser.
2. Press **Ctrl + A** (`Cmd + A`) to select all rendered content.
3. Press **Ctrl + C** (`Cmd + C`) to copy.
4. Go to **Gmail Compose** & press **Ctrl + V** (`Cmd + V`) to paste.
5. Edit your text in Gmail.

---

## 💾 How to Save as a Permanent Gmail Template

Once pasted into Gmail compose, you can save it so you never have to copy/paste again:

1. In the Gmail compose window, click the **⋮ (More options / three dots)** icon in the bottom-right toolbar.
2. Hover over **Templates** → **Save draft as template** → **Save as new template**.
3. Name it **`Rivlet — Official General Template`**.
4. To compose future emails: Click **⋮** → **Templates** → **`Rivlet — Official General Template`**. The header, footer, and editable content will load instantly!

---

## 🎨 Brand Design Tokens

| Token | Value | Description |
| :--- | :--- | :--- |
| **Primary Theme Color** | `#0C1E34` | Deep Midnight Navy |
| **Secondary Dark** | `#081422` | Deep Obsidian / Footer Base |
| **Accent & Highlight** | `#C4963A` | Cardamom Gold |
| **Light Gold Accent** | `#E5BE6B` | Warm Sun Amber |
| **Bronze Accent** | `#7A5C3A` | Cardamom Bronze / Earth |
| **Background Sand** | `#F6F4F0` / `#FAF9F6` | Warm Coastal Sand |
| **Text Primary** | `#0C1E34` / `#1F2937` | High-contrast readable dark slate |
| **Typography (Headings)** | *Cormorant Garamond* | Editorial serif luxury font |
| **Typography (Body & UI)**| *Inter* | Crisp modern sans-serif |

---

## 🌓 Perfect Centering & Graphic Wordmark

* **Dead-Center Gmail Alignment**: Engineered with `<center>` table architecture, `margin: 0 auto !important`, and nested table centering so that when pasted into Gmail Compose or viewed on widescreen monitors, the email card is positioned **dead center** in the reading pane rather than skewed to the left.
* **Graphic Wordmark & Logo Images**: Uses official high-res graphic wordmark and wave logo images hosted on high-availability HTTPS CDN so they load immediately without being stripped by Gmail.
* **Always-Right Header Navigation**: The `THERIVLET.COM →` link in the header is locked to the right margin on both desktop and mobile screens.
* **Client Compatibility**: Built with table-based structure and inline CSS tested for Gmail (Web, iOS, Android), Apple Mail, Microsoft Outlook, Yahoo Mail, and mobile screens.

---

## 🌐 Official References

* **Official Website**: [therivlet.com](https://therivlet.com)
* **Instagram**: [@rivletindia](https://www.instagram.com/rivletindia/)
* **LinkedIn**: [Rivlet](https://www.linkedin.com/company/rivlet/)
* **Contact**: [hello@therivlet.com](mailto:hello@therivlet.com)
