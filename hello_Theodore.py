import os

from flask import Flask, url_for, render_template, request



app = Flask(__name__)



@app.route('/')

def render_main():

    return render_template('home.html')



@app.route('/ctof')

def render_ctof():

    return render_template('ctof.html')



@app.route('/ftoc')

def render_ftoc():

    return render_template('ftoc.html')



@app.route('/mtokm')

def render_mtokm():

    return render_template('mtokm.html')

    

@app.route('/ftoc-result')

def render_ftoc_result():

    try:

        ftemp_result = float(request.args['ftemp'])

        ctemp_result = ftoc(ftemp_result)

        return render_template('ftoc_result.html', ftemp=ftemp_result, ctemp=ctemp_result)

    except ValueError:

        return "Sorry: something went wrong."



@app.route('/ctof-result')

def render_ctof_result():

    try:

        ctemp_result = float(request.args['ctemp'])

        ftemp_result = ctof(ctemp_result)

        return render_template('ctof_result.html', ctemp=ctemp_result, ftemp=ftemp_result)

    except ValueError:

        return "Sorry: something went wrong."



@app.route('/mtokm-result')

def render_mtokm_result():

    try:

        mdist_result = float(request.args['mdist'])

        kmdist_result = miles_to_km(mdist_result)

        return render_template('mtokm_result.html', kmdist=kmdist_result, mdist=mdist_result)
        return render_template('mtokm.html')

    except ValueError:

        return "Sorry: something went wrong."



def ftoc(ftemp):

   return (ftemp - 32.0) * (5.0 / 9.0)

    

def ctof(ctemp):

    return (ctemp *9/5) + 32


def miles_to_km(miles):
    return (miles*1.60934)

# You'll probably want a basic function here to convert miles to kilometers too...

    

if __name__=="__main__":

    app.run(host='0.0.0.0')