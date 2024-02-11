############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.pygithub.com>          #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.pygithub.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <pygithub@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.pygithub.com>        #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import pygithub

from . import Framework


class Issue134(Framework.BasicTestCase):  # https://github.com/jacquev6/PyGithub/pull/134
    def testGetAuthorizationsFailsWhenAutenticatedThroughOAuth(self):
        g = pygithub.Github(auth=self.oauth_token)
        with self.assertRaises(pygithub.GithubException) as raisedexp:
            list(g.get_user().get_authorizations())
        self.assertEqual(raisedexp.exception.status, 404)

    def testGetAuthorizationsSucceedsWhenAutenticatedThroughLoginPassword(self):
        g = pygithub.Github(auth=self.login)
        self.assertListKeyEqual(
            g.get_user().get_authorizations(),
            lambda a: a.note,
            [None, None, "cligh", None, None, "GitHub Android App"],
        )

    def testGetOAuthScopesFromHeader(self):
        g = pygithub.Github(auth=self.oauth_token)
        self.assertEqual(g.oauth_scopes, None)
        g.get_user().name
        self.assertEqual(g.oauth_scopes, ["repo", "user", "gist"])
