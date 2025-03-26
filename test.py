import folium
import mysql.connector

from model.Utils.spatial_handler import SpatialHandler

def read_poi_data():
    config = {
        "host" : "localhost",
        "user" : "root",
        "passwd" : "123456",
        "database" : "travel4",
        'raise_on_warnings': True
    }
    
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT " \
        "Pid, Pname, ST_X(`Plocation`) AS `longtitude`, ST_Y(`Plocation`) AS `latitude`" \
        " FROM pois WHERE ptype = %s AND " \
        "ST_X(Plocation) BETWEEN 114.1 AND 114.5 "\
        "AND ST_Y(Plocation) BETWEEN 30.5 AND 30.7 "\
        "LIMIT 300"
        params = ("旅游景点",)
        cursor.execute(query, params)
        results = cursor.fetchall()
        print(len(results))
        print(type(results[0]))
        return results

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_map_html(all_data:list, result_name: str):
    m = folium.Map(location=[30.6042, 114.3074], zoom_start=12)

    for data in all_data:
        folium.Marker(
            [data['latitude'], data['longtitude']],
            icon=folium.Icon(color='lightgray', icon='info-sign'),
        ).add_to(m)

    m.get_root().header.add_child(
        folium.Element(
            """
            <style>
                .leaflet-marker-icon {
                    width: 2px; /* 设置宽度 */
                    height: 2px; /* 设置高度 */
                }
            </style>
            """
        )
    )
    m.save(result_name)

def get_clusters_map(all_data:list, result_name: str, clusters: list):
    m = folium.Map(location=[30.6042, 114.3074], zoom_start=12)

    colors = ['red', 'blue', 'green', 'purple',
              'orange', 'darkred', 'lightred', 'beige',
              'darkblue', 'darkgreen', 'cadetblue',
              'darkpurple', 'pink', 'lightblue']
    for data in all_data:
        folium.Marker(
            [data['latitude'], data['longtitude']],
            icon=folium.Icon(color='lightgray', icon='info-sign'),
        ).add_to(m)

    for index, cluster in enumerate(clusters):
        if len(cluster) < 8:
            continue
        for data in [all_data[ID] for ID in cluster]:
            folium.Marker(
            [data['latitude'], data['longtitude']],
            icon=folium.Icon(color=colors[index], icon='info-sign'),
        ).add_to(m)


    m.get_root().header.add_child(
        folium.Element(
            """
            <style>
                .leaflet-marker-icon {
                    width: 2px; /* 设置宽度 */
                    height: 2px; /* 设置高度 */
                }
            </style>
            """
        )
    )
    m.save(result_name)

if __name__=="__main__":
    poi_data = read_poi_data()
    #get_map_html(poi_data, "origin_poi.html")
    spatial_handler = SpatialHandler(data = poi_data)
    idList = range(500)
    clusters = spatial_handler.get_clusters(idList)
    get_clusters_map(poi_data, 'clusters.html', clusters)