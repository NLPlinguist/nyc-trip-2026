#!/usr/bin/env python3
"""Generate the NYC trip website files."""
import json, os, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSET_SRC = "/opt/data/nyc-trip/assets"
ASSET_DST = os.path.join(ROOT, "assets")
os.makedirs(ASSET_DST, exist_ok=True)

# Copy assets
copied = 0
for f in os.listdir(ASSET_SRC):
    if f.endswith(".jpg"):
        shutil.copy2(os.path.join(ASSET_SRC, f), os.path.join(ASSET_DST, f))
        copied += 1

# ---------- Data ----------
def P(key, name, ptype, lat, lng, photo, website=None, phone=None, hours=None, gmaps=None):
    return {
        "key": key, "name": name, "type": ptype,
        "lat": lat, "lng": lng, "photo": photo,
        "website": website, "phone": phone, "hours": hours, "gmaps": gmaps,
    }

places = {
    "jfk": P("jfk", "John F. Kennedy International Airport", "Airport", 40.6446124, -73.7797278,
        "jfk-0.jpg", "https://www.jfkairport.com/", "+1 718-244-4444",
        gmaps="https://maps.google.com/?ftid=0x89c26650d5404947:0xec4fb213489f11f0"),
    "hotel": P("hotel", "Virgin Hotels New York City", "Hotel", 40.7466063, -73.9887910,
        "hotel-0.jpg", "https://virginhotels.com/nyc/", "+1 212-213-0090",
        gmaps="https://maps.google.com/?ftid=0x89c2594994e032e3:0xb6b095913d99d5ee"),
    "times": P("times", "Times Square", "Sight", 40.7579747, -73.9855426,
        "times-square-0.jpg", "https://www.timessquarenyc.org/",
        gmaps="https://maps.google.com/?ftid=0x89c25855c6480299:0x55194ec5a1ae072e"),
    "perse": P("perse", "Per Se", "Restaurant", 40.7682178, -73.9828988,
        "perse-0.jpg", "https://www.thomaskeller.com/perseny", "+1 212-823-9335",
        "Dinner 4:30–9:00 PM",
        gmaps="https://maps.google.com/?ftid=0x89c258f62fec73a7:0x5e24118dffac8a65"),
    "jean": P("jean", "Jean-Georges", "Restaurant", 40.7690576, -73.9815796,
        "jean-georges-0.jpg", "http://www.jean-georgesrestaurant.com/jean-georges/", "+1 212-299-3900",
        "Tue–Sun 4:45–9:30 PM (closed Mon)",
        gmaps="https://maps.google.com/?ftid=0x89c258f66d739287:0xb62f2ce924aab247"),
    "bluebox": P("bluebox", "Blue Box Café by Daniel Boulud", "Café", 40.7626931, -73.9739144,
        "blue-box-0.jpg", "http://blueboxcafenyc.com/", "+1 212-605-4090",
        "Sun 11 AM–7 PM · other days 10 AM–8 PM",
        gmaps="https://maps.google.com/?ftid=0x89c258fa8ac2cd01:0x4957c73b92e8f23d"),
    "onvand": P("onvand", "One Vanderbilt", "Observation Deck", 40.7529466, -73.9785134,
        "one-vanderbilt-0.jpg", "http://www.onevanderbilt.com/", "+1 212-884-0384",
        gmaps="https://maps.google.com/?ftid=0x89c2590199a4c12d:0x35c4d69dd805cc5e"),
    "radio": P("radio", "Radio City Music Hall", "Entertainment", 40.7599760, -73.9799772,
        "radio-city-0.jpg", "https://www.msg.com/radio-city-music-hall", "+1 212-465-6000",
        gmaps="https://maps.google.com/?ftid=0x89c258f8d61b2f3d:0x92c4e681d9aada95"),
    "lvc": P("lvc", "Le Café Louis Vuitton NYC", "Café", 40.7625680, -73.9733996,
        "louis-vuitton-cafe-0.jpg", "https://lecafelvnyc.com/", "+1 212-581-2300",
        "Mon–Sat 10 AM–7:15 PM · Sun 11 AM–5:45 PM",
        gmaps="https://maps.google.com/?ftid=0x89c259f16c797005:0xe4e4933de0b8dc33"),
    "saks": P("saks", "Saks Fifth Avenue", "Shopping", 40.7581380, -73.9772561,
        "saks-0.jpg", "https://www.saksfifthavenue.com/", "+1 212-753-4000",
        gmaps="https://maps.google.com/?ftid=0x89c258fea03b0371:0x9b2e542db73cb4be"),
    "esb": P("esb", "Empire State Building", "Observation Deck", 40.7484405, -73.9856644,
        "esb-0.jpg", "https://www.esbnyc.com/",
        "Daily 9 AM–11 PM",
        gmaps="https://maps.google.com/?ftid=0x89c259a9b3117469:0xd134e199a405a163"),
    "statue": P("statue", "Statue of Liberty", "Sight", 40.6892494, -74.0445004,
        "statue-0.jpg", "https://www.nps.gov/stli/index.htm", "+1 212-363-3200",
        gmaps="https://maps.google.com/?ftid=0x89c25090129c363d:0x40c6a5770d25022b"),
    "moma": P("moma", "The Museum of Modern Art", "Museum", 40.7614327, -73.9776216,
        "moma-0.jpg", "https://www.moma.org/", "+1 212-708-9400",
        "Mon–Sat 10:30–5:30 PM (Fri till 8:30)",
        gmaps="https://maps.google.com/?ftid=0x89c258f97bdb102b:0xea9f8fc0b3ffff55"),
    "fashion": P("fashion", "FASHIONPHILE Flagship", "Shopping", 40.7516571, -74.0071579,
        "fashionphile-0.jpg", "https://www.fashionphile.com/", "+1 332-330-6133",
        gmaps="https://maps.google.com/?ftid=0x89c25937f1195833:0x5201b699d1699c98"),
}

