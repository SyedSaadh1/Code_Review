import subprocess

# Define the Python files or directories you want to review
files_or_directories = ["code_review.py", "/Users/PRINCESSSADIYA/Downloads/Code_Review_ Project/code_review.py"]

def review_code(files_or_directories):
    for item in files_or_directories:
        try:
            subprocess.run(["pylint", "--disable=C0114,C0116,W0621,W0718,W1510,C0103,E302,E305,F0001,E902", item])
        except Exception as error:
            print(f"Error while reviewing {item}: {error}")

if __name__ == "__main__":
    review_code(files_or_directories)