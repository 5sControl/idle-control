#include "vector"
#include "opencv2/opencv.hpp"


std::vector<std::vector<float>> predict(cv::Mat img, std::string server_url)
{
    std::vector<std::vector<float>> results {{0, 0, 1, 1, 5}, {0, 1, 2, 3, 4}};
    return results;
}
