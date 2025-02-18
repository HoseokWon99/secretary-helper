import os
import time
import pandas as pd
from .ProofDocument import ProofDocument
from pathlib import Path

class NoImageExistsException(Exception):
    def __init__(self, path: str):
        super().__init__(f"{path} 폴더에 이미지 파일이 존재하지 않습니다. 다른 폴더를 선택해주세요.")

class ProofDocumentGenerator:
    _IMG_EXTS = ['jpg', 'jpeg', 'png']

    def __init__(self):
       pass

    def generate(
            self,
            year: int,
            semester: int,
            desc: str,
            path: str,
            out_dir: Path
    ):
        proof_document = ProofDocument(year, semester, desc)
        images = self.__get_images(path)

        if not images.size:
            raise NoImageExistsException(path)

        for _, row in images.iterrows():
            proof_document.append_content(row['index'], row['image'])

        (proof_document.to_docx(str(
            out_dir.joinpath(f"증빙자료({desc})-{int(time.time())}.docx")
        )))

    @staticmethod
    def __get_images(path)->pd.DataFrame:

        filenames = list(filter(
            lambda fpath: any(fpath.lower().endswith(exts) for exts in ProofDocumentGenerator._IMG_EXTS),
            os.listdir(path)
        ))

        data = map(
            lambda filename: [int(filename.split('.')[0]), f"{path}/{filename}"],
            filenames
        )


        images = pd.DataFrame(data=data, columns=['index', 'image'])
        images.astype({'index': int, 'image': str}, copy=False)
        images.sort_values('index', inplace=True)

        return images



