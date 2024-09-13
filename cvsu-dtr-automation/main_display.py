import os


def clear_screen():
    os.system("cls")


def isapi_logo():
    print_logo = """
╔═╗┬  ┬╔═╗╦ ╦  ╦┌┐┌┌┬┐┌─┐┬  ┬  ┬┌─┐┌─┐┌┐┌┌┬┐  ╔═╗┌┬┐┌┬┐┌─┐┌┐┌┌┬┐┌─┐┌┐┌┌─┐┌─┐ ╔╦╗┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
║  └┐┌┘╚═╗║ ║  ║│││ │ ├┤ │  │  ││ ┬├┤ │││ │   ╠═╣ │  │ ├┤ │││ ││├─┤││││  ├┤   ║ ├┬┘├─┤│  ├┴┐├┤ ├┬┘
╚═╝ └┘ ╚═╝╚═╝  ╩┘└┘ ┴ └─┘┴─┘┴─┘┴└─┘└─┘┘└┘ ┴   ╩ ╩ ┴  ┴ └─┘┘└┘─┴┘┴ ┴┘└┘└─┘└─┘  ╩ ┴└─┴ ┴└─┘┴ ┴└─┘┴└─ 
    Daily
    """
    print(print_logo)

def show_instruction():
    isapi_logo()
    print("""
Press "0" to quit to the automation.\n
            """)
