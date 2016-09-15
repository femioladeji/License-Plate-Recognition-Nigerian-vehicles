import subprocess

class connectToPhp():
    
    url = 'http://localhost/project/post.php'
    
    def __init__(self, plateText):
        self.callAPhpScript(plateText)
    
    def callAPhpScript(self, plateText):
        reply = subprocess.Popen("curl --data-urlencode \"platetext="+plateText+"\" "+self.url, shell=True, stdout=subprocess.PIPE)
        self.response = reply.stdout.read()