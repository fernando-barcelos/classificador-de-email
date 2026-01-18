import os
from flask import Flask
from controllers.data_controller import Index, DataController

app = Flask(__name__, template_folder=os.path.join('views', 'templates'))

#endpoints da pagina principal
app.add_url_rule('/', 'index', Index.index)
#endpoints para upload do arquivo
app.add_url_rule('/upload', 'upload_data', DataController.upload_data, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=False)