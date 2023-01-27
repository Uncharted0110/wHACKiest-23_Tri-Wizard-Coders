from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def print_to_pdf():
    # Create a file named 'output.pdf' in the current directory
    with open('output.pdf', 'wb') as pdf_file:
        # Create a canvas object, using the letter page size
        c = canvas.Canvas(pdf_file, pagesize=letter)
        
        # Write text to the canvas
        c.drawString(100, 750, "Hello, World!")
        
        # Save the canvas
        c.save()

print_to_pdf()