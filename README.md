# 🚍 Public Transport Route Optimizer

This project is a Python-based route optimization tool for public transportation systems. It allows users to find the most efficient route between two stops based on travel time, using real or sample transport data.

## 🚀 Project Goal

To build a system that can process real-world public transport data and eventually recommend the most optimal routes between stops using algorithms like Dijkstra or A*.

## 📂 Current Features

- ✅ Load and extract GTFS zip files

- ✅ Read and explore key GTFS tables: stops.txt, routes.txt, trips.txt, stop_times.txt

- ✅ Display stop schedule for a specific line (e.g., bus line 105), including:

  - Stop sequence

  - Stop names

  - Arrival and departure times

## 🔧 Project Structure

    transport-route-optimizer/
    ├── data/                   # Sample or GTFS transport data
    │   └── budapest_gtfs.zip   # GTFS data downloaded from BKK
    ├── src/                    # Python source files
    │   ├── __init__.py
    │   └── main.py             # Core logic for route calculation
    ├── README.md
    └── requirements.txt        # Dependencies



## 🛠️ How to Run

### 1. Clone the Repository and Download GTFS data

    git clone https://github.com/your-username/transport-route-optimizer.git
    cd transport-route-optimizer

Optional: Download the latest static GTFS dataset from:  
[https://bkk.hu/gtfs](https://bkk.hu/gtfs)  
and place the `.zip` file inside the `data/` folder.

### 2. Install Dependencies

    pip install -r requirements.txt
    
Required packages: pandas, networkx

### 3. Run the Optimizer

    python src/main.py

This will extract the GTFS zip file and load tables into pandas DataFrames.

## 📊 Example Output

    Directory already exists: ../data/budapest_gtfs — skipping extraction.
    Map saved to trip_map.html
    stop_sequence                         stop_name arrival_time departure_time
    0               0                   Apor Vilmos tér     06:24:00       06:24:00
    1               1       Kiss János altábornagy utca     06:25:00       06:25:00
    2               2                    Nagy Jenő utca     06:26:00       06:26:00
    3               3                      Márvány utca     06:27:00       06:27:00
    4               4                   Királyhágó utca     06:28:00       06:28:00
    5               5                          Győri út     06:29:00       06:29:00
    6               6                           Ág utca     06:30:00       06:30:00
    7               7                     Krisztina tér     06:32:00       06:32:00
    8               8                    Clark Ádám tér     06:34:00       06:34:00
    9               9              Széchenyi István tér     06:36:00       06:36:00
    10             10                  József nádor tér     06:37:00       06:37:00
    11             11                 Deák Ferenc tér M     06:39:00       06:40:00
    12             12            Bajcsy-Zsilinszky út M     06:41:00       06:41:00
    13             13                           Opera M     06:43:00       06:43:00
    14             14                         Oktogon M     06:44:00       06:44:00
    15             15                 Vörösmarty utca M     06:46:00       06:46:00
    16             16                   Kodály körönd M     06:47:00       06:47:00
    17             17                      Bajza utca M     06:48:00       06:48:00
    18             18                      Hősök tere M     06:51:00       06:51:00
    19             19     Vágány utca / Dózsa György út     06:52:00       06:52:00
    20             20      Lehel utca / Dózsa György út     06:53:00       06:53:00
    21             21                          Hun utca     06:54:00       06:54:00
    22             22  Lehel utca / Róbert Károly körút     06:56:00       06:56:00
    23             23                          Béke tér     06:57:00       06:57:00
    24             24                    Frangepán utca     06:58:00       06:58:00
    25             25                     Fiastyúk utca     07:00:00       07:00:00
    26             26                     Násznagy utca     07:01:00       07:01:00
    27             27                 József Attila tér     07:03:00       07:03:00
    28             28               Cziffra György park     07:05:00       07:05:00
    29             29                  Gyöngyösi utca M     07:07:00       07:07:00


## 📌 Next Steps

Build a stop-to-stop graph using networkx

Implement routing between two stops

Add weights based on distance or time

## 📈 Planned Features

Accept dynamic user input for start/end points

Integrate GTFS real-world transit data

Support multiple criteria: time, number of transfers, distance

Visualize routes on a map

## 🧑‍💻 Author
Created by [Krisztina Furdui](https://github.com/krisztinafurdui).
Feel free to contribute or reach out with ideas!