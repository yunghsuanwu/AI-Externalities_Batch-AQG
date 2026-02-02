# Reference Materials

Place your reference material files (PDFs, text files, etc.) in this folder.

In your `tasks.csv`, specify the filename in the `reference_material` column. For example:

- If you have `reference_materials/thyroid-guide.pdf`, use `thyroid-guide.pdf` in the CSV
- URLs (starting with `http://` or `https://`) are also supported and don't need to be in this folder

The `input_generator.py` script will automatically resolve local file paths relative to this directory.
