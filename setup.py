#!/usr/bin/env python

from distutils.core import setup

setup(name="PySynthesizer",
        version="0.1",
        description="UNKNOWN",
        author="UNKNOWN",
        author_email="UNKNOWN",
	url="UNKNOWN",
        py_modules=["pysynthesizer", "pysynthesizer_b", "pysynthesizer_c", "pysynthesizer_d", "pysynthesizer_e", "pysynthesizer_p", "pysynthesizer_s", "pysynthesizer_beeper", "pysynthesizer_samp", "play_wav", "mixfiles", "mkfreq", "demosongs"],
	scripts=["read_abc.py", "readmidi.py", "nokiacomposer2wav.py", "test_nokiacomposer2wav.py", "menv.py"],
)

