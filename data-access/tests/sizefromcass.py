# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pyximport
pyximport.install()

import ConfigParser

import pkg_resources

from nexustiles.dao.CassandraProxy import CassandraProxy

config = ConfigParser.RawConfigParser()

config.readfp(pkg_resources.resource_stream(__name__, "config/datastores.ini"), filename='datastores.ini')

cass = CassandraProxy(config)

tiles = cass.fetch_nexus_tiles('d9b5afe3-bd7f-3824-ad8a-d8d3b364689c')
print len(tiles[0].tile_blob)
