#!/bin/bash

# Use iwlist and the built-in wifi adapter to scan for nearby SSIDs. Dump the results to a file.
while [ 1 ]; do
  (date;sudo iwlist wlan0 scan | grep -e SSID -e Channel -e Signal) >> wifi_scan.txt
  sleep 1
done

