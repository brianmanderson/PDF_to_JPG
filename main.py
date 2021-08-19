__author__ = 'Brian M Anderson'
from pdf2image import convert_from_path
import os
import time


def write_files(path, needs_writing):
    time.sleep(5)
    for file in needs_writing:
        images = convert_from_path(os.path.join(path, file))
        file_name = file[:-4]
        for i in range(len(images)):
            images[i].save(os.path.join(path, '{}_Page_{}.jpg'.format(file_name, i + 1)), 'JPEG')
    return None


class ConvertPDF(object):
    def __init__(self, path=r'\\ro-ariaimg-v\va_data$\HDR\Bravos\Documents'):
        self.path = path

    def check_path(self):
        all_files = os.listdir(self.path)
        pdf_files = [i for i in all_files if i.lower().endswith('.pdf')]
        jpg_files = [i.split('_Page_')[0] for i in all_files if i.lower().endswith('.jpg')]
        needs_writing = []
        for file in pdf_files:
            if file[:-4] not in jpg_files:
                needs_writing.append(file)
        if needs_writing:
            print('Writing files')
            write_files(path=self.path, needs_writing=needs_writing)



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
