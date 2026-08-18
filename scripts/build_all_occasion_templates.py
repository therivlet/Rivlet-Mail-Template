import os

wave_navy = "https://files.catbox.moe/61pie8.png"
wave_white = "https://files.catbox.moe/0tko2b.png"
wave_gold = "https://files.catbox.moe/effuy6.png"

wordmark_navy = "https://files.catbox.moe/sqptty.png"
wordmark_white = "https://files.catbox.moe/w0wucy.png"
wordmark_gold = "https://files.catbox.moe/fyiiwn.png"

# Common base CSS
base_css = '''
    :root { color-scheme: light dark; supported-color-schemes: light dark; }
    body, table, td, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
    table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
    img { -ms-interpolation-mode: bicubic; border: 0; outline: none; text-decoration: none; display: block; max-width: 100%; height: auto; }
    body { margin: 0 !important; padding: 0 !important; width: 100% !important; background-color: #F6F4F0; -webkit-font-smoothing: antialiased; text-align: center; }
    a { color: inherit; text-decoration: none; }
    .btn-gold:hover { background-color: #D4A343 !important; }
    .btn-navy:hover { background-color: #173252 !important; }
    .nav-link:hover { color: #C4963A !important; }
    @media only screen and (max-width: 600px) {
      .email-container { width: 100% !important; max-width: 100% !important; }
      .mobile-padding { padding-left: 16px !important; padding-right: 16px !important; }
      .mobile-padding-body { padding-left: 20px !important; padding-right: 20px !important; padding-top: 24px !important; padding-bottom: 24px !important; }
      .mobile-stack { display: block !important; width: 100% !important; max-width: 100% !important; }
      .mobile-stack-gap { padding-bottom: 16px !important; }
      .header-right { text-align: right !important; }
    }
    @media (prefers-color-scheme: dark) {
      body, .dark-bg-outer { background-color: #081422 !important; }
      .dark-bg-card { background-color: #0C1E34 !important; border-color: #1E2E44 !important; }
      .dark-bg-header { background-color: #081422 !important; border-bottom-color: #1E2E44 !important; }
      .dark-text-primary { color: #FAF8F5 !important; }
      .dark-text-secondary { color: #CBD5E1 !important; }
      .dark-callout { background-color: #11253E !important; border-left-color: #E5BE6B !important; }
      .dark-callout-text { color: #E2E8F0 !important; }
      .dark-footer { background-color: #050D17 !important; border-top-color: #1E2E44 !important; }
    }
'''

# Standard Footer Component
def get_footer():
    return f'''
            <!-- FOOTER -->
            <tr>
              <td class="dark-footer mobile-padding" style="background-color: #081422; padding: 36px 36px 30px 36px; text-align: center; border-top: 1px solid #1A283B;">
                <table role="presentation" align="center" cellpadding="0" cellspacing="0" border="0" style="margin: 0 auto 14px auto;">
                  <tr>
                    <td valign="middle" style="padding-right: 10px; vertical-align: middle;">
                      <img src="{wave_white}" alt="Rivlet Wave" width="28" height="17" style="display: block; width: 28px; height: 17px; border: 0;" />
                    </td>
                    <td valign="middle" style="vertical-align: middle;">
                      <img src="{wordmark_white}" alt="Rivlet" width="76" height="23" style="display: block; width: 76px; height: 23px; border: 0;" />
                    </td>
                  </tr>
                </table>
                <p style="margin: 0 0 6px 0; font-family: 'Cormorant Garamond', Georgia, serif; font-size: 16px; font-style: italic; color: #E5BE6B; letter-spacing: 0.5px;">
                  Move like water. Feel like air.
                </p>
                <p style="margin: 0 0 20px 0; font-family: 'Inter', sans-serif; font-size: 12px; color: #8C9BAE; line-height: 18px;">
                  Indian-Crafted Activewear & Easy Wear &nbsp;·&nbsp; Tamil Nadu, India
                </p>
                <table role="presentation" align="center" cellpadding="0" cellspacing="0" border="0" style="margin: 0 auto 22px auto;">
                  <tr>
                    <td style="padding: 0 10px;"><a href="https://therivlet.com" target="_blank" style="font-family: 'Inter', sans-serif; font-size: 12px; color: #C4963A; text-decoration: none; font-weight: 500;">Official Website</a></td>
                    <td style="color: #4A5568; font-size: 12px;">·</td>
                    <td style="padding: 0 10px;"><a href="https://www.instagram.com/rivletindia/" target="_blank" style="font-family: 'Inter', sans-serif; font-size: 12px; color: #C4963A; text-decoration: none; font-weight: 500;">Instagram</a></td>
                    <td style="color: #4A5568; font-size: 12px;">·</td>
                    <td style="padding: 0 10px;"><a href="https://www.linkedin.com/company/rivlet/" target="_blank" style="font-family: 'Inter', sans-serif; font-size: 12px; color: #C4963A; text-decoration: none; font-weight: 500;">LinkedIn</a></td>
                    <td style="color: #4A5568; font-size: 12px;">·</td>
                    <td style="padding: 0 10px;"><a href="mailto:hello@therivlet.com" style="font-family: 'Inter', sans-serif; font-size: 12px; color: #C4963A; text-decoration: none; font-weight: 500;">Contact</a></td>
                  </tr>
                </table>
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 18px;">
                  <tr><td style="border-top: 1px solid #1A283B; font-size: 1px; line-height: 1px;">&nbsp;</td></tr>
                </table>
                <p style="margin: 0 0 6px 0; font-family: 'Inter', sans-serif; font-size: 11px; line-height: 16px; color: #64748B;">
                  Rivlet Activewear & Apparel, Tamil Nadu, India &nbsp;·&nbsp; <a href="mailto:hello@therivlet.com" style="color: #8C9BAE; text-decoration: underline;">hello@therivlet.com</a>
                </p>
                <p style="margin: 0; font-family: 'Inter', sans-serif; font-size: 11px; line-height: 16px; color: #4B5563;">
                  &copy; 2026 Rivlet. All rights reserved. &nbsp;·&nbsp; <a href="https://therivlet.com" target="_blank" style="color: #64748B; text-decoration: none;">Privacy Policy</a> &nbsp;·&nbsp; <a href="https://therivlet.com" target="_blank" style="color: #64748B; text-decoration: none;">Preferences</a>
                </p>
              </td>
            </tr>
    '''

