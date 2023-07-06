cmake_minimum_required(VERSION 3.25)
project(idle_python)

find_package( OpenCV REQUIRED )
find_package(NumCpp 2.6.2 REQUIRED)
find_package(cpr REQUIRED)

include_directories( ${OpenCV_INCLUDE_DIRS} )

execute_process(COMMAND "cp" "-r" "../src/confs" ".")

set(CMAKE_CXX_STANDARD 17)
add_subdirectory(cpp-dotenv)
add_executable(${PROJECT_NAME} src/main.cpp src/functional.cpp src/send_request.cpp)
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS} )
target_link_libraries(${PROJECT_NAME} cpp_dotenv)
target_link_libraries(${PROJECT_NAME} NumCpp::NumCpp)
target_link_libraries(${PROJECT_NAME} cpr::cpr)
