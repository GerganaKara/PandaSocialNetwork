from collections import deque


class SocialNetwork:

    def __init__(self):
        self._network = {}

    def add_panda(self, panda):

        if panda in self._network:
            raise Exception('PandaAlreadyThere')
        self._network[panda] = set()

    def has_panda(self, panda):
        return panda in self._network

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if not self.are_friends(panda1, panda2):
            self._network[panda1].add(panda2)
            self._network[panda2].add(panda1)

    def are_friends(self, panda1, panda2):
        # and panda1 in self._network[panda2]
        return panda2 in self._network[panda1]

    def friends_of(self, panda):
        if not self.has_panda(panda):
            return False
        return self._network[panda]

    def connection_level(self, panda1, panda2):
        pass

    def are_connected(self, panda1, panda2):
        pass

    def how_many_gender_in_network(self, level, panda, gender):
        pass
