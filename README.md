This script sets the Teenage Engineering ortho remote into "relative" mode. By the default mode is "absolute" mode, where it will not send any further messages if it is turned past the limits of "0" or "127". In "relative" mode, it sends "1" when turned clockwise and "127" when turned counter-clockwise, allowing you to use it as an endless knob, or set it to have arbitrary resolution for some parameter.

forked from https://github.com/simondemeule/orthocontrol/tree/master

# How to use
- Install by running `sh setup.sh` (creates venv and installs packages into it)

- Activate the environment with `source .venv/bin/activate`. Run with `python enable-relative-mode.py` with arguments
    - ex. `python set-relative-mode.py --midi-name="ortho remote Bluetooth" --relative` to enable relative mode

Here are the arguments:
- `--midi-name` provides the name of the MIDI port of the Ortho Remote. This is required.
    - you probably want `--midi-name="ortho remote Bluetooth"`, but if you get this wrong, you could potentially send sysex messages to the wrong midi device, which likely wouldn't do anything but could result in misconfiguration or data loss on the device you send it to.
- `--relative` enables relative mode
- `--absolute` enables absolute mode

