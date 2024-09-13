import os


def clear_screen():
    os.system("cls")


def isapi_logo():
    print_logo = """
╔═╗┬  ┬╔═╗╦ ╦  ╦┌┐┌┌┬┐┌─┐┬  ┬  ┬┌─┐┌─┐┌┐┌┌┬┐  ╔═╗┌┬┐┌┬┐┌─┐┌┐┌┌┬┐┌─┐┌┐┌┌─┐┌─┐ ╔╦╗┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
║  └┐┌┘╚═╗║ ║  ║│││ │ ├┤ │  │  ││ ┬├┤ │││ │   ╠═╣ │  │ ├┤ │││ ││├─┤││││  ├┤   ║ ├┬┘├─┤│  ├┴┐├┤ ├┬┘
╚═╝ └┘ ╚═╝╚═╝  ╩┘└┘ ┴ └─┘┴─┘┴─┘┴└─┘└─┘┘└┘ ┴   ╩ ╩ ┴  ┴ └─┘┘└┘─┴┘┴ ┴┘└┘└─┘└─┘  ╩ ┴└─┴ ┴└─┘┴ ┴└─┘┴└─ 
    """
    print(print_logo)

def show_instruction():
    isapi_logo()
    print("""
Press "1" to view the list of attendance in the website.
Press "2" to view the list of attendance today.
Press "3" insert the list of attendance in the website from the starting date.
Press "4" insert the list of current attendance in the database.
Press "5" insert the list of attendance in the database from the starting date.
Press "6" to quit to the automation.\n
            """)
