import subprocess
import optparse
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address")
    (options, arguments) =  parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface ,use --help for info")
    elif not options.new_mac:
        parser.error("[-] please specify the new mac , use --help for info")
    return options
def change_mac(interface, new_mac):
    print("[+] Changing Mac Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
