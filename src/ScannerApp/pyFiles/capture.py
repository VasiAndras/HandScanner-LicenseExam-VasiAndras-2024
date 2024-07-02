import os
import sys
import subprocess

def main(user_code, hand, ordnr):
    if hand not in ["R", "L"]:
        print("Error: hand must be 'R' or 'L'")
        return

    database_dir = os.path.join("Database", f"{user_code}_db")
    file_name = f"{user_code}_{hand}_{ordnr}.png"

    try:
        os.chdir(database_dir)
        print(f"Changed directory to {database_dir}")
    except FileNotFoundError:
        print(f"Error: Directory {database_dir} does not exist")
        return

    command = ["sudo", "libcamera-still", "--encoding", "png", "-o", file_name, "--awbgains",  "0.9, 0.75", "--brightness", "-0.4", "--width", "2000", "--height", "2000", "--saturation", "0.1", "--denoise", "cdn_hq", "-t", "10000"]

    try:
        subprocess.run(command, check=True)
        print(f"Image saved as {file_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <user_code> <hand> <ordnr>")
    else:
        user_code = sys.argv[1]
        hand = sys.argv[2]
        ordnr = sys.argv[3]
        main(user_code, hand, ordnr)