# Itinerary stops: key, time label, action label, travel from prev (name + min + mode)
# mode: 'taxi' / 'walk' / 'subway'
days = [
    {
        "label": "Day 1",
        "date": "Saturday · Nov 16",
        "stops": [
            {"key":"jfk", "time":"15:49", "action":"Arrive in New York",
             "travel":{"name":"from Phoenix (PHX)","min":None,"mode":"flight","note":"AA 2430 departs 8:50 AM"}},
            {"key":"hotel", "time":"~5:00 PM", "action":"Check in at the hotel",
             "travel":{"name":"JFK Airport","min":65,"mode":"taxi","note":"Taxi / Uber from JFK"}},
            {"key":"times", "time":"~6:00 PM", "action":"Stroll through Times Square",
             "travel":{"name":"Virgin Hotels","min":4,"mode":"walk","note":"10 min walk"}},
            {"key":"perse", "time":"~7:30 PM", "action":"Dinner at Per Se",
             "travel":{"name":"Times Square","min":4,"mode":"walk","note":"Short walk north"}},
            {"key":"hotel", "time":"~10:30 PM", "action":"Back to the hotel",
             "travel":{"name":"Per Se","min":8,"mode":"taxi","note":"Quick ride back"}},
        ],
        "free": ["esb","moma","saks","fashion"],
    },
    {
        "label": "Day 2",
        "date": "Sunday · Nov 17",
        "stops": [
            {"key":"hotel", "time":"9:00 AM", "action":"Breakfast / brunch & settle in",
             "travel":{"name":"Morning at the hotel","min":None,"mode":None}},
            {"key":"jean", "time":"~1:00 PM", "action":"Lunch at Jean-Georges",
             "travel":{"name":"Virgin Hotels","min":8,"mode":"taxi","note":"Midtown ride"}},
            {"key":"bluebox", "time":"~3:30 PM", "action":"Coffee & pastry at Blue Box Café",
             "travel":{"name":"Jean-Georges","min":3,"mode":"walk","note":"A few blocks"}},
            {"key":"onvand", "time":"~5:00 PM", "action":"View from One Vanderbilt",
             "travel":{"name":"Blue Box Café","min":4,"mode":"walk","note":"Walk to Midtown"}},
            {"key":"radio", "time":"~6:00 PM", "action":"Visit Radio City Music Hall",
             "travel":{"name":"One Vanderbilt","min":2,"mode":"walk","note":"Very close"}},
            {"key":"hotel", "time":"~8:30 PM", "action":"Back to the hotel",
             "travel":{"name":"Radio City Music Hall","min":5,"mode":"walk","note":"Walk back"}},
        ],
        "free": ["statue","esb","moma","saks"],
    },
    {
        "label": "Day 3",
        "date": "Monday · Nov 18",
        "stops": [
            {"key":"hotel", "time":"9:00 AM", "action":"Morning & last look around",
             "travel":{"name":"Morning at the hotel","min":None,"mode":None}},
            {"key":"lvc", "time":"~11:00 AM", "action":"Lunch at Le Café Louis Vuitton",
             "travel":{"name":"Virgin Hotels","min":7,"mode":"taxi","note":"Short ride up"}},
            {"key":"jfk", "time":"~1:00 PM", "action":"Head to JFK for the flight home",
             "travel":{"name":"Le Café Louis Vuitton","min":65,"mode":"taxi","note":"Allow buffer for security"}},
        ],
        "free": ["moma","saks","statue","fashion"],
    },
]

trip = {
    "title": "New York City",
    "subtitle": "3 days in Manhattan",
    "travelers": "Zachary Martin & Lennai Idso Martin",
    "start": "Sat, Nov 16, 2026",
    "end": "Mon, Nov 18, 2026",
    "flights": [
        {"label":"Outbound", "num":"AA 2430", "from":"Phoenix (PHX)", "to":"New York (JFK)",
         "dep":"Nov 16 · 8:50 AM", "arr":"Nov 16 · 3:49 PM", "conf":"YPQEVF"},
        {"label":"Return", "num":"AA 2430", "from":"New York (JFK)", "to":"Phoenix (PHX)",
         "dep":"Nov 18 · 5:05 PM", "arr":"Nov 18 · 8:49 PM", "conf":"YPQEVF"},
    ],
    "hotel": places["hotel"],
    "days": days,
    "optional": ["esb","statue","moma","saks","fashion"],
}

# Build slideshow list (chronological, distinct activities)
slides = []
seen = set()
for d in days:
    for s in d["stops"]:
        k = s["key"]
        # skip duplicate hotel "return" slides to keep slideshow focused, but keep first hotel
        if k == "hotel" and k in seen:
            continue
        p = places[k]
        slides.append({
            "key": k,
            "name": p["name"], "type": p["type"], "photo": p["photo"],
            "day": d["label"], "time": s["time"], "action": s["action"],
            "travel": s["travel"],
            "gmaps": p["gmaps"], "website": p["website"], "hours": p["hours"],
            "lat": p["lat"], "lng": p["lng"],
        })
        seen.add(k)
trip["slides"] = slides
trip["places"] = places

# directions link builder in JS uses lat/lng

with open(os.path.join(ROOT, "data.js"), "w") as f:
    f.write("window.TRIP = " + json.dumps(trip) + ";\n")

print("Generated data.js, copied", copied, "assets")
