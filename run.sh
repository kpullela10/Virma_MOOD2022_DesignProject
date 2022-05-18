#!/bin/zsh

pip install flask
pip install numpy
pip install flask_sqlAlchemy
pip install torch
pip install nltk
pip install flask_login


python train.py
python main.py

open "http://127.0.0.1:5000"