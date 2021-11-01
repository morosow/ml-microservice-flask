import logging
import connexion

import json
from typing import Dict, Tuple

logging.basicConfig(filename='tmp/app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(funcName)s %(message)s')


def health() -> Tuple[Dict[str, str], int]:
    logging.info('Health check')
    return {'health_status': 'running'}, 200


app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', server='gevent')
