# PDF-Protection-Tool

Python command-line utility for adding password protection to existing PDF files.

## Features
- Reads an input PDF and copies all of its pages using `PyPDF2`
- Applies password encryption with a single command
- Handles missing files and invalid PDFs with readable error messages

## Requirements
1. Python 3.9+ (any modern version works)
2. Dependencies installed via:

   ```
   pip install -r requirements.txt
   ```

## Usage
```
python pdf_protect.py <input_pdf> <output_pdf> <password>
```

Example:
```
python pdf_protect.py sample.pdf sample_protected.pdf Secret123
```

The script writes a new password-protected PDF (`sample_protected.pdf`) while leaving the original file untouched.

## Common Issues
- **Input file not found**: double-check the path you pass as `input_pdf`.
- **Unreadable PDF**: the file may be corrupt or not actually a PDF; try opening it manually.
- **Permission errors**: ensure you have write access to the output directory.

## Next Steps / Enhancements
- Add automated tests against dummy PDFs
- Provide a GUI or prompt-based flow for non-CLI users
- Allow setting owner passwords or custom permissions
