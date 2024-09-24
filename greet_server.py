from concurrent import futures
import time
import grpc
import greet_pb2
import greet_pb2_grpc


class sub_clients():

    clients = {}

    def __init__(self):
        self.clients = {}

    @staticmethod
    def add_client(client_id, client):
        sub_clients.clients[client_id] = client


class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print("sayHello request made ")
        print("the request ", request)
        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = "Hello " + request.greeting + " " + request.name

        # sub_clients.add_client("test", "noice")
        # print("all clients", sub_clients.clients)
        # print("all context", context)
        # client id
        peer = context.peer()
        client_id = peer.split(':')[-1]
        print(f"client ID:{client_id}")
#        for key, value in context.invocation_metadata():
#            print("Received initial metadata: key=%s value=%s" % (key, value))
        return hello_reply
        # return super().SayHello(request, context)

    def ParrotSaysHello(self, request, context):

        print("parrotSaysHello request made ")
        print(request)
        for i in range(3):
            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = "Hello " + \
                request.greeting + " " + request.name+str(i+1)
            yield hello_reply
            time.sleep(3)

        # return super().ParrotSaysHello(request, context)

    def ChattyClientSaysHello(self, request_iterator, context):

        delayed_reply = greet_pb2.DelayedReply()
        for request in request_iterator:
            print("chattyClientSaysHello request made ")
            print(request)
            delayed_reply.request.append(request)

        delayed_reply.message = "you have received " + \
            str(len(delayed_reply.request)) + " messages"

        return delayed_reply

        # return super().ChattyClientSaysHello(request_iterator, context)

    def InteractingHello(self, request_iterator, context):

        for request in request_iterator:
            print("interactingHello request made ")
            print("the request ", request)
            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = "Hello " + request.greeting + " " + request.name
            yield hello_reply
            # client id
            peer = context.peer()
            client_id = peer.split(':')[-1]
            print(f"client ID:{client_id}")
            client_id = context.peer()
            sub_clients.add_client(client_id, context)
            print("all clients", sub_clients.clients)

           # for client in sub_clients.clients:
           #     hello_reply2 = greet_pb2.HelloReply()
           #     hello_reply2.message = "testest "
           #     sub_clients.clients[client].send_initial_metadata(
           #         [hello_reply2]
           #     )
        # return super().InteractingHello(request_iterator, context)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

    server.add_insecure_port('192.168.1.16:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
