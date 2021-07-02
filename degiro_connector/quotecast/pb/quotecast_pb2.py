# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: degiro_connector/quotecast/pb/quotecast.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="degiro_connector/quotecast/pb/quotecast.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n-degiro_connector/quotecast/pb/quotecast.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto"v\n\x08Metadata\x12\x35\n\x11response_datetime\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x10request_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration"\xed\x02\n\tQuotecast\x12\x11\n\tjson_data\x18\x01 \x01(\t\x12\x1b\n\x08metadata\x18\x02 \x01(\x0b\x32\t.Metadata\x1a\xaf\x02\n\x07Request\x12<\n\rsubscriptions\x18\x01 \x03(\x0b\x32%.Quotecast.Request.SubscriptionsEntry\x12@\n\x0funsubscriptions\x18\x02 \x03(\x0b\x32\'.Quotecast.Request.UnsubscriptionsEntry\x1aP\n\x12SubscriptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValue:\x02\x38\x01\x1aR\n\x14UnsubscriptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValue:\x02\x38\x01"\x90\x02\n\x06Ticker\x12\x1b\n\x08metadata\x18\x01 \x01(\x0b\x32\t.Metadata\x12\'\n\x08products\x18\x02 \x03(\x0b\x32\x15.Ticker.ProductsEntry\x12\x14\n\x0cproduct_list\x18\x03 \x03(\t\x1ah\n\x07Metrics\x12-\n\x07metrics\x18\x01 \x03(\x0b\x32\x1c.Ticker.Metrics.MetricsEntry\x1a.\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a@\n\rProductsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.Ticker.Metrics:\x02\x38\x01"\xd7\x03\n\x05\x43hart\x12\x11\n\trequestid\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\t\x12\x0b\n\x03\x65nd\x18\x03 \x01(\t\x12\x12\n\nresolution\x18\x04 \x01(\t\x12\'\n\x06series\x18\x05 \x03(\x0b\x32\x17.google.protobuf.Struct\x1a\x8f\x01\n\x07Request\x12\x11\n\trequestid\x18\x01 \x01(\t\x12%\n\nresolution\x18\x02 \x01(\x0e\x32\x11.Chart.Resolution\x12\x0f\n\x07\x63ulture\x18\x03 \x01(\t\x12\x1d\n\x06period\x18\x04 \x01(\x0e\x32\r.Chart.Period\x12\x0e\n\x06series\x18\x05 \x03(\t\x12\n\n\x02tz\x18\x06 \x01(\t"k\n\nResolution\x12\x08\n\x04PT1S\x10\x00\x12\t\n\x05PT15S\x10\x01\x12\t\n\x05PT30S\x10\x02\x12\x08\n\x04PT1M\x10\x03\x12\x08\n\x04PT5M\x10\x04\x12\t\n\x05PT15M\x10\x05\x12\t\n\x05PT30M\x10\x06\x12\t\n\x05PT60M\x10\x07\x12\x08\n\x04PT1H\x10\x08"c\n\x06Period\x12\x07\n\x03P1D\x10\x00\x12\x07\n\x03P1W\x10\x01\x12\x07\n\x03P1M\x10\x02\x12\x07\n\x03P3M\x10\x03\x12\x07\n\x03P6M\x10\x04\x12\x07\n\x03P1Y\x10\x05\x12\x07\n\x03P3Y\x10\x06\x12\x07\n\x03P5Y\x10\x07\x12\x08\n\x04P10Y\x10\x08\x12\x07\n\x03YTD\x10\tb\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,
    ],
)


_CHART_RESOLUTION = _descriptor.EnumDescriptor(
    name="Resolution",
    full_name="Chart.Resolution",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="PT1S",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PT15S",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PT30S",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PT1M",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PT5M",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PT15M",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PT30M",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PT60M",
            index=7,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PT1H",
            index=8,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1171,
    serialized_end=1278,
)
_sym_db.RegisterEnumDescriptor(_CHART_RESOLUTION)

