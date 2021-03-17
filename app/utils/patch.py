from isaac import CapnpMessages
from isaac import CodeletHooks
from isaac import Message


def patch_capnp_paths():
    CapnpMessages.PATH = "/../com_nvidia_isaac_sdk/messages/*.capnp"
    CodeletHooks.CAPNP_DICT = CapnpMessages.get_capnp_proto_schemata()
    Message.CAPNP_DICT = CapnpMessages.get_capnp_proto_schemata()
    Message.CAPNP_TYPE_ID_DICT = CapnpMessages.capnp_schema_type_id_dict()
