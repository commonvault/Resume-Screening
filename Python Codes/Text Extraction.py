''' Step 1: extract text from pdf resume '''
import textract
text = textract.process('../Files/ornwipa_resume.pdf', encoding='ascii')

''' Below is the original code by the author '''
# # Import required package
# import PyPDF2

# # Open pdf file
# pdfFileObj = open('Roberto Salazar - Resume.pdf','rb') 

# # Read file
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# # Get total number of pages
# num_pages = pdfReader.numPages

# # Initialize a count for the number of pages
# count = 0

# # Initialize a text empty etring variable
# text = ""

# # Extract text from every page on the file
# while count < num_pages:
#     pageObj = pdfReader.getPage(count)
#     count +=1
#     text += pageObj.extractText()
