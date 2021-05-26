import sys
import os
import argparse

import argcomplete

from docx import Document
import base58

#def punctuate(chunk):


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

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    print(f"docxifying: {args.input_file} into: {args.output_directory}")

    print(f"creating directory: {args.output_directory}")
    os.mkdir(args.output_directory)

    document = Document()
    document.add_heading('Chapter 1', 0)

    with open(args.input_file, 'rb') as f:
        #paragraph = base58.b58encode(f.read())

        paragraph = f.read().hex()
        print(paragraph)
        p = document.add_paragraph(paragraph)

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
