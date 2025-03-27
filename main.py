import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random

class MemoryManagementVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Dynamic Memory Management Visualizer")
        self.master.geometry("1200x800")
        self.master.configure(bg='#f0f0f0')

        # Memory management parameters
        self.total_memory_size = 1024  # 1 GB default
        self.page_size = 64  # 64 MB page size
        self.current_algorithm = tk.StringVar(value="FIFO")
        
        # Memory state tracking
        self.memory_pages = []
        self.page_faults = 0
        self.total_memory_accesses = 0

        # Create UI components
        self.create_ui()

    def create_ui(self):
        # Top Frame - Configuration
        config_frame = tk.Frame(self.master, bg='#f0f0f0')
        config_frame.pack(pady=10, padx=20, fill=tk.X)

        # Algorithm Selection
        tk.Label(config_frame, text="Page Replacement Algorithm:", bg='#f0f0f0').pack(side=tk.LEFT, padx=10)
        algorithm_dropdown = ttk.Combobox(
            config_frame, 
            textvariable=self.current_algorithm, 
            values=['FIFO', 'LRU'], 
            state='readonly',
            width=15
        )
        algorithm_dropdown.pack(side=tk.LEFT, padx=10)
        algorithm_dropdown.set('FIFO')

        # Memory Size Configuration
        tk.Button(config_frame, text="Configure Memory", command=self.configure_memory).pack(side=tk.LEFT, padx=10)

        # Simulation Control Buttons
        control_frame = tk.Frame(self.master, bg='#f0f0f0')
        control_frame.pack(pady=10)

        tk.Button(control_frame, text="Generate Random Access", command=self.simulate_memory_access).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Reset Simulation", command=self.reset_simulation).pack(side=tk.LEFT, padx=5)

        # Visualization Frame
        self.visualization_frame = tk.Frame(self.master, bg='white', borderwidth=2, relief=tk.SUNKEN)
        self.visualization_frame.pack(pady=10, padx=20, expand=True, fill=tk.BOTH)

        # Statistics Frame
        stats_frame = tk.Frame(self.master, bg='#f0f0f0')
        stats_frame.pack(pady=10, padx=20, fill=tk.X)

        # Statistics Labels
        self.page_fault_label = tk.Label(stats_frame, text="Page Faults: 0", bg='#f0f0f0')
        self.page_fault_label.pack(side=tk.LEFT, padx=10)

        self.memory_usage_label = tk.Label(stats_frame, text="Memory Usage: 0%", bg='#f0f0f0')
        self.memory_usage_label.pack(side=tk.LEFT, padx=10)

    def configure_memory(self):
        # Dialog to configure memory parameters
        total_memory = simpledialog.askinteger(
            "Memory Configuration", 
            "Enter Total Memory Size (MB):", 
            initialvalue=self.total_memory_size,
            minvalue=64,
            maxvalue=4096
        )
        
        if total_memory:
            self.total_memory_size = total_memory
            page_size = simpledialog.askinteger(
                "Page Size", 
                "Enter Page Size (MB):", 
                initialvalue=self.page_size,
                minvalue=4,
                maxvalue=256
            )
            
            if page_size:
                self.page_size = page_size
                messagebox.showinfo("Memory Configured", f"Memory set to {total_memory} MB with page size {page_size} MB")

    def simulate_memory_access(self):
        # Simulate memory access based on selected algorithm
        max_pages = self.total_memory_size // self.page_size
        page_to_access = random.randint(0, 100)  # Simulating page number

        self.total_memory_accesses += 1

        if self.current_algorithm.get() == 'FIFO':
            self.fifo_page_replacement(page_to_access, max_pages)
        else:
            self.lru_page_replacement(page_to_access, max_pages)

        # Update visualization and statistics
        self.update_visualization()
        self.update_statistics()

    def fifo_page_replacement(self, page, max_pages):
        # First-In-First-Out Page Replacement
        if page not in self.memory_pages:
            self.page_faults += 1
            
            if len(self.memory_pages) >= max_pages:
                # Remove the oldest page
                self.memory_pages.pop(0)
            
            self.memory_pages.append(page)

    def lru_page_replacement(self, page, max_pages):
        # Least Recently Used Page Replacement
        if page in self.memory_pages:
            # Move the page to the end (most recently used)
            self.memory_pages.remove(page)
        else:
            self.page_faults += 1
            
            if len(self.memory_pages) >= max_pages:
                # Remove the least recently used page
                self.memory_pages.pop(0)
        
        self.memory_pages.append(page)

    def update_visualization(self):
        # Clear previous visualization
        for widget in self.visualization_frame.winfo_children():
            widget.destroy()

        # Create canvas
        canvas = tk.Canvas(self.visualization_frame, bg='white')
        canvas.pack(expand=True, fill=tk.BOTH)

        # Visualization parameters
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        
        # Draw memory blocks
        block_width = width // (self.total_memory_size // self.page_size)
        for i, page in enumerate(self.memory_pages):
            x1 = i * block_width
            y1 = 0
            x2 = x1 + block_width
            y2 = height

            # Generate color based on page number
            color = self.generate_color(page)
            
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')
            canvas.create_text(
                (x1 + x2) / 2, 
                (y1 + y2) / 2, 
                text=str(page)
            )

    def generate_color(self, page):
        # Generate a consistent color for each page
        random.seed(page)
        r = random.randint(100, 220)
        g = random.randint(100, 220)
        b = random.randint(100, 220)
        return f'#{r:02x}{g:02x}{b:02x}'

    def update_statistics(self):
        # Update page fault and memory usage statistics
        self.page_fault_label.config(
            text=f"Page Faults: {self.page_faults} "
                 f"(Rate: {self.page_faults/self.total_memory_accesses*100:.2f}%)"
        )
        
        memory_usage = len(self.memory_pages) / (self.total_memory_size // self.page_size) * 100
        self.memory_usage_label.config(
            text=f"Memory Usage: {memory_usage:.2f}% "
                 f"({len(self.memory_pages)}/{self.total_memory_size // self.page_size} Pages)"
        )

    def reset_simulation(self):
        # Reset all simulation parameters
        self.memory_pages.clear()
        self.page_faults = 0
        self.total_memory_accesses = 0
        
        # Clear visualization
        for widget in self.visualization_frame.winfo_children():
            widget.destroy()
        
        # Reset statistics
        self.page_fault_label.config(text="Page Faults: 0")
        self.memory_usage_label.config(text="Memory Usage: 0%")

def main():
    root = tk.Tk()
    app = MemoryManagementVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
