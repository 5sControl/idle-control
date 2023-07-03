#include <iostream>
#include "dotenv.h"
#include "unistd.h"
#include "chrono"
#include "functional.h"
#include "send_request.h"
#include "NumCpp.hpp"
#include <fstream>


inline bool is_file_exist (const std::string& name) {
    return ( access( name.c_str(), F_OK ) != -1 );
}

int main() {
    if (!is_file_exist("confs/settings.env")) std::cout << "File is not found\n";
    auto& env = dotenv::env.load_dotenv("confs/settings.env");
    auto& server_url = env["server_url"];
    std::string password = env["password"];
    std::string name = env["name"];
    std::string camera_url = env["camera_url"];
    for (
            long status_code {init_connection(password, name, camera_url)};
            status_code < 200 || status_code >= 300;
            status_code = init_connection(password, name, camera_url)
                    )
    {
        std::cout << "Cannot create connection. Status code - " << status_code << std::endl;
        usleep(1e6);
    }
    auto previous_coordinates = std::vector<std::vector<float>> {{}};
    int iter_idx = 0;
    /*
    while (!init_connection(password, name))
    {
        cv::Mat img = get_frame();
        if (!false)
        {
            std::cout << "Empty photo" << std::endl;
            usleep(1e6);
            continue;
        }
        std::vector<std::vector<float>> predictions = predict(img, server_url);


        if (!predictions.empty())
        {
            std::cout << "Telephone is detected" << std::endl;
            if (!check_coordinates_diffs(previous_coordinates, predictions))
            {

            }
            previous_coordinates = predictions;
        }

        std::time_t curr_time = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());
        break;
    }*/
    return 0;
}
