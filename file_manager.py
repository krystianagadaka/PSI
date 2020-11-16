class FileManager():
    def __init__(self,file_name):
        self.file_name = file_name
    def read_file(self,update_file):
        update_file.

    def update_file(self,text_data):
        text_data=""
        x=open('file_name')
        x.write(text_data)
        x.close()
napis=FileManager("plik")
napis.update_file("ttt")
napis.read_file()