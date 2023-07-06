#include "iostream"
#include "opencv2/opencv.hpp"
#include "ctime"
#include <cpr/cpr.h>
#include "NumCpp.hpp"
#include <cmath>

cv::Mat get_frame(const std::string& url, const std::string& username, const std::string& password)
{
    auto response = cpr::Get(
            cpr::Url{url},
            cpr::Authentication(password, username, cpr::AuthMode::BASIC),
            cpr::Body("foobar")
    );
    if (response.status_code < 200 || response.status_code >= 300)
    {
        std::cout << "Cannot retrieve image. Status code = " << response.status_code << std::endl;
        cv::Mat empty_mat;
        return empty_mat;
    }

    nc::NdArray<uint8_t> np_array = nc::frombuffer<uint8_t>(response.text.c_str(), response.text.length());
    cv::Mat image = cv::Mat(np_array.numRows(), np_array.numCols(), CV_8SC1, np_array.data());
    image = cv::imdecode(image, cv::IMREAD_COLOR);
    return image;
}

cv::Mat put_rectangle(cv::Mat image, const nc::NdArray<float>& boxes, const nc::NdArray<float>& scores)
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

bool check_coordinates_diffs(const nc::NdArray<float>& coordinates_1, const nc::NdArray<float>& coordinates_2, const double & threshold)
{
    return nc::sum(nc::abs(coordinates_1 - coordinates_2))[0] > threshold;
}

void send_report_and_save_photo(cv::Mat img, const std::time_t & start_track_time)
{
    std::cout << std::ctime(&start_track_time) << std::endl;
}
