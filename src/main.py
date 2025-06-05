import zipfile
import pandas as pd
import os
import folium


def extract_gtfs(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Extracted files: {zip_ref.namelist()}")


def load_gtfs_data(gtfs_dir):
    stops = pd.read_csv(os.path.join(gtfs_dir, "stops.txt"))
    routes = pd.read_csv(os.path.join(gtfs_dir, "routes.txt"))
    trips = pd.read_csv(os.path.join(gtfs_dir, "trips.txt"))
    stop_times = pd.read_csv(os.path.join(gtfs_dir, "stop_times.txt"), low_memory=False)
    calendar_dates = pd.read_csv(os.path.join(gtfs_dir, "calendar_dates.txt"))

    return stops, routes, trips, stop_times, calendar_dates


def plot_trip_on_map(stop_times, stops, trip_id):
    # Filter stop_times for this trip_id and sort by stop_sequence
    trip_stop_times = stop_times[stop_times["trip_id"] == trip_id]
    trip_stop_times = trip_stop_times.sort_values("stop_sequence")

    # Merge with stops to get lat/lon
    trip_stops = pd.merge(trip_stop_times, stops, on="stop_id", how="left")

    # Get start location for centering the map
    start_lat = trip_stops.iloc[0]["stop_lat"]
    start_lon = trip_stops.iloc[0]["stop_lon"]

    # Create Folium map centered at first stop
    trip_map = folium.Map(location=[start_lat, start_lon], zoom_start=13)

    # Add markers and lines
    points = []
    for _, row in trip_stops.iterrows():
        lat, lon = row["stop_lat"], row["stop_lon"]
        stop_name = row["stop_name"]
        folium.Marker([lat, lon], popup=stop_name).add_to(trip_map)
        points.append((lat, lon))

    # Draw a line between stops
    folium.PolyLine(points, color="blue", weight=4, opacity=0.7).add_to(trip_map)

    # Save map to HTML file
    output_path = "trip_map.html"
    trip_map.save(output_path)
    print(f"Map saved to {output_path}")


if __name__ == "__main__":
    zip_path = "../data/budapest_gtfs.zip"
    gtfs_dir = "../data/budapest_gtfs"

    # Only extract if the folder doesn't already exist
    if not os.path.exists(gtfs_dir):
        extract_gtfs(zip_path, gtfs_dir)
    else:
        print(f"Directory already exists: {gtfs_dir} — skipping extraction.")

    stops, routes, trips, stop_times, calendar_dates = load_gtfs_data(gtfs_dir)


    # # join trips with routes
    # routes_trips = pd.merge(trips, routes, on="route_id", how="left")
    # # join the result above with stop_times
    # trip_stop_times = pd.merge(routes_trips, stop_times, on="trip_id", how="left")
    # # sort by trip_id and stop_sequence
    # trip_stop_times_sorted = trip_stop_times.sort_values(by=["trip_id", "stop_sequence"])
    # # print a preview of a single trip
    # sample_trip_id = trip_stop_times_sorted["trip_id"].iloc[0]
    # print(trip_stop_times_sorted[trip_stop_times_sorted["trip_id"] == sample_trip_id])

    # Task Print the full stop schedule for a selected bus line ("105") including stop names and times
    selected_line = "105"
    # 1. Find the route_id where the route_short_name is "105" in the routes table.
    sample_route_id = routes[routes["route_short_name"] == selected_line]["route_id"].iloc[0]
    # 2. Find trips in the trips table that belong to that route_id. Pick just one trip_id for simplicity.
    sample_trip_id = trips[trips["route_id"] == sample_route_id]["trip_id"].iloc[0]
    plot_trip_on_map(stop_times, stops, sample_trip_id)
    # 3. Use stop_times to get the stop list for that trip_id. Sort by stop_sequence to get the correct order.
    sample_stops_list = stop_times[stop_times["trip_id"] == sample_trip_id]
    sample_stops_list_sorted = sample_stops_list.sort_values(by=["stop_sequence"])
    # 4. Join with stops table to get the names of the stops instead of just their IDs.
    sample_stops_list_with_stop_names = pd.merge(sample_stops_list_sorted, stops, on="stop_id", how="left")
    print(sample_stops_list_with_stop_names[["stop_sequence", "stop_name", "arrival_time", "departure_time"]])




