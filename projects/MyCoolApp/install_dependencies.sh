#!/bin/bash

echo 'Installing dependencies...'

# Install backend dependencies
pip install flask flask_sqlalchemy

# Install frontend dependencies
cd ./projects/MyCoolApp/frontend && npm install react react-dom && cd ..

