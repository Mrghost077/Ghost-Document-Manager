from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from ghost.presentation.resources.styles import colors, dimensions, typography


class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(f"""
            background-color: {colors.APP_BACKGROUND};
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            dimensions.SPACE_3XL,
            dimensions.SPACE_3XL,
            dimensions.SPACE_3XL,
            dimensions.SPACE_2XL
        )

        layout.setSpacing(dimensions.SPACE_SM)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        heading = QLabel("Give your documents a little peace.")

        heading.setStyleSheet(f"""
            color: {colors.TEXT_PRIMARY};
            font-family: "{typography.FONT_FAMILY}";
            font-size: {typography.SIZE_HEADING}px;
            font-weight: {typography.WEIGHT_SEMIBOLD};
        """)

        heading.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Fixed
        )

        layout.addWidget(heading)

        description = QLabel(
            "Simple tools to manage your documents, right on your desktop."
        )

        description.setStyleSheet(f"""
            color: {colors.TEXT_SECONDARY};
            font-family: "{typography.FONT_FAMILY}";
            font-size: {typography.SIZE_BODY}px;
            font-weight: {typography.WEIGHT_NORMAL};
        """)

        description.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Fixed
        )

        layout.addWidget(description)