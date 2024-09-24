import grpc
import messaging_pb2
import messaging_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = messaging_pb2_grpc.MessagingServiceStub(channel)

    # Broadcast a message
    response = stub.BroadcastMessage(messaging_pb2.BroadcastMessageRequest(
        sender_id="user1",
        message_content="Hello, everyone!"
    ))
    print(
        f"BroadcastMessage Response: success={response.success}, message_id={response.message_id}")

    # Stream messages
    for response in stub.StreamMessages(messaging_pb2.StreamMessagesRequest(user_id="user1")):
        print(
            f"StreamMessages Response: message_id={response.message_id}, sender_id={response.sender_id}, content={response.message_content}, timestamp={response.timestamp}")


if __name__ == '__main__':
    run()
