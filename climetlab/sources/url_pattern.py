# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from climetlab.utils.patterns import Pattern

from .multi_url import MultiUrl


class UrlPattern(MultiUrl):
    def __init__(self, pattern, *args, unpack=None, merger=None, **kwargs):
        urls = Pattern(pattern).substitute(*args, **kwargs)
        super().__init__(urls, unpack=None, merger=None, **kwargs)


source = UrlPattern
