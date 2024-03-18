cmake_minimum_required(VERSION 3.4)
project(TestRTD
        VERSION 1.0.0
	DESCRIPTION "blabla"
	LANGUAGES NONE)

set(CMAKE_CXX_STANDARD 14)

find_package(Doxygen REQUIRED dot)

configure_file(${PROJECT_SOURCE_DIR}/Doxyfile.in ${PROJECT_BINARY_DIR}/Doxyfile)

add_custom_target(doc
                ALL
                COMMENT "Generating API documentation with Doxygen" VERBATIM)

add_custom_command(TARGET doc
                COMMAND ${DOXYGEN_EXECUTABLE} ${PROJECT_BINARY_DIR}/Doxyfile)

add_custom_command(TARGET doc
                COMMAND make html
                WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/docs)
