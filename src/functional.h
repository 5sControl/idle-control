#include "cstring"
#include "opencv2/opencv.hpp"
#include "vector"

int init_connection(std::string password, std::string username);
cv::Mat get_frame();
bool check_coordinates_diffs(std::vector<std::vector<float>> prev_pred, std::vector<std::vector<float>> curr_pred);
void send_report_and_save_photo(cv::Mat img, const std::time_t & start_track_time);
