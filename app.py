import streamlit as st
import folium
from streamlit_folium import st_folium
import json

# 读取GeoJSON数据
# 读取GeoJSON数据
with open('events.geojson', 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)

# 创建Streamlit应用
st.title("GeoJSON Data Visualization")

# 创建Folium地图
m = folium.Map(location=[22.009037, 100.797002], zoom_start=5)

# 添加GeoJSON数据到地图
folium.GeoJson(geojson_data, name="GeoJSON").add_to(m)

# 显示地图
st_folium(m, width=700, height=500)

# 显示属性信息
st.subheader("属性信息")
for feature in geojson_data["features"]:
    properties = feature["properties"]
    for key, value in properties.items():
        st.write(f"{key}: {value}")
