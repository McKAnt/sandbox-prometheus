# sandbox-prometheus

## Purpose

Right now the sandbox has a `localhost.pem` and a `localhost-chain.pem`. See `server.py` for the reference. If you comment out the line that uses the chain and uncomment the line that uses only the localhost certificate, the `blackbox_exporter` process will report a certificate error because the intermediate CA is not there. This simulates a mistake that has happened before.

## Certificate Setup

See there references for how the CA, intermediate CA, and server certificate were set up. The `localhost-chain.pem` file is just a concatenation of the intermediate and server certificate (in a specific order, I believe).

* https://medium.com/@brendankamp757/setting-up-local-tls-on-mac-using-cloudflares-cfssl-b905a7bcf3e0
* https://medium.com/@brendankamp757/using-intermediate-certificates-on-localhost-for-mac-f4e310caa5bb
* https://github.com/cloudflare/cfssl

## Application Setup

This repository uses Git LFS. Be sure to install Git LFS and activate it for this repository after cloning.

## Running

Start some `node_exporter`s to simulate multiple nodes for the same job. This is just to expose some generic metrics to play around with.

```
cd node_exporter-1.0.1.darwin-amd64
./node_exporter --web.listen-address 127.0.0.1:8080
./node_exporter --web.listen-address 127.0.0.1:8081
./node_exporter --web.listen-address 127.0.0.1:8082
```

`sample_server` is a generic HTTPS server that will have its endpoint monitored. It uses a self-signed certificate chain but this is expected by the monitoring process.

```
cd sample_server
python server.py
```

This `blackbox_exporter` reads the sample_server upon each scrape request.

```
cd blackbox_exporter-0.18.0.darwin-amd64
./blackbox_exporter 
```

`post_catcher` is a basic Flask server that accepts generic POST requests. This is for `alertmanager` to have somewhere to send alerts. It logs the POST data to stdout.

```
cd post_catcher
poetry install
poetry run flask run
```

This `alertmanager` instance, upon receiving an alert, POSTs to the `post_catcher`.

```
cd alertmanager-0.21.0.darwin-amd64
./alertmanager --config.file="alertmanager.yml"
```

Finally, start the main Prometheus process.

```
cd prometheus-2.22.1.darwin-amd64
./prometheus --config.file=prometheus.yml
```

## Interfaces

* `prometheus` http://localhost:9090/graph
* `blackbox_exporter` http://localhost:9115/
