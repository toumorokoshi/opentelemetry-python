# Copyright 2019, OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc
import typing

from opentelemetry.context import BaseRuntimeContext

Setter = typing.Callable[[object, str, str], None]
Getter = typing.Callable[[object, str], typing.List[str]]


class HTTPTextFormat(abc.ABC):
    """API for propagation of span context via headers.

    This class provides an interface that enables extracting and injecting
    span context into headers of HTTP requests. HTTP frameworks and clients
    can integrate with HTTPTextFormat by providing the object containing the
    headers, and a getter and setter function for the extraction and
    injection of values, respectively.

    Example::

        import flask
        import requests
        from opentelemetry.context.propagation import HTTPTextFormat
        from opentelemetry.trace import tracer
        from opentelemetry.context import UnifiedContext

        PROPAGATOR = HTTPTextFormat()


        def get_header_from_flask_request(request, key):
            return request.headers.get_all(key)

        def set_header_into_requests_request(request: requests.Request,
                                             key: str, value: str):
            request.headers[key] = value

        def example_route():
            span = tracer().create_span("")
            context = UnifiedContext.create(span)
            PROPAGATOR.extract(
                context, get_header_from_flask_request,
                flask.request
            )
            request_to_downstream = requests.Request(
                "GET", "http://httpbin.org/get"
            )
            PROPAGATOR.inject(
                context,
                set_header_into_requests_request,
                request_to_downstream
            )
            session = requests.Session()
            session.send(request_to_downstream.prepare())


    .. _Propagation API Specification:
       https://github.com/open-telemetry/opentelemetry-specification/blob/master/specification/api-propagators.md
    """

    @abc.abstractmethod
    def extract(
        self,
        context: BaseRuntimeContext,
        get_from_carrier: Getter,
        carrier: object,
    ) -> None:
        """Extract values from the carrier into the context.

        The extract function should retrieve values from the carrier
        object using get_from_carrier, and use values to populate
        attributes of the UnifiedContext passed in.

        Args:
            context: A UnifiedContext instance that will be
                populated with values from the carrier.
            get_from_carrier: a function that can retrieve zero
                or more values from the carrier. In the case that
                the value does not exist, return an empty list.
            carrier: and object which contains values that are
                used to construct a SpanContext. This object
                must be paired with an appropriate get_from_carrier
                which understands how to extract a value from it.
        Returns:
            A SpanContext with configuration found in the carrier.

        """

    @abc.abstractmethod
    def inject(
        self,
        context: BaseRuntimeContext,
        set_in_carrier: Setter,
        carrier: object,
    ) -> None:
        """Inject values from a SpanContext into a carrier.

        inject enables the propagation of values into HTTP clients or
        other objects which perform an HTTP request. Implementations
        should use the set_in_carrier method to set values on the
        carrier.

        Args:
            context: The SpanContext to read values from.
            set_in_carrier: A setter function that can set values
                on the carrier.
            carrier: An object that a place to define HTTP headers.
                Should be paired with set_in_carrier, which should
                know how to set header values on the carrier.

        """