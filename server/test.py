from concurrent import futures
import time
import logging
import grpc
import find_entry_in_connections

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def find_in_mongo():
    print(find_entry_in_connections.find_entry('customer', {'email': "vtom2019@gmail.com"}))

find_in_mongo()