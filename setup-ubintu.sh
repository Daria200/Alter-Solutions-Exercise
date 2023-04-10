#!/bin/bash

# Copy the Python script to /usr/local/bin
sudo cp service/banana_detector.py /usr/local/bin/

# Copy the systemd service configuration file to /etc/systemd/system
sudo cp banana_detector.service /etc/systemd/system/

# Copy the socket configuration file to /etc/systemd/system
sudo cp banana_detector.socket /etc/systemd/system/

# Reload systemd configuration
sudo systemctl daemon-reload

# Enable the socket
sudo systemctl enable banana_detector.socket

# Start the socket
sudo systemctl start banana_detector.socket

# Enable the service to run on boot
sudo systemctl enable banana_detector

# Start the service
sudo systemctl start banana_detector

# Configure the firewall
sudo ufw allow from 192.168.0.0/16 to any port 6987
sudo ufw --force enable