# 1. VIP LAUNCH & EXCLUSIVE DROP TEMPLATE
vip_launch = f'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Rivlet — VIP Early Access Invitation</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,400;1,600&family=DM+Mono:wght@500;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style type="text/css">{base_css}</style>
</head>
<body class="dark-bg-outer">
  <center class="dark-bg-outer" style="width: 100%; background-color: #F6F4F0; text-align: center;">
    <table role="presentation" align="center" width="100%" cellpadding="0" cellspacing="0" border="0" class="dark-bg-outer" style="margin: 0 auto; width: 100%; border-collapse: collapse; background-color: #F6F4F0;">
      <tr>
        <td align="center" valign="top" style="padding: 28px 12px 44px 12px;">
          <table role="presentation" align="center" width="600" cellpadding="0" cellspacing="0" border="0" class="email-container dark-bg-card" style="max-width: 600px; width: 100%; margin: 0 auto !important; margin-left: auto !important; margin-right: auto !important; border-collapse: separate; text-align: left; background-color: #FFFFFF; border-radius: 12px; overflow: hidden; border: 1px solid #EBE7DF; box-shadow: 0 4px 20px rgba(12, 30, 52, 0.06);">
            
            <tr><td height="4" style="background: linear-gradient(90deg, #0C1E34 0%, #C4963A 50%, #E5BE6B 100%); line-height: 4px; font-size: 4px;">&nbsp;</td></tr>
            
            <!-- HEADER -->
            <tr>
              <td class="dark-bg-header mobile-padding" style="background-color: #FFFFFF; padding: 24px 32px 20px 32px; border-bottom: 1px solid #F0ECE4;">
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width: 100%; border-collapse: collapse;">
                  <tr>
                    <td align="left" valign="middle" style="text-align: left; vertical-align: middle; padding: 0;">
                      <a href="https://therivlet.com" target="_blank" style="text-decoration: none; display: inline-block;">
                        <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                          <tr>
                            <td valign="middle" style="padding-right: 12px; vertical-align: middle;">
                              <img src="{wave_navy}" alt="Rivlet Wave" width="34" height="21" style="display: block; width: 34px; height: 21px; border: 0;" />
                            </td>
                            <td valign="middle" style="vertical-align: middle;">
                              <img src="{wordmark_navy}" alt="Rivlet" width="92" height="28" style="display: block; width: 92px; height: 28px; border: 0;" />
                            </td>
                          </tr>
                        </table>
                      </a>
                    </td>
                    <td align="right" valign="middle" class="header-right" style="text-align: right !important; vertical-align: middle; white-space: nowrap; padding: 0 0 0 10px;">
                      <a href="https://therivlet.com" target="_blank" class="nav-link dark-text-primary" style="font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 700; color: #0C1E34; text-decoration: none; letter-spacing: 0.5px; text-transform: uppercase;">
                        THERIVLET.COM &rarr;
                      </a>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

            <!-- HERO EDITORIAL BANNER -->
            <tr>
              <td style="background-color: #0C1E34; padding: 36px 36px 32px 36px; text-align: center; background: radial-gradient(circle at 50% 0%, #173252 0%, #0C1E34 100%);" class="mobile-padding">
                <table role="presentation" align="center" cellpadding="0" cellspacing="0" border="0" style="margin: 0 auto 16px auto;">
                  <tr>
                    <td style="background-color: rgba(196, 150, 58, 0.15); border: 1px solid rgba(196, 150, 58, 0.45); border-radius: 20px; padding: 5px 14px; text-align: center;">
                      <span style="font-family: 'DM Mono', monospace; font-size: 11px; font-weight: 700; color: #E5BE6B; letter-spacing: 1.5px; text-transform: uppercase;">
                        ✦ PRIVATE VIP ACCESS · DROP NO. 01
                      </span>
                    </td>
                  </tr>
                </table>
                <h1 style="margin: 0 0 12px 0; font-family: 'Cormorant Garamond', Georgia, serif; font-size: 32px; line-height: 38px; color: #FAF8F5; font-weight: 600;">
                  Engineered for Heat.<br /><span style="font-style: italic; color: #E5BE6B;">Tailored for Daily Motion.</span>
                </h1>
                <p style="margin: 0 auto; max-width: 440px; font-family: 'Inter', sans-serif; font-size: 14px; line-height: 22px; color: #94A3B8;">
                  You are among the first invited to explore Rivlet's inaugural capsule collection before public release.
                </p>
              </td>
            </tr>

            <!-- EDITABLE BODY CONTENT -->
            <tr>
              <td class="dark-bg-card mobile-padding-body" style="background-color: #FFFFFF; padding: 36px 40px 36px 40px;">
                <p class="dark-text-primary" style="margin: 0 0 16px 0; font-family: 'Inter', sans-serif; font-size: 16px; line-height: 26px; color: #0C1E34; font-weight: 600;">
                  Dear [Recipient Name],
                </p>
                <p class="dark-text-secondary" style="margin: 0 0 18px 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 26px; color: #2D3748;">
                  We are thrilled to extend an exclusive first-look invitation to you. Rivlet was born out of a desire to create activewear that withstands tropical heat, zero-roll waistbands that refuse to slip, and proprietary sweat-adaptive fabrics that feel virtually weightless.
                </p>

                <!-- EXCLUSIVE CODE VIP CARD -->
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 26px 0; background: linear-gradient(135deg, #0C1E34 0%, #152A47 100%); border-radius: 10px; border: 1px solid #C4963A;">
                  <tr>
                    <td style="padding: 24px 20px; text-align: center;">
                      <span style="font-family: 'DM Mono', monospace; font-size: 11px; color: #E5BE6B; letter-spacing: 2px; text-transform: uppercase;">
                        VIP INAUGURAL PRIVILEGE
                      </span>
                      <h3 style="margin: 8px 0 6px 0; font-family: 'Cormorant Garamond', Georgia, serif; font-size: 22px; color: #FFFFFF; font-weight: 600;">
                        Enjoy 15% Off Your Early Access Order
                      </h3>
                      <p style="margin: 0 0 16px 0; font-family: 'Inter', sans-serif; font-size: 13px; color: #94A3B8;">
                        Apply your personal invitation code at checkout:
                      </p>
                      <div style="display: inline-block; background-color: #081422; border: 1px dashed #C4963A; padding: 8px 22px; border-radius: 6px; font-family: 'DM Mono', monospace; font-size: 15px; font-weight: 700; color: #E5BE6B; letter-spacing: 3px; margin-bottom: 16px;">
                        RIVLETFIRST
                      </div>
                      <div>
                        <a href="https://therivlet.com" target="_blank" class="btn-gold" style="background-color: #C4963A; color: #0C1E34; font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: 0.8px; padding: 12px 28px; border-radius: 4px; display: inline-block; text-decoration: none; text-transform: uppercase;">
                          Explore The Collection &rarr;
                        </a>
                      </div>
                    </td>
                  </tr>
                </table>

                <p class="dark-text-secondary" style="margin: 0 0 24px 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 26px; color: #2D3748;">
                  [Add your personalized message or note to the recipient here in Gmail compose.]
                </p>

                <!-- SIGN-OFF -->
                <p class="dark-text-secondary" style="margin: 28px 0 0 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 24px; color: #2D3748;">
                  With warm regards,<br />
                  <strong class="dark-text-primary" style="color: #0C1E34; font-size: 16px;">The Rivlet Founding Team</strong><br />
                  <span class="dark-signoff-quote" style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 16px; font-style: italic; color: #7A5C3A;">“Move like water. Feel like air.”</span>
                </p>
              </td>
            </tr>

            {get_footer()}
          </table>
        </td>
      </tr>
    </table>
  </center>
</body>
</html>
'''

# 2. FOUNDER'S PERSONAL LETTER & VISION NOTE
founder_letter = f'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Rivlet — A Note From The Founder</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,400;1,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style type="text/css">{base_css}</style>
</head>
<body class="dark-bg-outer">
  <center class="dark-bg-outer" style="width: 100%; background-color: #FAF9F6; text-align: center;">
    <table role="presentation" align="center" width="100%" cellpadding="0" cellspacing="0" border="0" class="dark-bg-outer" style="margin: 0 auto; width: 100%; border-collapse: collapse; background-color: #FAF9F6;">
      <tr>
        <td align="center" valign="top" style="padding: 28px 12px 44px 12px;">
          <table role="presentation" align="center" width="600" cellpadding="0" cellspacing="0" border="0" class="email-container dark-bg-card" style="max-width: 600px; width: 100%; margin: 0 auto !important; margin-left: auto !important; margin-right: auto !important; border-collapse: separate; text-align: left; background-color: #FFFFFF; border-radius: 12px; overflow: hidden; border: 1px solid #EBE7DF; box-shadow: 0 4px 20px rgba(12, 30, 52, 0.04);">
            
            <!-- MINIMALIST ELEGANT HEADER -->
            <tr>
              <td class="dark-bg-header mobile-padding" style="padding: 28px 36px 20px 36px; border-bottom: 1px solid #F0ECE4;">
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width: 100%; border-collapse: collapse;">
                  <tr>
                    <td align="left" valign="middle" style="text-align: left; vertical-align: middle; padding: 0;">
                      <a href="https://therivlet.com" target="_blank" style="text-decoration: none; display: inline-block;">
                        <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                          <tr>
                            <td valign="middle" style="padding-right: 12px; vertical-align: middle;">
                              <img src="{wave_navy}" alt="Rivlet Wave" width="34" height="21" style="display: block; width: 34px; height: 21px; border: 0;" />
                            </td>
                            <td valign="middle" style="vertical-align: middle;">
                              <img src="{wordmark_navy}" alt="Rivlet" width="92" height="28" style="display: block; width: 92px; height: 28px; border: 0;" />
                            </td>
                          </tr>
                        </table>
                      </a>
                    </td>
                    <td align="right" valign="middle" class="header-right" style="text-align: right !important; vertical-align: middle; white-space: nowrap; padding: 0 0 0 10px;">
                      <span style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 14px; font-style: italic; color: #7A5C3A;">
                        Founder’s Dispatch
                      </span>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

            <!-- EDITORIAL BODY -->
            <tr>
              <td class="dark-bg-card mobile-padding-body" style="background-color: #FFFFFF; padding: 40px 44px 36px 44px;">
                
                <h2 class="dark-text-primary" style="margin: 0 0 20px 0; font-family: 'Cormorant Garamond', Georgia, serif; font-size: 28px; line-height: 34px; color: #0C1E34; font-weight: 600;">
                  Why We Spent 18 Months Engineering a Better Activewear Fabric
                </h2>

                <p class="dark-text-primary" style="margin: 0 0 18px 0; font-family: 'Inter', sans-serif; font-size: 16px; line-height: 26px; color: #0C1E34; font-weight: 600;">
                  Dear [Recipient Name],
                </p>

                <p class="dark-text-secondary" style="margin: 0 0 18px 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 27px; color: #2D3748;">
                  When we started Rivlet in Tamil Nadu, we noticed a persistent problem with activewear in Indian conditions: fabrics designed for cold western climates simply do not perform under real tropical heat and humidity.
                </p>

                <!-- PULLQUOTE HIGHLIGHT -->
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="dark-callout" style="margin: 26px 0; background-color: #FAF9F6; border-left: 3px solid #C4963A; border-radius: 0 8px 8px 0;">
                  <tr>
                    <td style="padding: 20px 24px;">
                      <p style="margin: 0; font-family: 'Cormorant Garamond', Georgia, serif; font-size: 19px; line-height: 28px; font-style: italic; color: #0C1E34; font-weight: 500;">
                        “Garments should never be an obstacle between your body and your movement. When activewear is engineered with intention, you completely forget you are wearing it.”
                      </p>
                    </td>
                  </tr>
                </table>

                <p class="dark-text-secondary" style="margin: 0 0 18px 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 27px; color: #2D3748;">
                  [Add your personalized update, thoughts, milestone reflection, or announcement here in Gmail compose.]
                </p>

                <p class="dark-text-secondary" style="margin: 0 0 28px 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 27px; color: #2D3748;">
                  Thank you for being part of our early journey. We are building this with care, precision, and zero shortcuts.
                </p>

                <!-- PERSONAL SIGNATURE BLOCK -->
                <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin-top: 24px;">
                  <tr>
                    <td style="border-left: 2px solid #C4963A; padding-left: 14px;">
                      <strong class="dark-text-primary" style="font-family: 'Inter', sans-serif; font-size: 16px; color: #0C1E34; display: block;">
                        Harichandru S.
                      </strong>
                      <span style="font-family: 'Inter', sans-serif; font-size: 13px; color: #718096;">
                        Founder & Creative Director · Rivlet
                      </span>
                    </td>
                  </tr>
                </table>

              </td>
            </tr>

            {get_footer()}
          </table>
        </td>
      </tr>
    </table>
  </center>
</body>
</html>
'''

# 3. B2B, PARTNERSHIP & COLLABORATION INQUIRY
b2b_partnership = f'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Rivlet — Partnership & Collaboration</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,400;1,600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <style type="text/css">{base_css}</style>
</head>
<body class="dark-bg-outer">
  <center class="dark-bg-outer" style="width: 100%; background-color: #F6F4F0; text-align: center;">
    <table role="presentation" align="center" width="100%" cellpadding="0" cellspacing="0" border="0" class="dark-bg-outer" style="margin: 0 auto; width: 100%; border-collapse: collapse; background-color: #F6F4F0;">
      <tr>
        <td align="center" valign="top" style="padding: 28px 12px 44px 12px;">
          <table role="presentation" align="center" width="600" cellpadding="0" cellspacing="0" border="0" class="email-container dark-bg-card" style="max-width: 600px; width: 100%; margin: 0 auto !important; margin-left: auto !important; margin-right: auto !important; border-collapse: separate; text-align: left; background-color: #FFFFFF; border-radius: 12px; overflow: hidden; border: 1px solid #EBE7DF; box-shadow: 0 4px 20px rgba(12, 30, 52, 0.06);">
            
            <tr><td height="4" style="background: linear-gradient(90deg, #0C1E34 0%, #C4963A 100%); line-height: 4px; font-size: 4px;">&nbsp;</td></tr>

            <!-- HEADER -->
            <tr>
              <td class="dark-bg-header mobile-padding" style="background-color: #FFFFFF; padding: 24px 32px 20px 32px; border-bottom: 1px solid #F0ECE4;">
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width: 100%; border-collapse: collapse;">
                  <tr>
                    <td align="left" valign="middle" style="text-align: left; vertical-align: middle; padding: 0;">
                      <a href="https://therivlet.com" target="_blank" style="text-decoration: none; display: inline-block;">
                        <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                          <tr>
                            <td valign="middle" style="padding-right: 12px; vertical-align: middle;">
                              <img src="{wave_navy}" alt="Rivlet Wave" width="34" height="21" style="display: block; width: 34px; height: 21px; border: 0;" />
                            </td>
                            <td valign="middle" style="vertical-align: middle;">
                              <img src="{wordmark_navy}" alt="Rivlet" width="92" height="28" style="display: block; width: 92px; height: 28px; border: 0;" />
                            </td>
                          </tr>
                        </table>
                      </a>
                    </td>
                    <td align="right" valign="middle" class="header-right" style="text-align: right !important; vertical-align: middle; white-space: nowrap; padding: 0 0 0 10px;">
                      <span style="font-family: 'Inter', sans-serif; font-size: 11px; font-weight: 700; color: #7A5C3A; background-color: #FAF9F6; border: 1px solid #EBE7DF; padding: 5px 12px; border-radius: 14px; text-transform: uppercase; letter-spacing: 0.5px;">
                        Partnerships
                      </span>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

            <!-- CONTENT BODY -->
            <tr>
              <td class="dark-bg-card mobile-padding-body" style="background-color: #FFFFFF; padding: 36px 40px 36px 40px;">
                <p class="dark-text-primary" style="margin: 0 0 16px 0; font-family: 'Inter', sans-serif; font-size: 16px; line-height: 26px; color: #0C1E34; font-weight: 600;">
                  Dear [Partner Name / Team],
                </p>

                <p class="dark-text-secondary" style="margin: 0 0 18px 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 26px; color: #2D3748;">
                  Thank you for reaching out regarding a potential collaboration with <strong>Rivlet</strong>. We welcome opportunities to partner with forward-thinking retailers, studios, athletes, and creative collaborators who value technical craftsmanship and refined design.
                </p>

                <!-- 3-PILLAR BRAND VALUES -->
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 24px 0 28px 0; background-color: #FAF9F6; border-radius: 8px; border: 1px solid #EBE7DF;">
                  <tr>
                    <td style="padding: 20px;" class="mobile-padding">
                      <p style="margin: 0 0 12px 0; font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 700; color: #7A5C3A; text-transform: uppercase; letter-spacing: 1px;">
                        ✦ Collaboration Focus Areas
                      </p>
                      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                        <tr>
                          <td style="padding: 6px 0; font-family: 'Inter', sans-serif; font-size: 14px; color: #0C1E34;">
                            <strong style="color: #C4963A;">01.</strong> Retail & Specialty Stockists
                          </td>
                        </tr>
                        <tr>
                          <td style="padding: 6px 0; font-family: 'Inter', sans-serif; font-size: 14px; color: #0C1E34;">
                            <strong style="color: #C4963A;">02.</strong> Athlete & Creator Ambassador Circle
                          </td>
                        </tr>
                        <tr>
                          <td style="padding: 6px 0; font-family: 'Inter', sans-serif; font-size: 14px; color: #0C1E34;">
                            <strong style="color: #C4963A;">03.</strong> Studio, Gym & Corporate Wellness Programs
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>

                <p class="dark-text-secondary" style="margin: 0 0 24px 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 26px; color: #2D3748;">
                  [Type your custom response, partnership proposal outline, or next action steps here in Gmail compose.]
                </p>

                <!-- SCHEDULE CTA BUTTON -->
                <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin: 24px 0 28px 0;">
                  <tr>
                    <td align="center" style="background-color: #0C1E34; border-radius: 6px;" class="dark-btn">
                      <a href="mailto:hello@therivlet.com" target="_blank" class="btn-navy" style="display: inline-block; padding: 12px 28px; font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 700; color: #FAF8F5; text-decoration: none; text-transform: uppercase; letter-spacing: 0.8px; border-radius: 6px; background-color: #0C1E34;">
                        Schedule Introductory Discussion &rarr;
                      </a>
                    </td>
                  </tr>
                </table>

                <p class="dark-text-secondary" style="margin: 28px 0 0 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 24px; color: #2D3748;">
                  Warm regards,<br />
                  <strong class="dark-text-primary" style="color: #0C1E34; font-size: 16px;">Partnerships Team · Rivlet</strong><br />
                  <span style="font-size: 13px; color: #718096;">therivlet.com &nbsp;·&nbsp; hello@therivlet.com</span>
                </p>
              </td>
            </tr>

            {get_footer()}
          </table>
        </td>
      </tr>
    </table>
  </center>
</body>
</html>
'''

# 4. LUXE ORDER CONCIERGE & APPRECIATION
order_concierge = f'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Rivlet — Order Confirmation & Concierge</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,400;1,600&family=DM+Mono:wght@400;500;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style type="text/css">{base_css}</style>
</head>
<body class="dark-bg-outer">
  <center class="dark-bg-outer" style="width: 100%; background-color: #F6F4F0; text-align: center;">
    <table role="presentation" align="center" width="100%" cellpadding="0" cellspacing="0" border="0" class="dark-bg-outer" style="margin: 0 auto; width: 100%; border-collapse: collapse; background-color: #F6F4F0;">
      <tr>
        <td align="center" valign="top" style="padding: 28px 12px 44px 12px;">
          <table role="presentation" align="center" width="600" cellpadding="0" cellspacing="0" border="0" class="email-container dark-bg-card" style="max-width: 600px; width: 100%; margin: 0 auto !important; margin-left: auto !important; margin-right: auto !important; border-collapse: separate; text-align: left; background-color: #FFFFFF; border-radius: 12px; overflow: hidden; border: 1px solid #EBE7DF; box-shadow: 0 4px 20px rgba(12, 30, 52, 0.06);">
            
            <tr><td height="4" style="background: linear-gradient(90deg, #0C1E34 0%, #C4963A 100%); line-height: 4px; font-size: 4px;">&nbsp;</td></tr>

            <!-- HEADER -->
            <tr>
              <td class="dark-bg-header mobile-padding" style="background-color: #FFFFFF; padding: 24px 32px 20px 32px; border-bottom: 1px solid #F0ECE4;">
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width: 100%; border-collapse: collapse;">
                  <tr>
                    <td align="left" valign="middle" style="text-align: left; vertical-align: middle; padding: 0;">
                      <a href="https://therivlet.com" target="_blank" style="text-decoration: none; display: inline-block;">
                        <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                          <tr>
                            <td valign="middle" style="padding-right: 12px; vertical-align: middle;">
                              <img src="{wave_navy}" alt="Rivlet Wave" width="34" height="21" style="display: block; width: 34px; height: 21px; border: 0;" />
                            </td>
                            <td valign="middle" style="vertical-align: middle;">
                              <img src="{wordmark_navy}" alt="Rivlet" width="92" height="28" style="display: block; width: 92px; height: 28px; border: 0;" />
                            </td>
                          </tr>
                        </table>
                      </a>
                    </td>
                    <td align="right" valign="middle" class="header-right" style="text-align: right !important; vertical-align: middle; white-space: nowrap; padding: 0 0 0 10px;">
                      <span style="font-family: 'DM Mono', monospace; font-size: 11px; font-weight: 700; color: #0C1E34; background-color: #E5BE6B; padding: 5px 12px; border-radius: 14px; text-transform: uppercase;">
                        CONCIERGE
                      </span>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

            <!-- ORDER STATUS HERO -->
            <tr>
              <td style="background-color: #0C1E34; padding: 32px 36px; text-align: center;" class="mobile-padding">
                <span style="font-family: 'DM Mono', monospace; font-size: 11px; color: #E5BE6B; letter-spacing: 2px; text-transform: uppercase;">
                  ORDER CONFIRMATION · #RIV-2026-081
                </span>
                <h2 style="margin: 8px 0 6px 0; font-family: 'Cormorant Garamond', Georgia, serif; font-size: 26px; color: #FAF8F5; font-weight: 600;">
                  Thank You For Choosing Rivlet
                </h2>
                <p style="margin: 0; font-family: 'Inter', sans-serif; font-size: 13px; color: #94A3B8;">
                  Your order is currently being prepared and hand-inspected for dispatch.
                </p>
              </td>
            </tr>

            <!-- CONTENT BODY -->
            <tr>
              <td class="dark-bg-card mobile-padding-body" style="background-color: #FFFFFF; padding: 36px 40px 36px 40px;">
                <p class="dark-text-primary" style="margin: 0 0 16px 0; font-family: 'Inter', sans-serif; font-size: 16px; line-height: 26px; color: #0C1E34; font-weight: 600;">
                  Dear [Customer Name],
                </p>

                <p class="dark-text-secondary" style="margin: 0 0 20px 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 26px; color: #2D3748;">
                  We are delighted to welcome you to the Rivlet movement. Each garment is engineered to elevate your daily motion with unparalleled lightness and comfort.
                </p>

                <!-- ORDER SUMMARY TABLE PLACEHOLDER -->
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 20px 0 24px 0; border: 1px solid #EBE7DF; border-radius: 8px; overflow: hidden;">
                  <tr style="background-color: #FAF9F6;">
                    <td style="padding: 12px 16px; font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 700; color: #0C1E34; text-transform: uppercase;">Item</td>
                    <td align="right" style="padding: 12px 16px; font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 700; color: #0C1E34; text-transform: uppercase;">Details</td>
                  </tr>
                  <tr>
                    <td style="padding: 16px; border-top: 1px solid #F0ECE4; font-family: 'Inter', sans-serif; font-size: 14px; color: #0C1E34;">
                      <strong>Rivlet Flow Activewear Piece</strong><br />
                      <span style="font-size: 12px; color: #718096;">Proprietary Sweat-Adaptive Weave · Size M</span>
                    </td>
                    <td align="right" style="padding: 16px; border-top: 1px solid #F0ECE4; font-family: 'Inter', sans-serif; font-size: 14px; font-weight: 700; color: #0C1E34;">
                      Confirmed
                    </td>
                  </tr>
                </table>

                <p class="dark-text-secondary" style="margin: 0 0 20px 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 26px; color: #2D3748;">
                  [Add tracking information, delivery concierge notes, or custom message here in Gmail compose.]
                </p>

                <p class="dark-text-secondary" style="margin: 28px 0 0 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 24px; color: #2D3748;">
                  Warm regards,<br />
                  <strong class="dark-text-primary" style="color: #0C1E34; font-size: 16px;">Rivlet Customer Concierge</strong><br />
                  <span style="font-size: 13px; color: #718096;">hello@therivlet.com</span>
                </p>
              </td>
            </tr>

            {get_footer()}
          </table>
        </td>
      </tr>
    </table>
  </center>
</body>
</html>
'''

# 5. EVENT / MASTERCLASS / RUN CLUB INVITATION
event_invite = f'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Rivlet — Event Invitation & Motion Session</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,400;1,600&family=DM+Mono:wght@400;500;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <style type="text/css">{base_css}</style>
</head>
<body class="dark-bg-outer">
  <center class="dark-bg-outer" style="width: 100%; background-color: #F6F4F0; text-align: center;">
    <table role="presentation" align="center" width="100%" cellpadding="0" cellspacing="0" border="0" class="dark-bg-outer" style="margin: 0 auto; width: 100%; border-collapse: collapse; background-color: #F6F4F0;">
      <tr>
        <td align="center" valign="top" style="padding: 28px 12px 44px 12px;">
          <table role="presentation" align="center" width="600" cellpadding="0" cellspacing="0" border="0" class="email-container dark-bg-card" style="max-width: 600px; width: 100%; margin: 0 auto !important; margin-left: auto !important; margin-right: auto !important; border-collapse: separate; text-align: left; background-color: #FFFFFF; border-radius: 12px; overflow: hidden; border: 1px solid #EBE7DF; box-shadow: 0 4px 20px rgba(12, 30, 52, 0.06);">
            
            <tr><td height="4" style="background: linear-gradient(90deg, #0C1E34 0%, #C4963A 50%, #E5BE6B 100%); line-height: 4px; font-size: 4px;">&nbsp;</td></tr>

            <!-- HEADER -->
            <tr>
              <td class="dark-bg-header mobile-padding" style="background-color: #FFFFFF; padding: 24px 32px 20px 32px; border-bottom: 1px solid #F0ECE4;">
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width: 100%; border-collapse: collapse;">
                  <tr>
                    <td align="left" valign="middle" style="text-align: left; vertical-align: middle; padding: 0;">
                      <a href="https://therivlet.com" target="_blank" style="text-decoration: none; display: inline-block;">
                        <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                          <tr>
                            <td valign="middle" style="padding-right: 12px; vertical-align: middle;">
                              <img src="{wave_navy}" alt="Rivlet Wave" width="34" height="21" style="display: block; width: 34px; height: 21px; border: 0;" />
                            </td>
                            <td valign="middle" style="vertical-align: middle;">
                              <img src="{wordmark_navy}" alt="Rivlet" width="92" height="28" style="display: block; width: 92px; height: 28px; border: 0;" />
                            </td>
                          </tr>
                        </table>
                      </a>
                    </td>
                    <td align="right" valign="middle" class="header-right" style="text-align: right !important; vertical-align: middle; white-space: nowrap; padding: 0 0 0 10px;">
                      <a href="https://therivlet.com" target="_blank" class="nav-link dark-text-primary" style="font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 700; color: #0C1E34; text-decoration: none; letter-spacing: 0.5px; text-transform: uppercase;">
                        THERIVLET.COM &rarr;
                      </a>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

            <!-- EVENT HERO -->
            <tr>
              <td style="background-color: #0C1E34; padding: 36px 36px 32px 36px; text-align: center;" class="mobile-padding">
                <span style="font-family: 'DM Mono', monospace; font-size: 11px; color: #E5BE6B; letter-spacing: 2px; text-transform: uppercase;">
                  COMMUNITY & MOTION INVITATION
                </span>
                <h1 style="margin: 8px 0 10px 0; font-family: 'Cormorant Garamond', Georgia, serif; font-size: 30px; line-height: 36px; color: #FAF8F5; font-weight: 600;">
                  Rivlet Motion Circle · Morning Run & Recovery
                </h1>
                <p style="margin: 0 auto; max-width: 440px; font-family: 'Inter', sans-serif; font-size: 14px; line-height: 22px; color: #94A3B8;">
                  An intimate community gathering testing our proprietary heat-adaptive gear in daily movement.
                </p>
              </td>
            </tr>

            <!-- EVENT DETAILS CARD -->
            <tr>
              <td class="dark-bg-card mobile-padding-body" style="background-color: #FFFFFF; padding: 36px 40px 36px 40px;">
                <p class="dark-text-primary" style="margin: 0 0 16px 0; font-family: 'Inter', sans-serif; font-size: 16px; line-height: 26px; color: #0C1E34; font-weight: 600;">
                  Dear [Attendee Name],
                </p>

                <p class="dark-text-secondary" style="margin: 0 0 20px 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 26px; color: #2D3748;">
                  You are cordially invited to join us for the upcoming <strong>Rivlet Motion Session</strong> in Tamil Nadu, India. Experience activewear designed for pure freedom of movement.
                </p>

                <!-- DATE & LOCATION TABLE -->
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 20px 0 26px 0; background-color: #FAF9F6; border: 1px solid #EBE7DF; border-radius: 8px;">
                  <tr>
                    <td style="padding: 20px;" class="mobile-padding">
                      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                        <tr>
                          <td valign="top" style="padding-bottom: 12px; font-family: 'Inter', sans-serif; font-size: 14px; color: #0C1E34;">
                            <strong style="color: #7A5C3A; text-transform: uppercase; font-size: 12px; letter-spacing: 1px; display: block; margin-bottom: 4px;">📅 Date & Time</strong>
                            Saturday, 6:30 AM IST
                          </td>
                        </tr>
                        <tr>
                          <td valign="top" style="padding-bottom: 12px; font-family: 'Inter', sans-serif; font-size: 14px; color: #0C1E34;">
                            <strong style="color: #7A5C3A; text-transform: uppercase; font-size: 12px; letter-spacing: 1px; display: block; margin-bottom: 4px;">📍 Location</strong>
                            Tamil Nadu, India
                          </td>
                        </tr>
                        <tr>
                          <td valign="top" style="font-family: 'Inter', sans-serif; font-size: 14px; color: #0C1E34;">
                            <strong style="color: #7A5C3A; text-transform: uppercase; font-size: 12px; letter-spacing: 1px; display: block; margin-bottom: 4px;">✦ Experience</strong>
                            5K Gentle Flow Run · Breathwork & Recovery · Exclusive Gear Trial
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>

                <p class="dark-text-secondary" style="margin: 0 0 24px 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 26px; color: #2D3748;">
                  [Add additional instructions, meeting landmark, or pass reservation details here in Gmail compose.]
                </p>

                <!-- RSVP BUTTON -->
                <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin: 24px 0 28px 0;">
                  <tr>
                    <td align="center" style="background-color: #0C1E34; border-radius: 6px;" class="dark-btn">
                      <a href="mailto:hello@therivlet.com?subject=RSVP%20Motion%20Session" target="_blank" class="btn-navy" style="display: inline-block; padding: 12px 28px; font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 700; color: #FAF8F5; text-decoration: none; text-transform: uppercase; letter-spacing: 0.8px; border-radius: 6px; background-color: #0C1E34;">
                        Confirm Your Attendance &nbsp;&rarr;
                      </a>
                    </td>
                  </tr>
                </table>

                <p class="dark-text-secondary" style="margin: 28px 0 0 0; font-family: 'Inter', sans-serif; font-size: 15px; line-height: 24px; color: #2D3748;">
                  Looking forward to moving together,<br />
                  <strong class="dark-text-primary" style="color: #0C1E34; font-size: 16px;">Rivlet Community Team</strong><br />
                  <span class="dark-signoff-quote" style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 16px; font-style: italic; color: #7A5C3A;">“Move like water. Feel like air.”</span>
                </p>
              </td>
            </tr>

            {get_footer()}
          </table>
        </td>
      </tr>
    </table>
  </center>
</body>
</html>
'''

# Write occasion files
with open('occasion-vip-launch.html', 'w', encoding='utf-8') as f:
    f.write(vip_launch)

with open('occasion-founder-letter.html', 'w', encoding='utf-8') as f:
    f.write(founder_letter)

with open('occasion-b2b-partnership.html', 'w', encoding='utf-8') as f:
    f.write(b2b_partnership)

with open('occasion-order-concierge.html', 'w', encoding='utf-8') as f:
    f.write(order_concierge)

with open('occasion-event-invite.html', 'w', encoding='utf-8') as f:
    f.write(event_invite)

print('Successfully generated 5 elite occasion templates!')
