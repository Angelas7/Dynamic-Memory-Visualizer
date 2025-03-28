import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QColor
from PyQt5 import uic
from lru import LRUApp
from fifo import FIFOApp

class MemoryVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)  # Load UI file
        self.setWindowTitle("Memory Visualizer")
        
        # Connect buttons to methods
        self.run.clicked.connect(self.simulate_paging)
        self.run_2.clicked.connect(self.simulate_segmentation)
        self.run_3.clicked.connect(self.simulate_virtual_memory)
        self.fifo_btn.clicked.connect(self.open_fifo_window)
        self.lru_btn.clicked.connect(self.open_lru_window)
        self.fifo_window = None
        self.lru_window = None
    
    def simulate_paging(self):
        """Simulate paging by dividing memory into fixed-size pages."""
        try:
            memory_size_text = self.memory_input.text().strip()
            page_size_text = self.page_input.text().strip()

            if not memory_size_text or not page_size_text:
                raise ValueError("Memory size and page size cannot be empty.")

            memory_size = int(memory_size_text)
            page_size = int(page_size_text)

            if memory_size <= 0 or page_size <= 0:
                raise ValueError("Memory size and page size must be positive integers.")

            num_pages = memory_size // page_size

            self.memory_table.setRowCount(1)
            self.memory_table.setColumnCount(num_pages)

            for i in range(num_pages):
                item = QTableWidgetItem(f"Page {i}")
                item.setBackground(QColor(144, 238, 144))  # Light green
                self.memory_table.setItem(0, i, item)

        except ValueError as e:
            
            QMessageBox.warning(self, "Input Error", f"Invalid input: {str(e)}")


    def simulate_segmentation(self):
        """Simulate segmentation by dividing memory into variable-size segments."""
        try:
            memory_size = int(self.memorySizeSegmentation.text())
            segments = [("Code", memory_size * 0.4), ("Data", memory_size * 0.3), ("Stack", memory_size * 0.3)]
            
            self.tableSegmentation.setRowCount(1)
            self.tableSegmentation.setColumnCount(len(segments))
            
            for i, (name, size) in enumerate(segments):
                item = QTableWidgetItem(f"{name} ({int(size)} KB)")
                item.setBackground(QColor(255, 182, 193))  # Light red
                self.tableSegmentation.setItem(0, i, item)
        
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Enter a valid memory size.")

    def simulate_virtual_memory(self):
        """Simulate virtual memory by showing page swapping."""
        try:
            memory_size = int(self.memorySizeVirtual.text())
            page_size = int(self.pageSizeVirtual.text())
            if page_size <= 0:
                raise ValueError("Page size must be greater than 0.")
            
            num_pages = memory_size // page_size
            self.tableVirtualMemory.setRowCount(1)
            self.tableVirtualMemory.setColumnCount(num_pages + 1)  # Extra for swapped page
            
            for i in range(num_pages):
                item = QTableWidgetItem(f"Page {i}")
                item.setBackground(QColor(144, 238, 144))  # Light green
                self.tableVirtualMemory.setItem(0, i, item)
            
            swapped_item = QTableWidgetItem("Swapped Page")
            swapped_item.setBackground(QColor(255, 182, 193))  # Light red
            self.tableVirtualMemory.setItem(0, num_pages, swapped_item)
        
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Enter valid memory and page size.")

    def open_fifo_window(self):
        """Open FIFO Page Replacement window only if it's not already open."""
        if self.fifo_window is None or not self.fifo_window.isVisible():
            self.fifo_window = FIFOApp()
            self.fifo_window.show()
    
    def open_lru_window(self):
        """Open LRU Page Replacement window only if it's not already open."""
        if self.lru_window is None or not self.lru_window.isVisible():
            self.lru_window = LRUApp()
            self.lru_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MemoryVisualizer()
    window.show()
    sys.exit(app.exec_())
