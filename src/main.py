import logging
import signal
import sys

from .server.server import GRPCServer
from .proto.helloworld_pb2_grpc import add_GreeterServicer_to_server
from .services.greeter import Greeter


def add_services(server):
    add_GreeterServicer_to_server(Greeter(), server)


def signalHandler(signal, frame):
    print('Process Interrupted!\n\a')
    server.stop()
    sys.exit(0)


if __name__ == '__main__':
    logging.basicConfig()

    server = GRPCServer(address='0.0.0.0', port=4242)
    signal.signal(signal.SIGINT, signalHandler)

    add_services(server.instance)
    server.serve()
