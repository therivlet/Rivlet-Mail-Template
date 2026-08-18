# Rivlet — Email Templates

> **“Move like water. Feel like air.”**  
> Premium Indian-crafted activewear, sportswear, athleisure, and easy wear engineered for heat, humidity, and daily motion. Born in Madurai. Launching 2026.

This repository contains official, responsive, table-based HTML email templates for **Rivlet**, designed for high deliverability, Gmail compose compatibility, and mobile responsiveness.

---

## 📁 Repository Structure

```text
Rivlet-Mail-Template/
├── index.html        # Main branded HTML email template (table-based + inline CSS)
└── README.md         # Documentation, brand specs & usage guide
```

---

## 🎨 Brand Design Specifications

| Element | Specification |
| :--- | :--- |
| **Primary Theme Color** | `#0C1E34` (Deep Midnight Navy) |
| **Accent & Highlight** | `#C4963A` / `#E5BE6B` (Cardamom Gold / Amber) |
| **Secondary Accent** | `#7A5C3A` (Cardamom Bronze / Earth) |
| **Background Tint** | `#F6F4F0` / `#FAF9F6` (Clean Warm Sand) |
| **Surface White** | `#FFFFFF` |
| **Text Primary** | `#0C1E34` / `#1F2937` |
| **Editorial Typography** | *Cormorant Garamond* (Google Fonts serif) |
| **UI & Body Typography** | *Inter* (Google Fonts sans-serif) |
| **Technical Specs Font** | *DM Mono* (Google Fonts monospace) |

---

## 🚀 How to Use in Gmail (Copy & Paste Method)

Gmail does not have a native “Upload HTML file” button. Follow this workflow:

1. **Open `index.html` in your browser**:
   * Double-click `index.html` or drag it into Chrome, Edge, or Safari.
2. **Select & Copy the rendered email**:
   * Press `Ctrl + A` (or `Cmd + A` on Mac) to select all rendered content.
   * Press `Ctrl + C` (or `Cmd + C` on Mac) to copy.
3. **Paste into Gmail Compose**:
   * Open Gmail and click **Compose**.
   * Click inside the email body and press `Ctrl + V` (`Cmd + V`).
   * Gmail will preserve the layout, styling, fonts, buttons, and colors.
4. **Save as a Gmail Template**:
   * Click **⋮ (More options)** at the bottom-right of the compose toolbar.
   * Navigate to **Templates** → **Save draft as template** → **Save as new template**.
   * Name it `Rivlet — Early Access & Launch Edit`.

---

## 🏷️ Dynamic Personalization Fields

The template includes placeholder variables compatible with standard ESPs (Mailchimp, Klaviyo, Sendgrid, Brevo):

* `{{First Name | default: 'there'}}` — Recipient first name
* `RIVLETFIRST` — 15% VIP early-access launch promo code

---

## 🌐 Official References

* **Official Website**: [therivlet.com](https://therivlet.com)
* **Design & E-commerce Prototype**: [rivlet-ecom-prototype.vercel.app](https://rivlet-ecom-prototype.vercel.app)
* **Instagram**: [@rivletindia](https://www.instagram.com/rivletindia/)
* **Contact**: [hello@therivlet.com](mailto:hello@therivlet.com)
