# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ur_msgs/GripperMoveRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GripperMoveRequest(genpy.Message):
  _md5sum = "8e1410c2dff620c967ae982f954af617"
  _type = "ur_msgs/GripperMoveRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint8 pos
uint8 force
uint8 speed
bool position_compensation
"""
  __slots__ = ['pos','force','speed','position_compensation']
  _slot_types = ['uint8','uint8','uint8','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       pos,force,speed,position_compensation

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GripperMoveRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.pos is None:
        self.pos = 0
      if self.force is None:
        self.force = 0
      if self.speed is None:
        self.speed = 0
      if self.position_compensation is None:
        self.position_compensation = False
    else:
      self.pos = 0
      self.force = 0
      self.speed = 0
      self.position_compensation = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_4B().pack(_x.pos, _x.force, _x.speed, _x.position_compensation))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 4
      (_x.pos, _x.force, _x.speed, _x.position_compensation,) = _get_struct_4B().unpack(str[start:end])
      self.position_compensation = bool(self.position_compensation)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4B().pack(_x.pos, _x.force, _x.speed, _x.position_compensation))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 4
      (_x.pos, _x.force, _x.speed, _x.position_compensation,) = _get_struct_4B().unpack(str[start:end])
      self.position_compensation = bool(self.position_compensation)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4B = None
def _get_struct_4B():
    global _struct_4B
    if _struct_4B is None:
        _struct_4B = struct.Struct("<4B")
    return _struct_4B
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ur_msgs/GripperMoveResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GripperMoveResponse(genpy.Message):
  _md5sum = "b7c3e9566a7011a43c48ce986ef29228"
  _type = "ur_msgs/GripperMoveResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool success
bool has_object

"""
  __slots__ = ['success','has_object']
  _slot_types = ['bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success,has_object

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GripperMoveResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
      if self.has_object is None:
        self.has_object = False
    else:
      self.success = False
      self.has_object = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2B().pack(_x.success, _x.has_object))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 2
      (_x.success, _x.has_object,) = _get_struct_2B().unpack(str[start:end])
      self.success = bool(self.success)
      self.has_object = bool(self.has_object)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2B().pack(_x.success, _x.has_object))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 2
      (_x.success, _x.has_object,) = _get_struct_2B().unpack(str[start:end])
      self.success = bool(self.success)
      self.has_object = bool(self.has_object)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2B = None
def _get_struct_2B():
    global _struct_2B
    if _struct_2B is None:
        _struct_2B = struct.Struct("<2B")
    return _struct_2B
class GripperMove(object):
  _type          = 'ur_msgs/GripperMove'
  _md5sum = 'd1d55f75257890b063dd76689fbde353'
  _request_class  = GripperMoveRequest
  _response_class = GripperMoveResponse
