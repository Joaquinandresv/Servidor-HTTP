import os, signal, subprocess, time

def before_all(context):    
    #context.browser = webdriver.Chrome()    
    #context.director = urllib2.OpenerDirector()
    pass

def after_all(context):    
    #context.browser.quit()
    pass

def before_feature(context, feature):
    pass

def before_feature(context, feature):
    print("Launching Web Server")
    context.server_process = subprocess.Popen("bash ./iniciarServidor.sh &"
        , stdout=subprocess.PIPE
        , shell=True
        , preexec_fn=os.setsid)     
    print("Waiting 10 seconds for initialization...")
    time.sleep(10)

def after_feature(context, feature):
    print("Shutting down Web Server")        
    #print("pkill -f -9 -g %s" % context.server_process.pid)
    subprocess.call("pkill -f -9 -g %s" % context.server_process.pid, shell=True)
    
    