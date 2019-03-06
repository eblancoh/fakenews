#!/bin/python

import sys
from lxml import html
import requests
import os
import socket
import json


def webscrapper(url):

    page = requests.get(url)
    tree = html.fromstring(page.content)

    title = tree.xpath('//title/text()')

    p = tree.xpath('//p/text()')
    parrafos = ""
    for i in p:
        parrafos += i

    long = len(parrafos)
    if long > 4100:
        # print(parrafos[0:4100])
        parrafos = parrafos[0:4100]
    
    params = dict(
    url=url,
    content=parrafos,
    title=title
    )

    return params

# Función de comprobación de uso de puerto
def tryPort(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = False
    try:
        sock.bind(("0.0.0.0", port))
        result = True
    except:
        print("Port is in use")
    sock.close()
    return result


# Servicios a los que apuntar y sus URL
services = ['robinho', 'fakebox']
url_main_dict = {
                'robinho': 'https://robinho.fakenewsdetector.org/predict', 
                'fakebox': 'http://localhost:8080/fakebox/check'
                }


if __name__ == "__main__":

    if tryPort(port=8080):
        print("Start docker container according to https://machinebox.io/account instructions")
    else:
        # Suponemos que el Docker está arriba
        pass

    try:
        params = webscrapper(url = sys.argv[1])
    except IndexError:
        sys.exit("Please, enter a 'url' as argument to the script")

    jsonobj = {}
    for item in services:
        url_main = url_main_dict[item]
        try:
            resp = requests.get(url=url_main, params=params)
            if resp.status_code == 404:
                resp = requests.post(url=url_main, params=params)
            data = resp.json()
            jsonobj[item] = data
        except requests.exceptions.HTTPError as err:
            print(err)
            sys.exit(1)

    print(jsonobj)