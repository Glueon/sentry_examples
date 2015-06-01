from raven import Client
import yaml


def load_config():
    with open('config.yml') as f:
        return yaml.load(f)

config = load_config()

print(config['sentry']['url'])

client = Client(config['sentry']['url'])

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()
