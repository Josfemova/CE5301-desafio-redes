from ncclient import manager
import xmltodict

# Basado en la guía Device Level APIs on Cisco IoT Hardware: NETCONF
# de Cisco DevNet

m = manager.connect(host="devnetsandboxiosxe.cisco.com",
                    port=830,
                    username="admin",
                    password="C1sco12345",
                    hostkey_verify=False)


def change_interface(user_selection):
  int_status = user_selection

  config = '''
      <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
              <interface>
                  <name>GigabitEthernet3</name>
                  <enabled>false</enabled>
              </interface>
            </interfaces>
        </config>
      '''
  config_dict = xmltodict.parse(config)

  if int_status == int(1):
      config_dict["config"]["interfaces"]["interface"]["enabled"] = "true"
      config = xmltodict.unparse(config_dict)

  netconf_reply = m.edit_config(target='running', config=config)
  print("Cambio exitoso?: {}".format(netconf_reply.ok))

# dispara una notificación de cambio
change_interface(0) #disable
change_interface(1) #enable
