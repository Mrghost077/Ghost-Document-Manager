
from PySide6.QtCore import Qt
from pathlib import Path
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QSizePolicy,
    QGridLayout
)

from ghost.presentation.resources.styles import (
    colors,
    dimensions,
    typography
)

from ghost.presentation.widgets.tool_card import ToolCard
from ghost.presentation.resources.tool_catalog import PDF_TOOLS


class PDFToolsPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setAttribute(
            Qt.WidgetAttribute.WA_StyledBackground,
            True
        )

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

        heading = QLabel("PDF Tools")

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
            "Everything you need to organize, optimize and convert your PDFs."
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


        # Tool catalogue grid
        tools_layout = QGridLayout()

        tools_layout.setHorizontalSpacing(16)
        tools_layout.setVerticalSpacing(16)

        icon_directory = (
            Path(__file__).resolve().parent.parent
            / "resources"
            / "icons"
        )

        for index, tool in enumerate(PDF_TOOLS):

            row = index // 3
            column = index % 3

            icon_path = icon_directory / f"{tool['icon']}.svg"

            card = ToolCard(
                title=tool["title"],
                description=tool["description"],
                icon_path=icon_path
            )

            tools_layout.addWidget(card, row, column)

        layout.addLayout(tools_layout)

