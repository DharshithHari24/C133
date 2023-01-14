from flask import Flask, render_template

app = Flask(__name__)
#in the function return render_template(‘index.html’)
@app.route("/index")
def first_webpage():
    #Create a variable
    name = 'Flask'
    # Pass the variable in the template
    return render_template('index.html', index_variable = name)
app.run(debug=True)

