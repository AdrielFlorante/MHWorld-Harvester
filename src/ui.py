import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QSpinBox,
    QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QMessageBox, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Assuming these are in the same folder or correctly imported
from Crop import Crop
from Fertilizer import Fertilizer
from AStarSearch import AStarSearch

def run_ui_app():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Use modern Fusion style
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🌾 MHWorld Harvester Planner")
        self.setMinimumSize(700, 500)
        self.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }
            QPushButton {
                background-color: #0078D7;
                color: white;
                padding: 8px 16px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #005bb5;
            }
            QComboBox {
                padding: 4px;
                min-width: 140px;
            }
            QSpinBox {
                padding: 4px;
            }
            QTextEdit {
                background-color: #f4f4f4;
                border: 1px solid #ccc;
                padding: 10px;
                font-family: Consolas, monospace;
            }
        """)

        self.crops_list = [
            Crop("Herb", 1, 2, "Plant"),
            Crop("Nullberry", 2, 4, "Plant"),
            Crop("Might Seed", 2, 4, "Plant"),
            Crop("Dragonfall Berry", 3, 6, "Plant"),
            Crop("Needleberry", 1, 20, "Plant"),
            Crop("Honey", 1, 2, "Insect"),
            Crop("Flashbug", 2, 4, "Insect"),
            Crop("Godbug", 3, 8, "Insect"),
            Crop("Bitterbug", 1, 2, "Insect"),
            Crop("Thunderbug", 1, 2, "Insect"),
            Crop("Devil's Blight", 3, 4, "Mushroom"),
            Crop("Exciteshroom", 2, 4, "Mushroom"),
            Crop("Toadstool", 1, 2, "Mushroom"),
            Crop("Mandragora", 2, 4, "Mushroom"),
            Crop("Blue Mushroom", 1, 2, "Mushroom")

        ]

        self.fertilizers = [
            Fertilizer("Soft Soil", 5, 300, "SoftSoil"),
            Fertilizer("Catalyst", 4, 150, "Catalyst"),
            Fertilizer("Ancient Catalyst", 4, 250, "AncientCatalyst"),
            Fertilizer("Plant Fertilizer", 3, 50, "BoostPlant"),
            Fertilizer("Mushroom Substrate", 3, 50, "BoostMushroom"),
            Fertilizer("Summoner Jelly", 3, 50, "BoostInsect"),
            Fertilizer("None", 0, 0, "None")
        ]

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Header
        title = QLabel("MHWorld Harvester Optimal Fertilizer Planner")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Crop selection
        crop_row = QHBoxLayout()
        crop_row.addWidget(QLabel("Select 3 crops:"))

        self.crop_selectors = []
        for i in range(3):
            combo = QComboBox()
            for crop in self.crops_list:
                combo.addItem(crop.name)
            self.crop_selectors.append(combo)
            crop_row.addWidget(combo)
        layout.addLayout(crop_row)

        # Cycle input
        cycle_row = QHBoxLayout()
        cycle_row.addWidget(QLabel("Number of cycles:"))
        self.cycles_input = QSpinBox()
        self.cycles_input.setMinimum(1)
        self.cycles_input.setMaximum(100)
        self.cycles_input.setValue(15)
        cycle_row.addWidget(self.cycles_input)
        layout.addLayout(cycle_row)

        # Run button
        self.run_button = QPushButton("🔍 Run")
        self.run_button.clicked.connect(self.on_run_clicked)
        layout.addWidget(self.run_button, alignment=Qt.AlignCenter)

        # Output box
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setMinimumHeight(200)
        layout.addWidget(self.output_text)

        self.setLayout(layout)

    def on_run_clicked(self):
        selected_names = [combo.currentText() for combo in self.crop_selectors]

        if len(set(selected_names)) < 3:
            QMessageBox.warning(self, "Invalid selection", "Please select 3 different crops.")
            return

        selected_crops = [next((c for c in self.crops_list if c.name == name), None)
                          for name in selected_names]

        cycles = self.cycles_input.value()
        result = AStarSearch.search(selected_crops, self.fertilizers, cycles)

        output_lines = [f"🌱 Optimal Fertilizer Plan over {cycles} cycles:\n"]
        for i, fert in enumerate(result.plan, start=1):
            fert_name = fert.name if fert else "No Fertilizer"
            output_lines.append(f"Cycle {i:02d}: {fert_name}")

        output_lines.append("\n🌾 Final Yields:")
        total_yield = 0
        for crop in result.finalCrops:
            output_lines.append(f"- {crop.name}: {crop.yield_amount}")
            total_yield += crop.yield_amount

        output_lines.append(f"\n📦 Total Yield: {total_yield}")
        output_lines.append(f"💰 Total Cost: {result.totalCost}")

        self.output_text.setText("\n".join(output_lines))


if __name__ == "__main__":
    run_ui_app()
