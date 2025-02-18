from dataclasses import dataclass

@dataclass
class GenerateFileResponse:
    success: bool
    message: str