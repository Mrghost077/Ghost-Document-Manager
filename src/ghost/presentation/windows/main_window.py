from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFrame,
)


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

        # Sidebar
        sidebar = QWidget()
        sidebar.setStyleSheet("""
            background-color: #172033;
        """)
        sidebar.setFixedWidth(220)

        sidebar_layout = QVBoxLayout(sidebar)

        sidebar_layout.setSpacing(8)
        sidebar_layout.setContentsMargins(24, 28, 24, 20)

        # Branding container
        branding = QWidget()
        branding_layout = QVBoxLayout(branding)

        branding_layout.setSpacing(5)
        branding_layout.setContentsMargins(0, 0, 0, 0)

        # Application title
        title = QLabel("GHOST")
        title.setStyleSheet("""
            color: white;
            font-size: 22px;
            font-weight: bold;
        """)

        # Application subtitle
        subtitle = QLabel("Document Manager")
        subtitle.setStyleSheet("""
            color: #AAB6C8;
            font-size: 12px;
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

        # Add both sections to the main layout
        main_layout.addWidget(sidebar)
        main_layout.addWidget(workspace)