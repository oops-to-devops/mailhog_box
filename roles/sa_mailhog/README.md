sa-mailhog
==========

[![Build Status](https://travis-ci.org/softasap/sa-mailhog.svg?branch=master)](https://travis-ci.org/softasap/sa-mailhog)


Role to install mailhog on unix based box. (with either upstart or systemd)

Version is controlled by  mailhog_version parameter.


Example:

Simple

```YAML


     - {
         role: "sa-mailhog",
         mailhog_version: "1.0.0"
       }

```

Advanced

you can check table below

| Environment         | Command line    | Default         | Description
| ------------------- | --------------- | --------------- | -----------
| MH_CORS_ORIGIN      | -cors-origin    |                 | If set, a Access-Control-Allow-Origin header is returned for API endpoints
| MH_HOSTNAME         | -hostname       | mailhog.example | Hostname to use for EHLO/HELO and message IDs
| MH_API_BIND_ADDR    | -api-bind-addr  | 0.0.0.0:8025    | Interface and port for HTTP API server to bind to
| MH_UI_BIND_ADDR     | -ui-bind-addr   | 0.0.0.0:8025    | Interface and port for HTTP UI server to bind to
| MH_MAILDIR_PATH     | -maildir-path   |                 | Maildir path (for maildir storage backend)
| MH_MONGO_COLLECTION | -mongo-coll     | messages        | MongoDB collection name for message storage
| MH_MONGO_DB         | -mongo-db       | mailhog         | MongoDB database name for message storage
| MH_MONGO_URI        | -mongo-uri      | 127.0.0.1:27017 | MongoDB host and port
| MH_SMTP_BIND_ADDR   | -smtp-bind-addr | 0.0.0.0:1025    | Interface and port for SMTP server to bind to
| MH_STORAGE          | -storage        | memory          | Set message storage: memory / mongodb / maildir
| MH_OUTGOING_SMTP    | -outgoing-smtp  |                 | JSON file defining outgoing SMTP servers
| MH_UI_WEB_PATH      | -ui-web-path    |                 | WebPath under which the ui is served (without leading or trailing slahes), e.g. 'mailhog'
| MH_AUTH_FILE        | -auth-file      |                 | A username:bcryptpw mapping file

and provide additional configuration options either via `mailhog_env` variable (environment),
or by providing binary cmd arguments via `mailhog_params` string.


```YAML
  vars:
    box_mailhog_env: {
       MH_HOSTNAME: "mailhog.example"
    }
    box_mailhog_params: "-auth-file /etc/mailhog.authfile"

  roles:
     - {
         role: "sa-mailhog",
         mailhog_version: "1.0.0",
         mailhog_env: "{{ box_mailhog_env }}",
         mailhog_params: "{{ box_mailhog_params }}",
       }

```



Usage with ansible galaxy workflow
----------------------------------

If you installed the sa-mailhog role using the command

`
   ansible-galaxy install softasap.sa-mailhog
`

the role will be available in the folder library/softasap.sa-mailhog
Please adjust the path accordingly.

```YAML

     - {
         role: "softasap.sa-mailhog"
       }

```



Copyright and license
---------------------

Code is dual licensed under the [BSD 3 clause] (https://opensource.org/licenses/BSD-3-Clause) and the [MIT License] (http://opensource.org/licenses/MIT). Choose the one that suits you best.

Reach us:

Subscribe for roles updates at [FB] (https://www.facebook.com/SoftAsap/)

Join gitter discussion channel at [Gitter](https://gitter.im/softasap)

Discover other roles at  http://www.softasap.com/roles/registry_generated.html

visit our blog at http://www.softasap.com/blog/archive.html