_CHART_PERIOD = _descriptor.EnumDescriptor(
    name="Period",
    full_name="Chart.Period",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="P1D",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="P1W",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="P1M",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="P3M",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="P6M",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="P1Y",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="P3Y",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="P5Y",
            index=7,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="P10Y",
            index=8,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="YTD",
            index=9,
            number=9,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1280,
    serialized_end=1379,
)
_sym_db.RegisterEnumDescriptor(_CHART_PERIOD)


_METADATA = _descriptor.Descriptor(
    name="Metadata",
    full_name="Metadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="response_datetime",
            full_name="Metadata.response_datetime",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="request_duration",
            full_name="Metadata.request_duration",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=144,
    serialized_end=262,
)


_QUOTECAST_REQUEST_SUBSCRIPTIONSENTRY = _descriptor.Descriptor(
    name="SubscriptionsEntry",
    full_name="Quotecast.Request.SubscriptionsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="Quotecast.Request.SubscriptionsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="Quotecast.Request.SubscriptionsEntry.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=466,
    serialized_end=546,
)

_QUOTECAST_REQUEST_UNSUBSCRIPTIONSENTRY = _descriptor.Descriptor(
    name="UnsubscriptionsEntry",
    full_name="Quotecast.Request.UnsubscriptionsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="Quotecast.Request.UnsubscriptionsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="Quotecast.Request.UnsubscriptionsEntry.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=548,
    serialized_end=630,
)

_QUOTECAST_REQUEST = _descriptor.Descriptor(
    name="Request",
    full_name="Quotecast.Request",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="subscriptions",
            full_name="Quotecast.Request.subscriptions",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="unsubscriptions",
            full_name="Quotecast.Request.unsubscriptions",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _QUOTECAST_REQUEST_SUBSCRIPTIONSENTRY,
        _QUOTECAST_REQUEST_UNSUBSCRIPTIONSENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=327,
    serialized_end=630,
)

_QUOTECAST = _descriptor.Descriptor(
    name="Quotecast",
    full_name="Quotecast",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="json_data",
            full_name="Quotecast.json_data",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="metadata",
            full_name="Quotecast.metadata",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _QUOTECAST_REQUEST,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=265,
    serialized_end=630,
)


_TICKER_METRICS_METRICSENTRY = _descriptor.Descriptor(
    name="MetricsEntry",
    full_name="Ticker.Metrics.MetricsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="Ticker.Metrics.MetricsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="Ticker.Metrics.MetricsEntry.value",
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=793,
    serialized_end=839,
)

_TICKER_METRICS = _descriptor.Descriptor(
    name="Metrics",
    full_name="Ticker.Metrics",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="metrics",
            full_name="Ticker.Metrics.metrics",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _TICKER_METRICS_METRICSENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=735,
    serialized_end=839,
)

_TICKER_PRODUCTSENTRY = _descriptor.Descriptor(
    name="ProductsEntry",
    full_name="Ticker.ProductsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="Ticker.ProductsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="Ticker.ProductsEntry.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=841,
    serialized_end=905,
)

_TICKER = _descriptor.Descriptor(
    name="Ticker",
    full_name="Ticker",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="metadata",
            full_name="Ticker.metadata",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="products",
            full_name="Ticker.products",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="product_list",
            full_name="Ticker.product_list",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _TICKER_METRICS,
        _TICKER_PRODUCTSENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=633,
    serialized_end=905,
)


_CHART_REQUEST = _descriptor.Descriptor(
    name="Request",
    full_name="Chart.Request",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="requestid",
            full_name="Chart.Request.requestid",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="resolution",
            full_name="Chart.Request.resolution",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="culture",
            full_name="Chart.Request.culture",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="period",
            full_name="Chart.Request.period",
            index=3,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="series",
            full_name="Chart.Request.series",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="tz",
            full_name="Chart.Request.tz",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1026,
    serialized_end=1169,
)

