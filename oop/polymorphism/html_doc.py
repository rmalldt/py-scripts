class Tag:

    def __init__(self, name, contents):
        self.start_tag = f"<{name}>"
        self.end_tag = f"</{name}>"
        self.contents = contents

    def __str__(self):
        return f"{self.start_tag}{self.contents}{self.end_tag}"

    def display(self, file=None):
        print(self, file=file)


# Class DocType extends Class Tag
class DocType(Tag):

    def __init__(self):
        super().__init__("!DOCTYPE html", "")
        self.end_tag = ""  # DOCTYPE doesn't have an end tag


# Class Head extends Class Tag
class Head(Tag):

    def __init__(self, title=None):
        super().__init__("head", "")

        if title:
            self._title_tag = Tag("title", title)
            self.contents = str(self._title_tag)


# Class Body extends Class Tag
class Body(Tag):

    def __init__(self):
        super().__init__("body", "")
        self._body_contents = []  # body contents will be built up separately

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)
        super().display(file=file)


class HtmlDoc:
    # Aggregation
    def __init__(self, doctype, head, body):
        self._doc_type = doctype
        self._head = head
        self._body = body

    # Composition
    # def __init__(self, title=None):
    #     self._doc_type = DocType()
    #     self._head = Head(title)
    #     self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print("<html>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print("</html>", file=file)


# ------------------ Test

if __name__ == "__main__":
    # ----- Compostion example
    # htmlpage = HtmlDoc(title="Html Home Page")
    # htmlpage.add_tag("h1", "Main heading")
    # htmlpage.add_tag("h2", "Sub heading")
    # htmlpage.add_tag("p", "This is a paragraph element")
    # with open("test.html", mode="w", encoding="utf-8") as test_html:
    #     htmlpage.display(file=test_html)

    # ----- Aggregation example
    doctype = DocType()
    head = Head("Aggregation Document")
    body = Body()
    body.add_tag("h1", "Main heading")
    body.add_tag("h2", "Sub heading")
    body.add_tag("p", "This is a paragraph element")
    htmlpage = HtmlDoc(doctype, head, body)

    with open("test1.html", mode="w", encoding="utf-8") as test_html:
        htmlpage.display(file=test_html)
