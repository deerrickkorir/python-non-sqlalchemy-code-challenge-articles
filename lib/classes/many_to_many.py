class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            if hasattr(self, '_author'):
                self._author._articles.remove(self)
            self._author = value
            value._articles.append(self)
        else:
            raise ValueError("Author must be of type Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            if hasattr(self, '_magazine'):
                self._magazine._articles.remove(self)
            self._magazine = value
            value._articles.append(self)
        else:
            raise ValueError("Magazine must be of type Magazine")

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and value:
            self._category = value
        else:
            raise ValueError("Magazine category must be a non-empty string")

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def contributing_authors(self):
        from collections import Counter
        author_count = Counter(article.author for article in self._articles)
        return [author for author, count in author_count.items() if count > 2]

    def article_titles(self):
        return [article.title for article in self._articles]
