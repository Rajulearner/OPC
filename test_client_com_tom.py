import traceback

from opcua import Client

client = Client("opc.tcp//com_sam:Elmeasure@192.168.5.254:4840/test")
#client.activate_session(username="com_sam", password="Elmeasure")
# client.set_security_string("Basic256Sha256")
test = client.get_server_node()
print(test)
test1 = "as"
print(test1)
# print(client.load_type_definitions())
# https://github.com/FreeOpcUa/python-opcua/issues/778
#client.set_security_string("Basic256Sha256,SignAndEncrypt,OPCUAServerExpert.der,OPCUAServerExpertCsr.pem")
try:
    client.connect()
    obj = client.get_objects_node()
    obj_bn = client.get_objects_node().get_browse_name()
    print(obj_bn)
    print(obj)
    dri = obj.get_children()  ##out2
    print(dri)
    for i in dri:
        print("*" * 30)
        see_b_name = client.get_node(str(i))  # get all nodes
        print(see_b_name)
        print(see_b_name.get_browse_name())  # getting qualified names
        print(see_b_name.get_children())
        print("*" * 20)
    node = client.get_node("ns=1;i=4")  # get_qualified_name/browsename single node
    print(node)
    data = node.get_children()
    print(data)
    # for i in data:
    tes = [_.get_children() for _ in data]  # Earlier, here we have used data[0].get_children()
    print(tes)
    import time

    while True:
        for j in tes:  # list of list
            # print(j[0].get_browse_name())
            for i in j:  # parsing lists
                # print(j)
                print(client.get_node(\
                    i).get_browse_name())  # for getting the browse name don't give str(i), use that only for get_value()
                out1 = client.get_node(str(i)).get_value()  # getting the nodes
                print(out1)
            time.sleep(0.5)

    # print(node.get_value())
except Exception as e:
    traceback.print_exc()
    client.disconnect()
finally:
    client.disconnect()
