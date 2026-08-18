import json
import base64
import os

# Load base64 assets
with open('assets/b64_assets.json', 'r') as f:
    b64_data = json.load(f)

navy_logo_b64 = b64_data.get('assets\\rivlet-logo-navy.png') or b64_data.get('assets/rivlet-logo-navy.png')
gold_logo_b64 = b64_data.get('assets\\rivlet-logo-gold.png') or b64_data.get('assets/rivlet-logo-gold.png')
white_logo_b64 = b64_data.get('assets\\rivlet-logo-white.png') or b64_data.get('assets/rivlet-logo-white.png')
wave_navy_b64 = b64_data.get('assets\\rivlet-wave-navy.png') or b64_data.get('assets/rivlet-wave-navy.png')
wave_gold_b64 = b64_data.get('assets\\rivlet-wave-gold.png') or b64_data.get('assets/rivlet-wave-gold.png')
wave_white_b64 = b64_data.get('assets\\rivlet-wave-white.png') or b64_data.get('assets/rivlet-wave-white.png')
wordmark_navy_b64 = b64_data.get('assets\\rivlet-wordmark-navy.png') or b64_data.get('assets/rivlet-wordmark-navy.png')
wordmark_gold_b64 = b64_data.get('assets\\rivlet-wordmark-gold.png') or b64_data.get('assets/rivlet-wordmark-gold.png')
wordmark_white_b64 = b64_data.get('assets\\rivlet-wordmark-white.png') or b64_data.get('assets/rivlet-wordmark-white.png')

