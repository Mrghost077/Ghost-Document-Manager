
from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QWidget,
    QSizePolicy
)

from ghost.presentation.resources.styles import colors, typography



class ToolCard(QFrame):

    clicked = Signal()

    def __init__(self, title, description, icon_path, parent=None):
        super().__init__(parent)

        self.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Fixed
        )

        self.setObjectName("toolCard")

        self.setStyleSheet(f"""
            QFrame#toolCard {{
                background-color: {colors.SURFACE_BACKGROUND};
                border: 1px solid {colors.BORDER};
                border-radius: 10px;
            }}

            QFrame#toolCard:hover {{
                background-color: #243247;
                border: 1px solid {colors.ACCENT};
            }}
        """)

        self.setFrameShape(QFrame.Shape.NoFrame)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(4)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        content_layout = QHBoxLayout()
        content_layout.setSpacing(14)

        icon_label = QLabel()
        icon_label.setFixedSize(24, 24)

        icon_path = Path(icon_path)
        icon_label.setPixmap(QIcon(str(icon_path)).pixmap(24, 24))

        content_layout.addWidget(icon_label)
        content_layout.setAlignment(
            icon_label,
            Qt.AlignmentFlag.AlignVCenter
        )

        text_container = QWidget()

        text_layout = QVBoxLayout(text_container)
        text_layout.setContentsMargins(0, 0, 0, 0)
        text_layout.setSpacing(4)

        layout.addLayout(content_layout)

        title_label = QLabel(title)
        title_label.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Fixed
        )
        title_label.setStyleSheet(f"""
            color: {colors.TEXT_PRIMARY};
            font-family: "{typography.FONT_FAMILY}";
            font-size: {typography.SIZE_BODY}px;
            font-weight: {typography.WEIGHT_SEMIBOLD};
        """)

        text_layout.addWidget(title_label)

        description_label = QLabel(description)
        description_label.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Fixed
        )
        description_label.setStyleSheet(f"""
            color: {colors.TEXT_SECONDARY};
            font-family: "{typography.FONT_FAMILY}";
            font-size: {typography.SIZE_SMALL}px;
            font-weight: {typography.WEIGHT_NORMAL};
        """)

        description_label.setWordWrap(True)

        text_layout.addWidget(description_label)

        content_layout.addWidget(text_container, 1)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()

        super().mousePressEvent(event)