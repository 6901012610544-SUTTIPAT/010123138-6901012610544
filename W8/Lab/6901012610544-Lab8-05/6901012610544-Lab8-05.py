import os

#Allowed image extensions
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif')


def list_all_files(directory: str) -> None:
    """Lists every file in the directory and calculates total size."""
    print(f"\n=== All Files in '{directory}' ===")
    total_size = 0
    file_count = 0

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)
            total_size += size
            file_count += 1
            print(f"- {filename} ({size:,} bytes)")

    print("-" * 45)
    print(f"Total files: {file_count}")
    print(f"Total file size: {total_size:,} bytes ({total_size / (1024 * 1024):.2f} MB)")


def list_image_files(directory: str) -> None:
    """Lists only image files in the directory and calculates their total size."""
    print(f"\n=== Image Files in '{directory}' ===")
    total_size = 0
    image_count = 0

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(IMAGE_EXTENSIONS):
            size = os.path.getsize(filepath)
            total_size += size
            image_count += 1
            print(f"- {filename} ({size:,} bytes)")

    print("-" * 45)
    print(f"Total image files: {image_count}")
    print(f"Total image size: {total_size:,} bytes ({total_size / (1024 * 1024):.2f} MB)")


def main():
    directory = input("Enter directory path: ").strip()

    if not os.path.isdir(directory):
        print("Error: The specified path is not a valid directory.")
        return

    list_all_files(directory)
    list_image_files(directory)


if __name__ == "__main__":
    main()