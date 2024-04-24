#!/usr/bin/env python3
import bottle

@bottle.route('/')
def index():
    return bottle.template('index')

@bottle.route('/page1')
def page1():
    return bottle.template('page1')

@bottle.route('/page2')
def page2():
    return bottle.template('page2')

bottle.run(host='0.0.0.0', port=8090)