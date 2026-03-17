import os
import xml.etree.ElementTree as ET
import csv

class LogicProMetadataExtractor:
    def __init__(self, project_file):
        self.project_file = project_file
        self.metadata = {}

    def extract_metadata(self):
        """Extract metadata from the Logic Pro project file."""
        if not os.path.isfile(self.project_file):
            raise FileNotFoundError(f"Project file not found: {self.project_file}")

        try:
            tree = ET.parse(self.project_file)
            root = tree.getroot()
            
            name_elem = root.find('name')
            self.metadata['project_name'] = name_elem.text if name_elem is not None else 'Unknown'
            
            tempo_elem = root.find('tempo')
            self.metadata['tempo'] = tempo_elem.text if tempo_elem is not None else 'Unknown'
            
            time_sig_elem = root.find('time_signature')
            self.metadata['time_signature'] = time_sig_elem.text if time_sig_elem is not None else 'Unknown'
            
            self.metadata['track_count'] = len(root.findall('track'))

            # TODO: Extract more metadata if needed (instruments, effects, etc.)
        except ET.ParseError as e:
            raise ValueError(f"Error parsing XML: {e}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error: {e}")

        return self.metadata

    def save_metadata_to_csv(self, csv_file):
        """Save extracted metadata to a CSV file."""
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.metadata.keys())  # Write header
            writer.writerow(self.metadata.values())  # Write data

if __name__ == "__main__":
    # Example usage
    extractor = LogicProMetadataExtractor('example.logic')
    try:
        meta = extractor.extract_metadata()
        extractor.save_metadata_to_csv('metadata.csv')
        print("Metadata extracted and saved successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