_CHART = _descriptor.Descriptor(
    name="Chart",
    full_name="Chart",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="requestid",
            full_name="Chart.requestid",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="start",
            full_name="Chart.start",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="end",
            full_name="Chart.end",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="resolution",
            full_name="Chart.resolution",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="series",
            full_name="Chart.series",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _CHART_REQUEST,
    ],
    enum_types=[
        _CHART_RESOLUTION,
        _CHART_PERIOD,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=908,
    serialized_end=1379,
)

_METADATA.fields_by_name[
    "response_datetime"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_METADATA.fields_by_name[
    "request_duration"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_QUOTECAST_REQUEST_SUBSCRIPTIONSENTRY.fields_by_name[
    "value"
].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_QUOTECAST_REQUEST_SUBSCRIPTIONSENTRY.containing_type = _QUOTECAST_REQUEST
_QUOTECAST_REQUEST_UNSUBSCRIPTIONSENTRY.fields_by_name[
    "value"
].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_QUOTECAST_REQUEST_UNSUBSCRIPTIONSENTRY.containing_type = _QUOTECAST_REQUEST
_QUOTECAST_REQUEST.fields_by_name[
    "subscriptions"
].message_type = _QUOTECAST_REQUEST_SUBSCRIPTIONSENTRY
_QUOTECAST_REQUEST.fields_by_name[
    "unsubscriptions"
].message_type = _QUOTECAST_REQUEST_UNSUBSCRIPTIONSENTRY
_QUOTECAST_REQUEST.containing_type = _QUOTECAST
_QUOTECAST.fields_by_name["metadata"].message_type = _METADATA
_TICKER_METRICS_METRICSENTRY.containing_type = _TICKER_METRICS
_TICKER_METRICS.fields_by_name["metrics"].message_type = _TICKER_METRICS_METRICSENTRY
_TICKER_METRICS.containing_type = _TICKER
_TICKER_PRODUCTSENTRY.fields_by_name["value"].message_type = _TICKER_METRICS
_TICKER_PRODUCTSENTRY.containing_type = _TICKER
_TICKER.fields_by_name["metadata"].message_type = _METADATA
_TICKER.fields_by_name["products"].message_type = _TICKER_PRODUCTSENTRY
_CHART_REQUEST.fields_by_name["resolution"].enum_type = _CHART_RESOLUTION
_CHART_REQUEST.fields_by_name["period"].enum_type = _CHART_PERIOD
_CHART_REQUEST.containing_type = _CHART
_CHART.fields_by_name[
    "series"
].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CHART_RESOLUTION.containing_type = _CHART
_CHART_PERIOD.containing_type = _CHART
DESCRIPTOR.message_types_by_name["Metadata"] = _METADATA
DESCRIPTOR.message_types_by_name["Quotecast"] = _QUOTECAST
DESCRIPTOR.message_types_by_name["Ticker"] = _TICKER
DESCRIPTOR.message_types_by_name["Chart"] = _CHART
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Metadata = _reflection.GeneratedProtocolMessageType(
    "Metadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _METADATA,
        "__module__": "degiro_connector.quotecast.pb.quotecast_pb2"
        # @@protoc_insertion_point(class_scope:Metadata)
    },
)
_sym_db.RegisterMessage(Metadata)

Quotecast = _reflection.GeneratedProtocolMessageType(
    "Quotecast",
    (_message.Message,),
    {
        "Request": _reflection.GeneratedProtocolMessageType(
            "Request",
            (_message.Message,),
            {
                "SubscriptionsEntry": _reflection.GeneratedProtocolMessageType(
                    "SubscriptionsEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _QUOTECAST_REQUEST_SUBSCRIPTIONSENTRY,
                        "__module__": "degiro_connector.quotecast.pb.quotecast_pb2"
                        # @@protoc_insertion_point(class_scope:Quotecast.Request.SubscriptionsEntry)
                    },
                ),
                "UnsubscriptionsEntry": _reflection.GeneratedProtocolMessageType(
                    "UnsubscriptionsEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _QUOTECAST_REQUEST_UNSUBSCRIPTIONSENTRY,
                        "__module__": "degiro_connector.quotecast.pb.quotecast_pb2"
                        # @@protoc_insertion_point(class_scope:Quotecast.Request.UnsubscriptionsEntry)
                    },
                ),
                "DESCRIPTOR": _QUOTECAST_REQUEST,
                "__module__": "degiro_connector.quotecast.pb.quotecast_pb2"
                # @@protoc_insertion_point(class_scope:Quotecast.Request)
            },
        ),
        "DESCRIPTOR": _QUOTECAST,
        "__module__": "degiro_connector.quotecast.pb.quotecast_pb2"
        # @@protoc_insertion_point(class_scope:Quotecast)
    },
)
_sym_db.RegisterMessage(Quotecast)
_sym_db.RegisterMessage(Quotecast.Request)
_sym_db.RegisterMessage(Quotecast.Request.SubscriptionsEntry)
_sym_db.RegisterMessage(Quotecast.Request.UnsubscriptionsEntry)

