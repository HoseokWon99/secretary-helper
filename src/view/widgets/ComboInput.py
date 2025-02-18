from PyQt6.QtWidgets import QWidget, QHBoxLayout, QComboBox
from overrides import overrides
from .FormInput import FormInput


class ComboInput(FormInput):

    @staticmethod
    def __make_items(items: list[str]) -> list:
        res = ["select..."]
        res.extend(items)
        return res

    def __init__(
            self,
            parent: QWidget,
            desc: str,
            items: list[str],
            required: bool = False):

        super().__init__(parent, QHBoxLayout(), desc, required)
        self.__combo = QComboBox()
        self.__combo.addItems(self.__make_items(items))
        self.__combo.currentTextChanged.connect(self._update_data)
        self._register(self.__combo)

    @overrides
    def _update_data(self):
        if self.__combo.currentText() != "select...":
            self.data = self.__combo.currentText()