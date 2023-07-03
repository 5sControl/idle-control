#include <iostream>
#include "dotenv.h"
#include "unistd.h"
#include "chrono"
#include "functional.h"
#include "send_request.h"
#include "NumCpp.hpp"


int main() {
    auto a = nc::random::randInt<int>({10, 10}, 0, 100);
    std::cout << a;

    auto& env = dotenv::env.load_dotenv("confs/settings.env");
    auto& server_url = env["server_url"];
    auto& password = env["password"];
    auto& name = env["name"];
    while (true)
    {
        std::cout << "Cannot create connection" << std::endl;
        usleep(1e6);
    }
    auto previous_coordinates = std::vector<std::vector<float>> {{}};
    int iter_idx = 0;
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
    }
    return 0;
}
