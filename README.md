# Mixpanel Flask Proxy Example

An example Flask application that serves as a proxy to Mixpanel's Ingestion API and JavaScript library endpoints. To learn more, visit our [Data Collection Proxying Docs](https://developer.mixpanel.com/docs/data-collection-proxying).

:warning: **This is meant to be used for demonstration purposes only.** You should not run this in production without making [changes to the deployment](https://flask.palletsprojects.com/en/1.1.x/deploying/).

## Installation

There are a few ways you can use this repo to deploy a server that can be use to proxy Mixpanel API requests: one-click deploy to cloud, build a docker image, or copy and paste the nginx settings to your own nginx config file.

### Option 1: One-click Deploy
- [Run on Google Cloud](https://deploy.cloud.run?git_repo=https://github.com/jbwyme/mixpanel-flask-proxy)
- [Deploy to DigitalOcean](https://cloud.digitalocean.com/apps/new?repo=https://github.com/jbwyme/mixpanel-flask-proxy/tree/master)

### Option 2: Docker Image
Assuming you have Docker installed on your system, you can do the following:

1. Clone the repo
2. Build the Docker image: `docker build -t mixpanel-proxy .`
3. Run a container using the image: `docker run --name my-tracking-proxy -d -p 5000:5000 mixpanel-proxy`
4. Visit `http://localhost:5000`

### Option 3: Run the Flask application directly
1. Clone the repo
2. Install dependencies `pip install -r requirements.txt`
3. Start the app `python flask_proxy/app.py`
4. Visit `http://localhost:5000`
