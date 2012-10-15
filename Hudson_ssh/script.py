print ("Python script started")
import os, sys, shutil, glob, time

if not os.geteuid()==0:
    sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
pwd = os.getenv("PWD", os.getcwd())
print (pwd)

def download(url, file):
 import urllib, time
 start_t = time.time()
 def progress(bl, blsize, size):
   dldsize = min(bl*blsize, size)
   if size != -1:
     p = float(dldsize) / size
     try:
       elapsed = time.time() - start_t
       est_t = elapsed / p - elapsed
     except:
       est_t = 0
     print "%6.2f %% %6.0f s %6.0f s %6i / %-6i bytes" % (p*100, elapsed, est_t, dldsize, size)
   else:
     print "%6i / %-6i bytes" % (dldsize, size)
 urllib.urlretrieve(URL, FILE, progress)


def deleting (kat, P = True):
	if os.path.isdir(kat):
		if len(os.listdir(kat)) > 0:
			for x in os.listdir(kat):
				if os.path.isdir(os.path.join(kat,x)):
					if len(os.listdir(os.path.join(kat,x))) == 0: os.rmdir(os.path.join(kat,x))
					else: udalenie(os.path.join(kat,x))
			if P: udalenie(kat, False)
		else: os.rmdir(kat)

os.system('/etc/init.d/nginx stop')
time.sleep(10)
os.system('/etc/init.d/tomcat6 stop')
time.sleep(10)

os.system('rm -f /var/lib/tomcat6/conf/server.xml')
os.system('wget -P /var/lib/tomcat6/conf https://autobuilder.s3.amazonaws.com/server.xml')

os.system('rm -r /var/lib/tomcat6/conf/Catalina/localhost')
os.system('rm -r /var/lib/tomcat6/work/Catalina/localhost')
os.system('rm -r /home/ubuntu/PP')
os.system('mkdir /home/ubuntu/PP')
os.system('wget -P /home/ubuntu/PP https://autobuilder.s3.amazonaws.com/processing-platform.zip')
os.system('unzip /home/ubuntu/PP/processing-platform.zip -d /home/ubuntu/PP')
os.system('screen -dmS PPVasily java -jar ProcessingPlatform-* -cp /home/ubuntu/PP/processing-platform/')

os.system('rm -f /var/lib/tomcat6/webapps/ROOT.war')
os.system('rm -r /var/lib/tomcat6/webapps/ROOT')
os.system('wget -P /var/lib/tomcat6/webapps https://autobuilder.s3.amazonaws.com/ROOT.war')

os.system('rm -f /var/lib/tomcat6/webapps/ControlPlatform.war')
os.system('wget -P /var/lib/tomcat6/webapps https://autobuilder.s3.amazonaws.com/ControlPlatform.war')

os.system('rm -f /home/ubuntu/HQ/HornetQStandalone.tar.gz')
os.system('wget -P /home/ubuntu/HQ/ https://autobuilder.s3.amazonaws.com/HornetQStandalone.tar.gz')
os.system('tar xvfz /home/ubuntu/HQ/HornetQStandalone.tar.gz -C /home/ubuntu/HQ/')
os.system('rm -f /home/ubuntu/HQ/HornetQStandalone.tar.gz')
os.system('sudo screen -dmS HQAuto /.home/ubuntu/HQ/HornetQStandalone/bin/run.sh')

os.system('/etc/init.d/tomcat6 start')

time.sleep(60)

os.system('/etc/init.d/tomcat6 stop')

os.system('rm -r /var/lib/tomcat6/webapps/ROOT/initialGadgets')
os.system('mkdir /var/lib/tomcat6/webapps/ROOT/initialGadgets')
os.system('rm -r /var/lib/tomcat6/webapps/ROOT/config/options.properties')
os.system('wget -P /var/lib/tomcat6/webapps/ROOT/config https://autobuilder.s3.amazonaws.com/options.properties')

os.system('wget -P /var/lib/tomcat6/webapps/ROOT/initialGadgets https://autobuilder.s3.amazonaws.com/COListGadget.zip')
os.system('unzip /var/lib/tomcat6/webapps/ROOT/initialGadgets/COListGadget.zip -d /var/lib/tomcat6/webapps/ROOT/initialGadgets/COListGadget/')

os.system('wget -P /var/lib/tomcat6/webapps/ROOT/initialGadgets https://autobuilder.s3.amazonaws.com/FuelGadget.zip')
os.system('unzip /var/lib/tomcat6/webapps/ROOT/initialGadgets/FuelGadget.zip -d /var/lib/tomcat6/webapps/ROOT/initialGadgets/FuelGadget/')

os.system('wget -P /var/lib/tomcat6/webapps/ROOT/initialGadgets https://autobuilder.s3.amazonaws.com/MapGadget.jar')
os.system('unzip /var/lib/tomcat6/webapps/ROOT/initialGadgets/MapGadget.jar -d /var/lib/tomcat6/webapps/ROOT/initialGadgets/MapGadget')

time.sleep(20)
os.system('/etc/init.d/nginx start')
os.system('/etc/init.d/tomcat6 start')
os.system('screen -dmS MdeConsole java -jar MDEConsole-0.0.1.jar localhost 9978 7000 scripts -cp /home/ubuntu/MDEConsole/')
os.system('reboot')
print ("Python script ended")