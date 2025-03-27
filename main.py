import tkinter as tk  # GUI Library
from memory_allocation import MemoryAllocator  # Import memory allocation module
from page_replacement import PageReplacement  # Import page replacement module
from visualization import MemoryVisualizer  # Import visualization module

# Initialize the main window
root = tk.Tk()
root.title("Dynamic Memory Management Visualizer")
root.geometry("800x600")  # Set window size

# Display a label in the GUI
label = tk.Label(root, text="Welcome to Memory Management Visualizer!", font=("Arial", 14))
label.pack(pady=20)

# Run the main event loop
root.mainloop()
