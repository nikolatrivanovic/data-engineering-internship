import os
from download import download
from process_data import process_weather_data

if __name__ == "__main__":
    download()

    input_directory = os.path.join(os.getcwd(), "downloaded_files")
    output_csv = os.path.join(os.getcwd(), "processed_weather_data.csv")
    process_weather_data(input_directory, output_csv)
