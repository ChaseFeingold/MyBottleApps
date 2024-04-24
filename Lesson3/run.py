#!/usr/bin/env python3
import bottle

@bottle.route('/')
def index():
    return bottle.template('index')

@bottle.route('/food')
def food():
    return bottle.template('food')

@bottle.route('/excersize')
def excersize():
    return bottle.template('excersize')

bottle.run(host='0.0.0.0', port=8090)