import time
import glob
import os.path
import datetime
import shutil
import argparse
import re
from subprocess import Popen, PIPE

# directory paths
dropbox_dir = "/home/ajay/Dropbox/GPSDataSet/"
obs = "./*.22O"
nav = "./*.22N"

path = os.path.realpath(__file__)
script_name = os.path.basename(path)
config_path = re.sub(script_name, '', path)

print(config_path)

# variable for gnss-sdr runtime taking time in seconds provided from terminal
parser = argparse.ArgumentParser()
parser.add_argument('-r', '--runtime', default = 3600, dest = 'runtime', help = 'provide runtime in seconds', type= int)
args = parser.parse_args()
run_time = args.runtime

#Python subprocess to run gnss-sdr for the prescribed time witte
p = Popen(["gnss-sdr --config_file={}rtlsdr.conf".format(config_path)], stdin=PIPE, shell=True)
time.sleep(run_time)
p.communicate(input=b'q')

#finding the newly created obs and nav files from provided directory
obs_files = glob.glob(obs)
nav_files = glob.glob(nav)
new_obs = max(obs_files, key=os.path.getctime)
new_nav = max(nav_files, key=os.path.getctime)
new_obs_name = os.path.basename(new_obs)
new_nav_name = os.path.basename(new_nav)

#extracting the created time of the latest file in the directory 
obs_ctime = os.path.getctime(new_obs)
new_dir = str(datetime.datetime.fromtimestamp(obs_ctime))

new_dir_path = dropbox_dir+new_dir
#creating new folder in dropbox
if (os.path.isdir(new_dir_path)):
    print("The file directory already exists in dropbox. So the file is not being copied")
    print("Exiting execution")
    exit()
else:
    os.mkdir(new_dir_path)
    shutil.move(new_obs,new_dir_path+"/"+new_obs_name)
    shutil.move(new_nav,new_dir_path+"/"+new_nav_name)