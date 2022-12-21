from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/',)
def page_index():

    page_content = """ 
    <h1>Русский голубой Котофей</h1>
    <img src="https://i.pinimg.com/originals/4c/36/40/4c36404847164617a118f8f328ffb815.jpg" />
    <p>Привет, я <a href='https://ru.wikipedia.org/wiki/Русская_голубая_кошка'> русккий голубой кот </a> , и это моя собственная страничка!</p><br />
    <p>Здесь <em>моя территория</em> и мой код!</p><br />
    <p>Я очень <strong> послушный </strong>, поэтому я не ссу в тапки <del>и не деру обои</del></p><br />
    <p>Код у меня <u> корявый </u>, потому что у меня <mark>пушистые лапки</mark></p><br />
    <p><div>Всех рад видеть, мурмяу</div></p>

    """
    return page_content


app.run()
