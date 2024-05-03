# Use PyMuPDF to open a PDF file and get thumbnail image of the first page
# and save it as a PNG file.

import fitz  # PyMuPDF



# Use PyMuPDF to get a thumbnail of the first page of a PDF file with the height of 256 pixels
# and save it as a PNG file.

def generate_thumbnail(file_path: str, output_path: str, height: int) -> None:
    pdf = fitz.open(file_path)
    page = pdf[0]
    # Calculate zoom to fit the height
    zoom = height / page.rect.height
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    pix.save(output_path)
    pdf.close()
