# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "empatica_e4: 4 messages, 0 services")

set(MSG_I_FLAGS "-Iempatica_e4:/home/rwilson/catkin_ws/src/empatica_e4/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(empatica_e4_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/Acc3D.msg" NAME_WE)
add_custom_target(_empatica_e4_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "empatica_e4" "/home/rwilson/catkin_ws/src/empatica_e4/msg/Acc3D.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/GSR.msg" NAME_WE)
add_custom_target(_empatica_e4_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "empatica_e4" "/home/rwilson/catkin_ws/src/empatica_e4/msg/GSR.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/Heartrate.msg" NAME_WE)
add_custom_target(_empatica_e4_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "empatica_e4" "/home/rwilson/catkin_ws/src/empatica_e4/msg/Heartrate.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/SkinTemp.msg" NAME_WE)
add_custom_target(_empatica_e4_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "empatica_e4" "/home/rwilson/catkin_ws/src/empatica_e4/msg/SkinTemp.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/Acc3D.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/empatica_e4
)
_generate_msg_cpp(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/GSR.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/empatica_e4
)
_generate_msg_cpp(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/Heartrate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/empatica_e4
)
_generate_msg_cpp(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/SkinTemp.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/empatica_e4
)

### Generating Services

### Generating Module File
_generate_module_cpp(empatica_e4
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/empatica_e4
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(empatica_e4_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(empatica_e4_generate_messages empatica_e4_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/Acc3D.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_cpp _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/GSR.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_cpp _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/Heartrate.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_cpp _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/SkinTemp.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_cpp _empatica_e4_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(empatica_e4_gencpp)
add_dependencies(empatica_e4_gencpp empatica_e4_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS empatica_e4_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/Acc3D.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/empatica_e4
)
_generate_msg_eus(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/GSR.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/empatica_e4
)
_generate_msg_eus(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/Heartrate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/empatica_e4
)
_generate_msg_eus(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/SkinTemp.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/empatica_e4
)

### Generating Services

### Generating Module File
_generate_module_eus(empatica_e4
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/empatica_e4
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(empatica_e4_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(empatica_e4_generate_messages empatica_e4_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/Acc3D.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_eus _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/GSR.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_eus _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/Heartrate.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_eus _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/SkinTemp.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_eus _empatica_e4_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(empatica_e4_geneus)
add_dependencies(empatica_e4_geneus empatica_e4_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS empatica_e4_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/Acc3D.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/empatica_e4
)
_generate_msg_lisp(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/GSR.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/empatica_e4
)
_generate_msg_lisp(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/Heartrate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/empatica_e4
)
_generate_msg_lisp(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/SkinTemp.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/empatica_e4
)

### Generating Services

### Generating Module File
_generate_module_lisp(empatica_e4
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/empatica_e4
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(empatica_e4_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(empatica_e4_generate_messages empatica_e4_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/Acc3D.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_lisp _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/GSR.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_lisp _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/Heartrate.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_lisp _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/SkinTemp.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_lisp _empatica_e4_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(empatica_e4_genlisp)
add_dependencies(empatica_e4_genlisp empatica_e4_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS empatica_e4_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/Acc3D.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/empatica_e4
)
_generate_msg_nodejs(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/GSR.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/empatica_e4
)
_generate_msg_nodejs(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/Heartrate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/empatica_e4
)
_generate_msg_nodejs(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/SkinTemp.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/empatica_e4
)

### Generating Services

### Generating Module File
_generate_module_nodejs(empatica_e4
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/empatica_e4
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(empatica_e4_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(empatica_e4_generate_messages empatica_e4_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/Acc3D.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_nodejs _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/GSR.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_nodejs _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/Heartrate.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_nodejs _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/SkinTemp.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_nodejs _empatica_e4_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(empatica_e4_gennodejs)
add_dependencies(empatica_e4_gennodejs empatica_e4_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS empatica_e4_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/Acc3D.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/empatica_e4
)
_generate_msg_py(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/GSR.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/empatica_e4
)
_generate_msg_py(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/Heartrate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/empatica_e4
)
_generate_msg_py(empatica_e4
  "/home/rwilson/catkin_ws/src/empatica_e4/msg/SkinTemp.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/empatica_e4
)

### Generating Services

### Generating Module File
_generate_module_py(empatica_e4
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/empatica_e4
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(empatica_e4_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(empatica_e4_generate_messages empatica_e4_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/Acc3D.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_py _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/GSR.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_py _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/Heartrate.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_py _empatica_e4_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rwilson/catkin_ws/src/empatica_e4/msg/SkinTemp.msg" NAME_WE)
add_dependencies(empatica_e4_generate_messages_py _empatica_e4_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(empatica_e4_genpy)
add_dependencies(empatica_e4_genpy empatica_e4_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS empatica_e4_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/empatica_e4)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/empatica_e4
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(empatica_e4_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/empatica_e4)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/empatica_e4
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(empatica_e4_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/empatica_e4)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/empatica_e4
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(empatica_e4_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/empatica_e4)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/empatica_e4
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(empatica_e4_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/empatica_e4)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/empatica_e4\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/empatica_e4
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(empatica_e4_generate_messages_py std_msgs_generate_messages_py)
endif()
