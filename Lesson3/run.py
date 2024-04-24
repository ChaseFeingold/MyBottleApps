#!/usr/bin/env python3
import bottle

@bottle.route('/')
def index():
    return bottle.template('index')

@bottle.route('/page1')
def food():
    return bottle.template('food')

@bottle.route('/page2')
def excersize():
    return bottle.template('excersize')

bottle.run(host='0.0.0.0', port=8090)