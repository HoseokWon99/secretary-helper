from PyQt6.QtWidgets import QWidget, QLayout, QMessageBox, QLabel
from abc import abstractmethod

class FormInput(QWidget):

    def __init__(
            self,
            parent: QWidget,
            layout: QLayout,
            desc: str,
            required: bool = False
    ):
        super().__init__(parent)
        self._layout = layout

        self._label = QLabel(desc if required else f"{desc} (선택사항)", self)
        self._layout.addWidget(self._label)

        self.desc = desc
        self.required = required
        self.data = None

    def _register(self, *widgets: QWidget):

        for widget in widgets:
            self._layout.addWidget(widget)

        self.setLayout(self._layout)

    @abstractmethod
    def _update_data(self):
        pass

    def validate(self) -> bool:

        if self.required and self.data is None:

            QMessageBox.warning(
                self,
                f"{self.desc}가 입력 되지 않았습니다!",
                f"{self.desc}를 입력 해 주세요!"
            )

            QMessageBox.show(self)

            return False

        return True



