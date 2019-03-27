class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.db = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        db = self.db
        for c in word[:-1]:
            db = db.setdefault(c, [False, {}])[1]
        db.setdefault(word[-1], [True, {}])[0] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        db = self.db
        for c in word[:-1]:
            if not (db and c in db):
                return False
            else:
                db = db.get(c)[1]
        if not (word[-1] in db and db.get(word[-1])[0]):
            return False
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        db = self.db
        for c in prefix:
            if not (db and c in db):
                return False
            else:
                db = db.get(c)[1]
        return True
