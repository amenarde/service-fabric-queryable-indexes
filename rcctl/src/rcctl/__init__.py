# -----------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -----------------------------------------------------------------------------

"""Azure Service Fabric Reliable Collection command line environment for querying.

This package contains the following exports:
launch -- main entry point for the command line environment
"""

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

from rcctl.entry import launch
