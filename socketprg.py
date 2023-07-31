# Socket Programming
import socket

#created class for client-server connection
class localserver:
    def __init__(arg):
        arg.data_dict = {}
#server address 
        arg.ADDRESS = 'localhost'
#port number 
        arg.PORT_NO = 1234
        arg.msg = ''
        arg.localclient_socket = None
#binding to perform socket programming
        arg.localserver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        arg.localserver_socket.bind((arg.ADDRESS, arg.PORT_NO))
        arg.localserver_socket.listen(1)
#Connection indication 
        print(f"Connection{arg.ADDRESS} Established at {arg.PORT_NO}")

#defining operations to perform such as put,remove,get,dump
    def operations(arg):
        list_msg = arg.msg.strip().replace('=', ' ').split()
        print(list_msg)
        print(list_msg[2:])
#remove operation         
        if list_msg[0].upper() == 'REMOVE' and len(list_msg[1:]) != 0:
            print(list_msg[1])
            return arg.EntRemove(list_msg[1])
#put operation
        elif list_msg[0].upper() == 'PUT' and len(list_msg[2:]) != 0:
            values = ' '.join(_ for _ in list_msg[2:])
            return arg.EntPut(list_msg[1], values)
#dump operation 
        elif list_msg[0].upper() == 'DUMP':
            if arg.EntDump()=="":
                print("Empty\n")
            else:
                return arg.EntDump()
#get opertaion 
        elif list_msg[0].upper() == 'GET' and len(list_msg[1:]) != 0:
            print("Output : ")
            return arg.EntGet(list_msg[1])
#error message for wrong entry
        else:
            return "\nOutput : Incorrect Input\n"
#defining remove operation 
    def EntRemove(arg, keys):
        if keys in arg.data_dict:
            del arg.data_dict[keys]
            return "\nOutput : Removed        \n"
        else:
            return "\nOutput : No Match Found \n"
        
#defining put operation  
    def EntPut(arg, keys, values):
        arg.data_dict[keys] = values
        return "\nOutput : New Entry     \n"

#defining get operation
    def EntGet(arg, keys):
        if keys in arg.data_dict:
            print("Output: ")
            return arg.data_dict[keys]
        else:
            return "\nOutput : No Match Found \n"
#defining dump operation
    def EntDump(arg):
        return ' '.join(str(i) for i in arg.data_dict.keys())


#starting server to be open for client 
    def startlocalserver(arg):
        while True:
            arg.localclient_socket, (localclientAdd, localclientPort) = arg.localserver_socket.accept()
            print(f"Connected with {localclientAdd, localclientPort}")
#options to choose from
            initialM = "Input Command : (1) PUT (2) GET (3) DUMP (4) REMOVE\n"
#decoding method utf-8 for default
            arg.localclient_socket.send(bytes(initialM, "utf-8"))
            arg.msg = ' '
            while arg.localclient_socket:
                initialM = arg.localclient_socket.recv(1024)
                arg.msg += initialM.decode('utf-8')
#for successful operations and commands
                if arg.msg[-1:] == '\n' or arg.msg[-1:] == '\n':
                    print(f"msg recieved: {arg.msg}")
                    returninitialM = arg.operations()
                    arg.localclient_socket.send(
                        bytes(str(returninitialM) + "\n\nCommands : (1) PUT (2) GET (3) DUMP (4) REMOVE\n" + '\n', 'utf-8'))
                    arg.msg = ''

#Starting local server and connecting to it
if __name__ == "__main__":
    mainlocalserver = localserver()
    mainlocalserver.startlocalserver()