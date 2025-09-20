import subprocess
import shutil
import os
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor

output_folder_path = "../pack"
IGNORE_FOLDERS = {
	"zz_ignore_old"
}


def pack_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    if not os.path.exists(folder_name):
        print(f"Error: Folder \"{folder_name}\" doesn't exist")
        return

    try:
        result = subprocess.run(["PackMaker.exe", "--input", folder_name, "--output", output_folder_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while packing {folder_name}: {e}")
        return

def pack_all_folders():
    all_folders = [f for f in os.listdir() if os.path.isdir(f) and f not in IGNORE_FOLDERS]

    with ThreadPoolExecutor() as executor:
        executor.map(pack_folder, all_folders)

def main():
    parser = argparse.ArgumentParser(description="Pack folders for the game.")
    parser.add_argument("folder_name", nargs="?", help="The name of the folder to pack")
    parser.add_argument("--all", action="store_true", help="Pack all folders")

    args = parser.parse_args()

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    if args.all:
        pack_all_folders()
    elif args.folder_name:
        folder_path = os.path.abspath(args.folder_name)
        pack_folder(folder_path)
    else:
        print("Please provide a folder name or use the --all option to pack all folders.")

if __name__ == "__main__":
    main()
