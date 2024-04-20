import requests
import os;

def checkFile(filelink: str):
        last = filelink.split('.')
        if last[len(last)-1] != 'pdf':
            print(f'not a pdf file {len(last)-1}')
            return False
        else:
            return True
    
def fetchPDFfile(filename: str, name: str) -> bool:
    request = requests.get(filename)
    if checkFile(filename) == False:
        print(f'ERROR / {filename} is not a valid PDF File')
        return False
    if request.status_code == 200:
        path = os.path.join(os.getcwd(), filename)
        with open(f'{name}.pdf', 'wb') as pdf_object:
            pdf_object.write(request.content)
            print(f'SAVED AS / {path}')
            return True
    else:
        print(f'ERROR / {request.status_code} Status Code')
        return False

if __name__ == '__main__':
    print('Name of PDF: *NOT INCLUDING .pdf*')
    FileName: str = input()
    URL: str = None
    if(URL == None or len(URL) == 0):
        print('Paste Link:')
        URL = input()
    fetchPDFfile(URL, FileName)