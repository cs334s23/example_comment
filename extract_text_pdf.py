
# importing required modules
from pypdf import PdfReader
import os


supported_file_types = [
    'bmp', 'docx', 'gif', 'jpg', 'jpeg', 'pdf', 'png', 'pptx', 'rtf', 'sgml', 'tif',
 'tiff', 'txt', 'wpd', 'xlsx', 'xml']
 
def get_file_type(file_name):
    return file_name.split(".")[-1]



def extract_text(file):
    """
    The extract text method will use the pypdf library to extract text from a pdf

    Attributes
    ----------
    file : str
        The file that will have text extracted from it
    
    Returns
    -------
    text
        a string of the extracted text from the file
    """
    if get_file_type(file) != "pdf":
        return ""
    with open(file, "rb") as file:
        try:
            reader = PdfReader(file)
        except:
            return ""
        tot_pages = len(reader.pages)
        text = ""
        for i in range(tot_pages):
            text+= reader.pages[i].extract_text()
        print(text)
        return text

def format_json(commentId, docketId, attachments, extractedTextFilename):
     json_attachment = {
        "commentId": "USTR-2015-0010-0012",
        "docketId": "USTR-2015-0010",
        "attachments": [
            {
                "filename": "USTR-2015-0010-0012/attachment_1.pdf",
                "extractedTextFilename": "USTR-2015-0010-0012/extracted_attachment_1.txt"
            }
	                    ]
    }

with open('USTR_example/extracted_attachment_1.txt', 'w') as outfile:
    print(extract_text("USTR_example/attachment_1.pdf"),file = outfile)
    

