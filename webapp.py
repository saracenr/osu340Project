from flask import Flask, render_template, request, redirect

webapp = Flask(__name__)

@webapp.route('/')
def root():
    return "<p>foobar</p>"

