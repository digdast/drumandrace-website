# 🏁 DRUM & RACE // Worldwide Drift Culture, Homebrew Tuning & Track Events

```text
 ██████╗ ██████╗ ██╗   ██╗███╗   ███╗    ███████╗    ██████╗  █████╗  ██████╗███████╗
 ██╔══██╗██╔══██╗██║   ██║████╗ ████║    ██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝
 ██║  ██║██████╔╝██║   ██║██╔████╔██║    ███████╗    ██████╔╝███████║██║     █████╗  
 ██║  ██║██╔══██╗██║   ██║██║╚██╔╝██║    ╚════██║    ██╔══██╗██╔══██║██║     ██╔══╝  
 ██████╔╝██║  ██║╚██████╔╝██║ ╚═╝ ██║    ███████║    ██║  ██║██║  ██║╚██████╗███████╗
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝
```

> **[OFFICIAL PRODUCTION REPOSITORY]**  
> *The premier global digital hub for grassroots drift racing, homebrew garage modifications, worldwide track radar, and chassis alignment geometry.*  
> Engineered by **Efrain Rivas** — Senior Enterprise Infrastructure Architect.

---

## ⚡ Live Telemetry & Badges

[![Production Site](https://img.shields.io/badge/Production-drumandrace.com-ff5500?style=for-the-badge&logo=google-chrome&logoColor=white)](https://drumandrace.com)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Mirror-10b981?style=for-the-badge&logo=github)](https://digdast.github.io/drumandrace-website/)
[![Status](https://img.shields.io/badge/Status-100%25%20Operational-34d399?style=for-the-badge&logo=statuspage&logoColor=white)](https://drumandrace.com)
[![Cloudflare Edge](https://img.shields.io/badge/Edge-Cloudflare%20Anycast%20CDN-f38020?style=for-the-badge&logo=cloudflare&logoColor=white)](https://dash.cloudflare.com)
[![Security Hardened](https://img.shields.io/badge/Security-CSP%20%2B%20OWASP%20Shielded-emerald?style=for-the-badge&logo=shield&logoColor=white)](https://drumandrace.com)
[![Google AdSense](https://img.shields.io/badge/Monetization-Google%20AdSense%20Verified-4285f4?style=for-the-badge&logo=google-ads&logoColor=white)](https://drumandrace.com/ads.txt)
[![Design](https://img.shields.io/badge/Stack-TailwindCSS%20%2B%20Lucide-38bdf8?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com)

---

## 🌟 Core Platform Highlights

1. **Worldwide Drift Radar & Circuit Directory**:
   - Comprehensive event guide across **Japan** (Ebisu Circuit Matsuri, Meihan Sportsland, Nikko Circuit), **North America** (Formula Drift Irwindale, Final Bout, Drift Appalachia), and **Europe** (Drift Masters Grand Finale, Mondello Park, Iron Drift King).
2. **Grassroots Garage Showcase & Community Builds**:
   - Real missile builds documented with telemetry specs: BMW E46 330i Turbo, Nissan Silvia S14 Koguchi Spec, Toyota GR86 FA24, and Mazda Miata NA Turbo.
   - Technical teardowns of steering lock kits (Wisefab, SLR Speed, FDF), dual-caliper hydraulic handbrakes, and reinforced rear subframes.
3. **Drift Setup & Chassis Alignment Calculator**:
   - Interactive front negative camber, rear camber, positive caster, Ackerman angle, and cold tire pressure simulator for dry asphalt, intermediate, and rain conditions.
4. **Google AdSense Revenue Engine**:
   - High CPC automotive racing keywords, responsive leaderboard ads, in-feed missile build units, and 100% verified authorized `ads.txt` integration (`pub-1596056523034714`).
5. **Production Security Architecture**:
   - Zero-trust edge protection, Content Security Policy (CSP), automated DOM XSS sanitization (`escapeHTML`), and origin cloaking.

---

## 🏗️ High-Availability Edge Architecture

```mermaid
flowchart TD
    subgraph WAN ["🌐 Global Web Traffic"]
        Visitor["Global Drift Fans & Drivers"]
        Bot["Search Engine Crawlers & AdSense Bots"]
    end

    subgraph Cloudflare ["☁️ Cloudflare Global Anycast Edge (drumandrace.com)"]
        CF_DNS["Cloudflare DNS (Zone: ccd44ccbe0b9ca81a4b57f1cc32f27fc)"]
        CF_DDoS["DDoS Scrubbing & CDN Edge Caching"]
        CF_SSL["Universal SSL (Full Strict / TLS 1.3)"]
        CF_WAF["WAF & Bot Management"]
    end

    subgraph StorageOrigin ["🚀 GitHub Pages High-Availability Edge"]
        GHP["Static Asset Delivery & HTML5 Engine"]
        ADSTXT["Authorized ads.txt (ca-pub-1596056523034714)"]
        ROBOTS["robots.txt & sitemap.xml"]
    end

    subgraph Browser ["🖥️ Client-Side Security Sandbox"]
        CSP["Content-Security-Policy (AdSense-Safe)"]
        NOSNIFF["X-Content-Type-Options: nosniff"]
        XSS["escapeHTML() DOM Sanitization"]
    end

    Visitor --> CF_DNS
    Bot --> CF_DNS
    CF_DNS --> CF_DDoS --> CF_SSL --> CF_WAF
    CF_WAF --> GHP
    GHP --> ADSTXT
    GHP --> ROBOTS
    CF_WAF --> Browser
```

---

## 🛡️ Security Hardening & Compliance

- **Content-Security-Policy (CSP)**:
  `default-src 'self' data: blob: https:; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://pagead2.googlesyndication.com https://*.googlesyndication.com https://*.google.com https://*.doubleclick.net https://cdn.tailwindcss.com https://unpkg.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' data: https://fonts.gstatic.com; img-src 'self' data: blob: https:; connect-src 'self' https://pagead2.googlesyndication.com https://ep1.adtrafficquality.google https://googleads.g.doubleclick.net https://*.google.com https://*.googlesyndication.com; frame-src 'self' https://googleads.g.doubleclick.net https://tpc.googlesyndication.com https://pagead2.googlesyndication.com https://*.google.com;`
- **Clickjacking & MIME Protection**: `X-Content-Type-Options: nosniff` and `Referrer-Policy: strict-origin-when-cross-origin`.
- **Hardware Privacy**: `Permissions-Policy: camera=(), microphone=(), geolocation=()`.
- **DOM XSS Sanitization**: User-submitted chassis data and community specs pass through HTML entity encoders before DOM insertion.
- **Privacy & Compliance**: Integrated GDPR / CCPA cookie consent and privacy policy modals.

---

## 📂 Repository Topology

```text
drumandrace-website/
├── index.html        # High-performance single-page web app with Tailwind & Lucide
├── ads.txt           # Google AdSense publisher validation (pub-1596056523034714)
├── robots.txt        # Universal search engine indexing directive
├── sitemap.xml       # Canonical XML sitemap for SEO discovery
├── CNAME             # GitHub Pages custom domain binding (drumandrace.com)
├── static/           # Vector branding assets, SVGs, and logos
└── README.md         # Architecture, security & telemetry documentation
```

---

## ⚖️ License & Attribution

Designed and maintained by **Efrain Rivas**.  
All rights reserved © 2026 **DrumAndRace.com**.
