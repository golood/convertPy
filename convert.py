import datetime
import pyvips
# from memory_profiler import profile


# Предварительно создайте в корне папку img
# @profile
def main():
    image = pyvips.Image.new_from_file(filename)
    size = image.get('n-pages')
    for i in range(size):
        image = pyvips.Image.new_from_file(filename, page=i)
        image.write_to_file(f"img/page-{i}.jpg")


if __name__ == '__main__':
    # указать путь до файла.
    # [dpi=150] это дополнительная проперти для библиотеки
    filename = '/home/ashum/projects/sandbox/sample.pdf[dpi=150]'
    print(datetime.datetime.now())
    main()
    print(datetime.datetime.now())
