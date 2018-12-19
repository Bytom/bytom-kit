from flask import Blueprint
from flask_restful import Api

from app.api.resources import Hello
from app.api.resources import Sign
from app.api.resources import Verify
from app.api.resources import Create_Entropy
from app.api.resources import Entropy_To_Mnemonic
from app.api.resources import Mnemonic_To_Seed

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_resource(Hello, '/hello/<string:content>')
api.add_resource(Sign, '/sign')
api.add_resource(Verify, '/verify')
api.add_resource(Create_Entropy, '/create_entropy')
api.add_resource(Entropy_To_Mnemonic, '/entropy_to_mnemonic')
api.add_resource(Mnemonic_To_Seed, '/mnemonic_to_seed')