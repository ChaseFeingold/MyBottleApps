#!/usr/bin/env python3
import bottle

@bottle.route('/')
def index():
    return bottle.template('index')

@bottle.route('/<name>')
def name(name):
    return bottle.template('name', name=name)

@bottle.route('/<name>/<number>')
def namenumber():
    return bottle.template('namenumber', namenumber=namenumber)
 
number


bottle.run(host='0.0.0.0', port=8090)