from flask import Flask, request, flash, render_template, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/about/kim', methods=['GET', 'POST'])
def aboutKim():
    return render_template('Kim.html')


##Template copy the following three lines and make some changes:
##1. on first line, replace your name in the url; eg: '/about/kim'
##2. on second line, rename the def function (every def function needs to be unique); eg: def aboutKim()
##3. create your own html file under "templates" folder, and rename the html file properly; eg: Kim.html
##4. modify your html file properly. Please refer to TEMPLATE.html for instruction
##4. on third line, replace your html file name in the bracket (needs to be exactly same the name)

@app.route('/about/REPLACE_YOUR_NAME', methods=['GET', 'POST'])
def aboutYOURNAME():
    return render_template('YOUR_NAME.html')





if __name__ == "__main__":
    app.run()
