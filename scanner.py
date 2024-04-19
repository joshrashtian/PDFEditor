import requests;
import os;
def fetchPDFfile(filename: str, name: str) -> bool:
    request = requests.get(filename)
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
    FileName: str = 'people'
    URL: str = 'https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf'
    fetchPDFfile(URL, FileName)