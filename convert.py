import os
import logging
from PIL import Image

# Configuration de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_folder_if_not_exists(folder_path):
    """Create the folder if it does not exist."""
    try:
        os.makedirs(folder_path, exist_ok=True)
    except OSError as e:
        logging.error(f"Erreur de création du dossier {folder_path}: {e}")
        raise

def convert_image(input_file_path, output_file_path, format='webp'):
    """Convert an image to a specified format."""
    try:
        with Image.open(input_file_path) as img:
            img.save(output_file_path, format=format, quality=100)
        logging.info(f"Converti '{input_file_path}' en '{output_file_path}'")
    except Exception as e:
        logging.error(f"Erreur de conversion de l'image {input_file_path} en {output_file_path}: {e}")
        raise

def convert_images(source_folder, destination_folder):
    """Convert all PNG and JPG images in the source folder to WEBP format in the destination folder."""
    create_folder_if_not_exists(destination_folder)

    try:
        for filename in os.listdir(source_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_file_path = os.path.join(source_folder, filename)
                webp_file_path = os.path.join(destination_folder, os.path.splitext(filename)[0] + '.webp')
                convert_image(input_file_path, webp_file_path)
    except Exception as e:
        logging.error(f"Erreur lors du traitement des fichiers dans {source_folder}: {e}")
        raise

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(current_directory, 'x')
    destination_folder = os.path.join(current_directory, 'y')
    
    convert_images(source_folder, destination_folder)
