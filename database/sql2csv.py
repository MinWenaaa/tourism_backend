import mysql.connector

def sql2csv(file_path: str):
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
        "Pid, Pname, ST_X(`Plocation`) AS `longtitude`, ST_Y(`Plocation`) AS `latitude`," \
        "Pintroduce_long, Pintroduce_short, Paddress" \
        " FROM pois WHERE ptype = %s"
        params = ("旅游景点",)
        cursor.execute(query, params)
        results = cursor.fetchall()

        with open(file_path, "w", encoding="utf-8") as file:
            file.write("id,name,coord,desc\n")
            for row in results:
                if row['Pintroduce_long'] is not None:
                    file.write(f"{row['Pid']},{row['longtitude']},{row['latitude']},{row['Pname']},{row['Pname']}位于{row['Paddress']}，{row['Pintroduce_long']}\n")
                elif row['Pintroduce_short'] is not None:
                    file.write(f"{row['Pid']},{row['Pname']},{row['Plocation'].decode('utf-8')},{row['Pname']}位于{row['Paddress']}，{row['Pintroduce_short']}\n")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__=="__main__":
    sql2csv("model/data/test.csv")