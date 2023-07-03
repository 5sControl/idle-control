#include "iostream"
#include "opencv2/opencv.hpp"
#include "ctime"
#include <cpr/cpr.h>
#include "NumCpp.hpp"
#include <cmath>


long init_connection(const std::string & password, const std::string & username, const std::string & url)
{
    auto response = cpr::Get(
                cpr::Url{url},
                cpr::Body{"foobar"}
                );
    return response.status_code;
}

cv::Mat get_frame()
{
    cv::Mat img = cv::imread("snapshot.jpg", cv::IMREAD_COLOR);
    return img;
}

cv::Mat put_rectangle(cv::Mat image, const nc::NdArray<int>& boxes, const nc::NdArray<double>& scores)
{
    for (unsigned int idx {}; idx < nc::alen(scores); ++idx)
    {
        cv::rectangle(
                image,
                cv::Point(boxes[0], boxes[1]),
                cv::Point(boxes[2], boxes[3]),
                cv::Scalar(255, 255, 255),
                2
                );
        cv::putText(
                image,
                std::to_string(std::ceil(scores[idx] * 100.) / 100.),
                cv::Point(boxes[0], boxes[1]),
                cv::FONT_HERSHEY_COMPLEX,
                1,
                cv::Scalar(255, 0, 0),
                2,
                cv::LINE_AA
                );
    }
    return image;
}

bool check_coordinates_diffs(const nc::NdArray<double>& coordinates_1, const nc::NdArray<double>& coordinates_2, const double & threshold)
{
    return nc::sum(nc::abs(coordinates_1 - coordinates_2))[0] > threshold;
}

void send_report_and_save_photo(cv::Mat img, const std::time_t & start_track_time)
{
    std::cout << std::ctime(&start_track_time) << std::endl;
}
