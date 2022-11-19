# cv2.cvtColor takes a numpy ndarray as an argument
import time

# importing OpenCV
import cv2
import numpy as nm
import pytesseract
from PIL import ImageGrab

from comparison import most_associate_topic


def capture_words():
    # bbox(x0, y0, x1, y1) screen area
    cap = ImageGrab.grab()

    # Converted the image to monochrome for it to be easily
    # read by the OCR and obtained the output String.
    tesstr = pytesseract.image_to_string(
        cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
        lang='eng')
    return tesstr.strip()


if __name__ == '__main__':
    # Path of tesseract executable
    # pytesseract.pytesseract.tesseract_cmd = '**Path to tesseract executable**'
    time.sleep(5)
    screen = capture_words()
#     screen = """Automatic summarization is the process of reducing a text document with a \
# computer program in order to create a summary that retains the most important points \
# of the original document. As the problem of information overload has grown, and as \
# the quantity of data has increased, so has interest in automatic summarization. \
# Technologies that can make a coherent summary take into account variables such as \
# length, writing style and syntax. An example of the use of summarization technology \
# is search engines such as Google. Document summarization is another."""
    print(most_associate_topic(screen, ['keyword', 'sentence', 'words', 'summary']))
