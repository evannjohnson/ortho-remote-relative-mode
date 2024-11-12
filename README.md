This script sets the Teenage Engineering ortho remote into "relative" mode.

By default, the ortho remote is in "absolute" mode, where it will not send any further messages if it is turned past its internal limits of "0" and "127". In "relative" mode, it sends "1" when turned clockwise and "127" when turned counter-clockwise, allowing you to use it as an endless knob, or set it to have arbitrary resolution for some parameter.

> forked from https://github.com/simondemeule/orthocontrol/tree/master

# How to use
- Install by cloning the repo, `cd`ing into it, and running `sh setup.sh` (creates venv and installs packages into it)

- While in the repo's directory, activate the python virtual environment with `source .venv/bin/activate`. Then, run the script with `python enable-relative-mode.py` with arguments
    - ex. `python set-relative-mode.py --midi-name="ortho remote Bluetooth" --relative` to enable relative mode

arguments:
- `--midi-name` provides the name of the MIDI port of the Ortho Remote. This is required.
    - you probably want `--midi-name="ortho remote Bluetooth"`
- `--relative` enables relative mode
- `--absolute` enables absolute mode
    - if you pass both `--absolute` and `--relative`, `--relative` will take precedence
