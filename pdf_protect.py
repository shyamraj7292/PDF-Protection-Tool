import sys
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter


def protect_pdf(input_path: str, output_path: str, password: str) -> None:
    """Encrypt a PDF file with the given password."""
    in_file = Path(input_path)

    if not in_file.exists() or not in_file.is_file():
        raise FileNotFoundError(f"Input file not found: {in_file}")

    try:
        reader = PdfReader(str(in_file))
    except Exception as exc:  # PyPDF2 raises generic errors for bad PDFs
        raise ValueError(f"Could not read PDF file '{in_file}': {exc}") from exc

    writer = PdfWriter()

    # Copy all pages
    for page in reader.pages:
        writer.add_page(page)

    # Apply encryption (user password only)
    writer.encrypt(password)

    out_file = Path(output_path)

    # Ensure parent directory exists if a path was provided
    if out_file.parent and not out_file.parent.exists():
        out_file.parent.mkdir(parents=True, exist_ok=True)

    with out_file.open("wb") as f:
        writer.write(f)


def main(argv: list[str]) -> None:
    """
    Command-line interface.

    Usage:
        python pdf_protect.py input.pdf output_protected.pdf password
    """
    if len(argv) != 4:
        print(
            "Usage:\n"
            "  python pdf_protect.py <input_pdf> <output_pdf> <password>",
            file=sys.stderr,
        )
        sys.exit(1)

    _, input_pdf, output_pdf, password = argv

    try:
        protect_pdf(input_pdf, output_pdf, password)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Catch-all for unexpected issues (permissions, disk full, etc.)
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Password-protected PDF created: {output_pdf}")


if __name__ == "__main__":
    main(sys.argv)


