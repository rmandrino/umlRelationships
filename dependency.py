# Document class
class Document:
    def print_document(self):
        print("Printing document")


# Printer class
class Printer:
    def print_file(self, document):
        document.print_document()


# Main program
printer = Printer()
document = Document()

printer.print_file(document) 
