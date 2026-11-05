import os
import sys
import json
import mimetypes
import urllib.parse
from pathlib import Path
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

APP_DIR = Path(__file__).parent.resolve()
STATIC_DIR = APP_DIR / "static"
PORT = int(os.environ.get("PORT", "8080"))

GLOBAL_EVENTS = [
    {
        "id": "ebisu-matsuri",
        "name": "Ebisu Circuit Autumn Drift Matsuri",
        "location": "Nihonmatsu, Fukushima, Japan",
        "circuit": "Ebisu Minami & Touge Course",
        "region": "Japan",
        "dates": "Nov 14 - 15, 2026",
        "category": "Grassroots Festival",
        "description": "The sacred ground of drift culture. 48 hours of non-stop grassroots tandem drifting across Minami, Kita, and Touge mountain courses.",
        "badge": "Legendary Touge",
        "status": "Upcoming",
        "surface": "Mountain Asphalt",
        "spectators": "5,000+"
    },
    {
        "id": "final-bout-gallery",
        "name": "Final Bout Special Stage: Midwest",
        "location": "Shawano, Wisconsin, USA",
        "circuit": "USAIR Motorsports Raceway",
        "region": "North America",
        "dates": "Dec 05 - 06, 2026",
        "category": "Team Tandem Jam",
        "description": "Authentic Japanese style street-car team tandem competition. Authentic aero, low ride height, 3-to-5 car trains.",
        "badge": "Team Tandem",
        "status": "Registration Open",
        "surface": "Tight Karting Track",
        "spectators": "8,500+"
    },
    {
        "id": "drift-masters-ferropolis",
        "name": "Drift Masters European Championship Finals",
        "location": "Gräfenhainichen, Germany",
        "circuit": "Ferropolis Arena (City of Iron)",
        "region": "Europe",
        "dates": "Aug 21 - 22, 2027",
        "category": "Pro-Spec Arena",
        "description": "1,000+ HP pro missile battle inside a massive open-air museum surrounded by 100-meter industrial bucket-wheel excavators.",
        "badge": "1000+ HP Pro",
        "status": "Scheduled",
        "surface": "Industrial Concrete",
        "spectators": "25,000+"
    },
    {
        "id": "gatebil-rudskogen",
        "name": "Gatebil Extreme Horsepower Festival",
        "location": "Rakkestad, Norway",
        "circuit": "Rudskogen Motorpark",
        "region": "Europe",
        "dates": "Jul 08 - 11, 2027",
        "category": "No-Limit Festival",
        "description": "The wildest horsepower gathering on Earth. 1,200 HP twin-turbo 2JZ Volvos, V8 BMWs, and nonstop open-track drift carnage.",
        "badge": "Speed & Smoke",
        "status": "Scheduled",
        "surface": "Formula Grade GP",
        "spectators": "40,000+"
    },
    {
        "id": "clutch-kickers",
        "name": "Clutch Kickers $100K Invitational",
        "location": "Callahan, Florida, USA",
        "circuit": "Emerald Coast Dragway",
        "region": "North America",
        "dates": "Jan 16 - 17, 2027",
        "category": "Grassroots to Pro",
        "description": "The largest grassroots prize purse in drifting. Homebrew builds going door-to-door with Formula D veterans.",
        "badge": "$100K Shootout",
        "status": "Qualifying Open",
        "surface": "Short Oval Infield",
        "spectators": "12,000+"
    },
    {
        "id": "meihan-kansai-allstar",
        "name": "Meihan Sportsland Kansai All-Star Jam",
        "location": "Yamazoe, Nara, Japan",
        "circuit": "Meihan C-Course",
        "region": "Japan",
        "dates": "Feb 27 - 28, 2027",
        "category": "Wall Tap Masters",
        "description": "The legendary backward-entry clipping point against the concrete wall. Homebrew AE86s, Silvias, and JZX100s rubbing rear bumpers.",
        "badge": "Concrete Wall Run",
        "status": "Announced",
        "surface": "Technical Asphalt",
        "spectators": "6,000+"
    }
]

