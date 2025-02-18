from datetime import datetime
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox

from src.controller.Server import Server
from src.data import GenerateFileRequest
from.widgets import *

class Form(QWidget):

    _INPUT_KEYS = ["year", "semester", "receipt", "additional"]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__form_inputs : dict[str, FormInput] = {}
        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle("증빙 자료 파일 생성기")
        self.resize(800, 600)

        layout = QVBoxLayout()

        self.__form_inputs["year"] = ComboInput(
            self, "연도",
            (lambda year: [str(year-1), str(year)])(datetime.now().year),
            True
        )

        self.__form_inputs["semester"] = ComboInput(
            self, "학기", ["1", "2"], True
        )

        self.__form_inputs["receipt"] = PathInput(self, "영수증", True)
        self.__form_inputs["additional"] = PathInput(self, "기타증빙자료", False)

        for key in self._INPUT_KEYS:
            layout.addWidget(self.__form_inputs[key])

        submit_btn = QPushButton("파일 생성")
        submit_btn.clicked.connect(self.__on_submit)
        layout.addWidget(submit_btn)

        self.setLayout(layout)

    def __on_submit(self):

        if any(not self.__form_inputs[key].validate() for key in self._INPUT_KEYS):
            return

        request = []

        for key in self._INPUT_KEYS[2:]:

            if self.__form_inputs[key].data:

                request.append(GenerateFileRequest(
                    self.__form_inputs["year"].data,
                    self.__form_inputs["semester"].data,
                    self.__form_inputs[key].desc,
                    self.__form_inputs[key].data,
                ))

        response = Server().generate_file(request)

        for res in response:
            QMessageBox.information(self, "", res.message)
            QMessageBox.show(self)