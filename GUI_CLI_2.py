import subprocess
import sys
import PySimpleGUI as sg

"""
    Network Troubleshooting Tool - Testing CMD Interface

"""
def ipaddrpng():
    loop = False
    while not loop:
        if iping == None:
            break
        else:
            loop = True
            runCommand(cmd='ping ' + str(iping), window= window)

def ipaddrtrc():
    loop = False
    while not loop:
        if iptrcrt == None:
            break
        else:
            loop = True
            runCommand(cmd='tracert ' + str(iptrcrt), window= window)
            
def nslooku():
    loop = False
    while not loop:
        if nslook == None:
            break
        else:
            loop = True
            runCommand(cmd='nslookup ' + str(nslook), window= window)

## [sg.Button('1', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20))]
def mainGUI():
    global window
    menu_def = [['Help', 'About...'],]
    sg.change_look_and_feel('Dark')
    layout = [  [sg.Menu(menu_def)],
                [sg.Text('Enter the command you wish to run:', font='fixedsys')],
                [sg.Input(key='_INPUT_'), sg.Button('Run'), sg.Button('Clear')],
                [sg.Text('Premade commands below', font='fixedsys')],
                [sg.Button('IPConfig'),sg.Button(image_filename='questions.png', key='_ipconfg_'), sg.Button('System Info', pad=((35,3),3)),sg.Button(image_filename='questions.png', key='_sysinf_'), sg.Button('NbtStat',pad=((35,3),3)),sg.Button(image_filename='questions.png', key='_nbtstat_')],
                [sg.Button('Ping'),sg.Button(image_filename='questions.png', key='_ping_'), sg.Button('Nslookup',pad=((40,3),3)),sg.Button(image_filename='questions.png', key='_nslook_'), sg.Button('Traceroute',pad=((40,3),3)),sg.Button(image_filename='questions.png', key='_trrt_')],
                [sg.Output(size=(60,30), background_color=('black'))],
                [sg.Button('Exit')] ]
    window = sg.Window('CLI Networking Tool', keep_on_top=True, no_titlebar=False, location=(500,10), size=(500,700),icon='cmd-ico.ico').Layout(layout).Finalize()

    while True:             # The Main Button Event Loop
        global iping
        global iptrcrt
        global nslook
        event, values = window.Read()
        # print(event, values)
        if event in (None, 'Exit'):
            break
        elif event == 'Run':
            runCommand(cmd=values['_INPUT_'], window=window)
        elif event == 'Clear':
            for i in range(25):
                i = "cls"
                runCommand(cmd=str(i))
            continue
        elif event == 'IPConfig':
            runCommand(cmd='ipconfig' , window=window)
        elif event == 'IPConfig Help':
            sg.Popup('IPConfig is helpful in many ways')
        elif event == 'Traceroute Help':
            sg.Popup('Traceroute is helpful in many ways')
        elif event == 'About...':
            sg.PopupAnnoying('Group 2 IT 2019-2021', keep_on_top=True)
        elif event == 'Ping':
            iping = sg.PopupGetText('Enter IP address', 'Enter IP address', keep_on_top=True)
            ipaddrpng()
        elif event == 'Traceroute':
            iptrcrt = sg.PopupGetText('Enter IP address', 'Enter IP address', keep_on_top=True)
            ipaddrtrc()
        elif event == "Nslookup":
            nslook = sg.PopupGetText('Enter Address', 'Enter Address', keep_on_top=True)
            nslooku()
        elif event == 'System Info':
            runCommand(cmd='systeminfo', window=window)
        elif event == 'NbtStat':
            runCommand(cmd='nbtstat', window=window)
        elif event == "_ipconfg_":
            sg.PopupAnnoying("Ip config information?", keep_on_top=True)
        elif event == "_sysinf_":
            sg.PopupAnnoying("System info information?", keep_on_top=True)
        elif event == '_nbtstat_':
            sg.PopupAnnoying('Nbt stat info?', keep_on_top=True)
        elif event == '_ping_':
            sg.PopupAnnoying('PINg information?', keep_on_top=True)
        elif event == '_nslook_':
            sg.PopupAnnoying('NS LOOKUP INFO?', keep_on_top=True)
        elif event == '_trrt_':
            sg.PopupAnnoying('TRACE ROUTE INFO?', keep_on_top=True)

            

    window.Close()


def runCommand(cmd, timeout=None, window=None):
    """ run shell command
    @param cmd: command to execute
    @param timeout: timeout for command execution
    @param window: the PySimpleGUI window that the output is going to (needed to do refresh on)
    @return: (return code from command, command output)
    """
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.Refresh() if window else None        # yes, a 1-line if, so shoot me

    retval = p.wait(timeout)
    return (retval, output)


mainGUI()