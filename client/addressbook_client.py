from __future__ import print_function
import logging
import grpc
import addressbook_pb2
import addressbook_pb2_grpc
import yaml_parser

def run():
    connection_name = 'addressbook_server:' + str(yaml_parser.mongodb_out('grpc_port'))
    with grpc.insecure_channel(connection_name) as channel: # fixed
        stub = addressbook_pb2_grpc.address_infoStub(channel) # looking for stub of the service defined in proto file
        try:
           search_response = stub.search_user(addressbook_pb2.user_email(email='devohpsac@gmail.com'))  # call the rpc function defined in proto file and implemented in the server
           if search_response.id is -1:
               insert_response = stub.insert_user(addressbook_pb2.user_info(id=7,first_name="John",last_name="Doe",email="vtom2019@gmail.com"))
               print("insert_response: ", insert_response)
        except grpc.RpcError as e:
            print('Failed with {0}: {1}'.format(e.code(), e.details()))



if __name__ == '__main__':
    logging.basicConfig()
    run()
