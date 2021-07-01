from flask import Flask, request, redirect, render_template
import requests


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        q = request.form["search_bar"]
        # print(q)
        titles, contents, images = fetch_headlines(q)
        master_list = list(zip(titles, contents, images))
        return render_template("index.html", master_list=master_list)
    else:
        titles, contents, images = fetch_headlines("plain")
        master_list = list(zip(titles, contents, images))
        return render_template("index.html", master_list=master_list)


@app.route("/articles", methods=["POST", "GET"])
def articles():
    if request.method == "POST":
        q = request.form.post("search_bar")
        print(q)


def fetch_headlines(query):
    if query == "plain":
        print(query)
        url = (
            "http://newsapi.org/v2/top-headlines?"
            "country=us&"
            "apiKey="your api key"
        )

        response = requests.get(url)
        res = response.json()
    else:
        print(query)
        url = (
            f"http://newsapi.org/v2/everything?"
            "q={query}}&"
            "from=2020-12-27&"
            "sortBy=popularity&"
            "apiKey=37f2607dcff648e391b3d365742ebbc6"
        )

        response = requests.get(url)
        res = response.json()

    titles = []
    contents = []
    images = []

    for i in range(0, 10):
        if res["articles"][i]["title"] != None:
            titles.append(res["articles"][i]["title"])
        if res["articles"][i]["content"] != None:
            contents.append(res["articles"][i]["content"])
        if res["articles"][i]["urlToImage"] != None:
            images.append(res["articles"][i]["urlToImage"])

    return titles, contents, images


app.run(debug=True)
