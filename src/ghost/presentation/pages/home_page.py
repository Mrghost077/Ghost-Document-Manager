from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSizePolicy
)

from ghost.presentation.resources.styles import colors, dimensions, typography
from ghost.presentation.widgets.tool_card import ToolCard


class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

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

        # Recently Used Tab
        layout.addSpacing(dimensions.SPACE_3XL)

        recent_tools_heading = QLabel("Recently Used")

        recent_tools_heading.setStyleSheet(f"""
            color: {colors.TEXT_PRIMARY};
            font-family: "{typography.FONT_FAMILY}";
            font-size: {typography.SIZE_SECTION}px;
            font-weight: {typography.WEIGHT_SEMIBOLD};
        """)

        layout.addWidget(recent_tools_heading)

        icon_path = (
            Path(__file__).resolve().parents[1]
            / "resources"
            / "icons"
            / "merge.svg"
        )

        merge_card = ToolCard(
            "Merge PDFs",
            "Combine multiple PDF files into one document.",
            icon_path
        )
        merge_card.setMaximumWidth(360)
        recent_tools_layout = QHBoxLayout()
        recent_tools_layout.setSpacing(dimensions.SPACE_LG)

        recent_tools_layout.addWidget(merge_card)
        recent_tools_layout.addStretch()

        layout.addLayout(recent_tools_layout)