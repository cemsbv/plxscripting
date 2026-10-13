# Copyright (c) Plaxis bv. All rights reserved.
import os

VERSION = "1.0.10"

build_tag = os.environ.get("BUILD_TAG")
if build_tag:
    __version__ = f"{VERSION}.{build_tag}"
else:
    __version__ = VERSION
__title__ = "plxscripting"
__description__ = "Python wrapper for the PLAXIS Remote Scripting server API"
__url__ = "https://www.bentley.com"
__author__ = "Plaxis bv"
__author_email__ = "prg-pypi-deploy@bentley.com"
__license__ = "Plaxis Public License 1.0"
__copyright__ = "Copyright (c) Plaxis bv"
