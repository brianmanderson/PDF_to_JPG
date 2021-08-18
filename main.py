__author__ = 'Brian M Anderson'
from pdf2image import convert_from_path
import os
import time


class ConvertPDF(object):
    def __init__(self):
        self.path = r'\\ro-ariaimg-v\va_data$\HDR\Bravos\Documents'
        self.needs_writing = []

    def write_files(self):
        time.sleep(1)
        for file in self.needs_writing:
            images = convert_from_path(os.path.join(self.path, file))
            file_name = file[:-4]
            for i in range(len(images)):
                images[i].save(os.path.join(self.path, '{}_Page_{}.jpg'.format(file_name, i + 1)), 'JPEG')

    def check_path(self):
        all_files = os.listdir(self.path)
        pdf_files = [i for i in all_files if i.lower().endswith('.pdf')]
        jpg_files = [i.split('_Page_')[0] for i in all_files if i.lower().endswith('.jpg')]
        self.needs_writing = []
        for file in pdf_files:
            if file.split('.PDF')[0] not in jpg_files:
                self.needs_writing.append(file)
        if self.needs_writing:
            print('Writing files')
            self.write_files()

    def run(self):
        print('Running...')
        while True:
            time.sleep(5)
            self.check_path()


def main():
    file_writer = ConvertPDF()
    file_writer.run()


if __name__ == '__main__':
    main()
