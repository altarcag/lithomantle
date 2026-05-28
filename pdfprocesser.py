from pathlib import Path
from urllib.parse import quote
import shutil
import fitz  # PyMuPDF

project_root = Path(".")
source_pdf_dir = project_root / "literature"
pdf_out_dir = project_root / "_static" / "literature_pdfs"
thumb_out_dir = project_root / "_static" / "literature_thumbs"

pdf_out_dir.mkdir(parents=True, exist_ok=True)
thumb_out_dir.mkdir(parents=True, exist_ok=True)

pdf_files = sorted(source_pdf_dir.glob("*.pdf"))

for pdf_path in pdf_files:
    # Copy PDF into static folder
    copied_pdf = pdf_out_dir / pdf_path.name
    shutil.copy2(pdf_path, copied_pdf)

    # Render first page as thumbnail
    doc = fitz.open(pdf_path)
    page = doc[0]
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    thumb_path = thumb_out_dir / f"{pdf_path.stem}.png"
    pix.save(thumb_path)
    doc.close()

print(f"Copied {len(pdf_files)} PDFs to {pdf_out_dir}")
print(f"Created {len(pdf_files)} thumbnails in {thumb_out_dir}")