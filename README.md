# Wordpress-XMLRPC-DOS
Wordpress Xmlrpc Dos Exploit  (Only Works if  xmlrpc.php enabled)

This program is a proof of concept script that sends multiple HTTP requests to a specified URL. The payload, headers and the number of threads can be configured. The script is designed to test the resiliency of a server against a high number of incoming requests.
It uses Python's built-in urllib module to construct and send the HTTP requests, and the threading module to create multiple threads that can send requests simultaneously.
It is important to note that this script should be used for testing and demonstration purposes only, and should never be used to perform actual attacks on any website or server. Additionally, you should always obtain permission from the website or server owner before conducting any testing or demonstrations.

It is also important to note that this script is for educational or testing purposes only. The script should never be used to perform any kind of illegal or unauthorized activities.

To Install,
git clone https://github.com/Mohammedthoufeeq/Wordpress-XMLRPC-DOS

To Run,

cd Wordpress-XMLRPC-DOS

python wpdos.py
