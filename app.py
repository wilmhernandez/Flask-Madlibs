from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)

app.config["SECRET_KEY"] = "Let's GO"
debug = DebugToolbarExtension(app)


@app.route("/")
def show_home():
    """Displays form for story prompts"""
    
    prompts = story.prompts
    
    return render_template('home.html', prompts=prompts)


@app.route("/story")
def show_story():
    """Display story page"""
    
    text = story.generate(request.args)
    
    return render_template('story.html', text=text)