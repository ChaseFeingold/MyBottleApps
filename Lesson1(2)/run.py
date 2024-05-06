#!/usr/bin/env python3
import bottle

@bottle.route('/')
def index():
    return bottle.template('index')

@bottle.route('/<name>')
def name(name):
    return bottle.template('name', name=name)

@bottle.route('/<name>/<number>')
def namenumber(name,number):
    return bottle.template ('namenumber', name=name, number=number)
  



bottle.run(host='0.0.0.0', port=8090)