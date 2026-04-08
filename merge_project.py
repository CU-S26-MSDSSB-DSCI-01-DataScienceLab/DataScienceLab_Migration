import nbformat
import os

# 1. Define the input files and the output destination
# Note: Using 'se2.ipynb' as seen in your file list
notebooks = ["sec1.ipynb", "sec2.ipynb", "sec3.ipynb"]
output_file = "Final_Group_Project_Merged.ipynb"

# Create a new notebook container
combined_nb = nbformat.v4.new_notebook()

print("🚀 Starting Automated Merge...")

for nb_file in notebooks:
    if os.path.exists(nb_file):
        with open(nb_file, 'r', encoding='utf-8') as f:
            nb_content = nbformat.read(f, as_version=4)
            
            # Add a visual separator so you can find the start of each section
            separator = f"# --- START OF {nb_file.upper()} ---"
            combined_nb.cells.append(nbformat.v4.new_markdown_cell(separator))
            
            # Transfer all cells
            combined_nb.cells.extend(nb_content.cells)
            print(f"✅ Merged: {nb_file}")
    else:
        print(f"⚠️ Warning: {nb_file} not found. Skipping...")

# 2. Save the final integrated notebook
with open(output_file, 'w', encoding='utf-8') as f:
    nbformat.write(combined_nb, f)

print(f"\n🎉 Done! Combined project created as: {output_file}")