html_content = f'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="x-apple-disable-message-reformatting" />
  <meta name="format-detection" content="telephone=no,address=no,email=no,date=no,url=no" />
  <title>Rivlet — Move like water. Feel like air.</title>

  <!-- Google Fonts: Inter, Cormorant Garamond, DM Mono -->
  <!--[if !mso]><!-->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,400;1,600&family=DM+Mono:wght@400;500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <!--<![endif]-->

  <style type="text/css">
    /* Client-specific Resets */
    body, table, td, a {{ -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }}
    table, td {{ mso-table-lspace: 0pt; mso-table-rspace: 0pt; }}
    img {{ -ms-interpolation-mode: bicubic; border: 0; outline: none; text-decoration: none; display: block; max-width: 100%; height: auto; }}
    body {{ margin: 0 !important; padding: 0 !important; width: 100% !important; background-color: #F6F4F0; -webkit-font-smoothing: antialiased; }}

    /* Link color overrides */
    a {{ color: inherit; text-decoration: none; }}
    a[x-apple-data-detectors] {{
      color: inherit !important;
      text-decoration: none !important;
      font-size: inherit !important;
      font-family: inherit !important;
      font-weight: inherit !important;
      line-height: inherit !important;
    }}

    /* Hover & Interactive Styles */
    .btn-primary:hover {{
      background-color: #D4A343 !important;
      border-color: #D4A343 !important;
    }}
    .nav-link:hover {{
      color: #C4963A !important;
    }}

    /* Responsive Mobile Styles */
    @media only screen and (max-width: 600px) {{
      .email-container {{ width: 100% !important; max-width: 100% !important; }}
      .mobile-padding {{ padding-left: 20px !important; padding-right: 20px !important; }}
      .mobile-padding-body {{ padding-left: 20px !important; padding-right: 20px !important; padding-top: 24px !important; padding-bottom: 24px !important; }}
      .mobile-stack {{ display: block !important; width: 100% !important; max-width: 100% !important; }}
      .mobile-center {{ text-align: center !important; }}
      .mobile-hide {{ display: none !important; }}
      .mobile-show {{ display: block !important; }}
      .mobile-gap {{ margin-top: 16px !important; }}
    }}
  </style>
</head>

<body style="margin: 0; padding: 0; background-color: #F6F4F0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #0C1E34;">

  <!-- PREHEADER SNIPPET (Preview in Gmail Inbox) -->
  <div style="display: none; font-size: 1px; line-height: 1px; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden; mso-hide: all; font-family: sans-serif;">
    Move like water. Feel like air. — Rivlet official communication.
    &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
  </div>

  <!-- MAIN OUTER TABLE -->
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #F6F4F0; width: 100%; margin: 0; padding: 28px 0 44px 0;">
    <tr>
      <td align="center" style="padding: 0 12px;">

        <!-- 600px EMAIL WRAPPER -->
        <!--[if (gte mso 9)|(IE)]>
        <table role="presentation" width="600" align="center" cellpadding="0" cellspacing="0" border="0">
        <tr>
        <td>
        <![endif]-->
        <table role="presentation" class="email-container" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; width: 100%; background-color: #FFFFFF; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(12, 30, 52, 0.06); border: 1px solid #EBE7DF;">

          <!-- TOP GOLD ACCENT BAR -->
          <tr>
            <td height="4" style="background: linear-gradient(90deg, #0C1E34 0%, #C4963A 50%, #E5BE6B 100%); line-height: 4px; font-size: 4px;">&nbsp;</td>
          </tr>

          <!-- HEADER: OFFICIAL RIVLET LOGO & LINKS -->
          <tr>
            <td style="background-color: #FFFFFF; padding: 28px 36px 24px 36px; border-bottom: 1px solid #F0ECE4;" class="mobile-padding">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <!-- Brand Logo (Wave Mark + Rivlet Wordmark) -->
                  <td align="left" valign="middle">
                    <a href="https://therivlet.com" target="_blank" style="text-decoration: none; display: inline-block;">
                      <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                        <tr>
                          <td valign="middle" style="padding-right: 12px;">
                            <img src="{wave_navy_b64}" alt="Rivlet Wave" width="34" height="21" style="display: block; width: 34px; height: 21px; border: 0;" />
                          </td>
                          <td valign="middle">
                            <img src="{wordmark_navy_b64}" alt="Rivlet" width="92" height="28" style="display: block; width: 92px; height: 28px; border: 0;" />
                          </td>
                        </tr>
                      </table>
                    </a>
                  </td>

                  <!-- Right Header Links -->
                  <td align="right" valign="middle" class="mobile-hide">
                    <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                      <tr>
                        <td style="padding-left: 16px;">
                          <a href="https://therivlet.com" target="_blank" class="nav-link" style="font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 600; color: #0C1E34; text-decoration: none; letter-spacing: 0.5px; text-transform: uppercase;">therivlet.com &rarr;</a>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- ======================================================== -->
          <!-- IN-BETWEEN CONTENT AREA (COMPOSE & EDIT HERE IN GMAIL)   -->
          <!-- ======================================================== -->
          <tr>
            <td style="background-color: #FFFFFF; padding: 36px 40px 40px 40px;" class="mobile-padding-body">
              
              <!-- Salutation / Greeting -->
              <p style="margin: 0 0 18px 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 16px; line-height: 26px; color: #0C1E34; font-weight: 600;">
                Dear [Recipient Name],
              </p>

              <!-- Main Body Paragraph 1 -->
              <p style="margin: 0 0 18px 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 15px; line-height: 26px; color: #2D3748;">
                Thank you for connecting with us. We are pleased to reach out regarding our latest updates, partnership inquiries, and the upcoming launch of our Indian-crafted activewear line.
              </p>

              <!-- Main Body Paragraph 2 -->
              <p style="margin: 0 0 20px 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 15px; line-height: 26px; color: #2D3748;">
                At <strong>Rivlet</strong>, every piece is engineered for daily motion, extreme heat, and humidity. From our proprietary zero-roll waistbands to sweat-adaptive fabric weaves, our mission is to redefine comfort with uncompromising elegance.
              </p>

              <!-- OPTIONAL CALLOUT / KEY HIGHLIGHT BOX -->
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 24px 0; background-color: #FAF9F6; border-left: 3px solid #C4963A; border-radius: 0 8px 8px 0;">
                <tr>
                  <td style="padding: 18px 22px;">
                    <p style="margin: 0 0 6px 0; font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 700; color: #7A5C3A; text-transform: uppercase; letter-spacing: 1px;">
                      ✦ Key Update / Note
                    </p>
                    <p style="margin: 0; font-family: 'Inter', sans-serif; font-size: 14px; line-height: 22px; color: #0C1E34;">
                      You can replace this callout block with meeting dates, quotation notes, action items, or important highlights.
                    </p>
                  </td>
                </tr>
              </table>

              <!-- Main Body Paragraph 3 -->
              <p style="margin: 0 0 24px 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 15px; line-height: 26px; color: #2D3748;">
                Please feel free to reply directly to this email if you have any questions, feedback, or would like to schedule a time to speak.
              </p>

              <!-- OPTIONAL CALL-TO-ACTION BUTTON (If needed) -->
              <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin: 28px 0 32px 0;">
                <tr>
                  <td align="center" style="background-color: #0C1E34; border-radius: 6px;">
                    <a href="https://therivlet.com" target="_blank" class="btn-primary" style="display: inline-block; padding: 12px 28px; font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 700; color: #FAF8F5; text-decoration: none; text-transform: uppercase; letter-spacing: 0.8px; border-radius: 6px; background-color: #0C1E34;">
                      Visit Official Website &nbsp;&rarr;
                    </a>
                  </td>
                </tr>
              </table>

              <!-- Sign-off -->
              <p style="margin: 28px 0 0 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 15px; line-height: 24px; color: #2D3748;">
                Warm regards,<br />
                <strong style="color: #0C1E34; font-size: 16px;">The Rivlet Team</strong><br />
                <span style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 16px; font-style: italic; color: #7A5C3A;">“Move like water. Feel like air.”</span>
              </p>

            </td>
          </tr>

          <!-- ======================================================== -->
          <!-- FOOTER: BRANDING, SOCIAL LINKS & OFFICIAL INFO          -->
          <!-- ======================================================== -->
          <tr>
            <td style="background-color: #081422; padding: 36px 36px 30px 36px; text-align: center; border-top: 1px solid #1A283B;" class="mobile-padding">
              
              <!-- Footer Logo (White Wave + Wordmark) -->
              <table role="presentation" align="center" cellpadding="0" cellspacing="0" border="0" style="margin: 0 auto 14px auto;">
                <tr>
                  <td valign="middle" style="padding-right: 10px;">
                    <img src="{wave_white_b64}" alt="Rivlet Wave" width="28" height="17" style="display: block; width: 28px; height: 17px; border: 0;" />
                  </td>
                  <td valign="middle">
                    <img src="{wordmark_white_b64}" alt="Rivlet" width="76" height="23" style="display: block; width: 76px; height: 23px; border: 0;" />
                  </td>
                </tr>
              </table>

              <!-- Brand Slogan & Subtitle -->
              <p style="margin: 0 0 6px 0; font-family: 'Cormorant Garamond', Georgia, serif; font-size: 16px; font-style: italic; color: #E5BE6B; letter-spacing: 0.5px;">
                Move like water. Feel like air.
              </p>
              <p style="margin: 0 0 20px 0; font-family: 'Inter', sans-serif; font-size: 12px; color: #8C9BAE; line-height: 18px;">
                Indian-Crafted Activewear & Easy Wear &nbsp;·&nbsp; Born in Madurai, Tamil Nadu
              </p>

              <!-- Social Links & Navigation -->
              <table role="presentation" align="center" cellpadding="0" cellspacing="0" border="0" style="margin: 0 auto 22px auto;">
                <tr>
                  <td style="padding: 0 10px;">
                    <a href="https://therivlet.com" target="_blank" style="font-family: 'Inter', sans-serif; font-size: 12px; color: #C4963A; text-decoration: none; font-weight: 500;">Official Website</a>
                  </td>
                  <td style="color: #4A5568; font-size: 12px;">·</td>
                  <td style="padding: 0 10px;">
                    <a href="https://www.instagram.com/rivletindia/" target="_blank" style="font-family: 'Inter', sans-serif; font-size: 12px; color: #C4963A; text-decoration: none; font-weight: 500;">Instagram</a>
                  </td>
                  <td style="color: #4A5568; font-size: 12px;">·</td>
                  <td style="padding: 0 10px;">
                    <a href="https://www.linkedin.com/company/rivlet/" target="_blank" style="font-family: 'Inter', sans-serif; font-size: 12px; color: #C4963A; text-decoration: none; font-weight: 500;">LinkedIn</a>
                  </td>
                  <td style="color: #4A5568; font-size: 12px;">·</td>
                  <td style="padding: 0 10px;">
                    <a href="https://rivlet-ecom-prototype.vercel.app/" target="_blank" style="font-family: 'Inter', sans-serif; font-size: 12px; color: #C4963A; text-decoration: none; font-weight: 500;">E-Com Prototype</a>
                  </td>
                </tr>
              </table>

              <!-- Divider -->
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 18px;">
                <tr>
                  <td style="border-top: 1px solid #1A283B; font-size: 1px; line-height: 1px;">&nbsp;</td>
                </tr>
              </table>

              <!-- Contact, Location & Disclaimer -->
              <p style="margin: 0 0 6px 0; font-family: 'Inter', sans-serif; font-size: 11px; line-height: 16px; color: #64748B;">
                Rivlet Activewear & Apparel, Madurai, Tamil Nadu 625001, India &nbsp;·&nbsp; <a href="mailto:hello@therivlet.com" style="color: #8C9BAE; text-decoration: underline;">hello@therivlet.com</a>
              </p>
              <p style="margin: 0; font-family: 'Inter', sans-serif; font-size: 11px; line-height: 16px; color: #4B5563;">
                &copy; 2026 Rivlet. All rights reserved. &nbsp;·&nbsp;
                <a href="https://therivlet.com" target="_blank" style="color: #64748B; text-decoration: none;">Privacy Policy</a> &nbsp;·&nbsp;
                <a href="https://therivlet.com" target="_blank" style="color: #64748B; text-decoration: none;">Preferences</a>
              </p>

            </td>
          </tr>

        </table>
        <!--[if (gte mso 9)|(IE)]>
        </td>
        </tr>
        </table>
        <![endif]-->

      </td>
    </tr>
  </table>

</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Successfully generated index.html!')
