from pathlib import Path
import json


content = Path("cryptids.json").read_text(encoding="utf-8")
data = json.loads(content)

new_cryptid = {
    "navn": "Bybjørnen",
    "sted": "Bergen sentrum",
    "observasjoner": 3,
    "farlig": False,
    "kjennetegn": ["regnjakke", "spiser boller"]
}

data["kryptider"].append(new_cryptid)

data["versjon"] += 1
data["sist_oppdatert"] = "2026-09-28"

content = json.dumps(data, ensure_ascii=False, indent=2)
Path("new_cryptids.json").write_text(content, encoding="utf-8")
