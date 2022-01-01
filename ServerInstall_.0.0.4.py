import os
import urllib.request
from time import sleep
import webbrowser

debug = False

version = '0.0.4'

selected_server = ''

error543 = 'error 543 --internal command not executed (basically if you see this im bad at coding lol)'
error674 = 'error 674 -- java was not installed correctly, try again and if it continues try a diffrent version'

HELP_txt = '###################################################\n' \
           '#						    #\n' \
           '#		Minecraft Server Installer 		    #\n' \
           '#						    #\n' \
           '###################################################\n' \
           '\n' \
           'By: Backflop\n' \
           '\n' \
           'GitHub: https://github.com/ImBadAtCodingStuff/MinecraftServerInstaller\n' \
           '\n' \
           'Discord: backflop#7189\n' \
           '\n' \
           'Intended For: People just trying to easily set up a simple minecraft server on there home wifi.\n' \
           '\n' \
           'This Does Not: Port forward you server, so people not on your wifi will not be able to join.\n' \
           '\n' \
           '\n' \
           '	----HOW TO USE----\n' \
           '\n' \
           '    1. Install and run ServerInstall.exe\n' \
           '\n' \
           '    2. Answer the questions as you go through them\n' \
           '\n' \
           '    3. If you have to install java it should ba as simple as clicking yes or accept until you finish the java installation\n' \
           '        (NOTE: in order to run a minecraft server you need to install the java jdk which is NOT the same java that you install when you install minecraft)\n' \
           '\n' \
           '   4. When the program asks you to accept the eula.txt -- open the newly created eula.txt file in the folder and change False to True.\n' \
           '\n' \
           '    --- it should look somthing like this --\n' \
           '\n' \
           '        eula=False\n' \
           '\n' \
           '      --- change it to ---\n' \
           '\n' \
           '       eula=True\n' \
           '\n' \
           '     5. Once you have accepted to eula it should start the server automatically and a new server window should come up.\n' \
           '\n' \
           '\n' \
           '\n' \
           '	----SPECIAL FUNCTIONS---\n' \
           '\n' \
           '   1. when the program starts type "debug" to skip past the installing java and server phase.\n' \
           '	--this is just used by me when coding it so I can test parts of my code without installing a server every time--\n' \
           '\n' \
           '    2. when the program starts type "version" to see what version of the program you are running.\n' \
           '	--used if im ever helping someone and need to know what version they are on--\n' \
           '		--I do know that in the early verions the version is in the name of the file--\n' \
           '\n' \
           '\n' \
           '\n' \
           'Feel free to message me on discord if you need help.\n' \
           'Im not always avaible cuz im in high school and have alot of schoolwork lol, but ill try to respond as soon as I can\n' \
           '\n' \
           'Discord: backflop#7189'



help_link_1 = 'https://apexminecrafthosting.com/how-to-update-your-eula-txt-file-for-1-7-10/#:~:text=Accepting%20the%20EULA%C2%A0,and%20restart%20your%20server'
help_link_2 = 'https://thebreakdown.xyz/how-to-download-install-the-java-se-development-kit/'
java_jdk_17 = 'https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe'

def write_help_file():
    help_text_file = open('HELP.txt', 'w')
    help_text_file.write(HELP_txt)
    help_text_file.close()


def close_application():
    closing_application = input('press enter to close application... ')
    exit()

def error_installing_java():
    print('')
    sleep(2)
    print(error674)
    close_application()

def install_java():
    print('')
    print('java jdk install will now begin...\n\nplease wait as this may take a while on slow computers')

    urllib.request.urlretrieve('https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe',
                               'java_installer.exe')
    print('')
    try:
        os.startfile('java_installer.exe')
    except:
        error_installing_java()

    sleep(2)
    java_is_installed = input('Please type "done" when the installation is complete: ')
    while java_is_installed != 'done':
        java_is_installed = input('Please type "done" when the installation is complete: ')



def ask_for_java():
    print('')
    ask_if_java_is_needed = input('do you need to install java (this is not the same as minecrafts java, it is seperate) ? ')
    if ask_if_java_is_needed == 'yes' and 'Yes' and 'YEs' and 'YES' and 'y' and 'Y' and 'ya' and 'yeet' and 'yeeet':
        install_java()
    else:
        double_check_java_is_installed = input('Are you sure you do not need to install java?\n you will not be able to run a server if it is not installed. type "back" to go back and "no" to continue without java: ')
        if double_check_java_is_installed == 'back':
            ask_for_java()
        else:
            print('')
            print('okay, java will not be installed')


