#!/usr/bin/env python3
import json

# ---------- DATA ----------
flights = [
  {"label":"Outbound","num":"AA 2430","from":"Phoenix (PHX)","to":"New York (JFK)",
   "dep":"Mon, Nov 16 · 8:50 AM","arr":"Mon, Nov 16 · 3:49 PM","conf":"YPQEVF"},
  {"label":"Return","num":"AA 2430","from":"New York (JFK)","to":"Phoenix (PHX)",
   "dep":"Wed, Nov 18 · 5:05 PM","arr":"Wed, Nov 18 · 8:49 PM","conf":"YPQEVF"},
]

hotel = {
  "key":"hotel","name":"Virgin Hotels New York City","type":"Hotel",
  "lat":40.7466063,"lng":-73.988791,"photo":"hotel-0.jpg",
  "website":"https://virginhotels.com/nyc/","phone":"+1 212-213-0090","hours":None,
  "gmaps":"https://maps.google.com/?ftid=0x89c2594994e032e3:0xb6b095913d99d5ee"
}

P = {
  "jfk": {"key":"jfk","name":"John F. Kennedy International Airport","type":"Airport","photo":"jfk-0.jpg",
          "website":"https://www.jfkairport.com/","phone":"+1 718-244-4444","hours":None,
          "gmaps":"https://maps.google.com/?ftid=0x89c26650d5404947:0xec4fb213489f11f0","lat":40.6446124,"lng":-73.7797278},
  "hotel": hotel,
  "times": {"key":"times","name":"Times Square","type":"Landmark","photo":"times-square-0.jpg",
            "website":"https://www.timessquarenyc.org/","phone":None,"hours":None,
            "gmaps":"https://maps.google.com/?ftid=0x89c25855c6480299:0x55194ec5a1ae072e","lat":40.7579747,"lng":-73.9855426},
  "perse": {"key":"perse","name":"Per Se","type":"Restaurant","photo":"perse-0.jpg",
            "website":"https://www.thomaskeller.com/perseny","phone":"+1 212-823-9335","hours":"Dinner 4:30–9:00 PM",
            "gmaps":"https://maps.google.com/?ftid=0x89c258f62fec73a7:0x5e24118dffac8a65","lat":40.7682178,"lng":-73.9828988},
  "esb": {"key":"esb","name":"Empire State Building","type":"Landmark","photo":"esb-0.jpg",
          "website":"https://www.esbnyc.com/","phone":None,"hours":None,
          "gmaps":"https://maps.google.com/?ftid=0x89c259a9b3117469:0xd134e199a405a163","lat":40.7484405,"lng":-73.9856644},
  "moma": {"key":"moma","name":"The Museum of Modern Art","type":"Museum","photo":"moma-0.jpg",
           "website":"https://www.moma.org/","phone":"+1 212-708-9400","hours":"Mon, Wed–Sun 10:30 AM–5 PM",
           "gmaps":"https://maps.google.com/?ftid=0x89c258f97bdb102b:0xea9f8fc0b3ffff55","lat":40.7614327,"lng":-73.9776216},
  "saks": {"key":"saks","name":"Saks Fifth Avenue","type":"Shopping","photo":"saks-0.jpg",
           "website":"https://www.saksfifthavenue.com/locations/s/newyork","phone":"+1 212-753-4000","hours":"Daily 10 AM–8 PM",
           "gmaps":"https://maps.google.com/?ftid=0x89c258fea03b0371:0x9b2e542db73cb4be","lat":40.758138,"lng":-73.9772561},
  "fashion": {"key":"fashion","name":"FASHIONPHILE Flagship","type":"Shopping","photo":"fashionphile-0.jpg",
              "website":"https://www.fashionphile.com/","phone":"+1 332-330-6133","hours":"Daily 10 AM–7 PM",
              "gmaps":"https://maps.google.com/?ftid=0x89c25937f1195833:0x5201b699d1699c98","lat":40.7516571,"lng":-74.0071579},
  "radio": {"key":"radio","name":"Radio City Music Hall","type":"Entertainment","photo":"radio-city-0.jpg",
            "website":"https://www.msg.com/radio-city-music-hall","phone":"+1 212-465-6000","hours":None,
            "gmaps":"https://maps.google.com/?ftid=0x89c258f8d61b2f3d:0x92c4e681d9aada95","lat":40.759976,"lng":-73.9799772},
  "jean": {"key":"jean","name":"Jean-Georges","type":"Restaurant","photo":"jean-georges-0.jpg",
           "website":"http://www.jean-georgesrestaurant.com/jean-georges/","phone":"+1 212-299-3900","hours":"Tue–Sun 4:45–9:30 PM (closed Mon)",
           "gmaps":"https://maps.google.com/?ftid=0x89c258f66d739287:0xb62f2ce924aab247","lat":40.7690576,"lng":-73.9815796},
  "bluebox": {"key":"bluebox","name":"Blue Box Café by Daniel Boulud (Tiffany & Co.)","type":"Café","photo":"blue-box-0.jpg",
              "website":"http://blueboxcafenyc.com/","phone":"+1 212-605-4090","hours":"Daily 10 AM–8 PM",
              "gmaps":"https://maps.google.com/?ftid=0x89c258fa8ac2cd01:0x4957c73b92e8f23d","lat":40.7626931,"lng":-73.9739144},
  "onvand": {"key":"onvand","name":"One Vanderbilt Observation Deck","type":"Observation Deck","photo":"one-vanderbilt-0.jpg",
             "website":"http://www.onevanderbilt.com/","phone":"+1 212-884-0384","hours":"Daily 10 AM–7 PM",
             "gmaps":"https://maps.google.com/?ftid=0x89c2590199a4c12d:0x35c4d69dd805cc5e","lat":40.7529466,"lng":-73.9785134},
  "dinner": {"key":"dinner","name":"Dinner with Marko & Natalia","type":"Dinner","photo":"dinner-0.jpg",
             "website":None,"phone":None,"hours":None,
             "gmaps":"https://maps.google.com/?q=La+Boca+at+Faena+Hotel+Chelsea+NYC","lat":40.7546,"lng":-74.0000,
             "options":[
               {"name":"La Boca (Faena Hotel, Chelsea)","gmaps":"https://maps.google.com/?q=La+Boca+at+Faena+Hotel+Chelsea+NYC"},
               {"name":"Peak with Priceless (30 Hudson Yards)","gmaps":"https://maps.google.com/?q=Peak+30+Hudson+Yards+NYC"},
               {"name":"Westlight (The William Vale, Brooklyn)","gmaps":"https://maps.google.com/?q=Westlight+The+William+Vale+Brooklyn"},
             ]},
  "lvc": {"key":"lvc","name":"Le Café Louis Vuitton NYC","type":"Café","photo":"louis-vuitton-cafe-0.jpg",
          "website":"https://lecafelvnyc.com/","phone":"+1 212-581-2300","hours":"Mon–Sat 10 AM–7:15 PM · Sun 11 AM–5:45 PM",
          "gmaps":"https://maps.google.com/?ftid=0x89c259f16c797005:0xe4e4933de0b8dc33","lat":40.762568,"lng":-73.9733996},
  "statue": {"key":"statue","name":"Statue of Liberty","type":"Landmark","photo":"statue-0.jpg",
             "website":"https://www.nps.gov/stli/index.htm","phone":"+1 212-363-3200","hours":None,
             "gmaps":"https://maps.google.com/?ftid=0x89c25090129c363d:0x40c6a5770d25022b","lat":40.6892494,"lng":-74.0445004},
}

