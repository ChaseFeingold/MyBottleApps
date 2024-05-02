#!/usr/bin/env python3
import bottle


@bottle.route('/')
def index():
    return bottle.template('index')

@bottle.route('/<name>')
def name():
    return bottle.template('name')

@bottle.route('/<name>/<number>')
def namenumber():
    return bottle.template('namenumber')

def different_index(name='', number=''):
    if not name and not number:
        return bottle.template('welcome')
    if name and not number:
        the_message = f'The name {name} was passed to me!'
    else:
        the_message = f'Received name {name} and number {number}!'
    return bottle.template('message', message=the_message)


bottle.run(host='0.0.0.0', port=8090)