# Dynamic Memory Management Visualizer

## 📌 Overview

Dynamic Memory Management Visualizer is a PyQt5-based application designed to **simulate and visualize memory management techniques** such as **Paging, Segmentation, and Virtual Memory**. Additionally, it includes **FIFO and LRU page replacement algorithms** to enhance understanding of memory management.

## 🚀 Features

- **Paging Simulation** 📄: Divides memory into fixed-size pages.
- **Segmentation Simulation** 🔍: Demonstrates variable-size memory segments (Code, Data, Stack).
- **Virtual Memory Simulation** 🔄: Shows page swapping and memory mapping.
- **FIFO (First-In-First-Out) Page Replacement** 🕒: Simulates how pages are replaced using FIFO.
- **LRU (Least Recently Used) Page Replacement** 📉: Implements LRU algorithm to replace pages.
- **User-Friendly UI** 🎨: Tab-based layout for easy navigation and visualization.
- **Error Handling** ⚠️: Prevents invalid inputs and provides warnings.

## 📂 Project Structure

```
DynamicMemoryVisualizer/
│── main.py                   # Main application file
│── fifo_window.py            # FIFO algorithm window
│── lru_window.py             # LRU algorithm window
│── ui_mainwindow.py          # UI file generated from Qt Designer
│── README.md                 # Documentation
```

## 🛠️ Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/DynamicMemoryVisualizer.git
   cd DynamicMemoryVisualizer
   ```
2. **Install dependencies**
   ```sh
   pip install PyQt5
   ```
3. **Run the application**
   ```sh
   python main.py
   ```

## 📖 Usage

1. **Run the application**
2. **Choose a tab**
   - "Simulate Paging" to visualize fixed-size page allocation.
   - "Simulate Segmentation" to view variable-sized memory segments.
   - "Simulate Virtual Memory" to see page swapping in action.
3. **Enter Memory Size & Page Size**
4. **Click the "Simulate" button**
5. **Click FIFO or LRU buttons** to open their respective windows (if not already open).

## 🛠️ Future Enhancements

- ✅ Allow user-defined segment sizes for segmentation.
- ✅ Improve UI theme for better clarity.
- 🔜 Add more memory management algorithms.
- 🔜 Optimize visualization with animations.

## 🤝 Contributing

1. Fork the repository 🍴
2. Create your feature branch 🚀
   ```sh
   git checkout -b feature-name
   ```
3. Commit your changes 💡
   ```sh
   git commit -m "Added new feature"
   ```
4. Push to the branch 📤
   ```sh
   git push origin feature-name
   ```
5. Open a Pull Request 🔁

##

---

Feel free to contribute and improve the project! 🎉

