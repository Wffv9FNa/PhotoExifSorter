import os
import shutil
import subprocess
import json
from colorama import Fore, Style

# The directory to scan
source_dir = "."

# The subdirectory to move matching camera files to
camera_target_dir = "Camera"

# The subdirectory to move matching phone files to
phone_target_dir = "Phone"

# The camera model to match
camera_model = "Canon LEGRIA HF R506"

# The phone model to match
phone_model = "motorola one zoom"

# Ensure the target directories exist
os.makedirs(camera_target_dir, exist_ok=True)
os.makedirs(phone_target_dir, exist_ok=True)

# Iterate over each file in the source directory
for file in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file)
    # We only want to process files, not directories, and skip .py files
    if os.path.isfile(file_path) and not file.endswith(".py"):
        # Use subprocess to call ExifTool directly
        try:
            print(f"{Fore.GREEN}Processing file {file_path}{Style.RESET_ALL}")
            result = subprocess.run(
                ["exiftool", "-j", "-Model", "-AndroidModel", file_path],
                capture_output=True,
                text=True,
            )
            exif_data = json.loads(result.stdout)[0]
            exif_camera_model = exif_data.get("Model", "No Model Found")
            exif_phone_model = exif_data.get("AndroidModel", "No Android Model Found")
            print(
                f"{Fore.BLUE}Camera model: {Fore.YELLOW}{exif_camera_model}{Style.RESET_ALL}"
            )
            print(
                f"{Fore.BLUE}Android model: {Fore.YELLOW}{exif_phone_model}{Style.RESET_ALL}"
            )
            # If the camera model matches, move the file
            if exif_camera_model == camera_model:
                print(
                    f"{Fore.GREEN}Match found for camera! Moving file {file_path} to {camera_target_dir}{Style.RESET_ALL}"
                )
                shutil.move(file_path, os.path.join(camera_target_dir, file))
            # If the phone model matches, move the file
            elif exif_phone_model == phone_model:
                print(
                    f"{Fore.GREEN}Match found for phone! Moving file {file_path} to {phone_target_dir}{Style.RESET_ALL}"
                )
                shutil.move(file_path, os.path.join(phone_target_dir, file))
            else:
                print(f"{Fore.RED}No match found for file {file_path}{Style.RESET_ALL}")
        except Exception as e:
            print(
                f"{Fore.RED}Error processing file {file_path}: {str(e)}{Style.RESET_ALL}"
            )
