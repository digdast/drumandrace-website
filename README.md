# Drum and Race (drumandrace.com)

**Drum & Race** is a high-octane community portal dedicated to car modifications, grassroots & homebrew drift racing, international drift radar events, and alignment / chassis engineering.

## Features
- **Worldwide Drift Radar**: Track events across Japan (Ebisu, Nikko, Meihan), North America (Formula Drift, Final Bout, Drift Appalachia), and Europe (Drift Masters).
- **Homebrew Garage Showcase**: Verified grassroots builds (BMW E46, Nissan 180SX, GR86, Mazda Miata) featuring lock kits, turbo setups, dual caliper hydro e-brakes, and chassis reinforcement notes.
- **Drift Setup & Alignment Calculator**: Interactive chassis engineering tool estimating front negative camber, caster, cold tire pressures, and Ackerman angles for any drift configuration.
- **Community Build Submission**: Dynamic submission API allowing grassroots drivers to submit their builds for editorial review.
- **Google AdSense Monetization Ready**: Fully wired with Auto Ads, in-feed banners, verified `ads.txt` (`ca-pub-1596056523034714`), crawlers-enabled `robots.txt`, XML `sitemap.xml`, and GDPR / CCPA compliant Privacy Policy and Terms modals.

## Architecture
- **Backend**: Python 3.11 concurrent HTTP server with JSON REST APIs (`/api/events`, `/api/builds`, `/api/submit-build`, `/api/health`).
- **Cluster Deployment**: Hosted on K3s Kubernetes cluster (`k3s-cp-01`), running in namespace `tools` as a containerized service with NodePort `30084`.
- **Edge Routing**: Nginx Proxy Manager (NPM) reverse proxy routing through Cloudflare Argo Tunnel (`2f5e2042-9913-439c-8df2-bb8312ce022c.cfargotunnel.com`) over HTTP/2 with zero required router port forwarding.
