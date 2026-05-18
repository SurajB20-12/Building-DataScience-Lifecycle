from src.DataScience_lifecycle import logger
from src.DataScience_lifecycle.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_colums(self) -> bool:
        try:
            validation_status = False
            data = pd.read_csv(self.config.unzip_data_dir)

            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for i in all_cols:
                if i not in all_schema:
                    validation_status = False

                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True

                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        except Exception as e:
            raise e
