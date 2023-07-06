#include "cstring"
#include "opencv2/opencv.hpp"
#include "vector"
#include "NumCpp.hpp"


cv::Mat get_frame(const std::string& url, const std::string& username, const std::string& password);
bool check_coordinates_diffs(const nc::NdArray<float>& coordinates_1, const nc::NdArray<float>& coordinates_2, const float & threshold);
cv::Mat put_rectangle(cv::Mat image, const nc::NdArray<float>& boxes, const nc::NdArray<float>& scores);
void send_report_and_save_photo(cv::Mat img, const std::time_t & start_track_time);
