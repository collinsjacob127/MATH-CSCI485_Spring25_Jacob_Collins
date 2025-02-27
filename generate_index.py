"""
Author: Jacob Collins
Description: Python script to automatically generate an index.html file for hosting pages in this git repo.
Note: This script was generated with ChatGPT: https://chatgpt.com/share/67c0fab7-7ebc-800c-a2f7-84b2c4e70f5f
"""
import os

# Define the directory where the index.html should be created
repo_dir = "."  # Set to the root of your repo
index_file = os.path.join(repo_dir, "index.html")

# HTML Header
html_header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSCI 485 - Jacob Collins</title>
</head>
<body>
    <h1>Welcome to the homepage for data science assignments.</h1>
    <ul>
"""

# HTML Footer
html_footer = """    </ul>
</body>
</html>
"""

# Find all .html files in subdirectories
html_links = []
for root, _, files in os.walk(repo_dir):
    for file in files:
        if file.endswith(".html") and root != repo_dir:
            relative_path = os.path.relpath(os.path.join(root, file), repo_dir)
            html_links.append(f'        <li><a href="{relative_path}">{relative_path}</a></li>\n')

# Write the index.html file
with open(index_file, "w", encoding="utf-8") as f:
    f.write(html_header)
    f.writelines(html_links)
    f.write(html_footer)

print(f"index.html generated with {len(html_links)} links.")

