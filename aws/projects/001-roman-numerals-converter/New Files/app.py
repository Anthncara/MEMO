from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', developer_name = 'E2031-Salih')

@app.route('/', methods = ['POST'])
def get_data_from_html():
    z = request.form['number']
    i = False
    def roma(rakam, a, b = "V", c = "X"):
        if rakam < 4:
            return rakam * a
        elif rakam == 4:
            return a + b
        elif rakam == 5:
            return b
        elif rakam < 9:
            return b + (rakam - 5) * a
        elif rakam == 9:
            return a + c
        else:
            pass
    
    while not z.isdigit():
        i = True
        return render_template('index.html', developer_name = 'E2031-Salih', not_valid = i)
    while int(z) < 1 or int (z) > 3999:
        i = True
        return render_template('index.html', developer_name = 'E2031-Salih', not_valid = i)
    sonuc = ""
    for j in range(len(z), 0, -1):
        if j == 4:
            sonuc += roma(int(z[len(z) - j]), 'M')
        if j == 3:
            sonuc += roma(int(z[len(z) - j]), 'C', 'D', 'M')
        if j == 2:
            sonuc += roma(int(z[len(z) - j]), 'X', 'L', 'C')
        if j == 1:
            sonuc += roma(int(z[len(z) - j]), 'I', 'V', 'X')
    
    return render_template('result.html', developer_name = 'E2031-Salih', number_decimal = z, number_roman = sonuc)

if __name__ == "__main__":
    #app.run(debug = True)

    app.run(host='0.0.0.0', port=80)