# check_if_up
Its a python3 program to check if DTU's website is up and running and notifies the user by playing a song. It also automates the login process.
Done using selenium.

## Why?
DTU's registration always crashes before registration of subject due to high traffic and its taken to lot of effort to sit and keep refreshing the webpage mannually to check if it loads. Since the registration process works in a first come first serve basis, the program helps make life a bit easier.

## Getting Started

Clone or downlod the program and replace the url and the music ( with the music file being in the same directory ) if required. 

## Dependencies
download the following python3 packages.

* copy & paste this in the terminal.
```
pip3 install pygame selenium urllib3 
```


* [driver](https://chromedriver.storage.googleapis.com/index.html?path=75.0.3770.90/)-download the chrome driver as per your operating system.

## Deploying 
Run the program.
```
python3 check_if_up.py -u <username> -p <password>
```
eg

```
python3 check_if_ip.py -u 2k16/it/36 -p aba28jak
```

## Testing
* tested google chrome Version 75 and python 3.7 on macOS 10.14

## Built With

* [pygame](https://www.pygame.org/docs/) - To add the music 
* [urllib](https://docs.python.org/3/library/urllib.html) - To access the URL
* [selenium](https://selenium-python.readthedocs.io/)- To automate the web access


