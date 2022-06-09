import asyncio
import logging

import grpc
import math_pb2
import math_pb2_grpc


class Math(math_pb2_grpc.MathServicer):

    async def Sum(
            self, request: math_pb2.SumRequest,
            context: grpc.aio.ServicerContext) -> math_pb2.SumResponse:

        sum_values = request.firstNumber + request.secondNumber
        message = f'The sum of {request.firstNumber} with {request.secondNumber} equals {sum_values}'

        return math_pb2.SumResponse(message=message, response=sum_values)


async def serve() -> None:
    server = grpc.aio.server()
    math_pb2_grpc.add_MathServicer_to_server(Math(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info('Math server starting on %s', listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())

