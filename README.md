# autorun_GNSS-SDR
Python script to run gnss-sdr for a given amount of time and save the generated OBS and NAV to the specified directory. 

## Usage

~~~
python gnss_run.py -r 3600
~~~

The parameter 'r' passes the duration for which gnss-sdr is to be run. After running gnss-sdr for the given duration the script moves the obs and nav files generated in the current working directory to the dropbox folder in the system.

### Note: 
Change the dropbox directory path to the one in your pc within the code
