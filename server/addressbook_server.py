from concurrent import futures
import time
import logging
import grpc
import addressbook_pb2
import addressbook_pb2_grpc
import time
import yaml_parser
from mongo_setup import create_database
from mongo_setup import find_entry_in_connections
from mongo_setup import insert_into_db

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Server(addressbook_pb2_grpc.address_infoServicer):  # looking for stub of the service defined in proto file

    def search_user(self, request, context): # instantiate the rpc function defined in proto file
        out = find_entry_in_connections.find_entry(yaml_parser.mongodb_out('mongodb_name'), {'email': request.email})
        f= open("/tmp/output.txt","w+")
        f.write(str(out))
        if out is not None:
            return addressbook_pb2.user_info( id      = int(out['id']),
                                          first_name  = out['first_name'],
                                          last_name   = out['last_name'],
                                          email       = out['email']
                                        )
        else:
            return addressbook_pb2.user_info( id      = -1,
                                          first_name  = None,
                                          last_name   = None,
                                          email       = None
                                        )
    def insert_user(self, request, context): # instantiate the rpc function defined in proto file
        print("context: ", context)
        info = {"id"          : request.id,
                "first_name"  : '%s' % request.first_name,
                "last_name"   : '%s' % request.last_name,
                "email"       : '%s' % request.email
        }
        insert_into_db.insert_db(yaml_parser.mongodb_out('mongodb_name'), info)
        return addressbook_pb2.user_info( id          = request.id,
                                          first_name  = '%s' % request.first_name,
                                          last_name   = '%s' % request.last_name,
                                          email       = '%s' % request.email
                                        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) #fixed
    addressbook_pb2_grpc.add_address_infoServicer_to_server(Server(), server) # # looking for stub of the service defined in proto file
    server.add_insecure_port('[::]:50057') # fixed
    server.start() # fixed
    create_database.create_db(yaml_parser.mongodb_out('mongodb_name'))
    try: # fixed
        while True: # fixed
            time.sleep(_ONE_DAY_IN_SECONDS) # fixed
    except KeyboardInterrupt: # fixed
        server.stop(0) # fixed


if __name__ == '__main__':
    logging.basicConfig()
    # func_input = addressbook_pb2.user_email(email = 'devopsac@gmail.com')
    # test = Server()
    # test.search_user(func_input)
    serve() # fixed
