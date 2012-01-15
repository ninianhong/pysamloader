# Copyright (c) 2012 Chintalagiri Shashank
#
# This file is part of pysamloader.

# pysamloader is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pysamloader is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pysamloader.  If not, see <http://www.gnu.org/licenses/>.

class SAMDevice(object):
    EFC_FCR = None
    EFC_FSR = None
    AutoBaud = None
    FullErase = None
    WP_COMMAND = None
    EWP_COMMAND = None
    EA_COMMAND = None
    FS_ADDRESS = None
    PAGE_SIZE = None
    SGP = [0, 0, 0]
    def __init__(self, args):
        pass
