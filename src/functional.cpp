#include "iostream"
#include "opencv2/opencv.hpp"
#include "ctime"

int init_connection(std::string password, std::string username)
{
    try
    {
        // attempt to create connection
        return 1;
    }
    catch (std::string error_msg)
    {
        std::cout << error_msg << std::endl;
        return 0;
    }
}

cv::Mat get_frame()
{
    cv::Mat img = cv::imread("snapshot.jpg", cv::IMREAD_COLOR);
    return img;
}

bool check_coordinates_diffs(std::vector<std::vector<float>> prev_pred, std::vector<std::vector<float>> curr_pred)
{
    return false;
}

void send_report_and_save_photo(cv::Mat img, const std::time_t & start_track_time)
{
    std::cout << std::ctime(&start_track_time) << std::endl;
}
