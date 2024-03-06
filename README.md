# File Sorter Based on Camera and Android Models

This Python script was created as a personal project to sort personal photographs based on their camera and Android models. It extracts metadata from files using ExifTool, identifies the camera and Android model of each file, and sorts them into different directories based on this information.


## Prerequisites

### Python

The script requires Python 3.6 or later. You can download Python from the [official website](https://www.python.org/downloads/). After installation, you can verify the Python version by running the following command in a terminal:

```bash
python --version
```

### ExifTool

ExifTool is a platform-independent Perl library plus a command-line application for reading, writing, and editing meta information in a wide variety of files. You can download ExifTool from the [official website](https://exiftool.org/). After installation, add ExifTool to your system's PATH.

### colorama

colorama is a Python library for cross-platform colored terminal text. You can install colorama using pip, which is a package manager for Python.

```bash
pip install colorama
```

## Configuration

Before running the script, you need to configure it according to your requirements. Open the script in a text editor and modify the following variables:

- `source_dir`: The directory that the script will scan for files.
- `camera_target_dir`: The subdirectory where the script will move files that match the specified camera model.
- `phone_target_dir`: The subdirectory where the script will move files that match the specified Android phone model.
- `camera_model`: The camera model that the script will look for.
- `phone_model`: The Android phone model that the script will look for.

## Usage

After configuring the script, you can run it with Python:

```bash
python photoExifSorter.py
```

## Detailed Workflow

1. The script first ensures that the `camera_target_dir` and `phone_target_dir` directories exist, creating them if necessary.
2. It then iterates over each file in the `source_dir`.
3. For each file, it uses ExifTool to extract the metadata. Specifically, it extracts the "Model" field (for the camera model) and the "AndroidModel" field (for the Android model).
4. It compares these extracted values to the `camera_model` and `phone_model` specified at the top of the script.
5. If the extracted camera model matches `camera_model`, it moves the file to the `camera_target_dir` directory.
6. If the extracted Android model matches `phone_model`, it moves the file to the `phone_target_dir` directory.
7. If there's an error processing a file, it prints an error message and continues with the next file.


## Error Handling

The script includes basic error handling. If there's an error while processing a file (for example, if the file can't be read, or if the metadata can't be extracted), the script will print an error message and continue with the next file. The error message includes the filename and a description of the error.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Disclaimer

This script was developed as a personal project for sorting personal photographs. It is provided as-is, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.