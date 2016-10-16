__author__ = 'Phil'

class DocumentOverriden():
	def __str__(self):
		return "This is a document"

class Document():
		pass


if __name__ == '__main__':
	documentOverriden = DocumentOverriden()
	document = Document()

	print("Regular Document: {}".format(document))
	print("Overriden: {0}".format(documentOverriden))
