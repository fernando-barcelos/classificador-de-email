from flask import render_template, request
from config import IaTratament as iaResponse
from config import DocumentRead as read
from config import PreProcessing as spacy
class Index:
    @staticmethod
    def index():
        return render_template('index.html')

class DataController:
    @staticmethod
    def upload_data():
        if request.method == 'POST':
           file = request.files['fileUpload']
           text = request.form.get('emailText')
    
           if file.filename != "" or text != None:
                if ".pdf" in file.filename:
                    text_file =  read.pdf(file)
                    if len(text_file) <= 20:
                        return render_template('index.html', message = 
                            iaResponse.generate_response(text_file))
                    
                    return render_template('index.html', message = 
                        iaResponse.generate_response((iaResponse.classify_email(text_file),
                             text_file)))
                
                #trata arquivos TXT egera a resposta
                if ".txt" in file.filename:
                    text_file = read.txt(file)
                    if len(text_file) <= 20:
                        return render_template('index.html', message =
                            iaResponse.generate_response(text_file))
                
                    return render_template('index.html', message=(
                        iaResponse.generate_response((iaResponse.classify_email(text_file)),
                             text_file)))
                #trata o texto colado
                if len(text) != 0:
                    text = spacy.processing(text)
                    classify = iaResponse.classify_email(text)
                    res = iaResponse.generate_response(text, classify)

                    return render_template('index.html', message = res)
                        
                else:
                    return render_template('index.html', message = "Você deve escolher um arquivo ou escrever algo relevante")
           else:
               return render_template('index.html', message="Não foi encontrado arquivo ou dados de texto")