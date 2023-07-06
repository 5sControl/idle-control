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
    nc::NdArray<float> previous_coordinates;
    int iter_idx = 0;
    while (true)
    {
        cv::Mat img = get_frame(camera_url, name, password);
        if (img.empty())
        {
            std::cout << "Empty photo" << std::endl;
        }
        nc::NdArray<float> predictions = predict(img, server_url);
        if (predictions.isempty()) continue;
        nc::NdArray<float> coordinates = predictions(predictions.rSlice(), 0);
        nc::NdArray<float> probabilities = predictions(predictions.rSlice(), -1);
        if (!coordinates.isempty())
        {
            std::cout << "Telephone is detected" << std::endl;
            if (check_coordinates_diffs(previous_coordinates, coordinates, 200))
            {
                img = put_rectangle(img, coordinates, probabilities);
                send_report_and_save_photo(img, start_tracking_time);
            }
        }
        previous_coordinates = coordinates;
    }
    return 0;
}
