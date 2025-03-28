import sys
import random
from PyQt5 import QtWidgets, QtGui, uic

class LRUApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("LRU.ui", self)  # Load your UI file

        # Connect buttons
        self.generate.clicked.connect(self.generate_random_reference)
        self.run.clicked.connect(self.run_lru_algorithm)

    def generate_random_reference(self):
        """Generates a random reference string."""
        reference_string = [str(random.randint(0, 9)) for _ in range(20)]
        self.reference.setText(",".join(reference_string))

    def run_lru_algorithm(self):
        """Runs the LRU Page Replacement algorithm and updates the table."""
        reference_string = self.reference.text().split(',')
        reference_string = [int(x) for x in reference_string if x.isdigit()]
        frames = self.frames.text()

        if not frames.isdigit():
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter a valid number of frames.")
            return
        
        frames = int(frames)
        self.lru_algorithm(reference_string, frames)
        hit_count = sum(1 for i in range(self.tableWidget.columnCount()) if self.tableWidget.item(self.tableWidget.rowCount()-1, i).text().lower() == "hit")
        miss_count = self.tableWidget.columnCount() - hit_count
        hit_ratio = hit_count / self.tableWidget.columnCount()

        self.ratio.setText(f"Page Faults: {miss_count} | Hit Ratio: {hit_ratio:.2f}")

    def lru_algorithm(self, reference_string, frames):
        """Executes the LRU algorithm and displays the results in the table."""
        n = len(reference_string)
        self.tableWidget.setRowCount(frames + 1)  # Extra row for status
        self.tableWidget.setColumnCount(n)
        
        # Set column headers (Page number sequence)
        self.tableWidget.setHorizontalHeaderLabels([str(i+1) for i in range(n)])
        self.tableWidget.setVerticalHeaderLabels(
            [f"Frame {i+1}" for i in range(frames)] + ["Status"]
        )

        page_frames = []
        page_order = []
        status = []
        
        for i in range(n):
            page = reference_string[i]

            if page in page_frames:
                status.append("Hit")
                page_order.remove(page)
            else:
                if len(page_frames) < frames:
                    page_frames.append(page)
                else:
                    # LRU Replacement: Remove the least recently used page
                    lru_page = page_order.pop(0)
                    index = page_frames.index(lru_page)
                    page_frames[index] = page
                status.append("Miss")
            
            page_order.append(page)

            # Update Table
            for j in range(frames):
                if j < len(page_frames):
                    item = QtWidgets.QTableWidgetItem(str(page_frames[j]))
                    self.tableWidget.setItem(j, i, item)

            # Add status row
            item = QtWidgets.QTableWidgetItem(status[-1])
            self.tableWidget.setItem(frames, i, item)

        # Apply coloring
        self.update_table_style()

    def update_table_style(self):
        """Updates table styling by coloring 'Hit' and 'Miss' cells differently."""
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    if item.text().lower() == "hit":
                        item.setBackground(QtGui.QColor("#C8E6C9"))  # Light green for "Hit"
                        item.setForeground(QtGui.QColor("#1B5E20"))  # Dark green text
                    elif item.text().lower() == "miss":
                        item.setBackground(QtGui.QColor("#FFCDD2"))  # Light red for "Miss"
                        item.setForeground(QtGui.QColor("#B71C1C"))  # Dark red text


