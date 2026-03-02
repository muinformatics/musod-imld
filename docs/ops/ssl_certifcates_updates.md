# SSL Certificate Updates for MUSoD Prod and Sand

When the SSL certificate is due for renewal an email alert will be sent to ITS security and informatics. This will have to be perfomed annually. 
A CSR will need to be generated from each of the server
https://www.encryptionconsulting.com/education-center/csr/

* vs-dentappsnd
* vs-dentappprod

ssh into server
```
ssh username@vsdentappsnd
```

You can use the year of renewal (repeat for Prod)
Replace sand and year as needed.
https://www.tecmint.com/generate-csr-certificate-signing-request-in-linux/

Bash: 
```
cd /tmp
openssl req -new -newkey rsa:2018 -nodes -keyout musod_sand_202x.key -out musod_sand_202x.csr

................................................+++++..............+++++
writing new private key to 'musod_sand_202x.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:US
State or Province Name (full name) []:Wisconsin
Locality Name (eg, city) [Default City]:Milwaukee
Organization Name (eg, company) [Default Company Ltd]:Marquette University
Organizational Unit Name (eg, section) []:Dental
Common Name (eg, your name or your server's hostname) []:*.marquette.edu
Email Address []:.

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:.

```

A .csr file and private .key file will be created in the /tmp dir.

Copy the csr file to local machine.
Send the csr files from both the sand and prod servers to IT security (Trevon Forbes)
Give the following Subject Alternate Names (SAN) to ITS as well:

For the prod server: vs-dentappprod

- musod.marquette.edu
- dental-apps.marquette.edu

For the sand server: vs-dentappsnd

- musod-sand.marquette.edu
- dental-apps-sand.marquette.edu

This will be a multi-domain SSL certificate.

ITS will register. Once approved an email with several links will be sent to the informatics developer. 

Download 'as Certificate only, PEM encoded' certificate file. Separate certificate files for prod and sand servers.

Rename this to avoid confusion: For example musod_sand_202x_cert.cer

SCP the certificate file to /tmp directory on the server

The /tmp dir should have the key (created earlier) and certificate file now. 

For example:

- musod_sand_202x.key
- musod_sand_202x_cert.cer
- sudo copy the .key file to /etc/pki/tls/private/
- sudo copy the .cer file to /etc/pki/tls/certs/

After the files have been copied to their respective dir the nginx.conf will need to edited to point to the new certificate and private key file

- sudo nano /etc/nginx/nginx.conf

Edit the following 2 lines to reference new certificate and key:

- ssl_certificate /etc/pki/tls/certs/musod_sand_202x_cert.cer;
- ssl_certificate_key /etc/pki/tls/private/musod_sand_202x.key;

This will have to be done on 2 locations on the same nginx.conf file: One each for musod-sand@marquette.edu and dental-apps-sand.marquette.edu

- Save the file (Ctrl + x followed by Y)

- Run sudo nginx -t

If there are no errors in the nginx config then you should see the following messages:

- nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
- nginx: configuration file /etc/nginx/nginx.conf test is successful

Run the following to restart nginx and gunicorn services.

- sudo systemctl restart nginx gunicorn gunicorn_dental_external

If the certificates have been updated you should be able to open the websites on a browser and view the validity of the updated certificates.

Repeat the same steps on the Prod server. Replace files names and year as necessary.
