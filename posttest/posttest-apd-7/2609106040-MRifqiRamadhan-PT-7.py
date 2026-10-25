import os

accounts = {
    "adminvlao": {"password": "admin123", "role": "admin"},
    "bangyoga": {"password": "049", "role": "admin"},
    "mbafina": {"password": "016", "role": "admin"},
    "aja": {"password": "041", "role": "user"},
}

daftar_rank = {1: "Iron", 2: "Bronze", 3: "Silver", 4: "Gold", 5: "Platinum", 6: "Diamond", 7: "Ascendant", 8: "Immortal", 9: "Radiant"}

daftar_map = {"Ascent": True, "Bind": True, "Haven": True, "Split": True, "Lotus": True, "Sunset": True, "Abyss": True, "Corrode": True, "Icebox": True, "Summit": True, "Pearl": True, "Fracture": True, "Breeze": True}

agents = {
    "Duelist": {"Jett": True, "Phoenix": True, "Raze": True, "Reyna": True, "Yoru": True, "Neon": True, "Iso": True, "Waylay": True, "Hush": True},
    "Initiator": {"Breach": True, "Sova": True, "Skye": True, "Kayo": True, "Fade": True, "Gekko": True, "Tejo": True},
    "Controller": {"Brimstone": True, "Omen": True, "Viper": True, "Astra": True, "Harbor": True, "Clove": True, "Miks": True},
    "Sentinel": {"Sage": True, "Cypher": True, "Killjoy": True, "Chamber": True, "Deadlock": True, "Vyse": True}
}

data_performa = {}
bintang = "=" * 45