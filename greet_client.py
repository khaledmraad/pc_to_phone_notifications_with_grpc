import greet_pb2_grpc
import greet_pb2
import time
import grpc


def get_client_stream_requests():
    while True:
        name = input("Enter your name: ")
        if name=="":
            break
        hello_request=greet_pb2.HelloRequest(greeting="hello there ",name=name)

        yield hello_request
        time.sleep(1)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - unary ")
        print("2. ParrotSayHello - server side streaming")
        print("3. ChattyClientSayHello - client side streaming")
        print("4. InteractingHello - bidirectional streaming")
        rpc_call=input("enter your input: ")

        if rpc_call == '1':
            hello_request = greet_pb2.HelloRequest(greeting="hello there ",name="world")
            hello_reply=stub.SayHello(hello_request)
            print("sayHello response received: ",hello_reply)

        elif rpc_call == '2':

            hello_request = greet_pb2.HelloRequest(greeting="hello there ",name="world")
            hello_reply=stub.ParrotSaysHello(hello_request)

            for hello_reply in hello_reply:
                print("sayHello response received: ",hello_reply)


        elif rpc_call == '3':
            delayed_reply=stub.ChattyClientSaysHello(get_client_stream_requests())

            print("ChattyClientSayHello response received: ",delayed_reply)

        elif rpc_call == '4':
            responses=stub.InteractingHello(get_client_stream_requests())
            for response in responses:
                print("InteractingHello response received: ",response)

            

        else:
            print("invalid input")


if __name__ == '__main__':
    run()