days = [
  {
    "label":"Day 1","date":"Monday · Nov 16",
    "stops":[
      {"key":"jfk","time":"15:49","action":"Arrive in New York",
       "travel":{"name":"from Phoenix (PHX)","min":None,"mode":"flight","note":"AA 2430 departs 8:50 AM"},
       "name":"John F. Kennedy International Airport","type":"Airport"},
      {"key":"hotel","time":"~5:00 PM","action":"Check in at the hotel",
       "travel":{"name":"JFK Airport","min":65,"mode":"taxi","note":"Taxi / Uber from JFK"},
       "name":"Virgin Hotels New York City","type":"Hotel"},
      {"key":"times","time":"~6:00 PM","action":"Stroll through Times Square",
       "travel":{"name":"Virgin Hotels","min":10,"mode":"walk","note":"Walk to Times Square"},
       "name":"Times Square","type":"Landmark"},
      {"key":"perse","time":"~7:30 PM","action":"Dinner at Per Se",
       "travel":{"name":"Times Square","min":6,"mode":"walk","note":"Short walk north"},
       "name":"Per Se","type":"Restaurant"},
      {"key":"hotel","time":"~10:30 PM","action":"Back to the hotel",
       "travel":{"name":"Per Se","min":8,"mode":"taxi","note":"Quick ride back"},
       "name":"Virgin Hotels New York City","type":"Hotel"},
    ],
    "free":["esb","moma","saks","fashion"]
  },
  {
    "label":"Day 2","date":"Tuesday · Nov 17",
    "stops":[
      {"key":"bluebox","time":"~10:00 AM","action":"Breakfast at Blue Box Café (Tiffany's)",
       "travel":{"name":"Virgin Hotels","min":15,"mode":"taxi","note":"Short ride to 57th St"},
       "name":"Blue Box Café by Daniel Boulud (Tiffany & Co.)","type":"Café"},
      {"key":"jean","time":"~1:00 PM","action":"Lunch at Jean-Georges",
       "travel":{"name":"Blue Box Café","min":6,"mode":"taxi","note":"Across Midtown"},
       "name":"Jean-Georges","type":"Restaurant"},
      {"key":"onvand","time":"~2:30 PM","action":"View from One Vanderbilt",
       "travel":{"name":"Jean-Georges","min":8,"mode":"taxi","note":"To Midtown"},
       "name":"One Vanderbilt Observation Deck","type":"Observation Deck"},
      {"key":"radio","time":"~4:00 PM","action":"Visit Radio City Music Hall",
       "travel":{"name":"One Vanderbilt","min":6,"mode":"taxi","note":"A few blocks south"},
       "name":"Radio City Music Hall","type":"Entertainment"},
      {"key":"dinner","time":"~6:30 PM","action":"Dinner with Marko & Natalia",
       "travel":{"name":"Radio City Music Hall","min":20,"mode":"taxi","note":"~20 min to Chelsea / Brooklyn"},
       "name":"Dinner with Marko & Natalia","type":"Dinner"},
      {"key":"hotel","time":"~9:30 PM","action":"Back to the hotel",
       "travel":{"name":"Dinner spot","min":25,"mode":"taxi","note":"Ferry + ride if Westlight"},
       "name":"Virgin Hotels New York City","type":"Hotel"},
    ],
    "free":["saks","moma","statue","fashion"]
  },
  {
    "label":"Day 3","date":"Wednesday · Nov 18",
    "stops":[
      {"key":"hotel","time":"9:00 AM","action":"Morning & last look around",
       "travel":{"name":"Morning at the hotel","min":None,"mode":None},
       "name":"Virgin Hotels New York City","type":"Hotel"},
      {"key":"lvc","time":"~11:00 AM","action":"Lunch at Le Café Louis Vuitton",
       "travel":{"name":"Virgin Hotels","min":7,"mode":"taxi","note":"Short ride up"},
       "name":"Le Café Louis Vuitton NYC","type":"Café"},
      {"key":"jfk","time":"~1:00 PM","action":"Head to JFK for the flight home",
       "travel":{"name":"Le Café Louis Vuitton","min":65,"mode":"taxi","note":"Allow buffer for security"},
       "name":"John F. Kennedy International Airport","type":"Airport"},
    ],
    "free":["moma","saks","statue","fashion"]
  }
]

# Build slides in trip order from days
slides = []
for d in days:
    for s in d["stops"]:
        p = P[s["key"]]
        slide = {
          "key": s["key"], "name": s["name"], "type": s["type"],
          "photo": p["photo"], "day": d["label"], "time": s["time"],
          "action": s["action"],
          "travel": s["travel"],
          "gmaps": p["gmaps"], "website": p["website"], "hours": p["hours"],
          "lat": p["lat"], "lng": p["lng"],
        }
        if p.get("options"):
            slide["options"] = p["options"]
        slides.append(slide)

trip = {
  "title":"New York City","subtitle":"3 days in Manhattan",
  "travelers":"Zachary Martin & Lennai Idso Martin",
  "start":"Mon, Nov 16, 2026","end":"Wed, Nov 18, 2026",
  "flights":flights,"hotel":hotel,"days":days,"slides":slides,"places":P,
  "optional":["esb","statue","moma","saks","fashion"]
}

with open("data.js","w") as f:
    f.write("window.TRIP = " + json.dumps(trip) + ";\n")

print("data.js written")
print("slides:", len(slides))
