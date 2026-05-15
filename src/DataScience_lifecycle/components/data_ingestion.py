import os
import requests
from src.DataScience_lifecycle import logger
import zipfile
from src.DataScience_lifecycle.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # Dowloading zip file from source url and save it in local directory
    def download_file(self):
        os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)

        try:
            logger.info("Starting file download...")
            # Download file
            response = requests.get(self.config.source_URL)
            response.raise_for_status()

            # Save file
            with open(self.config.local_data_file, "wb") as file:
                file.write(response.content)

            file_size = os.path.getsize(self.config.local_data_file)

            logger.info(f"File downloaded successfully!")
            logger.info(f"File location: {self.config.local_data_file}")
            logger.info(f"File size: {file_size} bytes")

        except Exception as e:
            logger.error(f"Error while downloading file: {e}")
            raise e

    # Extract zip file
    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir

        # Create unzip directory
        os.makedirs(unzip_path, exist_ok=True)

        if not os.path.exists(self.config.local_data_file):

            logger.error(f"File not found: {self.config.local_data_file}")

            raise FileNotFoundError(f"File not found: {self.config.local_data_file}")

        # Validate ZIP file
        if not zipfile.is_zipfile(self.config.local_data_file):

            logger.error(f"{self.config.local_data_file} is not a valid ZIP file")

            raise ValueError(f"{self.config.local_data_file} is not a valid ZIP file")

        try:
            logger.info("Starting ZIP extraction...")

            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)

            logger.info(f"ZIP extracted successfully to: {unzip_path}")

        except Exception as e:
            logger.error(f"Error while extracting ZIP file: {e}")
            raise e
