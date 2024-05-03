import bcrypt # used in hash_password,
import fitz

# Hash passwords using bcrypt
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")



'''
Document handling utitlites
'''

# Check if the file is an allowed file type

def allowed_file(filename: str) -> bool:
    ALLOWED_EXTENSIONS = {'pdf'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_thumbnail(file: str, output_path: str, height: int, pdfpage: int) -> None:
    pdf = fitz.open(file)
    page = pdf[pdfpage]
    # Calculate zoom to fit the height
    zoom = height / page.rect.height
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    pix.save(output_path)
    pdf.close()

    