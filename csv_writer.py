import csv
import os

class CSVWriter:
    def __init__(self, filename):
        """Initialize the CSVWriter with the given filename."""
        self.filename = filename
        # Check if the file already exists to avoid overwriting
        if os.path.exists(self.filename):
            print(f"Warning: {self.filename} already exists and will be overwritten.")

    def write_metadata(self, metadata):
        """Write extracted metadata to a CSV file.

        Args:
            metadata (list of dict): A list of dictionaries containing metadata.
        """
        if not metadata:
            print("Error: No metadata to write.")
            return
        
        # Use the keys of the first dictionary as the CSV header
        headers = metadata[0].keys()

        try:
            with open(self.filename, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                writer.writerows(metadata)
                print(f"Successfully wrote metadata to {self.filename}")

        except IOError as e:
            print(f"Error writing to {self.filename}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# TODO: Add functionality to append to existing CSV files
# TODO: Implement better error handling and logging mechanisms
# TODO: Consider adding options for different CSV formats or delimiters
