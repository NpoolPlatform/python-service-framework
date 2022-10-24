from .service import Service
from ..proto.helloworld_pb2_grpc import GreeterServicer
from ..proto.helloworld_pb2 import HelloReply


class Greeter(Service, GreeterServicer):
    def SayHello(self, request, context):
        return HelloReply(message='Hello, %s!' % request.name)

    def SayHelloAgain(self, request, context):
        return HelloReply(
            message='Hello again, %s!' % request.name)
