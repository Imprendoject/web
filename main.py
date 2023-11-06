from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from forms import CodeForm
from morse import MorseCode


app = Flask(__name__)

bootstrap = Bootstrap5(app)
app.secret_key = "imprendo"
morse_code = MorseCode()

def clear_form(form):
    # Reset the form fields to their initial state
    form.text.data = ''
    form.Output.data = ''



@app.route('/')
def get_app():
    return render_template('index.html')

@app.route('/contact')
def get_contact():
    return render_template('form.html')



@app.route('/morese code', methods=['GET','POST'])
def morse_form():
    form = CodeForm()

    if request.method == 'POST':
        if request.form.get('clear_button'):  # Check if the clear button was clicked
            clear_form(form)
        elif form.validate_on_submit():
            decode_select = form.checkbox.data
            text = form.text.data

            if decode_select:
                decoded_value = morse_code.decode(text)

            else:
                text_upper = text.upper()
                decoded_value = morse_code.coded(text_upper)

            form.Output.data = decoded_value


    else:
        flash("Form validation failed, please check your input.")

    return render_template('morseForm.html', form=form)
@app.route('/ep')
def e_product():
    return render_template('e_product.html')

@app.route('/et')
def e_trade():
    return render_template('e_trade.html')

@app.route('/ec')
def e_coding():
    return render_template('e_code.html')

@app.route('/ttt')

def ttt():
    return render_template('ttt.html')





if __name__ == '__main__':
    app.run(debug=True)