DRIFT_BUILDS = [
    {
        "chassis": "BMW E46 330i Coupe // 'Missile Stage 2'",
        "builder": "Homebrew Shed Build (Efrain Rivas)",
        "engine": "M54B30 Turbo w/ Garrett GT3582R (14 PSI, 465 WHP)",
        "steering_angle": "68° Dual-Lock Kit (SLR Super Angle)",
        "differential": "Welded OEM 3.91 Final Drive with Reinforced Subframe",
        "handbrake": "Dual-Caliper Hydraulic Setup w/ Wilwood 0.625 Master",
        "suspension": "BC Racing Custom 12k Front / 8k Rear True Coilover",
        "badge": "Street Missile",
        "hp": "465 WHP"
    },
    {
        "chassis": "Nissan 180SX (RPS13) // 'Kansai Spec'",
        "builder": "Midnight Garage Tokyo",
        "engine": "SR20DET Stroker 2.2L w/ Tomei ARMS M7960 (420 WHP)",
        "steering_angle": "65° Custom Modified Knuckles + Extended LCAs",
        "differential": "Nismo 2-Way GT LSD (4.08 Final Drive)",
        "handbrake": "In-line Hydro Handbrake + Project Mu D1 Spec Shoes",
        "suspension": "D-Max Super Street Coilovers + D-Max Tension Rods",
        "badge": "Pure JDM",
        "hp": "420 WHP"
    },
    {
        "chassis": "Toyota GR86 // 'Turbo Touge Runner'",
        "builder": "Apex Craft USA",
        "engine": "FA24 w/ HKS GTIII-RS Turbo Kit (9.5 PSI, 385 WHP)",
        "steering_angle": "62° Wisefab Half-Angle Kit",
        "differential": "Cusco Type-RS 1.5/2-Way Switchable LSD",
        "handbrake": "Chase Bays Standalone Dual Rear Caliper Kit",
        "suspension": "Fortune Auto 510 Series w/ Swift Springs (9k/7k)",
        "badge": "Modern Platform",
        "hp": "385 WHP"
    },
    {
        "chassis": "Mazda Miata MX-5 (NB) // 'Screamer Turbo'",
        "builder": "Budget Skid Shack",
        "engine": "BP-4W 1.8L Turbo w/ TD04-19T (260 WHP @ 2,150 lbs)",
        "steering_angle": "58° Extended Balljoints + Rack Spacers",
        "differential": "Torsen Type 2 LSD (4.10 Ratio)",
        "handbrake": "Flyin' Miata Proportioning + High-Friction Pads",
        "suspension": "MeisterR ClubRace 12.5k / 7k",
        "badge": "Featherweight",
        "hp": "260 WHP"
    }
]

class DrumAndRaceHandler(BaseHTTPRequestHandler):
    def send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, HEAD, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_cors_headers()
        self.end_headers()

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/health":
            body = json.dumps({"status": "healthy", "service": "drumandrace-website", "domain": "drumandrace.com"}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(body)
            return

        if path == "/api/events":
            body = json.dumps({"events": GLOBAL_EVENTS, "total": len(GLOBAL_EVENTS)}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(body)
            return

        if path == "/api/builds":
            body = json.dumps({"builds": DRIFT_BUILDS, "total": len(DRIFT_BUILDS)}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(body)
            return

        # Static files
        if path == "/" or path == "":
            target = STATIC_DIR / "index.html"
        elif path.startswith("/static/"):
            rel = path[len("/static/"):]
            target = (STATIC_DIR / rel).resolve()
        else:
            target = (STATIC_DIR / path.lstrip("/")).resolve()

        try:
            target.relative_to(STATIC_DIR)
        except ValueError:
            self.send_error(403, "Access denied")
            return

        if target.exists() and target.is_file():
            mime, _ = mimetypes.guess_type(str(target))
            with open(target, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", (mime or "application/octet-stream") + "; charset=utf-8" if mime and "text" in mime else (mime or "application/octet-stream"))
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-cache")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/submit-build":
            content_len = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_len).decode("utf-8", errors="ignore")
            try:
                data = json.loads(post_data)
                DRIFT_BUILDS.insert(0, {
                    "chassis": data.get("chassis", "Custom Drift Missile"),
                    "builder": data.get("builder", "Garage Enthusiast"),
                    "engine": data.get("engine", "Custom Engine Swap"),
                    "steering_angle": data.get("steering_angle", "60° Angle Kit"),
                    "differential": data.get("differential", "Welded Differential"),
                    "handbrake": data.get("handbrake", "Hydraulic Handbrake"),
                    "suspension": data.get("suspension", "Custom Coilover Setup"),
                    "badge": "Community Build",
                    "hp": data.get("hp", "350+ WHP")
                })
                res = json.dumps({"success": True, "message": "Build submitted to DrumAndRace catalog!"}).encode("utf-8")
                self.send_response(201)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(res)))
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(res)
                return
            except Exception as e:
                self.send_error(400, f"Invalid JSON payload: {e}")
                return
        else:
            self.send_error(404, "Endpoint not found")

    def log_message(self, format, *args):
        pass

def main():
    server = ThreadingHTTPServer(("0.0.0.0", PORT), DrumAndRaceHandler)
    print(f"[*] DrumAndRace.com official engine running on http://0.0.0.0:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Shutting down server...")
        server.server_close()

if __name__ == "__main__":
    main()
