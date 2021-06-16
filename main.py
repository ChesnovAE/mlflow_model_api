import json
import argparse

from mlflow_model_api.api import ModelApi


def get_model_by_name(args):
    api = ModelApi(args.host, args.port)
    response_json = api.get_model_by_name(args.model_name)
    print(json.dumps(response_json, indent=4, sort_keys=True))


def setup_parser(parser: argparse.ArgumentParser):
    subparsers = parser.add_subparsers(
        help='Choose command. Type <command> -h for more help'
    )
    get_model_parser = subparsers.add_parser(
        'get-model',
        help='Get registered model info'
    )
    get_model_parser.add_argument(
        '--host',
        help='mflow host',
        type=str,
        required=True,
        dest='host'
    )
    get_model_parser.add_argument(
        '--port',
        help='mflow port',
        type=str,
        required=True,
        dest='port'
    )
    get_model_parser.add_argument(
        '--model-name',
        help='mflow model name',
        type=str,
        required=True,
        dest='model_name'
    )
    get_model_parser.add_argument(
        '--http',
        help='Use for connection http if True and use https if False. DEFAULT = TRUE',
        type=bool,
        required=False,
        default=True,
        dest='is_http'
    )
    get_model_parser.set_defaults(callback=get_model_by_name)


def main():
    parser = argparse.ArgumentParser('MLflow model api')
    setup_parser(parser)
    args = parser.parse_args()
    args.callback(args)


if __name__ == '__main__':
    main()
