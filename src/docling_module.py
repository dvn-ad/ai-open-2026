from docling.document_converter import DocumentConverter

def run_docling(source):
    converter = DocumentConverter()
    result = converter.convert(source)
    return result.document.export_to_markdown()  # output: "## Docling Technical Report[...]"
