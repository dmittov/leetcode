from collections import defaultdict, deque
from typing import Dict, List, Set
from dataclasses import dataclass


class Solution:
    """
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.
    All words contain only lowercase alphabetic characters.
    Return 0 if there is no such transformation sequence.
    All words have the same length.
    """

    forbidden_char = "?"

    @staticmethod
    def __build_connection_dict(wordSet: Set[str]) -> Dict[str, List[str]]:
        connections = defaultdict(list)
        for word in wordSet:
            for exchange_position in range(len(word)):
                anchor_word = list(word)
                anchor_word[exchange_position] = "?"
                connections[str(anchor_word)].append(word)
        return connections

    @staticmethod
    def __build_graph(connections: Dict[str, List[str]]) \
            -> Dict[str, List[str]]:
        graph = defaultdict(list)
        for _, clique in connections.items():
            clique_sz = len(clique)
            for left_position in range(clique_sz):
                for right_position in range(left_position, clique_sz):
                    left_word = clique[left_position]
                    right_word = clique[right_position]
                    graph[left_word].append(right_word)
                    graph[right_word].append(left_word)
        return graph

    @dataclass
    class Node:
        word: str
        distance: int

    def ladderLength(self,
                     beginWord: str,
                     endWord: str,
                     wordList: List[str]) -> int:
        if not beginWord or not endWord:
            return 0
        wordSet = set(wordList) | {beginWord}
        connections = self.__build_connection_dict(wordSet)
        graph = self.__build_graph(connections)
        bfs_queue = deque()
        checked_words = {word: False for word in wordSet}
        bfs_queue.append(self.Node(beginWord, 0))
        while bfs_queue:
            current = bfs_queue.popleft()
            if checked_words[current.word]:
                continue
            if current.word == endWord:
                return current.distance + 1
            checked_words[current.word] = True
            for destination in graph[current.word]:
                bfs_queue.append(self.Node(destination, current.distance + 1))
        return 0
