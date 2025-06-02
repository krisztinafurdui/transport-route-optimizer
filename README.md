# 🚍 Public Transport Route Optimizer

This project is a Python-based route optimization tool for public transportation systems. It allows users to find the most efficient route between two stops based on travel time, using real or sample transport data.

## 🚀 Project Goal

To build a system that can process real-world public transport data and eventually recommend the most optimal routes between stops using algorithms like Dijkstra or A*.

## 📂 Current Features

- ✅ Parses **real GTFS static data** from [BKK FUTÁR (Budapest)](https://bkk.hu/).
- ✅ Loads key GTFS tables like `routes.txt`, `stops.txt`, and `stop_times.txt` using `pandas`.
- ✅ Prints sample data to confirm successful loading.

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

    stop_id  ... wheelchair_boarding
    0  002133  ...                 NaN
    2  003002  ...                 NaN
    3  004716  ...                 2.0
    4  004948  ...                 NaN
    ...
    
    agency_id route_id  ... route_text_color  route_sort_order
    0       BKK     0050  ...           FFFFFF                20
    1       BKK     0070  ...           FFFFFF                24
    2       BKK     0075  ...           FFFFFF                25
    3       BKK     0078  ...           FFFFFF                26
    4       BKK     0085  ...           FFFFFF                27

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