def finished():
    print('')
    print('succesful finish')
    print('')
    sleep(1)
    close_application()
def completed():
    sleep_time = 6
    if debug == True:
        sleep_time = 0
    print('')
    print('Please change the eula.txt to true')
    print('')
    sleep(sleep_time)
    def accept_eula():
        global selected_server
        if selected_server == 'paper':
            print('paper servers will take longer to load the eula file so if you dont see it just wait')
            print('')
        have_you_accepted = input('have you accepted the eula? ')
        print('')
        if have_you_accepted == 'yes' and 'Yes' and 'YEs' and 'YES' and 'y' and 'Y' and 'ya' and 'yeet' and 'yeeet':
            print('great finishing up and starting server')
            sleep(3)
            if selected_server == 'vanilla':
                try:
                    os.startfile('minecraft_server.1.18.1.jar')
                except:
                    print('')
                    print(error543)
                    print('')
                    print('closing program because of an error ¯\_(ツ)_/¯')
                    sleep(5)
                    exit()
            else:
                if selected_server == 'paper':
                    try:
                        os.startfile('paper_server.1.18.1.jar')
                    except:
                        print('')
                        print(error543)
                else:
                    print(error543)
                    sleep(2)
                    print('')
                    print('closing program because of an error ¯\_(ツ)_/¯')
            finished()
        else:
            print('')
            need_help = input('do you need help accepting the eula? ')
            if need_help == 'yes' and 'Yes' and 'YEs' and 'YES' and 'y' and 'Y' and 'ya' and 'yeet' and 'yeeet':
                webbrowser.open(help_link_1)
                sleep(5)
                print('')
                accept_eula()
            else:
                accept_eula()
    accept_eula()


def create_new_vanilla_server():
    global selected_server
    selected_server = 'vanilla'
    print('')
    print('creating new vanilla server...')
    print('')

    if debug == True:
        completed()

    if debug == False:
        print('this may take a second...')
        print('')
        print('please wait for response...')

        urllib.request.urlretrieve(
            'https://launcher.mojang.com/v1/objects/125e5adf40c659fd3bce3e66e67a16bb49ecc1b9/server.jar',
            'minecraft_server.1.18.1.jar')

        os.startfile('minecraft_server.1.18.1.jar')
        completed()

def create_new_paper_server():
    global selected_server
    selected_server = 'paper'
    print('')
    print('creating new paper server...')
    print('')

    print('this may take a second...')
    print('')
    print('please wait for response...')

    urllib.request.urlretrieve(
        'https://papermc.io/api/v2/projects/paper/versions/1.18.1/builds/111/downloads/paper-1.18.1-111.jar',
        'paper_server.1.18.1.jar')

    os.startfile('paper_server.1.18.1.jar')
    completed()


def start():
    global debug
    ask_to_create_new_server = input('(type "help" for help) --- would you like to create a new server? ')

    if ask_to_create_new_server == 'help':
        write_help_file()
        sleep(1)
        print('')
        print('A file called HELP.txt was created please open it for assistance')
        print('')

    if ask_to_create_new_server == 'debug':
        debug = True
        create_new_vanilla_server()

    if ask_to_create_new_server == 'version':
        print(version)
        start()

    ask_for_java()

    if debug == False:
        if ask_to_create_new_server == 'yes' and 'Yes' and 'YEs' and 'YES' and 'y' and 'Y' and 'ya' and 'yeet' and 'yeeet':
            print('')
            print('creating a new server will put the server file in the same folder as this file')
            agree_and_begin = input('are you sure you would like to continue? ')
            if agree_and_begin == 'yes' and 'Yes' and 'YEs' and 'YES' and 'y' and 'Y' and 'ya' and 'yeet' and 'yeeet':
                print('')
                def ask_for_type():
                    ask_for_server_type = input('what type of server would you like to create (vanilla / paper) : ')
                    if ask_for_server_type == 'vanilla':
                        create_new_vanilla_server()
                    else:
                        if ask_for_server_type == 'paper':
                            create_new_paper_server()
                        else:
                            ask_for_type()
                ask_for_type()
            else:
                print('')
                print('ok, backing out now')
                print('')
                start()
        else:
            print('')
            print('well i guess i cant argue with that ¯\_(ツ)_/¯')
            pass

start()






