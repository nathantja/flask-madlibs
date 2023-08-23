from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

STORIES = {"silly": silly_story, "excited": excited_story}

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def homepage():
    return render_template("menu.html", stories=STORIES.keys())

@app.get("/questions")
def show_prompts():
    """Generates inputs for each story prompt"""
    return render_template("questions.html", prompts=STORY.prompts)

@app.get("/results")
def show_results():
    """Gets user input and generates the story"""
    answers = STORY.get_result_text(request.args)

    return render_template("results.html", generated_story=answers)