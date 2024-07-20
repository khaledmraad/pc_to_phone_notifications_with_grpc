from concurrent import futures
import time
import grpc
import greet_pb2
import greet_pb2_grpc



class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print("sayHello request made ")
        print(request)
        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = "Hello " + request.greeting + " " + request.name
        return hello_reply
        # return super().SayHello(request, context)
    

    def ParrotSaysHello(self, request, context):

        print("parrotSaysHello request made ")
        print(request)
        for i in range(3):
            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = "Hello " + request.greeting + " " + request.name+str(i+1)
            yield hello_reply
            time.sleep(3)

        # return super().ParrotSaysHello(request, context)
    
    def ChattyClientSaysHello(self, request_iterator, context):
        
        delayed_reply=greet_pb2.DelayedReply()
        for request in request_iterator:
            print("chattyClientSaysHello request made ")
            print(request)
            delayed_reply.request.append(request)
        
        delayed_reply.message = "you have received " + str(len(delayed_reply.request)) + " messages"

        return delayed_reply

        # return super().ChattyClientSaysHello(request_iterator, context)
    
    def InteractingHello(self, request_iterator, context):

        for request in request_iterator:
            print("interactingHello request made ")
            print(request)
            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = "Hello " + request.greeting + " " + request.name
            yield hello_reply

        # return super().InteractingHello(request_iterator, context)
    

def serve():
    server =grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()