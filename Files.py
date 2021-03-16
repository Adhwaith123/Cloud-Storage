import dropbox;
class TransferData:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken
        relative_path=os.path.relpath(local_path,filefrom)
        dropbox_path=os.path.join(file_to,relative_path)

    def uploadfiles(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        f=open(filefrom,"rb")
        with open(local_path,'rb') as f:
        dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))

def mainfunction():
     access_token="sl.AsXzEHKQvGWz1eX41aa6ksRS2dxbq8HmqyxlTde1oXoK9idTpOqGd9_j3adfH3vpsrQ7dVpioqqOAt__zbdiXzvkvHB-tkZfAR03fZ7jewk03InsqcoT8CxR5nwe964nOWE4tVA"
     transferData = TransferData(accesstoken)
     
     filefrom=input("enter the file path to transfer: ")
     fileto=input("enter the full path to upload to dropbox: ")

     transferData.uploadfiles(filefrom,fileto)
     print("file has been moved" )


mainfunction() 