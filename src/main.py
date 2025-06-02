import zipfile
import pandas as pd
import os


def extract_gtfs(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Extracted files: {zip_ref.namelist()}")


def load_gtfs_data(gtfs_dir):
    stops = pd.read_csv(os.path.join(gtfs_dir, "stops.txt"))
    routes = pd.read_csv(os.path.join(gtfs_dir, "routes.txt"))
    trips = pd.read_csv(os.path.join(gtfs_dir, "trips.txt"))
    stop_times = pd.read_csv(os.path.join(gtfs_dir, "stop_times.txt"), low_memory=False)

    return stops, routes, trips, stop_times


if __name__ == "__main__":
    zip_path = "../data/budapest_gtfs.zip"
    extract_to = "../data/gtfs_extracted"

    extract_gtfs(zip_path, extract_to)

    stops, routes, trips, stop_times = load_gtfs_data(extract_to)

    print(stops.head())
    print(routes.head())

