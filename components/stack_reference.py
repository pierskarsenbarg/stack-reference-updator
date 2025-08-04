from pulumi import Input
from pulumi.dynamic import CreateResult, ResourceProvider, UpdateResult, Resource
import os
import binascii

class StackReferenceUpdateInputs(object):
    value: Input[str]

    def __init__(
            self,
            value,
    ):
        self.value = value

class StackReferenceUpdateProvider(ResourceProvider):

    def create(self, props):
        return CreateResult("stackref-" + binascii.b2a_hex(os.urandom(16)).decode("utf-8"), outs=props)
    
    
    def update(self, id, old_inputs, new_inputs):
        return UpdateResult(outs={**new_inputs})
    
class StackReferenceUpdate(Resource):
    def __init__(self, name: str, args:StackReferenceUpdateInputs, opts=None):
        super().__init__(StackReferenceUpdateProvider(), name, vars(args), opts)