#include "cstring"
#include "opencv2/opencv.hpp"
#include "vector"

int init_connection(std::string password, std::string username);
cv::Mat get_frame();
bool check_coordinates_diffs(std::vector<std::vector<float>> prev_pred, std::vector<std::vector<float>> curr_pred);
long init_connection(const std::string & password, const std::string & username, const std::string & url);
