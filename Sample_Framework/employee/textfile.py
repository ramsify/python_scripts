class TextFile:

    def __init__(self):
        self.txt = ''

    def file_append(self, file):
        with open(file, 'a') as outfile:
            print('Module tf = ', self.txt)
            outfile.write(self.txt)
            outfile.close()

































    @staticmethod
    def file_clear(file):
        with open(file, 'w') as outfile:
            outfile.write('')
            outfile.close()
