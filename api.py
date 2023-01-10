from connexion import FlaskApp

def init_api():
    app = FlaskApp(__name__, specification_dir='./')
    app.add_api('api.yaml', resolver_error=502, strict_validation=True)

    return app


def get_version():
    return "1.0"


if __name__ == "__main__": 
    init_api().run(8080, debug=True)