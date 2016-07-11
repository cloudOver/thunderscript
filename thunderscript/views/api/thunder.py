"""
Copyright (c) 2016 cloudover.io

This file is part of Thunder project.

cloudover.coreCluster is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from corecluster.utils.decorators import register
from thunderscript.drivers.driver_corecluster import DriverCoreCluster


@register(log=True, auth='token')
def call(context, script, variables):
    d = DriverCoreCluster()
    d.variables = variables
    d.context = context
    d.debug = True
    d.cmd_require([script])

    return d.log