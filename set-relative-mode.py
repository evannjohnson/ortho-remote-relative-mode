import sys
import rtmidi
import getopt

options, _ = getopt.getopt(sys.argv[1:], [], ["midi-name=", "absolute", "relative"])
options = dict(options)
port_name = options["--midi-name"]

if "--relative" in options:
    relative_mode = True
elif "--absolute" in options:
    relative_mode = False

midi_out = rtmidi.MidiOut()
ports_out = midi_out.get_ports()

if port_name in ports_out:
    try:
        with midi_out.open_port(ports_out.index(port_name)) as port_out:
            print(f"Port opened successfully: '{port_name}'")
            if relative_mode:
                print(f"Sending sysex to enable relative mode")
                midi_out.send_message([0xF0, 0x00, 0x20, 0x76, 0x02, 0x00, 0x02, 0x00, 0xF7])
            else:
                print(f"Sending sysex to enable absolute mode")
                midi_out.send_message([0xF0, 0x00, 0x20, 0x76, 0x02, 0x00, 0x02, 0x01, 0xF7])
        print(f"Port closed: '{port_name}'")
    except Exception:
        print(f"Port failed to open or encountered an error: '{port_name}'")         

"""
OR1 SYSEX SPEC
strt | TE       OR1 | cmd  addr values | end
-----|--------------|------------------|----
F0   | 00 20 76 02  | xx   xx   xx ... | F7

cmd
00      write
01      read

addr    setting                            default     note
00      midi channel                       0
01      midi cc                            1
02      midi cc abs (0 or 1)               1           set to 1 to enable absolute mode
03      midi note                          60
04      midi velocity                      100
05      disable hid                        0           set to 1 to disable hid - will restart remote
06      set cc absolute value              63          write 63 to reset

values
write   list of values for consecutive addresses after addr
read    number of consecutive addresses to read after addr (0 = read all)
        - response msg can be used to write those values back

EXAMPLES
F0 00 20 76 02 00 01 0e F7     set send cc 14
F0 00 20 76 02 01 00 00 F7     read all
"""
