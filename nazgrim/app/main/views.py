# -*- coding:utf-8 -*-
__author__ = 'jinxiu.qi'
from . import nazgrim
from ..tools.markdown import markdown
from flask import render_template, send_file
from .. import db
import json


@nazgrim.route('/')
def home():
    from ..models import User

    print 'request index'
    db.create_all()
    text = markdown.to_html('app/article/test.md')
    return render_template('index.html', text=text)


@nazgrim.route('/article')
def article_list():
    article_list = json.load(open('app/article/articles.json'))
    return render_template('article/list.html', article_list=article_list)


@nazgrim.route('/article/<article_name>')
def article(article_name):
    html = markdown.to_html('app/article/%s/main.md' % article_name)
    return render_template('article/show.html', text=html)


@nazgrim.route('/article/<article_name>/image/<image_name>')
def article_image(article_name, image_name):
    return send_file('article/%s/image/%s' % (article_name, image_name))


@nazgrim.route('/photo')
def photo():
    return render_template('photo/list.html')
