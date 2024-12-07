# Tkinter Replacement Project

This repository contains a simple GUI program implemented using different Python GUI toolkits. The main file, `version_tkinter`, uses Tkinter, while the other Python files implement the same application using various other toolkits.

## Getting Started

To get started with this project, you need to create a virtual environment and install the dependencies listed in `requirements.txt`.

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Setting Up the Virtual Environment

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Create a virtual environment by running the following command:
   ```sh
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```

### Installing Dependencies

Once the virtual environment is activated, install the required dependencies listed in [`requirements.txt`](requirements.txt) using `pip`:

```sh
pip install -r requirements.txt
```

### Running the Application

After installing the dependencies, you can run any of the GUI applications. For example, to run the Tkinter version, use the following command:

```sh
python version_tkinter.py
```

Replace `version_tkinter.py` with the appropriate file name for other toolkits.

## Toolkits Used

The following Python GUI toolkits are used in this project:

- NiceGUI ([nicegui.io](https://nicegui.io)): A modern Python UI framework
- GTK3 ([gtk.org](https://www.gtk.org)): The GNOME GUI toolkit
- Flet ([flet.dev](https://flet.dev)): Flutter-based toolkit for Python
- Streamlit ([streamlit.io](https://streamlit.io)): Web-based interactive applications
- Kivy ([kivy.org](https://kivy.org)): Multi-touch application framework
- wxPython ([wxpython.org](https://wxpython.org)): Native GUI toolkit wrapper

For a detailed comparison and review of these toolkits, check out [`notes.csv`](notes.csv) in this repository.
