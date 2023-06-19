import os, socket, random, string
from api.fmovies import getMovies
from api.anime import getAnime
from flask import Flask, request, jsonify
from flask_cors import CORS
from colorama import Fore
from waitress import serve
from time import sleep
from sys import platform

'''
TODO: 
• Make Host Check
• Grab Direct Link
• Add More Site Support
'''

app = Flask(__name__)

def getDevice():
    match platform:
        case "linux":
            os.system('clear')
        case "linux2": 
            os.system('clear')
        case "darwin":
           os.system('clear')
        case "win32":
            os.system('cls')

def logo():
    getDevice()
    width = os.get_terminal_size().columns
    print(Fore.LIGHTMAGENTA_EX+'                                                           '.center(width))
    print(Fore.LIGHTMAGENTA_EX+'     ██╗     ███████╗████████╗██╗  ██╗ █████╗ ██╗          '.center(width))
    print(Fore.LIGHTMAGENTA_EX+'     ██║     ██╔════╝╚══██╔══╝██║  ██║██╔══██╗██║          '.center(width))
    print(Fore.LIGHTMAGENTA_EX+'     ██║     █████╗     ██║   ███████║███████║██║          '.center(width))
    print(Fore.LIGHTMAGENTA_EX+'     ██║     ██╔══╝     ██║   ██╔══██║██╔══██║██║          '.center(width))
    print(Fore.LIGHTMAGENTA_EX+'     ███████╗███████╗   ██║   ██║  ██║██║  ██║███████╗     '.center(width))
    print(Fore.LIGHTMAGENTA_EX+'     ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝     '.center(width))
    print(Fore.LIGHTCYAN_EX+'        TOS: Lethal Holds No Responsibility At ALL!         '.center(width))
    print(Fore.WHITE+f'             Version: Beta 1.0.0 https://lethals.org/            \n\n'.center(width))

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
    print(f'-• [{Fore.GREEN}DOC{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Status{Fore.WHITE}: http://127.0.0.1:{port}')
    print(f'\nFMovies:')
    print(f'-• [{Fore.GREEN}DOC{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Simple Search{Fore.WHITE}: http://127.0.0.1:{port}/api/fmovies?search=MOVIENAME')
    print(f'-• [{Fore.GREEN}DOC{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Advanced Search{Fore.WHITE}: http://127.0.0.1:{port}/api/fmovies?search=MOVIENAME&page=1')
    print(f'\n9Anime:')
    print(f'-• [{Fore.GREEN}DOC{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Simple Search{Fore.WHITE}: http://127.0.0.1:{port}/api/9anime?search=ANIME')
    print(f'-• [{Fore.GREEN}DOC{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Advanced Search{Fore.WHITE}: http://127.0.0.1:{port}/api/9anime?search=ANIME&page=1')

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
        return jsonify(getMovies('fmovies.wtf', keyword, page, proxy))
    
@app.route('/api/9anime', methods=['GET'])
def anime():
    if request.method == 'GET':
        keyword = request.args.get('search')
        page = request.args.get('page')
        proxy = request.args.get('proxy')
        return jsonify(getAnime('9anime.to', keyword, page, proxy))


if __name__ == '__main__':
    logo()
    port = getRandomPort()
    logs(port)
    app.secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32)).encode('utf-8')                            
    CORS(app)
    serve(app, host="0.0.0.0", port=port)
