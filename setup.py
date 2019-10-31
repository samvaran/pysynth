#!/usr/bin/env python

from distutils.core import setup

setup(name="PySynthesizer",
        version="0.1",
        description="UNKNOWN",
        author="UNKNOWN",
        author_email="UNKNOWN",
	url="UNKNOWN",
        py_modules=["pysynth", "pysynth_b", "pysynth_c", "pysynth_d", "pysynth_e", "pysynth_p", "pysynth_s", "pysynth_beeper", "pysynth_samp", "play_wav", "mixfiles", "mkfreq", "demosongs"],
	scripts=["read_abc.py", "readmidi.py", "nokiacomposer2wav.py", "test_nokiacomposer2wav.py", "menv.py"],
)

