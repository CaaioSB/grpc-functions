import asyncio
import logging

import grpc
import math_pb2
import math_pb2_grpc


async def run() -> None:
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = math_pb2_grpc.MathStub(channel)
        response = await stub.Sum(math_pb2.SumRequest(firstNumber=5, secondNumber=5))
        print(response)


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())

