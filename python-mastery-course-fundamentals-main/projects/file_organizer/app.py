import os
import shutil


def organize_directory(path):

    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            continue

        # Extract file extension and format directory name
        # name.jpg
        filename, file_extension = os.path.splitext(file)
        directory = file_extension[1:].upper()  # /JPG

        if not directory:
            directory = "Other"

        # Construct the new directory path
        new_dir_path = os.path.join(path, directory)

        # Create directory if it doesn't exist
        os.makedirs(new_dir_path, exist_ok=True)

        # Move the file
        shutil.move(src=os.path.join(path, file), dst=os.path.join(new_dir_path, file))
        print(f"Moved: {file} --> {new_dir_path}")


def main():
    organize_directory("/Users/pdichone/Downloads")


if __name__ == "__main__":
    main()
