from flask import Flask

app = Flask(__name__)



@app.route("/")

def hello():

   return "Hello World! (Theo)"



def ftoc(ftemp):

   return (ftemp - 32.0) * (5.0 / 9.0)

@app.route('/ftoc/<ftemp_str>')

def convert_ftoc(ftemp_str):

    ftemp = 0.0

    try:

        ftemp = float(ftemp_str)

        ctemp = ftoc(ftemp)

        return "In Farenheit: " + ftemp_str + " In Celsius " + str(ctemp) 

    except ValueError:

        return "Sorry.  Could not convert " + ftemp_str + " to a number"


@app.route('/mtokm/<mdist_str>')

def convert_mtokm(mdist_str):

    ftemp = 0.0

    try:

        mdist = float(mdist_str)

        kmdist = ftoc(mdist)

        return "In Miles: " + mdist_str + " In Kilometers " + str(kmdist) 

    except ValueError:

        return "Sorry.  Could not convert " + mdist_str + " to a number"

if __name__ == "__main__":

   app.run(host='0.0.0.0')