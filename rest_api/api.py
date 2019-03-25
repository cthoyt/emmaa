import json
from os import path

import boto3
import logging
from botocore.exceptions import ClientError
from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)
logger = logging.getLogger(__name__)


HERE = path.dirname(path.abspath(__file__))
EMMAA = path.join(HERE, path.pardir)
DASHBOARD = path.join(EMMAA, 'dashboard')


# Create a template object from the template file, load once
def _load_template(fname):
    template_path = path.join(DASHBOARD, fname)
    with open(template_path, 'rt') as f:
        template_str = f.read()
        template = Template(template_str)
    return template


INDEX = _load_template('index.html')
MODEL = _load_template('model.html')
QUERIES = _load_template('query.html')


def _get_models():
    s3 = boto3.client('s3')
    resp = s3.list_objects(Bucket='emmaa', Prefix='models/', Delimiter='/')
    model_data = []
    for pref in resp['CommonPrefixes']:
        model_id = pref['Prefix'].split('/')[1]
        meta_key = f'models/{model_id}/{model_id}_model_meta.json'
        try:
            resp = s3.get_object(Bucket='emmaa', Key=meta_key)
        except ClientError:
            logger.warning(f"Model {model_id} has no metadata. Skipping...")
            continue
        meta_json = json.loads(resp['Body'].read())
        model_data.append((model_id, meta_json))
    return model_data


@app.route('/')
@app.route('/home')
def get_home():
    model_data = _get_models()
    return INDEX.render(model_data=model_data)


@app.route('/dashboard/<model>')
def get_model_dashboard(model):
    model_data = _get_models()
    return MODEL.render(model=model, model_data=model_data)


@app.route('/query')
def get_query_page():
    # TODO Should pass user specific info in the future when logged in
    return QUERIES.render()


if __name__ == '__main__':
    print(app.url_map)  # Get all avilable urls and link them
    app.run()
