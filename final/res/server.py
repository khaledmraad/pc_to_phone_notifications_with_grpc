import grpc
from concurrent import futures
import messaging_pb2
import messaging_pb2_grpc
import time


class MessagingService(messaging_pb2_grpc.MessagingServiceServicer):
    def __init__(self):
        self.messages = []
        self.subscribers = []

    def BroadcastMessage(self, request, context):
        message_id = str(len(self.messages) + 1)  # Dummy message ID
        self.messages.append(
            (message_id, request.sender_id, request.message_content))

        # Notify all subscribers
        for subscriber in self.subscribers:
            subscriber(message_id, request.sender_id, request.message_content)

        return messaging_pb2.BroadcastMessageResponse(success=True, message_id=message_id)

    def StreamMessages(self, request, context):
        def notify_subscribers(message_id, sender_id, message_content):
            # Yield messages to the stream
            context.send_message(
                messaging_pb2.StreamMessagesResponse(
                    message_id=message_id,
                    sender_id=sender_id,
                    message_content=message_content,
                    timestamp=time.strftime("%Y-%m-%d %H:%M:%S")
                )
            )

        # Define a generator to stream messages
        def message_generator():
            # Stream previously stored messages
            for message_id, sender_id, message_content in self.messages:
                yield messaging_pb2.StreamMessagesResponse(
                    message_id=message_id,
                    sender_id=sender_id,
                    message_content=message_content,
                    timestamp=time.strftime("%Y-%m-%d %H:%M:%S")
                )
                time.sleep(1)  # Simulate delay

            # Stream new messages as they arrive
            self.subscribers.append(notify_subscribers)
            try:
                while True:
                    time.sleep(1)  # Keep the stream open
            except grpc.RpcError:
                # Client has disconnected
                self.subscribers.remove(notify_subscribers)

        return message_generator()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messaging_pb2_grpc.add_MessagingServiceServicer_to_server(
        MessagingService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051.")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

