from zmq import Context, SUB, SUBSCRIBE, Socket
from zlib import decompress
from json import loads
from sqlite3 import connect

def setupConnection(address = "tcp://eddn.edcd.io:9500"):
    context = Context()
    socket = context.socket(SUB)
    
    socket.connect(address)
    socket.setsockopt_string(SUBSCRIBE, "")
    return socket


def recieveMsg(socket : Socket):
    return decompress(socket.recv()).decode('utf-8')

def insertExoBioDB (database, name, timeStamp, system, systemAddress, bodyName, bodyID):
    connection = connect(database)
    cursor = connection.cursor()
    query = f'''
            INSERT INTO ExoBio 
            (Name, TimeStamp, System, SystemAddress, BodyName, BodyID)
            VALUES 
            ("{name}", "{timeStamp}", "{system}", "{systemAddress}", "{bodyName}", "{bodyID}" ) ;'''
    cursor.execute(query)
    connection.commit()
    connection.close()


def insertExoBio (database, json_msg):
    name = json_msg['message']['Name']
    timeStamp = json_msg['message']['timestamp']
    system  = json_msg['message']['System']
    systemAddress  = json_msg['message']['SystemAddress']
    bodyName = json_msg['message']['BodyName']
    bodyID  = json_msg['message']['BodyID']
    insertExoBioDB(database, name, timeStamp, system, systemAddress, bodyName, bodyID)

def insertBodiesDB(database, bodyName, bodyID, systemAddress, starSystem, timeStamp, surfaceTemperature, surfaceGravity, parentStarID, atmosphereType, surfacePressure, volcanism):
    connection = connect(database)
    cursor = connection.cursor()
    query = f'''
            INSERT INTO ExoBio 
            (BodyName, BodyID, SystemAddress, StarSystem, TimeStamp, SurfaceTemperature, SurfaceGravity, ParentStarID, PlanetClass, AtmosphereType, SurfacePressure, Volcanism)
            VALUES 
            ("{bodyName}", "{bodyID}", "{systemAddress}", "{starSystem}", "{timeStamp}", "{surfaceTemperature}", "{surfaceGravity}", "{parentStarID}", "{atmosphereType}", "{surfacePressure}", "{volcanism}" ) ;'''
    cursor.execute(query)
    connection.commit()
    connection.close()

def insertBodies (database, json_msg):
    bodyName = json_msg['message']
    bodyID = json_msg['message']
    systemAddress = json_msg['message']
    starSystem = json_msg['message']
    timeStamp = json_msg['message']
    surfaceTemperature = json_msg['message']
    surfaceGravity = json_msg['message']
    parentStarID = "TODO"
    atmosphereType = json_msg['message']
    surfacePressure = json_msg['message']
    volcanism = json_msg['message']
    insertBodiesDB(database, bodyName, bodyID, systemAddress, starSystem, timeStamp, surfaceTemperature, surfaceGravity, parentStarID, atmosphereType, surfacePressure, volcanism)




def get_n_entries(n, socket, verbose = False):
    counter = 0
    while counter <= n-1:
        msg = recieveMsg(socket)
        json_msg = loads(msg)
        if json_msg['$schemaRef'] == 'https://eddn.edcd.io/schemas/codexentry/1' and json_msg['message']['Category'] == '$Codex_Category_Biology;' and 'BodyName' in json_msg['message'].keys():
            insertExoBio('smollEDDN', json_msg)
            counter += 1
            if verbose:
                print (counter)