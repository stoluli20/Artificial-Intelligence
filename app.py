import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = smart_function(prompt)
        return redirect(url_for("index", result=response))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def smart_function(prompt):
    prompt = prompt
    model = "davinci"
    temperature = 0.5
    max_tokens = 5          

    response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens
    )

    return response.choices[0].text