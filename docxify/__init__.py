import sys
import os
import argparse
from functools import partial

import argcomplete

from docx import Document
import base58


def punctuate(chunk):
    pass


def unpunctuate(chunk):
    pass


# def yield_chapter_docs(chapter):
#     current_chapter = chapter
#     while True:

#         document = Document()
#         document.add_heading('Chapter 1', 0)
#         yield


def docxify():
    """
    Entry point for application script.
    """

    description = "Docxify"
    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument("-i",
                        "--input-file",
                        type=str,
                        help="File to be docxified.")

    parser.add_argument("-o", "--output-directory", type=str, help="")

    parser.add_argument("--paragraph-size", type=int, default=1024, help="")

    parser.add_argument("--chapter-size", type=int, default=64, help="")

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    print(f"docxifying: {args.input_file} into: {args.output_directory}")

    print(f"creating directory: {args.output_directory}")
    os.mkdir(args.output_directory)

    f = open(args.input_file, "rb")
    paragraphs = (c for c in iter(lambda: f.read(args.paragraph_size), b""))

    #with open(args.input_file, 'rb') as f:
    #while current_chapter_size < args.chapter_size:

    document = Document()
    document.add_heading('Chapter 1', 0)

    for paragraph in paragraphs:
        p = base58.b58encode(paragraph).decode('utf-8')
        #    paragraph = f.read().hex()
        print(p)
        result = document.add_paragraph(p)

        #print(sys.getsizeof(document))

    document.save(os.path.join(args.output_directory, "Chapter1.docx"))


def dedocxify():
    """
    Entry point for application script.
    """

    description = "Dedocxify"
    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument("-o",
                        "--output-file",
                        type=str,
                        help="File to be dedocxified.")

    parser.add_argument("-i", "--input-directory", type=str, help="")

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    print(f"dedocxifying: {args.input_directory} into: {args.output_file}")
