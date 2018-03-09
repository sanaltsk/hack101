while :
do
    #Start Monitor Mode
    monstart

    #Accept WiFi Probes & log to a file
    timeout 60 python probemon.py -i wlan0mon -f -s -r -l | tee probes.data 
    #Shutdown Monitor Mode
    monstop

    #Run Python script to upload data to Server
    python send_probe.py
done
