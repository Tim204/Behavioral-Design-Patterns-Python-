from iterator import Iterator


class BrowseHistory:

    urls = []

    def push(self, url):
        self.urls.append(url)

    def pop(self):
        last_item = self.urls[-1]
        self.urls.remove(last_item)
        return last_item

    class ListIterator(Iterator):
        def has_next(self):
            pass

        def current(self):
            pass

        def next(self):
            pass


history = BrowseHistory()
history.push("a")
history.push("a")
history.push("a")
history.pop()
history.pop()
history.pop()
print(history.urls)
