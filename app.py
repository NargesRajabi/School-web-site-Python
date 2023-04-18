import csv
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('welcome_page.html')


@app.route('/careers')
def documents():
    employment = [{'title': 'Lunch monitor staff: 2 person', 'link': 'https://google.com',  },
                  {'title': ' Daycare staff: 1 person', 'link': 'https://google.com',  },
                  ]
    return render_template('careers_page.html', data=employment, )


@app.route('/news')
def assignments():
    with open('data/news.csv') as f:
        doc_list = list(csv.reader(f))[1:]
    return render_template('news_list.html', doc_list=doc_list, )


@app.route('/news/<id>')
def news_list(id):
    number = int(id)
    number = number
    with open('data/news.csv') as f:
        doc_list = list(csv.reader(f))[number:number + 1]
        print(doc_list)
    return render_template('news_page.html', doc_list=doc_list[0], )


@app.route('/info')
def contact():
    return render_template('information_page.html')


if __name__ == '__main__':
    # app.run()
    app.run( )
