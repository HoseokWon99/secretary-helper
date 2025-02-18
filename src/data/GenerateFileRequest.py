from dataclasses import dataclass

@dataclass
class GenerateFileRequest:
    year: int
    semester: int
    description: str
    images_directory: str