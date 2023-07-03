cmake_minimum_required(VERSION 3.25)
project(idle_python)

find_package( OpenCV REQUIRED )
find_package(NumCpp 2.6.2 REQUIRED)
find_package(cpr REQUIRED)

include_directories( ${OpenCV_INCLUDE_DIRS} )


set(CMAKE_CXX_STANDARD 17)
add_subdirectory(cpp-dotenv)
add_executable(idle_python src/main.cpp src/functional.cpp src/send_request.cpp)
target_link_libraries(idle_python ${OpenCV_LIBS} )
target_link_libraries(idle_python cpp_dotenv)
target_link_libraries(idle_python NumCpp::NumCpp)
target_link_libraries(idle_python cpr::cpr)
