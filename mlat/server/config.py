# -*- mode: python; indent-tabs-mode: nil -*-

# Part of mlat-server: a Mode S multilateration server
# Copyright (C) 2015  Oliver Jowett <oliver@mutability.co.uk>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Poor man's configuration system, because I'm lazy.."""

from mlat import constants

# Location at which _this copy_ of the server code may be found. This URL will
# be sent to network clients. Remember to uncomment this after updating it.
#
# See COPYING and README.md - the AGPL requires that you make your
# modified version of the server source code available to users that interact
# with the server over a network.
#
# Please remember that this needs to be _the code that the server is running_.
#
AGPL_SERVER_CODE_URL = "https://github.com/nitro999/mlat-server"

# minimum NUCp value to accept as a sync message
MIN_NUC = 6

# absolute maximum receiver range for sync messages, metres
MAX_RANGE = 500e3

# maximum distance between even/odd DF17 messages, metres
MAX_INTERMESSAGE_RANGE = 10e3

# absolute maximum altitude, metres
MAX_ALT = 50000 * constants.FTOM

# how long to wait to accumulate messages before doing multilateration, seconds
MLAT_DELAY = 2.5

# maxfev (maximum function evaluations) for the solver
SOLVER_MAXFEV = 50

# limit group size, discard the rest of message copies
# first pruning step before clock normalization
MAX_GROUP = 200

# hard limit the absolute size of the cluster given to the solver
MAX_CLUSTER = 25

# the following spreading of receivers would not be necessary if we would just use all
# receivers, but as we do limit the number of receivers, it's beneficial to use
# those which are further apart

# initial number of receivers for which minimum distance is not checked
# we don't want to have too few receivers just because they are close to each other
CLUSTER_NOSPREAD = 10

# only add receivers to the cluster if they are further than a certain distance
# from all receivers already in the cluster
# required distance is zero up to 10 receivers already in cluster
# then the distance increases by CLUSTER_SPREAD m for every additional receiver
# so for CLUSTER_SPREAD = 1000, if there are already 16 receivers, the new receiver
# needs to be further than 16-10 = 6 km from all receivers in the cluster
CLUSTER_SPREAD = 1000

if 'AGPL_SERVER_CODE_URL' not in globals():
    raise RuntimeError('Please update AGPL_SERVER_CODE_URL in mlat/server/config.py')
