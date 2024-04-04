import requests
import re
import json
r = requests.get("https://hackmd.io/@l10n-tw/glossaries", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'})
temps = re.findall(r"\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|", r.text)[3:]
datas = []
for temp in temps:
    if not temp[1].strip() or not temp[2].strip():
        continue
    parts = re.split(r'&lt;br&gt;|/|（.*?）', temp[2])
    parts = [part.strip() for part in parts if part.strip()]
    for part in parts:
        while True:
            try:
                r = requests.post("https://api.zhconvert.org/convert", json={
                    "converter": "Traditional",
                    "text": part
                }).json()
                break
            except:
                pass
        datas.append([
            temp[0].strip(),
            temp[1].split(r"&lt;br&gt;")[0].strip(),
            r['data']['text'].strip(),
            temp[3].strip()
        ])

    print(parts)
with open('datas.json', 'w', encoding="utf-8") as f:
    json.dump(datas, f, sort_keys=True, indent=4, ensure_ascii=False)