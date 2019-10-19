def warning_filter_generator(file_object):
    yield from (line for line in file_object if '[Warning]' in line)


class LogFileWarningFilter:

    def __init__(self, file_obj):
        self.file = file_obj

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readLine()

        #skip all the lines without the warning tag
        while line and '[warning]' not in line:
            line = self.file.readline()

        if not line:
            raise StopIteration
        else:
            yield line


with open("log_file.txt", mode="r", encoding="utf-8") as log_file:
    filter = warning_filter_generator(log_file)
    print(type(filter))
    #for warning_line in filter:
    #    print(warning_line)
    print(next(filter))
    print(next(filter))