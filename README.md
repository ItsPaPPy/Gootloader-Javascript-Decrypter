# Gootloader-Javascript-Decrypter

This Python script is used to decrypt the Gootloader (redraws the page to resemble a forum post) and extract the download URL for the Gootloader malware. 

Save the obfuscated Javascript and pass the path into the python script (example: http://example.com/?a1b2c3d=1234567)

Usage: python.exe decrypt-gootloader-js.py /path/to/blog.js

If will then output the URL, split on the question mark, and you have the domain that is serving up the malicious zip/js.

All credit to https://twitter.com/sometimessleepi, rockstar at reversing this stuff!
