import json
import pygal.maps.world as ff
from pygal.style import RotateStyle
def get_code(ii):
    for i,j in ff.COUNTRIES.items():
        if ii==j:
            return i
    return None

filename = "population.json"
c_p = {};c1={};c2={};c3={}
with open(filename) as f :
    data = json.load(f)
for i in data:
    if i["Year"] =="2010":
        c_n=i["Country Name"]
        v = int(float(i["Value"]))
        result= get_code(c_n)
        if result:
            c_p[result] = v
        else:
            print("Error",c_n)
for i,j in c_p.items():
    if j < 10000000:
        c1[i] = j
    elif j < 1000000000:
        c2[i] = j
    else:
        c3[i] = j
ww = RotateStyle('#336699')
map = ff.World(style=ww)
map.title="the population of the countries"
map.add("一千万以一下",c1)
map.add("一千万到10亿",c2)
map.add("大于10亿",c3)
map.render_to_file("map.svg")
D:\python37\learning_log\ll_env\Lib\site-packages\django\contrib\admin\static\admin\img
