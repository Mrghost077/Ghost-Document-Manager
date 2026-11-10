from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFrame,
    QSizePolicy
)

from ghost.presentation.resources.styles import colors
from ghost.presentation.resources.styles import typography
from ghost.presentation.resources.styles import dimensions


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ghost Document Manager")
        self.resize(1050, 640)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main horizontal layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Sidebar
        sidebar = QWidget()
        sidebar.setStyleSheet(f"""
           background-color: {colors.SIDEBAR_BACKGROUND};
        """)
        sidebar.setFixedWidth(220)

        sidebar_layout = QVBoxLayout(sidebar)

        sidebar_layout.setSpacing(dimensions.SPACE_SM)
        sidebar_layout.setContentsMargins(
            dimensions.SPACE_XL,
            28,
            dimensions.SPACE_XL,
            dimensions.SPACE_LG
        )

        # Branding container
        branding = QWidget()
        branding_layout = QVBoxLayout(branding)

        branding_layout.setSpacing(dimensions.SPACE_XS)
        branding_layout.setContentsMargins(0, 0, 0, 0)

        # Application title
        title = QLabel("GHOST")
        title.setStyleSheet(f"""
            color: {colors.TEXT_PRIMARY};
            font-family: "{typography.FONT_FAMILY}";
            font-size: {typography.SIZE_BRAND}px;
            font-weight: {typography.WEIGHT_BOLD};
        """)

        # Application subtitle
        subtitle = QLabel("Document Manager")
        subtitle.setStyleSheet(f"""
            color: {colors.TEXT_SECONDARY};
            font-family: "{typography.FONT_FAMILY}";
            font-size: {typography.SIZE_SMALL}px;
            font-weight: {typography.WEIGHT_NORMAL};
        """)

        branding_layout.addWidget(title)
        branding_layout.addWidget(subtitle)

        # Add branding to sidebar
        sidebar_layout.addWidget(branding)

        # Navigation section heading
        sidebar_layout.addSpacing(30)

        section_label = QLabel("WORKSPACE")
        section_label.setStyleSheet("""
            color: #8996AB;
            font-size: 11px;
            font-weight: bold;
        """)

        sidebar_layout.addWidget(section_label)
                

        home_button = QPushButton("Home")
        home_button.setObjectName("active")

        pdf_button = QPushButton("PDF Tools")
        image_button = QPushButton("Image Tools")
        settings_button = QPushButton("Settings")

        sidebar_layout.addWidget(home_button)
        sidebar_layout.addWidget(pdf_button)
        sidebar_layout.addWidget(image_button)

        # Flexible empty space
        sidebar_layout.addStretch()

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet("color: #354158;")

        sidebar_layout.addWidget(separator)

        # Settings at the bottom
        sidebar_layout.addWidget(settings_button)

        # Navigation button styling
        button_style = """
            QPushButton {
                background-color: transparent;
                color: #DCE3EF;
                border: none;
                padding: 12px;
                text-align: left;
                border-radius: 6px;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #2B3D5D;
            }

            QPushButton#active {
                background-color: #2B3D5D;
                color: white;
                font-weight: bold;
            }
        """

        home_button.setStyleSheet(button_style)
        pdf_button.setStyleSheet(button_style)
        image_button.setStyleSheet(button_style)
        settings_button.setStyleSheet(button_style)

       # Workspace
        workspace = QWidget()

        workspace_layout = QVBoxLayout(workspace)

        workspace.setStyleSheet(f"""
            background-color: {colors.APP_BACKGROUND};
        """)

        workspace_layout.setContentsMargins(
            dimensions.SPACE_3XL,
            dimensions.SPACE_3XL,
            dimensions.SPACE_3XL,
            dimensions.SPACE_2XL
        )

        workspace_layout.setSpacing(dimensions.SPACE_SM)
        workspace_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Workspace heading
        heading = QLabel("Give your documents a little peace.")
        heading.setObjectName("workspaceHeading")
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

        workspace_layout.addWidget(heading)
        workspace_layout.addWidget(description)


        # Add both sections to the main layout
        main_layout.addWidget(sidebar)
        main_layout.addWidget(workspace)