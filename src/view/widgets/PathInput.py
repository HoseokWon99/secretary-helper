import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel, QMessageBox
from overrides import overrides
from .FormInput import FormInput

class PathInput(FormInput):

    def __init__(
            self,
            parent: QWidget,
            desc: str,
            required: bool = False,
    ):
        super().__init__(parent, QVBoxLayout(), desc, required)

        self.__label = QLabel(".    .   .", self)
        self.__label.adjustSize()
        self.__label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__label.setStyleSheet("QLabel { background-color : gray; color : white; }")

        self.__button = QPushButton(f"{self.desc} 폴더 선택", self)
        self.__button.clicked.connect(self.__on_selected)

        self._register(self.__label, self.__button)


    def __on_selected(self):
        self._update_data()

        if self.data:
            self.__label.setText(self.data)
            self.__label.adjustSize()


    @overrides
    def _update_data(self):
        self.data = QFileDialog.getExistingDirectory(self, "열기", os.path.expanduser("~"))

    @overrides
    def validate(self)-> bool:

        if not super().validate():
            return False

        if self.data is None:
            return True

        if not os.path.isdir(self.data):

            QMessageBox.warning(
                self,
                "유효하지 않은 경로",
                f"{os.path.basename(self.data)}는 폴더가 아닙니다!"
            )

            return False

        return True