import lab_functions as labf
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST':
        nome = request.form['nome'].lower()
        local = request.form['local'].lower()
        resp = request.form['responsavel'].lower()
        if labf.LabExists(nome, local) == False:
            labf.insertNewLab(nome, local, resp)
            labs = labf.retriveLab()
            return render_template('mysite.html', labs=labs) + 'Insercao foi um sucesso'
        else:
            labs = labf.retriveLab()
            return render_template('mysite.html', labs=labs) + 'Esse laboratorio ja existe no registro'
    else:
        return render_template('mysite.html')

@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        nome = request.form['nome'].lower()
        local = request.form['local'].lower()
        new_resp = request.form['new_responsavel'].lower()

        if labf.LabExists(nome, local) == True:
            labf.updateResponsavelLab(nome, local, new_resp)
            labs = labf.retriveLab()
            return render_template('upsite.html', labs=labs) + 'Atualizacao foi um sucesso'
        else:
            labs = labf.retriveLab()
            return render_template('upsite.html', labs=labs) + 'Atualizacao falhou, nao existe um lab com este nome, no local especificado'

    else:
        return render_template('upsite.html')

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        nome = request.form['delnome'].lower()
        local = request.form['dellocal'].lower()
        if labf.LabExists(nome, local) == True:
            labf.deleteLab(nome, local)
            labs = labf.retriveLab()
            return render_template('delpg.html', labs=labs) + 'Laboratorio foi deletado do registro'
        else:
            labs = labf.retriveLab()
            return render_template('delpg.html', labs=labs) + 'Laboratorio nao pode ser deletado por que ele nao existe no registro'
    else:
        return render_template('delpg.html')

@app.route('/', methods=['POST', 'GET'])
def homepg():
    labs = labf.retriveLab()
    return render_template('homepg.html', labs=labs)

app.run()