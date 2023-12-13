#Basic Libs:
from flask import Flask, request, jsonify
from flask_cors import CORS
from colorama import Fore
from waitress import serve
from time import sleep
from sys import platform

#Custom Libs:
from api.fmovies import getMovies
from api.anime import getAnime

import os, socket, random, string

'''
TODO: Make Host Check
hosts = ['fmovies.to','fmovies.wtf','fmovies.taxi','fmovies.pub','fmovies.cafe','fmovies.world']
'''

app = Flask(__name__)

def getDevice():
    match platform:
        case "win32":
            os.system('cls')
        case _:
            os.system("clear")

def CreateGradiantLogo(text):
    faded = ""
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

def Logo():
    getDevice()
    logo = """
                          ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗ █████╗ ██████╗ ██╗
                          ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗██╔══██╗██║
                          ███████╗█████╗  ███████║██████╔╝██║     ███████║███████║██████╔╝██║
                          ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║██╔══██║██╔═══╝ ██║
                          ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║██║  ██║██║     ██║
                          ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
                               ════════════════════════════════════════════════════════                               
                                      ╔════════════════════════════════════╗
                                      ║   Simple WIP Streaming Parse API   ║
                                      ║       Developed By: Joshua         ║
                                      ╚════════════════════════════════════╝
    """
    print(CreateGradiantLogo(logo))
           
def logs(port):
    print(f'Server Information:')
    print(f'-• [{Fore.GREEN}Info{Fore.WHITE}] Initializing Server.')
    sleep(1)
    print(f'-• [{Fore.GREEN}Info{Fore.WHITE}] Generating Random Port.')
    sleep(1)
    print(f'-• [{Fore.GREEN}Info{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Server Status{Fore.WHITE}: {Fore.LIGHTGREEN_EX}Operational{Fore.WHITE}.')
    sleep(1)
    print(f'-• [{Fore.GREEN}Info{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}URL{Fore.WHITE}: http://127.0.0.1:{port}.\n\n')
    sleep(1)
    print(f'Helpful Information:')
    print(f'-• [{Fore.GREEN}Info{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Status{Fore.WHITE}: http://127.0.0.1:{port}')
    print(f'\nFMovies:')
    print(f'-• [{Fore.GREEN}Info{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Simple Search{Fore.WHITE}: http://127.0.0.1:{port}/api/fmovies?search=MOVIENAME')
    print(f'-• [{Fore.GREEN}Info{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Advanced Search{Fore.WHITE}: http://127.0.0.1:{port}/api/fmovies?search=MOVIENAME&page=1')
    print(f'\nUpMovies:')
    print(f'-• [{Fore.GREEN}Info{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Simple Search{Fore.WHITE}: http://127.0.0.1:{port}/api/upmovies?search=MOVIENAME')
    print(f'-• [{Fore.GREEN}Info{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Advanced Search{Fore.WHITE}: http://127.0.0.1:{port}/api/upmovies?search=MOVIENAME&page=1')
    print(f'\nAniHD:')
    print(f'-• [{Fore.GREEN}Info{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Simple Search{Fore.WHITE}: http://127.0.0.1:{port}/api/anihd?search=ANIME')
    print(f'-• [{Fore.GREEN}Info{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Advanced Search{Fore.WHITE}: http://127.0.0.1:{port}/api/anihd?search=ANIME&page=1')
    print(f'\nAnix:')
    print(f'-• [{Fore.GREEN}Info{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Simple Search{Fore.WHITE}: http://127.0.0.1:{port}/api/anix?search=ANIME')
    print(f'-• [{Fore.GREEN}Info{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Advanced Search{Fore.WHITE}: http://127.0.0.1:{port}/api/anix?search=ANIME&page=1')
   
def getRandomPort():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port

@app.route('/', methods=['GET'])
def index():
    return {"Status": "Online"}

@app.route('/api/fmovies', methods=['GET'])
def fmovies():
    if request.method == 'GET':
        keyword = request.args.get('search')
        page = request.args.get('page')
        proxy = request.args.get('proxy')
        return jsonify(getMovies('fmoviesz.to', keyword, page, proxy))
    
@app.route('/api/9anime', methods=['GET'])
def anime():
    if request.method == 'GET':
        keyword = request.args.get('search')
        page = request.args.get('page')
        proxy = request.args.get('proxy')
        return jsonify(getAnime('aniwave.to', keyword, page, proxy))
   
if __name__ == '__main__':
    Logo()
    port = getRandomPort()
    logs(port)
    app.secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32)).encode('utf-8')                            
    CORS(app)
    serve(app, host="0.0.0.0", port=port)