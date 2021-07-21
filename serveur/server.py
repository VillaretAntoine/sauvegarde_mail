from flask import Flask, request
import json

app = Flask('')

data = {
            'keys': ['a21aa059-b54a-2505-dc7d-012893bd700c@cevennes-parcnational.fr', '001501d776ef$48650400$d92f0c00$@cevennes-parcnational.fr'],
            'fileids': [('test.pdf', '123456'), ('test2.pdf', '567890')]
       }

@app.route('/')
def index():
    return 'Sauvegarde mails serveur'


@app.route('/check_all')
def check_all():
    return json.dumps(data)

@app.route('/check_one')
def check_one():
    key = request.args.get('idmsg')
    return str(key in data['keys'])

@app.route('/check_fichier')
def check_fichier():
    fname = request.args['fname']
    fsum = request.args['fsum']
    return str((fname, fsum) in data['fileids'])

@app.route('/upload_mail', methods=['POST'])
def upload_mail():
    data = request.json()
    #TODO
    return json.dumps(data)

@app.route('/upload_fichier', methods=['POST'])
def upload_fichier():
    #TODO
    return 'OK'


if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000)
