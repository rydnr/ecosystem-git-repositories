"""
pythonedagitrepositories/git_add_failed.py

This file defines the GitAddFailed exception class.

Copyright (C) 2023-today rydnr's pythoneda/git-repositories

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
class GitAddFailed(Exception):
    """
    Adding a file to the git repository failed.

    Class name: GitAddFailed

    Responsibilities:
        - Represent the error when adding a file to a git repository.

    Collaborators:
        - None
    """

    def __init__(self, file: str, output: str):
        """
        Creates a new instance.
        :param file: The file we tried to add.
        :type file: str
        :param output: The output of the git command.
        :type output: str
        """
        super().__init__(f'"git add {file}" failed')
        self._output = output

    @property
    def output(self) -> str:
        """
        Retrieves the output of the git command.
        :return: Such output.
        :rtype: str
        """
        return self._output
