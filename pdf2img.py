import fitz  # PyMuPDF
import os

def pdf_to_images(pdf_file, output_folder):
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)
    
    # Iterate through each page and convert it to an image
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        
        # Convert the page to a Pixmap
        pixmap = page.get_pixmap()
        
        # Save the Pixmap as a JPG image file
        image_file = f"{output_folder}/page_{page_number + 1}.jpg"
        pixmap.save(image_file, "jpeg")
    
    # Close the PDF file
    pdf_document.close()

# Example usage
print("Welcom to pdf2img app\n")
pdf_file = input("\n \t Give me the file name:- ")  # Replace with the path to your PDF file
output_folder = "file_"+pdf_file

if not os.path.exists(output_folder):
    os.mkdir(output_folder)
    print("\nfolder created")
    
else:
    print("\nFolder already exists \n" )

print("Images stored on that folder: "+output_folder)
pdf_file = pdf_file+".pdf"


pdf_to_images(pdf_file, output_folder)
