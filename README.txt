# Image to WEBP Converter

This Python script is designed to convert all PNG and JPG images in a specified source folder to WEBP format in a specified destination folder. The script ensures that the destination folder exists and logs all operations for easy debugging and monitoring.

## Features

- Converts PNG and JPG images to WEBP format.
- Ensures the destination folder exists before saving converted images.
- Logs detailed information and errors for easy debugging.

## Prerequisites

- Python 3.x
- Pillow library

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the required Python library using pip: 
    ```sh
    pip install Pillow
    ```

## Usage

1. Place the PNG and JPG images you want to convert in a folder named `x` in the same directory as the script.
2. The converted WEBP images will be saved in a folder named `y` in the same directory as the script.
3. Run the script using the following command: 
    ```sh
    python convert_images.py
    ```

## Logging

The script logs detailed information about its operations, including successful conversions and any errors encountered, to assist with debugging and monitoring the process.
