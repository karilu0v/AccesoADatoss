from lxml import etree
from pathlib import Path

ruta = Path(_file_).parent / "everything.xml"

print(ruta)

tree = etree.parse(ruta)
root = tree.getroot()

first_season = root.find("temporada")

if etree.iselement(first_season):
    print(first_season.tag)
    first_season.tag = "season"
    print(type(first_season.text))
    print(fist_person.text.strip() =="")
    print(first_season.tag, first_season.text)
    
    print(first_season.find("minutos").text())
    mins = first_Season.find("minutos").text
    try:
        mins = int(mins)
    except Exception:
        mins = 18
        
    season_obj = root.find("season@[id='1']")
    mins_et = eason_obj.find("minutos")
    if etree.iselement(mins_et):
        mins = season_obj.find("minutos").text
    try:
        mins = int(mins)
    except Exception:
        mins = 18
    mins = mins + 1
    mins_et.text = str(mins)
    
    for e in season_obj:
        print(e.tag, e.text)