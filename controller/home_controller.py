from flask import render_template


def home_index():
    return render_template("/home/index.html")