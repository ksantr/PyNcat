# PyNcat - netcat implementation in Python

## Features

* Written on pure sockets
* Compatible with python 2.x and 3.x

## Usage
    `pyncat.py [-h] [-e EXECUTE] [-c] -l LISTEN -p PORT`
    
* run command shell

    `python pyncat.py -l 127.0.0.1 -p 9900 -c`

* execute a single command

    `python pyncat.py -l 127.0.0.1 -p 9900 -e 'id;grep root'`

* Use --help for detailed information

    `python pyncat.py --help`

## License

MIT
