from flask import Flask, render_template, redirect, url_for, request, flash, send_from_directory
from flask_bootstrap import Bootstrap5
from forms import CodeForm
from morse import MorseCode
import smtplib
import json

app = Flask(__name__)

with open('secrets.json', 'r') as config_file:
    config = json.load(config_file)

my_email = config['email']
password = config['password']
secret_key = config['secret_key']

bootstrap = Bootstrap5(app)
app.secret_key = secret_key
morse_code = MorseCode()

def clear_form(form):
    # Reset the form fields to their initial state
    form.text.data = ''
    form.Output.data = ''



@app.route('/')
def get_app():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def get_contact():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        address = request.form['address']

        msg = f'First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nMessage: {address}'
        try:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs='chetansharama@gmail.com',
                                    msg=f'Subject: Portfolio Mail\n\n{msg}')
        except Exception as e:
            # Handle email sending error here
            print(f"Error sending email: {str(e)}")

            # Redirect to the download page after sending the email
        return redirect(url_for('download'))

    return render_template('form.html')

@app.route('/download')
def download():
    return send_from_directory('static', 'files/Chetan_Sharma_GT.pdf')


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

