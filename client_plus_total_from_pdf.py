# importing required modules 
import PyPDF2 
import re 
    
# creating a pdf file object 
pdfFileObj = open('2.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
# printing number of pages in pdf file 
#print(pdfReader.numPages)     

# creating a page object 
pageObj = pdfReader.getPage(0)     
# extracting text from page 
pdf_text = (pageObj.extractText()) 

# find client
client = re.compile(r"""
	(Attention:\s\!\!.*?)	
	(.*) 				
	(\s*Address) 
	""", flags=re.VERBOSE  | re.DOTALL)

client_name = (client.match(pdf_text))

# find total 
total = re.compile(r"""
	(.*)
	(Total)
	(\s?)
	(kr)(.*,\d\d)
	""", flags=re.VERBOSE | re.DOTALL)

total_amount = (total.match(pdf_text))

print ('"' + client_name.group(2).strip() + '","' 
	+ total_amount.group(5).strip().replace("\"", "").replace(",",".")
	+'"')
    
# closing the pdf file object 
pdfFileObj.close() 
