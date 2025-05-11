import os
import pypandoc

# Define the source and target directories
source_dir = "chapters"
target_dir = "chapters_rst"

# Create the target directory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# Iterate over all .tex files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith(".tex"):
        source_path = os.path.join(source_dir, filename)
        target_path = os.path.join(target_dir, filename.replace(".tex", ".md"))

        # Convert the LaTeX file to Markdown
        try:
            pypandoc.convert_file(source_path, "rst", outputfile=target_path)
            print(f"Converted {filename} to {target_path}")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")
