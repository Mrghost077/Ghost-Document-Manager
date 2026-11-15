
from PySide6.QtCore import Qt
from pathlib import Path
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QSizePolicy,
    QGridLayout,
    QHBoxLayout,
    QPushButton,
    QButtonGroup
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


        # Category filter buttons
        filter_layout = QHBoxLayout()
        filter_layout.setSpacing(10)

        self.category_group = QButtonGroup(self)
        self.category_group.setExclusive(True)

        categories = ["All", "Organize", "Optimize", "Convert"]

        for category in categories:

            button = QPushButton(category)
            button.setCheckable(True)

            button.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #A6B2C2;
                    border: 1px solid #2B394B;
                    border-radius: 14px;
                    padding: 7px 16px;
                    font-size: 13px;
                }

                QPushButton:hover {
                    background-color: #243247;
                    color: #F2F5F9;
                }

                QPushButton:checked {
                    background-color: #C2C6CC;
                    color: #111722;
                    border: 1px solid #C2C6CC;
                    font-weight: 600;
                }
            """)

            self.category_group.addButton(button)
            filter_layout.addWidget(button)

            if category == "All":
                button.setChecked(True)

            button.clicked.connect(
                lambda checked=False, selected=category:
                    self.populate_tools(selected)
            )

        filter_layout.addStretch()

        layout.addLayout(filter_layout)


        # Tool catalogue grid
        self.tools_layout = QGridLayout()

        self.tools_layout.setHorizontalSpacing(16)
        self.tools_layout.setVerticalSpacing(16)

        layout.addLayout(self.tools_layout)

        self.icon_directory = (
                    Path(__file__).resolve().parent.parent
                    / "resources"
                    / "icons"
                )
        

        self.populate_tools()

        
    
    def populate_tools(self, selected_category="All"):

        while self.tools_layout.count():

            item = self.tools_layout.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

        # Create cards for the selected category
        for tool in PDF_TOOLS:

            if (
                selected_category != "All"
                and tool["category"] != selected_category
            ):
                continue

            row = self.tools_layout.count() // 3
            column = self.tools_layout.count() % 3

            icon_path = self.icon_directory / f"{tool['icon']}.svg"

            card = ToolCard(
                title=tool["title"],
                description=tool["description"],
                icon_path=icon_path
            )

            self.tools_layout.addWidget(card, row, column)

