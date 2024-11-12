import sys
import rtmidi
import getopt

options, _ = getopt.getopt(sys.argv[1:], [], ["midi-name=", "absolute", "relative"])
options = dict(options)
port_name = options["--midi-name"]

if "--relative" in options:
    relative_mode = True


midi_out = rtmidi.MidiOut()

ports_out = midi_out.get_ports()

if port_name in ports_out:
    try:
        with midi_out.open_port(ports_out.index(port_name)) as port_out:
            print(f"Port opened successfully: '{port_name}'")
            if relative_mode:
                print(f"Sending sysex to enable relative mode")
                midi_out.send_message([0xF0, 0x00, 0x20, 0x76, 0x02, 0x00, 0x02, 0x00, 0xF7])
        print(f"Port closed: '{port_name}'")
    except Exception:
        print(f"Port failed to open or encountered an error: '{port_name}'")         


