import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QColor  

class FIFOApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(FIFOApp, self).__init__()
        uic.loadUi("FIFO.ui", self)

        # Connect buttons
        self.generate.clicked.connect(self.generate_reference_string)
        self.run.clicked.connect(self.run_fifo_algorithm)

    def generate_reference_string(self):
        """Generate a random reference string and display it."""
        reference_string = [str(random.randint(0, 9)) for _ in range(20)]
        self.reference.setText(",".join(reference_string))

    def run_fifo_algorithm(self):
        """Runs the FIFO page replacement algorithm and displays the result."""
        ref_string = self.reference.text().strip()
        frame_count_text = self.frames.text().strip()

        if not ref_string or not frame_count_text:
            QMessageBox.warning(self, "Input Error", "Please enter a reference string and frame count.")
            return

        try:
            frame_count = int(frame_count_text)
            if frame_count <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Frame count must be a positive integer.")
            return

        try:
            reference_list = [int(x) for x in ref_string.split(",")]
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Reference string must contain only integers separated by commas.")
            return

        # Run FIFO Algorithm
        table, status_list = self.fifo_algorithm(reference_list, frame_count)

        # Display results
        self.display_results(reference_list, table, frame_count, status_list)

    def fifo_algorithm(self, reference_list, frame_count):
        """Correct FIFO Page Replacement Algorithm."""
        frame_queue = []
        table = []
        status_list = []

        for page in reference_list:
            snapshot = frame_queue.copy()  # Store a snapshot before modification

            if page in frame_queue:
                status_list.append("Hit")  # ✅ Correct hit detection
            else:
                status_list.append("Miss")
                if len(frame_queue) < frame_count:
                    frame_queue.append(page)  # Add new page if space is available
                else:
                    frame_queue.pop(0)  # ✅ Remove the oldest page (FIFO)
                    frame_queue.append(page)  # Add new page

            # Store updated snapshot with proper frame alignment
            snapshot = frame_queue.copy()
            while len(snapshot) < frame_count:
                snapshot.append("")  # Fill empty spaces

            table.append(snapshot)

        return table, status_list


    def display_results(self, reference_list, table, frame_count, status_list):
        """Display results in the QTableWidget."""
        self.tableWidget.clear()

        num_columns = len(reference_list)  # Number of columns should match reference string length
        self.tableWidget.setRowCount(frame_count + 1)  # Frames + Status row
        self.tableWidget.setColumnCount(num_columns)

        # Set column headers to reference string values
        for col, val in enumerate(reference_list):
            self.tableWidget.setHorizontalHeaderItem(col, QTableWidgetItem(str(val)))

        # Fill table with page frames
        for row in range(frame_count):  # Frame rows
            self.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(f"Frame {row + 1}"))
            for col in range(len(table)):
                item_value = str(table[col][row]) if table[col][row] != "" else ""
                self.tableWidget.setItem(row, col, QTableWidgetItem(item_value))

        # Fill status row (Hit/Miss)
        self.tableWidget.setVerticalHeaderItem(frame_count, QTableWidgetItem("Status"))
        for col in range(len(reference_list)):
            status = status_list[col]  # ✅ Use precomputed status from `fifo_algorithm()`
            item = QTableWidgetItem(status)
            if status == "Hit":
                item.setBackground(QColor(144, 238, 144))  # Light green for hits
            else:
                item.setBackground(QColor(255, 182, 193))  # Light red for misses
            self.tableWidget.setItem(frame_count, col, item)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FIFOApp()
    window.show()
    sys.exit(app.exec_())
