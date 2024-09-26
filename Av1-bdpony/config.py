from flask import Flask, render_template, request, redirect, url_for
from pony.orm import *
db = Database()
app = Flask(__name__)
