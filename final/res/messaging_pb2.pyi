from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BroadcastMessageRequest(_message.Message):
    __slots__ = ("sender_id", "message_content")
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    sender_id: str
    message_content: str
    def __init__(self, sender_id: _Optional[str] = ..., message_content: _Optional[str] = ...) -> None: ...

class BroadcastMessageResponse(_message.Message):
    __slots__ = ("success", "message_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message_id: str
    def __init__(self, success: bool = ..., message_id: _Optional[str] = ...) -> None: ...

class StreamMessagesRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class StreamMessagesResponse(_message.Message):
    __slots__ = ("message_id", "sender_id", "message_content", "timestamp")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    sender_id: str
    message_content: str
    timestamp: str
    def __init__(self, message_id: _Optional[str] = ..., sender_id: _Optional[str] = ..., message_content: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...
