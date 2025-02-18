import os
from pathlib import Path
from ..service import ProofDocumentGenerator
from ..data import GenerateFileRequest, GenerateFileResponse
from typing import Iterable
from concurrent.futures import ThreadPoolExecutor

class Server:
    _OUT_PATH = Path(os.path.expanduser("~")).joinpath("Desktop")

    def __init__(self):
        self.__service = ProofDocumentGenerator()

    def generate_file(self, requests: Iterable[GenerateFileRequest]) -> Iterable[GenerateFileResponse]:
       try:
           with ThreadPoolExecutor(max_workers=10) as executor:
               responses = executor.map(self.__handle_request, requests)
               return list(responses)
       except Exception as e:
           return [GenerateFileResponse(False, str(e))]

    def __handle_request(self, request: GenerateFileRequest) -> GenerateFileResponse:

        try:
            self.__service.generate(
                request.year,
                request.semester,
                request.description,
                request.images_directory,
                self._OUT_PATH
            )

            return GenerateFileResponse(True, f"파일이 {self._OUT_PATH}에 성공적으로 저장되었습니다")

        except Exception as e:
            return GenerateFileResponse(False, str(e))