Ticker = _reflection.GeneratedProtocolMessageType(
    "Ticker",
    (_message.Message,),
    {
        "Metrics": _reflection.GeneratedProtocolMessageType(
            "Metrics",
            (_message.Message,),
            {
                "MetricsEntry": _reflection.GeneratedProtocolMessageType(
                    "MetricsEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _TICKER_METRICS_METRICSENTRY,
                        "__module__": "degiro_connector.quotecast.pb.quotecast_pb2"
                        # @@protoc_insertion_point(class_scope:Ticker.Metrics.MetricsEntry)
                    },
                ),
                "DESCRIPTOR": _TICKER_METRICS,
                "__module__": "degiro_connector.quotecast.pb.quotecast_pb2"
                # @@protoc_insertion_point(class_scope:Ticker.Metrics)
            },
        ),
        "ProductsEntry": _reflection.GeneratedProtocolMessageType(
            "ProductsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _TICKER_PRODUCTSENTRY,
                "__module__": "degiro_connector.quotecast.pb.quotecast_pb2"
                # @@protoc_insertion_point(class_scope:Ticker.ProductsEntry)
            },
        ),
        "DESCRIPTOR": _TICKER,
        "__module__": "degiro_connector.quotecast.pb.quotecast_pb2"
        # @@protoc_insertion_point(class_scope:Ticker)
    },
)
_sym_db.RegisterMessage(Ticker)
_sym_db.RegisterMessage(Ticker.Metrics)
_sym_db.RegisterMessage(Ticker.Metrics.MetricsEntry)
_sym_db.RegisterMessage(Ticker.ProductsEntry)

Chart = _reflection.GeneratedProtocolMessageType(
    "Chart",
    (_message.Message,),
    {
        "Request": _reflection.GeneratedProtocolMessageType(
            "Request",
            (_message.Message,),
            {
                "DESCRIPTOR": _CHART_REQUEST,
                "__module__": "degiro_connector.quotecast.pb.quotecast_pb2"
                # @@protoc_insertion_point(class_scope:Chart.Request)
            },
        ),
        "DESCRIPTOR": _CHART,
        "__module__": "degiro_connector.quotecast.pb.quotecast_pb2"
        # @@protoc_insertion_point(class_scope:Chart)
    },
)
_sym_db.RegisterMessage(Chart)
_sym_db.RegisterMessage(Chart.Request)


_QUOTECAST_REQUEST_SUBSCRIPTIONSENTRY._options = None
_QUOTECAST_REQUEST_UNSUBSCRIPTIONSENTRY._options = None
_TICKER_METRICS_METRICSENTRY._options = None
_TICKER_PRODUCTSENTRY._options = None
# @@protoc_insertion_point(module_scope)
