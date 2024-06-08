from ncclient import manager
import xml.dom.minidom
import xmltodict

m = manager.connect(host="devnetsandboxiosxe.cisco.com",
                    port=830,
                    username="admin",
                    password="C1sco12345",
                    hostkey_verify=False)

print("Connected")
m.create_subscription(filter=None)

allowed_sessions = [m.session_id]
print(f"Son reconocidas las sesiones: {allowed_sessions}")

while True:
    n = m.take_notification()
    raw_data = xmltodict.parse(n.notification_xml)
    change_data = raw_data["notification"].get("netconf-config-change")
    if (change_data != None):
        identity = change_data["changed-by"];
        if(identity["session-id"] not in allowed_sessions):
            print("============= INICIO ALERTA ==================================")
            print("Modificación ejecutada desde session no autorizada!:");
            for op in change_data["edit"]:
                print(f"| Op: {op["operation"]:<10} | Desc: {op["target"]["#text"]}")
            print("============= FINAL ALERTA =================================\n")



